# COMPACT — athena-agent

Curated digest for experts answering asks from this repo. **Read this before you reason.**
Then `grep -ril "<keywords>" knowledge/asks/` for a past answer to the same question.

Seeded 2026-09-11 from README.md + CLAUDE.md. Everything below is derived from the repo,
not from an ask; ask-derived facts accumulate under `knowledge/asks/`.

## What this repo is

A knowledge base + read-only MCP server that turns plain-English questions about the AWS
Athena warehouse into correct, efficient SQL. The warehouse is fed from MongoDB, so **string
columns frequently hide rich JSON** — that is the single most common source of wrong answers.

## Layout worth knowing

- `schemas/INDEX.md` — generated table of contents. **Start here to locate a table.**
- `schemas/processed/`, `schemas/raw/`, `schemas/source/`, `schemas/_gaps/` — one `.md` per table.
- `semantics/glossary.md` — business term → table/column.
- `semantics/joins.md` — canonical join keys (hand-curated + mined). **Use these, do not guess joins.**
- `semantics/dependencies.md` — view → upstream-table graph.
- `examples/` — vetted SQL patterns; prefer reusing one over writing fresh SQL.

Each table file carries: YAML front-matter (database, type, **partition keys**, S3 location,
last-synced), a typed column table, enum-like value distributions for low-cardinality strings,
an inferred JSON path tree for varchar-holding-JSON columns, the full `SHOW CREATE` DDL, and a
`<!-- HUMAN NOTES BELOW -->` marker — **anything below that marker survives re-sync**, so that
is where a durable correction belongs.

## Regions: IN vs NA

Two parallel databases hold the same shapes for two deployments:

| Region | Database |
|---|---|
| IN | `processed` |
| NA | `processed_na` |

They are separate databases, not a partition column. A cross-region question means **two
queries**, one per database. A namespace can in principle exist in both — do not assume one.

## Query review — what to check, in order

1. **Partition filters.** Missing one turns a cheap query into a full scan. Partition keys are
   in each table file's front-matter.
2. **JSON in varchar.** If a column holds JSON, a plain `=` comparison silently matches nothing.
   Use the inferred JSON path tree in the table file.
3. **Joins.** Check `semantics/joins.md`. A wrong-but-plausible join key is the classic silent
   wrong answer — it returns rows, just the wrong ones.
4. **Views over raw.** Prefer the documented view; `semantics/dependencies.md` says what it wraps.
5. **Region.** Did the query pick the right database, and does the question need both?
6. **Validate.** `explain_query` first, then `run_query` with a small `max_rows`.

## Safety guarantees of the MCP server

Only `SELECT / WITH / SHOW / DESCRIBE / EXPLAIN`; DML and DDL rejected by token match;
multi-statement payloads rejected; workgroup + S3 output pinned by config (not by tool args);
per-query timeout and bytes-scanned cap; sensitive columns redacted before rows reach the model.

**This expert is `ask` only.** It reviews and explains. It does not write, deploy, or push.

## Credentials

boto3 default chain — `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` / `AWS_SESSION_TOKEN`, or
`AWS_PROFILE`, or SSO / instance role. `scripts/config.yaml` is gitignored.
**Names only, here and in every answer. Never a value.**
