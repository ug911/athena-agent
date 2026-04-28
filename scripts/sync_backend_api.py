#!/usr/bin/env python3
"""
sync_backend_api.py — extract Mongoose schemas from the wise/backend-api repo.

Goal: capture the *de jure* schema (what the application code declares) for
every Mongo collection, so we can later diff against the de-facto Athena
schema and find extraction gaps.

Inputs:
  - <backend-api>/src/models/*.js     (Mongoose schema definitions)

Outputs:
  - schemas/source/mongo/<collection>.md
  - schemas/source/INDEX.md

The parser is intentionally pragmatic: it tokenizes JS via brace balance and
regex, handles every shape we observed in the wise repo, and degrades to
`type: '?'` rather than crashing when it meets something unfamiliar. Mongoose
schemas are declarative enough that this catches >95% of fields without
needing a real JS parser.

No values are sampled — only field names and types are read — so the
redaction policy that protects sync_schemas.py does not apply here.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "schemas" / "source" / "mongo"
INDEX_PATH = ROOT / "schemas" / "source" / "INDEX.md"
HUMAN_MARKER = "<!-- HUMAN NOTES BELOW -->"

# Mongoose primitive types (case-insensitive match against the bare identifier).
PRIMITIVE_TYPES = {
    "string": "String",
    "number": "Number",
    "boolean": "Boolean",
    "date": "Date",
    "buffer": "Buffer",
    "mixed": "Mixed",
    "objectid": "ObjectId",
    "decimal128": "Decimal128",
    "map": "Map",
    "array": "Array",
    "object": "Object",
}

# ---------------------------------------------------------------------------
# Lexing helpers — comment stripping + brace-balanced span finder
# ---------------------------------------------------------------------------

def strip_comments(text: str) -> str:
    """Remove // and /* */ comments while preserving string and template-literal
    contents. A naïve regex eats `//` inside URL strings (`https://...`) which
    breaks brace tracking downstream; this walker is string-aware."""
    out: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        # Strings: ' or " — non-multiline, escape with \.
        if c in ("'", '"'):
            out.append(c)
            i += 1
            while i < n and text[i] != c:
                if text[i] == "\\" and i + 1 < n:
                    out.append(text[i:i + 2])
                    i += 2
                    continue
                out.append(text[i])
                i += 1
            if i < n:
                out.append(text[i])  # closing quote
                i += 1
            continue
        # Template literal: ` ... ` (multiline, supports ${...} interpolations
        # whose contents are JS code — we keep them as-is).
        if c == "`":
            out.append(c)
            i += 1
            while i < n and text[i] != "`":
                if text[i] == "\\" and i + 1 < n:
                    out.append(text[i:i + 2])
                    i += 2
                    continue
                # ${ ... } interpolation: copy the JS expression verbatim,
                # respecting brace balance, so a } inside a nested template
                # literal doesn't terminate the interpolation early.
                if text[i] == "$" and i + 1 < n and text[i + 1] == "{":
                    end = find_matching(text, i + 1)
                    if end < 0:
                        out.append(text[i:])
                        i = n
                        break
                    out.append(text[i:end + 1])
                    i = end + 1
                    continue
                out.append(text[i])
                i += 1
            if i < n:
                out.append(text[i])  # closing backtick
                i += 1
            continue
        # Line comment.
        if c == "/" and i + 1 < n and text[i + 1] == "/":
            while i < n and text[i] != "\n":
                i += 1
            continue
        # Block comment.
        if c == "/" and i + 1 < n and text[i + 1] == "*":
            i += 2
            while i + 1 < n and not (text[i] == "*" and text[i + 1] == "/"):
                i += 1
            i += 2
            continue
        out.append(c)
        i += 1
    return "".join(out)


def find_matching(text: str, open_idx: int) -> int:
    """Given `text` and an index pointing at an opening `{`, `[`, or `(`,
    return the index of the matching closing bracket. Skips quoted strings
    and template literals. -1 if unbalanced."""
    pairs = {"{": "}", "[": "]", "(": ")"}
    open_ch = text[open_idx]
    close_ch = pairs[open_ch]
    depth = 0
    i = open_idx
    n = len(text)
    while i < n:
        c = text[i]
        if c in "'\"`":
            quote = c
            i += 1
            while i < n and text[i] != quote:
                if text[i] == "\\":
                    i += 2
                    continue
                i += 1
            i += 1
            continue
        if c == open_ch:
            depth += 1
        elif c == close_ch:
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def split_top_level(body: str, sep: str = ",") -> list[str]:
    """Split `body` on `sep` only at depth 0 (outside any (), [], {})."""
    parts = []
    depth = 0
    start = 0
    i = 0
    in_quote = ""
    while i < len(body):
        c = body[i]
        if in_quote:
            if c == "\\":
                i += 2
                continue
            if c == in_quote:
                in_quote = ""
            i += 1
            continue
        if c in "'\"`":
            in_quote = c
            i += 1
            continue
        if c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        elif c == sep and depth == 0:
            parts.append(body[start:i])
            start = i + 1
        i += 1
    parts.append(body[start:])
    return [p.strip() for p in parts if p.strip()]


# ---------------------------------------------------------------------------
# Schema parsing
# ---------------------------------------------------------------------------

@dataclass
class FieldInfo:
    path: str
    type: str = "?"  # primitive name, sub-schema name, or '?'
    ref: str | None = None  # foreign key target (Mongoose `ref:` value)
    enum: list[str] | None = None
    required: bool = False
    default: str | None = None
    unique: bool = False
    indexed: bool = False  # `index: true` on the field
    notes: str = ""


@dataclass
class SchemaInfo:
    name: str  # const name or 'inline'
    fields: list[FieldInfo] = field(default_factory=list)
    sub_schema_options: dict[str, str] = field(default_factory=dict)  # collection, _id, etc.


def parse_field_value(expr: str, sub_schemas: dict[str, SchemaInfo]) -> FieldInfo:
    """Parse one field VALUE expression and return a FieldInfo with `path=''`
    (caller fills `path`)."""
    info = FieldInfo(path="")
    expr = expr.strip()
    if not expr:
        return info

    # Array shorthand: `[X]` or `[new Schema(...)]` or `[SubSchema]`.
    if expr.startswith("["):
        end = find_matching(expr, 0)
        if end > 0:
            inner = expr[1:end].strip()
            inner_info = parse_field_value(inner, sub_schemas)
            info.type = f"Array<{inner_info.type}>"
            if inner_info.ref:
                info.ref = inner_info.ref
            return info

    # Object literal: `{ type: X, ref: 'Y', enum: [...], required: true, ... }`
    if expr.startswith("{"):
        end = find_matching(expr, 0)
        if end > 0:
            body = expr[1:end]
            kvs = parse_object_kvs(body)
            if "type" in kvs:
                inner_info = parse_field_value(kvs["type"], sub_schemas)
                info.type = inner_info.type
                if inner_info.ref:
                    info.ref = inner_info.ref
            if "ref" in kvs:
                ref_val = kvs["ref"].strip().strip("'\"")
                info.ref = ref_val
            if "enum" in kvs:
                info.enum = parse_enum(kvs["enum"])
            if "required" in kvs:
                info.required = kvs["required"].strip().lower().startswith("true")
            if "default" in kvs and kvs["default"]:
                info.default = kvs["default"].strip()[:80]
            if "unique" in kvs:
                info.unique = kvs["unique"].strip().lower().startswith("true")
            if "index" in kvs:
                info.indexed = kvs["index"].strip().lower().startswith("true")
            return info

    # Inline `new Schema({ ... }, opts)`
    m = re.match(r"new\s+(?:mongoose\.)?Schema\s*\(", expr)
    if m:
        info.type = "<inline-schema>"
        return info

    # `Schema.Types.ObjectId` / `mongoose.Types.ObjectId` / `mongoose.Schema.Types.ObjectId`
    if re.search(r"(?:Schema|mongoose)\.(?:Schema\.)?Types\.(\w+)", expr):
        m = re.search(r"Types\.(\w+)", expr)
        info.type = m.group(1)
        return info

    # Bare identifier: primitive (`String`, `Number`, ...) or sub-schema reference.
    m = re.match(r"([A-Za-z_$][\w$]*)", expr)
    if m:
        ident = m.group(1)
        lower = ident.lower()
        if lower in PRIMITIVE_TYPES:
            info.type = PRIMITIVE_TYPES[lower]
        elif ident in sub_schemas:
            info.type = ident
        else:
            info.type = ident
        return info

    return info


def parse_object_kvs(body: str) -> dict[str, str]:
    """Parse a JS object literal body into top-level key → value-string map.
    Doesn't recurse — values stay as raw expressions for later inspection."""
    out: dict[str, str] = {}
    for entry in split_top_level(body, sep=","):
        # Match `key:` or `'key':` or `"key":` at start.
        m = re.match(r"\s*(?:'([^']+)'|\"([^\"]+)\"|([A-Za-z_$][\w$]*))\s*:\s*(.*)$", entry, re.DOTALL)
        if not m:
            continue
        key = m.group(1) or m.group(2) or m.group(3)
        val = (m.group(4) or "").strip()
        out[key] = val
    return out


def parse_enum(expr: str) -> list[str] | None:
    """Parse an enum value: array literal or imported identifier."""
    expr = expr.strip()
    if not expr.startswith("["):
        return [f"<{expr}>"]  # imported list
    end = find_matching(expr, 0)
    if end < 0:
        return None
    inner = expr[1:end]
    out = []
    for part in split_top_level(inner, sep=","):
        v = part.strip().strip("'\"")
        if v:
            out.append(v)
    return out


def find_schema_definitions(text: str) -> dict[str, str]:
    """Return {schema_var_name: 'body|opts'} for every `const X = new Schema(...)`.
    Body is the first arg, opts is the second arg (or empty)."""
    out: dict[str, str] = {}
    for m in re.finditer(r"(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*new\s+(?:mongoose\.)?Schema\s*\(", text):
        name = m.group(1)
        open_paren = text.index("(", m.end() - 1)
        close_paren = find_matching(text, open_paren)
        if close_paren < 0:
            continue
        args = text[open_paren + 1: close_paren]
        # Split into [body, opts]
        parts = split_top_level(args, sep=",")
        body = ""
        opts = ""
        if parts:
            first = parts[0].strip()
            if first.startswith("{"):
                end = find_matching(first, 0)
                body = first[1:end] if end > 0 else first[1:]
            if len(parts) > 1:
                rest = ",".join(parts[1:]).strip()
                if rest.startswith("{"):
                    end = find_matching(rest, 0)
                    opts = rest[1:end] if end > 0 else rest[1:]
        out[name] = (body, opts)
    return out


def parse_schema_body(body: str, sub_schemas: dict[str, SchemaInfo]) -> list[FieldInfo]:
    """Parse the body of `new Schema({ ... })`."""
    fields: list[FieldInfo] = []
    for entry in split_top_level(body, sep=","):
        m = re.match(r"\s*(?:'([^']+)'|\"([^\"]+)\"|([A-Za-z_$][\w$]*))\s*:\s*(.*)$", entry, re.DOTALL)
        if not m:
            continue
        name = m.group(1) or m.group(2) or m.group(3)
        if name == "_id":
            continue
        val = (m.group(4) or "").strip()
        info = parse_field_value(val, sub_schemas)
        info.path = name
        fields.append(info)
    return fields


def find_models(text: str) -> list[tuple[str, str, str]]:
    """Return list of (model_name, schema_var_name, collection_name).

    Matches `mongoose.model('X', <whatever>(schemaVar), 'collection?')`."""
    out = []
    for m in re.finditer(r"mongoose\.model\s*\(", text):
        open_paren = text.index("(", m.end() - 1)
        close_paren = find_matching(text, open_paren)
        if close_paren < 0:
            continue
        args = text[open_paren + 1: close_paren]
        parts = split_top_level(args, sep=",")
        if not parts:
            continue
        model_name = parts[0].strip().strip("'\"")
        # Schema arg may be wrapped: attachDBInstrumentation(<schemaVar>)
        schema_arg = parts[1].strip() if len(parts) > 1 else ""
        sm = re.search(r"([A-Za-z_$][\w$]*)\s*\)?\s*$", schema_arg)
        schema_var = sm.group(1) if sm else schema_arg
        collection = parts[2].strip().strip("'\"") if len(parts) > 2 else ""
        out.append((model_name, schema_var, collection))
    return out


def find_indexes_array(text: str) -> list[str]:
    """Find a top-level `const indexes = [ ... ]` and return entries as strings."""
    m = re.search(r"(?:const|let|var)\s+indexes\s*=\s*\[", text)
    if not m:
        return []
    start = text.index("[", m.end() - 1)
    end = find_matching(text, start)
    if end < 0:
        return []
    body = text[start + 1: end]
    return [p.strip() for p in split_top_level(body, sep=",")]


def parse_options(opts_body: str) -> dict[str, str]:
    return parse_object_kvs(opts_body)


# ---------------------------------------------------------------------------
# Field-tree expansion: inline local sub-schemas into the path tree
# ---------------------------------------------------------------------------

def expand_fields(fields: list[FieldInfo], sub_schemas: dict[str, SchemaInfo],
                  prefix: str = "", visited: set[str] | None = None,
                  out: list[FieldInfo] | None = None) -> list[FieldInfo]:
    """Recursively inline sub-schemas referenced by name into a flat path list."""
    visited = visited or set()
    out = out if out is not None else []
    for f in fields:
        full_path = f"{prefix}.{f.path}" if prefix else f.path
        # Detect array-of-subschema: type like "Array<X>"
        sub_name = None
        is_array = False
        m = re.match(r"Array<(\w+)>$", f.type)
        if m and m.group(1) in sub_schemas:
            sub_name = m.group(1)
            is_array = True
        elif f.type in sub_schemas:
            sub_name = f.type
        if sub_name and sub_name not in visited:
            new_prefix = full_path + ("[]" if is_array else "")
            entry = FieldInfo(
                path=full_path + ("[]" if is_array else ""),
                type=f"<{sub_name}>",
                required=f.required, default=f.default, unique=f.unique,
                indexed=f.indexed, ref=f.ref, enum=f.enum,
            )
            out.append(entry)
            expand_fields(sub_schemas[sub_name].fields, sub_schemas,
                          prefix=new_prefix, visited=visited | {sub_name}, out=out)
        else:
            cleaned = FieldInfo(**{**f.__dict__, "path": full_path})
            out.append(cleaned)
    return out


# ---------------------------------------------------------------------------
# Markdown rendering
# ---------------------------------------------------------------------------

def render_md(model_name: str, collection: str, file_rel: str,
              indexes: list[str], fields: list[FieldInfo],
              sub_schema_names: list[str]) -> str:
    out = []
    front = {
        "collection": collection,
        "model": model_name,
        "source_file": file_rel,
        "field_count": len(fields),
        "last_synced": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    out.append("---")
    for k, v in front.items():
        out.append(f"{k}: {json.dumps(v) if isinstance(v, str) else v}")
    out.append("---")
    out.append("")
    out.append(f"# `{collection}` (Mongo collection)")
    out.append("")
    out.append(f"- **Model**: `{model_name}`")
    out.append(f"- **Source**: [`{file_rel}`](../../../{file_rel})")
    snake = re.sub(r'(?<!^)(?=[A-Z])', '_', collection).lower()
    lc = collection.lower()
    candidates = [f"`processed.wise_app_backend__{snake}`"]
    if lc != snake:
        candidates.append(f"`processed.wise_app_backend__{lc}`")
    out.append(f"- **Athena counterpart**: try {' or '.join(candidates)} — verify in `schemas/INDEX.md`.")
    out.append("")

    if indexes:
        out.append("## Indexes")
        out.append("")
        for idx in indexes:
            out.append(f"- `{idx}`")
        out.append("")

    if sub_schema_names:
        out.append("## Local sub-schemas referenced")
        out.append("")
        out.append(", ".join(f"`{n}`" for n in sub_schema_names))
        out.append("")

    out.append("## Fields")
    out.append("")
    out.append("| Path | Type | Ref | Enum | Required | Default | Notes |")
    out.append("| --- | --- | --- | --- | --- | --- | --- |")
    for f in fields:
        enum = ", ".join(f.enum) if f.enum else ""
        if len(enum) > 60:
            enum = enum[:57] + "…"
        flags = []
        if f.required:
            flags.append("required")
        if f.unique:
            flags.append("unique")
        if f.indexed:
            flags.append("indexed")
        flag_str = ", ".join(flags)
        default = (f.default or "").replace("|", "\\|").replace("\n", " ")
        if len(default) > 40:
            default = default[:37] + "…"
        out.append(f"| `{f.path}` | `{f.type}` | {('`' + f.ref + '`') if f.ref else ''} | {enum} | {flag_str} | {default} | {f.notes} |")
    out.append("")
    out.append(HUMAN_MARKER)
    out.append("")
    out.append("<!-- Add human notes (descriptions, gotchas) below this line. -->")
    out.append("")
    return "\n".join(out)


def write_doc(p: Path, new_content: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    if p.exists():
        old = p.read_text()
        if HUMAN_MARKER in old:
            human = old.split(HUMAN_MARKER, 1)[1]
            new_content = new_content.split(HUMAN_MARKER, 1)[0] + HUMAN_MARKER + human
    p.write_text(new_content)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

@dataclass
class ParsedFile:
    file: Path
    file_rel: str
    sub_schemas: dict[str, SchemaInfo]
    indexes: list[str]
    models: list[tuple[str, str, str]]  # (model_name, schema_var, collection)


def parse_file(path: Path, repo_root: Path) -> ParsedFile:
    text = strip_comments(path.read_text())
    rel = path.relative_to(repo_root.parent.parent if path.is_absolute() else Path.cwd())
    raw_defs = find_schema_definitions(text)  # {name: (body, opts)}
    # Two passes so sub-schemas can resolve each other where possible.
    sub_schemas: dict[str, SchemaInfo] = {n: SchemaInfo(name=n) for n in raw_defs}
    for name, (body, opts) in raw_defs.items():
        info = sub_schemas[name]
        info.fields = parse_schema_body(body, sub_schemas)
        info.sub_schema_options = parse_options(opts) if opts else {}
    indexes = find_indexes_array(text)
    models = find_models(text)
    return ParsedFile(file=path, file_rel=str(path), sub_schemas=sub_schemas,
                      indexes=indexes, models=models)


def derive_collection(model_name: str, schema_var: str,
                      sub_schemas: dict[str, SchemaInfo],
                      explicit_arg: str) -> str:
    """Resolve the actual Mongo collection name for a model.

    Order of precedence:
      1. Third arg to `mongoose.model('X', schema, 'collection')`.
      2. `{ collection: 'Y' }` in the schema's options arg.
      3. Mongoose default = lowercase + pluralize of model name (we don't pluralize;
         document the model name as-is and note the default rule)."""
    if explicit_arg:
        return explicit_arg
    schema = sub_schemas.get(schema_var)
    if schema and "collection" in schema.sub_schema_options:
        return schema.sub_schema_options["collection"].strip("'\"")
    return model_name


def write_index(parsed: list[tuple[ParsedFile, str, str, str]]) -> None:
    out = ["# Backend-API (Mongoose) Schema Index", "",
           f"_Last synced: {datetime.now(timezone.utc).isoformat(timespec='seconds')}_", "",
           "Static-extracted from `wise/backend-api/src/models/*.js`. One row per model declaration.", ""]
    out.append("| Collection | Model | File |")
    out.append("| --- | --- | --- |")
    for pf, model_name, collection, file_rel in sorted(parsed, key=lambda x: x[2]):
        rel_md = (OUTPUT_DIR / f"{collection}.md").relative_to(INDEX_PATH.parent).as_posix()
        out.append(f"| [`{collection}`]({rel_md}) | `{model_name}` | `{file_rel}` |")
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    INDEX_PATH.write_text("\n".join(out) + "\n")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--backend-api", required=True,
                    help="Path to wise/backend-api repo (e.g. ~/Documents/wise/backend-api)")
    ap.add_argument("--file", help="Restrict to a single model file (basename, e.g. Classroom.js)")
    args = ap.parse_args()

    repo = Path(args.backend_api).expanduser().resolve()
    models_dir = repo / "src" / "models"
    if not models_dir.is_dir():
        print(f"Models directory not found: {models_dir}", file=sys.stderr)
        return 2

    files = sorted(models_dir.glob("*.js"))
    if args.file:
        files = [f for f in files if f.name == args.file]
    print(f"Parsing {len(files)} model file(s) from {models_dir}")

    rendered: list[tuple[ParsedFile, str, str, str]] = []
    for f in files:
        try:
            pf = parse_file(f, repo)
        except Exception as e:
            print(f"  [skip] {f.name}: {e}", file=sys.stderr)
            continue
        if not pf.models:
            print(f"  [info] {f.name}: no mongoose.model() found (probably a sub-schema-only file)")
            continue
        for model_name, schema_var, explicit_collection in pf.models:
            collection = derive_collection(model_name, schema_var, pf.sub_schemas, explicit_collection)
            schema = pf.sub_schemas.get(schema_var)
            if not schema:
                print(f"  [warn] {f.name}: model '{model_name}' references unknown schema var '{schema_var}'", file=sys.stderr)
                continue
            expanded = expand_fields(schema.fields, pf.sub_schemas)
            file_rel = f"src/models/{f.name}"
            md = render_md(model_name, collection, file_rel, pf.indexes,
                           expanded, sorted(pf.sub_schemas.keys()))
            # Filename-safe: replace spaces and slashes (collection names like
            # "study materials" exist in the wild). Front-matter still carries
            # the real collection name verbatim.
            safe_name = re.sub(r"[\s/]+", "_", collection)
            target = OUTPUT_DIR / f"{safe_name}.md"
            write_doc(target, md)
            rendered.append((pf, model_name, collection, file_rel))
            print(f"  - {model_name} → {collection} ({len(expanded)} fields)")

    write_index(rendered)
    print(f"\nDone. Wrote {len(rendered)} collection file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
