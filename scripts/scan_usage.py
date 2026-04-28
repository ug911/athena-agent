#!/usr/bin/env python3
"""
scan_usage.py — scan the wise/backend-api controllers / services / repositories
for how each Mongo model is queried, and surface the patterns as machine-
readable usage hints.

Inputs:
  <backend-api>/src/models/*.js          (to map import-name → collection)
  <backend-api>/src/controllers/*.js
  <backend-api>/src/services/**/*.js
  <backend-api>/src/repositories/*.js
  <backend-api>/src/workers/**/*.js
  <backend-api>/src/helpers/**/*.js

Output:
  semantics/usage_patterns.md            — global summary across all models
  schemas/source/mongo/<collection>.md   — appended `## Usage` section per model

What we extract per model:
  * count of `<Model>.<query-method>` invocations
  * top files where the model is queried
  * `.populate('field')` chains — flags which fields are commonly joined,
    which is the strongest hint for "what JOINs matter in Athena queries"
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MONGO_DIR = ROOT / "schemas" / "source" / "mongo"
USAGE_INDEX = ROOT / "semantics" / "usage_patterns.md"
HUMAN_MARKER = "<!-- HUMAN NOTES BELOW -->"

# Mongoose query methods we count as "this model is being read/written here".
QUERY_METHODS = {
    "find", "findOne", "findById", "findByIdAndUpdate", "findByIdAndDelete",
    "findOneAndUpdate", "findOneAndDelete", "findOneAndReplace",
    "aggregate", "count", "countDocuments", "estimatedDocumentCount",
    "distinct", "exists", "where",
    "updateOne", "updateMany", "replaceOne",
    "deleteOne", "deleteMany", "remove",
    "insertOne", "insertMany", "create", "save", "bulkWrite",
    "populate",
}

# Patterns that look like usage — the key is the IDENTIFIER preceding the
# `.method(`. We assume the identifier is the JS variable bound to the model
# (e.g. `Classroom.find(...)` after `import Classroom from '../models/Classroom'`).
USAGE_RE = re.compile(
    r"\b([A-Z][A-Za-z0-9_]*)\.(" + "|".join(sorted(QUERY_METHODS, key=len, reverse=True)) + r")\b"
)
POPULATE_RE_STRING = re.compile(r"\.populate\s*\(\s*['\"]([^'\"]+)['\"]")
POPULATE_RE_OBJECT = re.compile(r"\.populate\s*\(\s*\{[^}]*?path:\s*['\"]([^'\"]+)['\"]", re.DOTALL)


@dataclass
class ModelInfo:
    file_basename: str  # the .js basename without extension — the canonical import name
    model_name: str  # the registered mongoose.model('X', ...) name
    collection: str  # the actual Mongo collection name


@dataclass
class Usage:
    method_counts: Counter = field(default_factory=Counter)
    file_counts: Counter = field(default_factory=Counter)  # file → query count
    populate_targets: Counter = field(default_factory=Counter)  # populated field name → count


# ---------------------------------------------------------------------------
# Build import-name → model map from model files
# ---------------------------------------------------------------------------

_MODEL_DECL_RE = re.compile(
    r"const\s+([A-Za-z_$][\w$]*)\s*=\s*mongoose\.model\s*\(\s*['\"]([^'\"]+)['\"]",
    re.MULTILINE,
)


def discover_models(models_dir: Path) -> dict[str, ModelInfo]:
    """Return {variable_name: ModelInfo} where variable_name is the binding
    used by `module.exports = X` (and therefore the import name in callers).
    Falls back to file basename when the model file uses an unusual pattern."""
    out: dict[str, ModelInfo] = {}
    # Build a parallel map: collection → file basename (via Mongo md frontmatter).
    collection_by_file: dict[str, str] = {}
    if MONGO_DIR.is_dir():
        for md in MONGO_DIR.glob("*.md"):
            text = md.read_text()
            m = re.search(r'^source_file:\s*"src/models/([A-Za-z0-9_]+)\.js"', text, re.MULTILINE)
            cm = re.search(r'^collection:\s*"([^"]+)"', text, re.MULTILINE)
            if m and cm:
                collection_by_file[m.group(1)] = cm.group(1)

    for f in sorted(models_dir.glob("*.js")):
        text = f.read_text()
        # Try: `const X = mongoose.model('Y', ...)`
        m = _MODEL_DECL_RE.search(text)
        if m:
            var_name = m.group(1)
            registered = m.group(2)
        else:
            # Some files use shorthand `module.exports = mongoose.model(...)`
            m2 = re.search(r"mongoose\.model\s*\(\s*['\"]([^'\"]+)['\"]", text)
            if not m2:
                continue
            var_name = f.stem  # fall back to file basename
            registered = m2.group(1)
        collection = collection_by_file.get(f.stem, registered)
        # Index under both the variable name and the file basename to be
        # robust against import-rename quirks.
        info = ModelInfo(file_basename=f.stem, model_name=registered, collection=collection)
        out[var_name] = info
        out.setdefault(f.stem, info)
    return out


# ---------------------------------------------------------------------------
# Walk source dirs and tally usage
# ---------------------------------------------------------------------------

def scan_file(path: Path, models: dict[str, ModelInfo],
              usage_by_collection: dict[str, Usage]) -> None:
    try:
        text = path.read_text()
    except Exception:
        return
    rel = str(path)
    # Strip block comments so we don't count code-in-comments. Cheap regex —
    # not string-aware, but good enough for usage counting.
    text_no_block = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)

    seen_files: set[str] = set()
    for m in USAGE_RE.finditer(text_no_block):
        ident, method = m.group(1), m.group(2)
        info = models.get(ident)
        if not info:
            continue
        u = usage_by_collection.setdefault(info.collection, Usage())
        u.method_counts[method] += 1
        if rel not in seen_files:
            u.file_counts[rel] += 1
            seen_files.add(rel)
        else:
            u.file_counts[rel] += 1
        # When the method itself is `populate`, also record the field arg.
        if method == "populate":
            tail = text_no_block[m.end(): m.end() + 400]
            sm = POPULATE_RE_STRING.match("." + method + "(" + tail.split("(", 1)[-1] if "(" in tail else "")
            if sm:
                u.populate_targets[sm.group(1)] += 1

    # Standalone `.populate('X')` chains — capture every occurrence regardless
    # of the receiver, since chained calls (`Model.find().populate()`) lose
    # the model identifier by the time we hit `.populate`.
    # We attribute these to whichever model appears in the same statement
    # via a small lookback heuristic.
    for m in POPULATE_RE_STRING.finditer(text_no_block):
        field_name = m.group(1)
        # Look back ~400 chars for a `<Model>.find / findOne / aggregate / ...`
        back = text_no_block[max(0, m.start() - 400): m.start()]
        bm = list(USAGE_RE.finditer(back))
        if not bm:
            continue
        ident = bm[-1].group(1)
        info = models.get(ident)
        if not info:
            continue
        usage_by_collection.setdefault(info.collection, Usage()).populate_targets[field_name] += 1
    for m in POPULATE_RE_OBJECT.finditer(text_no_block):
        field_name = m.group(1)
        back = text_no_block[max(0, m.start() - 400): m.start()]
        bm = list(USAGE_RE.finditer(back))
        if not bm:
            continue
        ident = bm[-1].group(1)
        info = models.get(ident)
        if not info:
            continue
        usage_by_collection.setdefault(info.collection, Usage()).populate_targets[field_name] += 1


def walk_sources(repo: Path, models: dict[str, ModelInfo]) -> dict[str, Usage]:
    usage: dict[str, Usage] = {}
    src = repo / "src"
    targets = [
        src / "controllers",
        src / "services",
        src / "repositories",
        src / "workers",
        src / "helpers",
    ]
    for t in targets:
        if not t.is_dir():
            continue
        for f in t.rglob("*.js"):
            scan_file(f, models, usage)
    return usage


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_usage_section(collection: str, u: Usage, repo: Path) -> str:
    lines = []
    lines.append("## Usage (from backend-api)")
    lines.append("")
    total = sum(u.method_counts.values())
    lines.append(f"_{total} call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._")
    lines.append("")

    if u.method_counts:
        lines.append("### Query methods")
        lines.append("")
        for method, n in u.method_counts.most_common():
            lines.append(f"- `.{method}` × {n}")
        lines.append("")

    if u.populate_targets:
        lines.append("### Populated fields (join hints)")
        lines.append("")
        lines.append("Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.")
        lines.append("")
        for fld, n in u.populate_targets.most_common(15):
            lines.append(f"- `{fld}` × {n}")
        lines.append("")

    if u.file_counts:
        lines.append("### Top call sites")
        lines.append("")
        for fp, n in u.file_counts.most_common(8):
            try:
                rel = Path(fp).resolve().relative_to(repo.resolve()).as_posix()
            except ValueError:
                rel = fp
            lines.append(f"- `{rel}` × {n}")
        lines.append("")
    return "\n".join(lines)


def patch_mongo_md(path: Path, usage_section: str) -> bool:
    text = path.read_text()
    # Replace any prior `## Usage (...)` section up to the next `##` or the human marker.
    new_section = usage_section.rstrip() + "\n"
    pat = re.compile(r"## Usage \(from backend-api\)\n.*?(?=\n##\s|\n<!-- HUMAN NOTES BELOW -->)", re.DOTALL)
    if pat.search(text):
        text = pat.sub(new_section, text)
    else:
        # Insert before the human-notes marker so notes survive.
        if HUMAN_MARKER in text:
            head, tail = text.split(HUMAN_MARKER, 1)
            text = head.rstrip() + "\n\n" + new_section + "\n" + HUMAN_MARKER + tail
        else:
            text = text.rstrip() + "\n\n" + new_section
    path.write_text(text)
    return True


def render_global_index(usage: dict[str, Usage], total_files_scanned: int) -> str:
    out = [
        "# Backend-API usage patterns",
        "",
        "_Static-extracted from `wise/backend-api/src/{controllers,services,repositories,workers,helpers}/**/*.js`._",
        "",
        f"Scanned {total_files_scanned} JS files. Per-collection details live in `schemas/source/mongo/<collection>.md` under `## Usage`.",
        "",
        "## Models ranked by call-site count",
        "",
        "Higher = the model is touched more often by application code, so its Athena table is more likely to be a hot query target.",
        "",
        "| Collection | Total calls | Distinct files | Top method | Top populate field |",
        "| --- | ---: | ---: | --- | --- |",
    ]
    rows = []
    for collection, u in usage.items():
        total = sum(u.method_counts.values())
        files = len(u.file_counts)
        top_method = u.method_counts.most_common(1)
        top_pop = u.populate_targets.most_common(1)
        rows.append((collection, total, files,
                     f"`.{top_method[0][0]}` ×{top_method[0][1]}" if top_method else "",
                     f"`{top_pop[0][0]}` ×{top_pop[0][1]}" if top_pop else ""))
    rows.sort(key=lambda r: r[1], reverse=True)
    for collection, total, files, m, p in rows:
        out.append(f"| `{collection}` | {total} | {files} | {m} | {p} |")
    out.append("")
    out.append("## Most-populated fields globally")
    out.append("")
    out.append("Tells you which `populate(...)` paths are hot across the codebase — these are the joins Claude should know to write proactively in Athena SQL.")
    out.append("")
    glob_pop: Counter = Counter()
    for u in usage.values():
        glob_pop.update(u.populate_targets)
    for fld, n in glob_pop.most_common(30):
        out.append(f"- `{fld}` × {n}")
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend-api", required=True,
                    help="Path to wise/backend-api repo")
    args = ap.parse_args()

    repo = Path(args.backend_api).expanduser().resolve()
    models = discover_models(repo / "src" / "models")
    print(f"Discovered {len(set(m.collection for m in models.values()))} unique collections "
          f"across {len(models)} model bindings.")

    usage = walk_sources(repo, models)

    # Count files actually scanned (cheap to recompute for the index header).
    src = repo / "src"
    total_scanned = sum(1 for d in ("controllers", "services", "repositories", "workers", "helpers")
                       for f in (src / d).rglob("*.js") if (src / d).is_dir())

    # Patch each collection's mongo md.
    patched = 0
    for collection, u in usage.items():
        safe = re.sub(r"[\s/]+", "_", collection)
        md = MONGO_DIR / f"{safe}.md"
        if not md.exists():
            continue
        section = render_usage_section(collection, u, repo)
        patch_mongo_md(md, section)
        patched += 1

    USAGE_INDEX.parent.mkdir(parents=True, exist_ok=True)
    USAGE_INDEX.write_text(render_global_index(usage, total_scanned))
    print(f"Patched {patched} mongo md file(s) with usage sections; wrote {USAGE_INDEX.relative_to(ROOT)}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
