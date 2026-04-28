#!/usr/bin/env python3
"""
extract_deps.py — parse view DDLs already saved under schemas/ and emit:

  - semantics/dependencies.md  (forward + reverse view-table graph)
  - semantics/joins.md         (deduped join clauses observed across views)

No Athena queries. Run after sync_schemas.py.
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = ROOT / "schemas"
SEMANTICS_DIR = ROOT / "semantics"

DDL_FENCE = re.compile(r"```sql\n(.*?)\n```", re.DOTALL)

# Identifier: `db`.`table`, "db"."table", db.table, or bare table.
IDENT = r'(?:"[^"]+"|`[^`]+`|[A-Za-z_][\w]*)'
QUALIFIED = re.compile(rf"({IDENT})\.({IDENT})|({IDENT})")

# FROM / JOIN <ref>  — capture next identifier-or-qualified, possibly aliased.
FROM_JOIN = re.compile(
    rf"\b(?:FROM|JOIN)\s+({IDENT}(?:\.{IDENT})?)(?:\s+(?:AS\s+)?({IDENT}))?",
    re.IGNORECASE,
)

# ON <left> = <right>  — capture both sides as `<alias_or_table>.<col>` patterns.
ON_EQ = re.compile(
    rf"\bON\s+\(?\s*({IDENT}(?:\.{IDENT})?)\s*=\s*({IDENT}(?:\.{IDENT})?)",
    re.IGNORECASE,
)


def _strip_quote(s: str) -> str:
    s = s.strip()
    if s.startswith('"') and s.endswith('"'):
        return s[1:-1]
    if s.startswith("`") and s.endswith("`"):
        return s[1:-1]
    return s


def parse_ddl(ddl: str, current_db: str) -> tuple[list[tuple[str, str]], list[tuple[str, str]]]:
    """
    Returns (sources, joins) where:
      sources: [(db, table), ...]  — every FROM/JOIN target, qualified to db when possible
      joins:   [(left_qualified, right_qualified), ...]  — raw ON equality pairs
    """
    sources: list[tuple[str, str]] = []
    aliases: dict[str, tuple[str, str]] = {}  # alias -> (db, table)

    for m in FROM_JOIN.finditer(ddl):
        ref = m.group(1)
        alias = m.group(2)
        if "." in ref:
            db_part, tbl_part = ref.split(".", 1)
            db, tbl = _strip_quote(db_part), _strip_quote(tbl_part)
        else:
            db, tbl = current_db, _strip_quote(ref)
        if tbl.lower() in ("unnest", "lateral", "select"):
            continue
        sources.append((db, tbl))
        if alias:
            aliases[_strip_quote(alias).lower()] = (db, tbl)
        # Also register the bare table name as an alias to itself.
        aliases.setdefault(tbl.lower(), (db, tbl))

    joins: list[tuple[str, str]] = []
    for m in ON_EQ.finditer(ddl):
        left, right = m.group(1), m.group(2)
        joins.append((_resolve(left, aliases, current_db), _resolve(right, aliases, current_db)))

    return sources, joins


def _resolve(ref: str, aliases: dict[str, tuple[str, str]], current_db: str) -> str:
    """Resolve `alias.col` or `tbl.col` or `col` into `<db>.<table>.<col>` when possible."""
    parts = [p for p in re.split(r"\.", ref) if p]
    parts = [_strip_quote(p) for p in parts]
    if len(parts) == 1:
        return parts[0]
    if len(parts) == 2:
        prefix, col = parts
        a = aliases.get(prefix.lower())
        if a:
            return f"{a[0]}.{a[1]}.{col}"
        return f"{prefix}.{col}"
    if len(parts) >= 3:
        return ".".join(parts)
    return ref


def parse_file(path: Path) -> tuple[str, str, str, str | None]:
    """Returns (layer, db, name, ddl_or_None)."""
    text = path.read_text()
    # Layer/db from path: schemas/<layer>/<db>/<name>.md
    rel = path.relative_to(SCHEMAS_DIR).parts
    layer, db, name = rel[0], rel[1], path.stem
    m = DDL_FENCE.search(text)
    return layer, db, name, (m.group(1) if m else None)


def main() -> int:
    SEMANTICS_DIR.mkdir(parents=True, exist_ok=True)

    # forward: (db, view) -> set of (db, table)
    forward: dict[tuple[str, str], set[tuple[str, str]]] = defaultdict(set)
    # reverse: (db, table) -> set of (db, view)
    reverse: dict[tuple[str, str], set[tuple[str, str]]] = defaultdict(set)
    # joins: (left_qualified, right_qualified) -> set of source views ("db.view")
    joins: dict[tuple[str, str], set[str]] = defaultdict(set)

    files = sorted(SCHEMAS_DIR.rglob("*.md"))
    files = [f for f in files if f.name != "INDEX.md"]
    parsed_views = 0
    for f in files:
        layer, db, name, ddl = parse_file(f)
        if not ddl:
            continue
        # Only views are interesting for deps; tables' DDL doesn't reference others.
        # We detect view-ness by the DDL starting with CREATE VIEW.
        if not re.match(r"\s*CREATE\s+(OR REPLACE\s+)?VIEW", ddl, re.IGNORECASE):
            continue
        parsed_views += 1
        sources, eq_pairs = parse_ddl(ddl, current_db=db)
        view_key = (db, name)
        for src in sources:
            forward[view_key].add(src)
            reverse[src].add(view_key)
        # Normalize joins: sort the pair so (a=b) and (b=a) dedupe.
        for left, right in eq_pairs:
            pair = tuple(sorted([left, right]))
            joins[pair].add(f"{db}.{name}")

    write_dependencies(forward, reverse, parsed_views)
    write_joins(joins)
    print(f"Parsed {parsed_views} views. {len(forward)} forward edges, "
          f"{len(reverse)} downstream tables, {len(joins)} unique join pairs.")
    return 0


def write_dependencies(forward, reverse, view_count) -> None:
    out = ["# View dependency graph",
           "",
           f"_Auto-generated from view DDLs in `schemas/`. {view_count} views parsed._",
           "",
           "## Forward (view → tables it reads)",
           ""]
    for (db, view), srcs in sorted(forward.items()):
        out.append(f"### `{db}.{view}`")
        for s_db, s_tbl in sorted(srcs):
            out.append(f"- `{s_db}.{s_tbl}`")
        out.append("")
    out.append("## Reverse (table → views that read it)")
    out.append("")
    for (db, tbl), views in sorted(reverse.items()):
        out.append(f"### `{db}.{tbl}`")
        for v_db, v_view in sorted(views):
            out.append(f"- `{v_db}.{v_view}`")
        out.append("")
    (SEMANTICS_DIR / "dependencies.md").write_text("\n".join(out))


def write_joins(joins: dict[tuple[str, str], set[str]]) -> None:
    out = ["# Auto-extracted join clauses",
           "",
           "_Mined from view DDLs. Each entry is a `LEFT = RIGHT` equality observed inside an `ON` clause, with the views in which it appears. Use as **hints**, not a contract — verify against the table's schema file before relying on them._",
           "",
           "| Left | Right | Seen in |",
           "| --- | --- | --- |"]
    for (l, r), views in sorted(joins.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        seen = ", ".join(f"`{v}`" for v in sorted(views)[:5])
        more = f" (+{len(views)-5} more)" if len(views) > 5 else ""
        out.append(f"| `{l}` | `{r}` | {seen}{more} |")
    (SEMANTICS_DIR / "joins.md").write_text("\n".join(out))


if __name__ == "__main__":
    sys.exit(main())
