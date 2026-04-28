# Athena Agent — Claude Playbook

This repo is a knowledge base for an AWS Athena warehouse fed by MongoDB. Your job, when invoked here, is to translate plain-English requirements into correct, efficient Athena (Presto) SQL.

## Pipeline at a glance

MongoDB → flattened json.gz → S3 → Athena `raw` external tables → CTAS → Athena `processed` (query-optimized) → Athena `views` (curated, pre-joined).

**Refresh cadence: full Mongo collection dump once per day.** Same-day / "last hour" questions are not answerable from this warehouse — scope windows in days (e.g. trailing 7d / 28d).

- **`raw`**: faithful, wide, slow. Avoid unless `processed` is missing what you need.
- **`processed`**: prefer for analytical queries. Partitioned, columnar.
- **`views`**: prefer for canonical entities and common joins.

Because data originates in Mongo, **string columns frequently hold JSON**. Always check `## Inferred JSON structure` in the table's schema file before writing SQL — fields you need may live inside a varchar.

## Where to look (in order)

1. `schemas/INDEX.md` — table of contents.
2. `schemas/<layer>/<db>/<table>.md` — generated columns + inferred JSON paths + DDL + human notes.
3. `semantics/joins.md` — canonical join keys between entities.
4. `semantics/glossary.md` — business term → table/column mapping.
5. `examples/` — vetted SQL patterns. Reuse when one matches.

To find a table for an entity: `grep -ri "<entity>" schemas/ semantics/`.

## Hard rules for SQL you write

- **Prefer `views` > `processed` > `raw`** in that order.
- **Always include a partition filter** when querying `raw` or partitioned `processed` tables. The partition keys are listed in each table's schema file.
- **Never `SELECT *`** in returned queries; project the columns the user actually needs.
- For JSON-bearing varchar columns, extract with `json_extract_scalar(col, '$.path')` (scalar) or `json_extract` + `CAST(... AS ARRAY<...>)` (nested). Reference the inferred path tree in the schema file.
- Inferred JSON paths are **not authoritative** — they come from a sample. Treat absent keys as nullable; cast defensively.
- Use double quotes for identifiers with special chars: `"db"."table"`.
- Timestamps: check the column's notes; assume UTC unless the schema file says otherwise.

## Athena MCP (`athena` server)

Tools available (read-only, hardened — only SELECT/WITH/SHOW/DESCRIBE/EXPLAIN accepted; DML/DDL rejected; sensitive columns redacted):

- `list_databases()` — all databases.
- `list_tables(database)` — `{tables: [...], views: [...]}`.
- `describe_table(database, table)` — columns, partition keys, full DDL. Use this instead of `SHOW CREATE TABLE` via `run_query` (the latter is blocked by the validator).
- `get_partitions(database, table)` — existing partition values, most recent first.
- `explain_query(sql)` — wraps the SQL in `EXPLAIN`. Use to validate syntax/plan without executing.
- `run_query(sql, max_rows=200, timeout_s=60)` — runs read-only SQL. Output bytes-scanned + truncation are returned alongside rows.

### Validation loop (do this before returning SQL)

1. Draft the query against the conventions above.
2. `explain_query` it. Fix any errors.
3. `run_query` with a small `max_rows` (≤100) to sanity-check shape and types.
4. Then return the final SQL with a brief explanation.

Sensitive columns (`loginpin`, `phonenumber`, `email`, `password`, `token`, `secret`, `apikey`, plus anything in `$ATHENA_REDACT_COLS`) come back as `[REDACTED]`. Don't try to bypass — request aggregates instead.

**Redaction matches OUTPUT column names, not just source columns.** A pivoted column aliased `email` will be redacted even if the source column is `answer`. When pivoting form/survey data into wide columns, name the outputs e.g. `reg_email_addr`, `reg_contact_number` — descriptive but not on the redaction list. This is a UX workaround, not a bypass: the underlying values are not sensitive when they're survey answers from the user themselves.

## Updating the knowledge base

- Schema regen: `python scripts/sync_schemas.py` (uses `scripts/config.yaml`).
  - Idempotent. Anything below `<!-- HUMAN NOTES BELOW -->` in each table file is preserved.
- When you discover non-obvious knowledge during a session (a column that means something surprising, a join that needs a coalesce, a bad partition layout), add it under the human-notes marker of the relevant table or to `semantics/`.
- When a non-trivial query worked, drop it into `examples/<short-name>.sql` with a one-line `-- intent:` comment.

## When the user asks for SQL

1. Identify the entities and metrics in the request.
2. Find candidate tables/views via `schemas/INDEX.md` and grep.
3. Read the relevant table file(s) — pay attention to inferred JSON paths and human notes.
4. Check `semantics/joins.md` for canonical join keys.
5. Draft the query. Apply hard rules above.
6. Validate via MCP (`EXPLAIN` + `LIMIT 100`).
7. Return the SQL with a brief explanation of the columns used and any assumptions.
