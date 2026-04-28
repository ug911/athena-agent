#!/usr/bin/env python3
"""
compare_schemas.py — diff Mongoose source-of-truth against the inferred
Athena schema and emit a gap report per collection.

Inputs:
  schemas/source/mongo/<collection>.md   (de jure, from sync_backend_api.py)
  schemas/processed/processed/wise_app_backend__<x>.md  (de facto, from sync_schemas.py)

Output:
  schemas/_gaps/<collection>.md  — one per Mongo collection with a matched Athena
                                  counterpart, listing:
                                    * fields in Mongo but absent from Athena
                                    * fields in Athena but absent from Mongo
                                    * coverage stats
  schemas/_gaps/INDEX.md         — summary across all collections, sorted by gap size

Matching: tries snake_case, lowercase, and underscore-stripped variants of the
Mongo collection name to find the Athena table. Field-path comparison is
normalized (lowercase, strip underscores, drop trailing `[]`) since the lake
pipeline tends to flatten JSON keys with case/separator changes.
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MONGO_DIR = ROOT / "schemas" / "source" / "mongo"
ATHENA_PROCESSED_DIR = ROOT / "schemas" / "processed" / "processed"
GAPS_DIR = ROOT / "schemas" / "_gaps"
GAPS_INDEX = GAPS_DIR / "INDEX.md"

# Athena tables sourced from the wise-app-backend Mongo dump are prefixed
# `wise_app_backend__`. There are also tables from other sources (`mat_*`,
# `rudder_*`, etc.) that we don't try to match.
ATHENA_PREFIX = "wise_app_backend__"


# ---------------------------------------------------------------------------
# Mongo md parsing
# ---------------------------------------------------------------------------

@dataclass
class MongoField:
    path: str
    type: str
    ref: str | None = None
    required: bool = False


@dataclass
class MongoSchema:
    collection: str
    model: str
    source_file: str
    fields: list[MongoField] = field(default_factory=list)


_FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
_FIELD_ROW_RE = re.compile(
    r"^\| `([^`]+)` \| `([^`]+)` \| (`?[^|`]*`?) \| ([^|]*) \| ([^|]*) \| ([^|]*) \| ([^|]*) \|$"
)


def parse_mongo_md(path: Path) -> MongoSchema | None:
    text = path.read_text()
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip("\"'")
    schema = MongoSchema(
        collection=fm.get("collection", path.stem),
        model=fm.get("model", ""),
        source_file=fm.get("source_file", ""),
    )
    in_fields = False
    for line in text.splitlines():
        if line.startswith("## Fields"):
            in_fields = True
            continue
        if in_fields and line.startswith("## "):
            break
        if not in_fields:
            continue
        m = _FIELD_ROW_RE.match(line)
        if not m:
            continue
        if m.group(1) == "Path":  # header row
            continue
        path_str, type_str, ref_str, _enum, flags, _default, _notes = m.groups()
        ref = ref_str.strip().strip("`") or None
        required = "required" in flags
        schema.fields.append(MongoField(path=path_str, type=type_str, ref=ref, required=required))
    return schema


# ---------------------------------------------------------------------------
# Athena md parsing
# ---------------------------------------------------------------------------

@dataclass
class AthenaField:
    path: str  # column or column.json.path
    type: str
    is_json: bool = False  # path was inferred from a JSON-bearing varchar


@dataclass
class AthenaSchema:
    table: str
    fields: list[AthenaField] = field(default_factory=list)


_ATHENA_COL_ROW_RE = re.compile(r"^\| `([^`]+)` \| `([^`]+)` \| ([^|]*) \|$")
_ATHENA_JSON_LEAF_RE = re.compile(r"^(\s*)- `([^`]+)` — `([^`]+)`")


def parse_athena_md(path: Path) -> AthenaSchema | None:
    text = path.read_text()
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip("\"'")
    schema = AthenaSchema(table=fm.get("table", path.stem))

    section: str | None = None  # "columns" | "json"
    json_column: str = ""
    parent_stack: list[tuple[int, str]] = []  # (indent_level, parent_leaf)

    for line in text.splitlines():
        if line.startswith("## Columns"):
            section = "columns"
            continue
        if line.startswith("## Inferred JSON structure"):
            section = "json"
            json_column = ""
            parent_stack.clear()
            continue
        if line.startswith("## ") or line.startswith("<!-- HUMAN NOTES BELOW"):
            section = None
            continue

        if section == "columns":
            m = _ATHENA_COL_ROW_RE.match(line)
            if m and m.group(1) != "Column":
                schema.fields.append(AthenaField(path=m.group(1), type=m.group(2), is_json=False))
            continue

        if section == "json":
            if line.startswith("### `"):
                hm = re.match(r"^### `([^`]+)`", line)
                json_column = hm.group(1) if hm else ""
                parent_stack.clear()
                continue
            m = _ATHENA_JSON_LEAF_RE.match(line)
            if not m:
                continue
            indent_str, leaf, type_str = m.groups()
            indent_level = len(indent_str) // 2
            while parent_stack and parent_stack[-1][0] >= indent_level:
                parent_stack.pop()
            ancestors = [json_column] if json_column else []
            ancestors += [p for _, p in parent_stack]
            full = ".".join(ancestors + [leaf])
            schema.fields.append(AthenaField(path=full, type=type_str, is_json=True))
            # Object/array nodes carry no example values per the existing renderer
            # but still appear here; track them as parents for deeper leaves.
            parent_stack.append((indent_level, leaf))

    return schema


# ---------------------------------------------------------------------------
# Matching + diffing
# ---------------------------------------------------------------------------

def candidate_athena_names(collection: str) -> list[str]:
    """Naming variants to try when matching a Mongo collection to an Athena table."""
    snake = re.sub(r"(?<!^)(?=[A-Z])", "_", collection).lower()
    lc = collection.lower()
    safe_lc = re.sub(r"\s+", "_", lc)
    candidates = []
    for c in (snake, lc, safe_lc):
        if c not in candidates:
            candidates.append(c)
    return [ATHENA_PREFIX + c for c in candidates]


def find_athena_match(collection: str) -> Path | None:
    for cand in candidate_athena_names(collection):
        p = ATHENA_PROCESSED_DIR / f"{cand}.md"
        if p.exists():
            return p
    return None


def normalize_segment(seg: str) -> str:
    """Lowercase and strip underscores/spaces from one path segment.
    Drops trailing `[]` (we treat a field and its array form as the same key)."""
    seg = seg.replace("[]", "")
    return re.sub(r"[_\s]+", "", seg.lower())


def normalize_path(path: str) -> str:
    return ".".join(normalize_segment(s) for s in path.split(".") if s)


@dataclass
class GapReport:
    collection: str
    athena_table: str
    mongo_only: list[MongoField]
    athena_only: list[AthenaField]
    matched: int
    mongo_total: int
    athena_total: int


def diff(mongo: MongoSchema, athena: AthenaSchema) -> GapReport:
    # Build normalized → original maps. For Athena, collapse top-level columns
    # and their JSON children into one set so a Mongo path like `metadata.tags`
    # matches either `metadata_tags` (flattened column) or `metadata.tags`
    # (JSON path under the `metadata` column).
    athena_keys: dict[str, AthenaField] = {}
    for f in athena.fields:
        # The full normalized path is one key.
        athena_keys.setdefault(normalize_path(f.path), f)
        # Also index the leaf segment alone — matches when the lake flattened
        # nested JSON into a column with `_` separators we already strip.
        leaf = f.path.split(".")[-1]
        athena_keys.setdefault(normalize_segment(leaf), f)

    matched_count = 0
    mongo_only: list[MongoField] = []
    for f in mongo.fields:
        norm = normalize_path(f.path)
        # Try full path, then fall back to leaf-only match (cheap heuristic for
        # the lake's habit of flattening one level deep).
        if norm in athena_keys:
            matched_count += 1
            continue
        leaf_norm = normalize_segment(f.path.split(".")[-1])
        if leaf_norm in athena_keys:
            matched_count += 1
            continue
        # Hide MongoDB-internal fields from gap reporting.
        if f.path in ("__v",) or f.path.startswith("_"):
            continue
        mongo_only.append(f)

    # For Athena-only, build a Mongo key set using the same normalization.
    mongo_keys = set()
    for f in mongo.fields:
        mongo_keys.add(normalize_path(f.path))
        mongo_keys.add(normalize_segment(f.path.split(".")[-1]))
    athena_only: list[AthenaField] = []
    seen = set()
    for f in athena.fields:
        norm = normalize_path(f.path)
        if norm in mongo_keys:
            continue
        leaf_norm = normalize_segment(f.path.split(".")[-1])
        if leaf_norm in mongo_keys:
            continue
        # Skip mongo-internal / housekeeping fields and Athena partition keys.
        if f.path in ("_id", "__v", "createdat", "updatedat") or f.path.startswith("$"):
            continue
        if norm in seen:
            continue
        seen.add(norm)
        athena_only.append(f)

    return GapReport(
        collection=mongo.collection,
        athena_table=athena.table,
        mongo_only=mongo_only,
        athena_only=athena_only,
        matched=matched_count,
        mongo_total=len([f for f in mongo.fields if not f.path.startswith("_")]),
        athena_total=len(athena.fields),
    )


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_gap(report: GapReport, mongo: MongoSchema, athena_path: Path) -> str:
    cov = (report.matched / report.mongo_total * 100) if report.mongo_total else 100.0
    out = [
        "---",
        f'collection: "{report.collection}"',
        f'athena_table: "{report.athena_table}"',
        f"mongo_field_count: {report.mongo_total}",
        f"athena_field_count: {report.athena_total}",
        f"matched: {report.matched}",
        f"coverage_pct: {cov:.1f}",
        f"last_diffed: \"{datetime.now(timezone.utc).isoformat(timespec='seconds')}\"",
        "---",
        "",
        f"# Schema gap: `{report.collection}` ↔ `processed.{report.athena_table}`",
        "",
        f"- **Mongo source**: [`{mongo.source_file}`](../source/mongo/{Path(mongo.collection.replace(' ', '_')).with_suffix('.md').name})",
        f"- **Athena counterpart**: [`schemas/processed/processed/{athena_path.name}`](../processed/processed/{athena_path.name})",
        f"- **Coverage**: {report.matched}/{report.mongo_total} Mongo fields are present in Athena (**{cov:.1f}%**).",
        "",
    ]

    if report.mongo_only:
        out.append("## In Mongo, missing from Athena")
        out.append("")
        out.append("These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.")
        out.append("")
        out.append("| Path | Type | Ref | Required |")
        out.append("| --- | --- | --- | --- |")
        for f in report.mongo_only:
            ref = f"`{f.ref}`" if f.ref else ""
            req = "required" if f.required else ""
            out.append(f"| `{f.path}` | `{f.type}` | {ref} | {req} |")
        out.append("")
    else:
        out.append("## In Mongo, missing from Athena")
        out.append("")
        out.append("_None — every Mongo field has a counterpart in Athena._")
        out.append("")

    if report.athena_only:
        out.append("## In Athena, missing from Mongo")
        out.append("")
        out.append("These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).")
        out.append("")
        out.append("| Path | Type | Source |")
        out.append("| --- | --- | --- |")
        for f in report.athena_only:
            src = "JSON path" if f.is_json else "column"
            out.append(f"| `{f.path}` | `{f.type}` | {src} |")
        out.append("")
    return "\n".join(out)


def render_index(reports: list[GapReport], unmatched: list[str]) -> str:
    out = [
        "# Schema gaps — Mongo ↔ Athena",
        "",
        f"_Last diffed: {datetime.now(timezone.utc).isoformat(timespec='seconds')}_",
        "",
        "Coverage = fraction of Mongoose fields that have a counterpart in the Athena table for that collection. Lower = more extraction debt.",
        "",
        "| Collection | Athena table | Coverage | Missing in Athena | Extra in Athena |",
        "| --- | --- | ---: | ---: | ---: |",
    ]
    sorted_reports = sorted(reports, key=lambda r: (r.mongo_total - r.matched, -r.mongo_total), reverse=True)
    for r in sorted_reports:
        cov = (r.matched / r.mongo_total * 100) if r.mongo_total else 100.0
        gap_md = (GAPS_DIR / f"{r.collection.replace(' ', '_')}.md").relative_to(GAPS_INDEX.parent).as_posix()
        out.append(f"| [`{r.collection}`]({gap_md}) | `{r.athena_table}` | {cov:.0f}% ({r.matched}/{r.mongo_total}) | {len(r.mongo_only)} | {len(r.athena_only)} |")
    out.append("")
    if unmatched:
        out.append("## Mongo collections with no Athena counterpart")
        out.append("")
        for c in sorted(unmatched):
            out.append(f"- `{c}`")
        out.append("")
        out.append("These collections exist in code but aren't (yet?) flowing to Athena. Confirm with the data-lake owners whether they should be ingested.")
    return "\n".join(out)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--collection", help="Restrict to a single Mongo collection")
    args = ap.parse_args()

    if not MONGO_DIR.is_dir():
        print(f"Mongo source dir not found: {MONGO_DIR} — run sync_backend_api.py first.", file=sys.stderr)
        return 2

    GAPS_DIR.mkdir(parents=True, exist_ok=True)

    reports: list[GapReport] = []
    unmatched: list[str] = []

    for mp in sorted(MONGO_DIR.glob("*.md")):
        if mp.name == "INDEX.md":
            continue
        mongo = parse_mongo_md(mp)
        if not mongo or not mongo.fields:
            continue
        if args.collection and mongo.collection != args.collection:
            continue
        ap_path = find_athena_match(mongo.collection)
        if not ap_path:
            unmatched.append(mongo.collection)
            continue
        athena = parse_athena_md(ap_path)
        if not athena:
            unmatched.append(mongo.collection)
            continue
        report = diff(mongo, athena)
        reports.append(report)
        target = GAPS_DIR / f"{mongo.collection.replace(' ', '_')}.md"
        target.write_text(render_gap(report, mongo, ap_path))

    GAPS_INDEX.write_text(render_index(reports, unmatched))
    print(f"Wrote {len(reports)} gap report(s); {len(unmatched)} collection(s) had no Athena counterpart.")
    if reports:
        avg_cov = sum(r.matched / max(1, r.mongo_total) for r in reports) / len(reports) * 100
        total_missing = sum(len(r.mongo_only) for r in reports)
        print(f"Average coverage: {avg_cov:.1f}%. Total Mongo-only fields across matched collections: {total_missing}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
