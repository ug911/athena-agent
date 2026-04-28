# athena-agent

A knowledge base + MCP server that lets Claude Code translate plain-English questions about an AWS Athena warehouse into correct, efficient SQL.

The warehouse is fed from MongoDB, so string columns frequently hide rich JSON. This repo solves that problem twice over: (a) a sync script that introspects every table and infers nested JSON structure into committed Markdown, and (b) a hardened, read-only MCP server that lets Claude `EXPLAIN` and `LIMIT 100` queries against Athena before returning final SQL to the user.

## Repo layout

```
athena-agent/
├── CLAUDE.md                   # playbook Claude reads on every session
├── .mcp.json                   # registers the Athena MCP server
├── schemas/
│   ├── INDEX.md                # generated table of contents
│   ├── processed/              # processed-layer table docs (one .md per table)
│   └── raw/                    # raw-layer table docs
├── semantics/
│   ├── glossary.md             # business term → table/column mapping
│   ├── joins.md                # canonical join keys (hand-curated + mined)
│   └── dependencies.md         # view → upstream-table dependency graph
├── examples/                   # vetted SQL patterns Claude can reuse
└── scripts/
    ├── athena_mcp_server.py    # read-only Athena MCP server
    ├── sync_schemas.py         # regenerates schemas/ from Athena
    ├── extract_deps.py         # builds semantics/dependencies.md from view DDLs
    ├── config.example.yaml     # copy → config.yaml and fill in
    └── requirements.txt
```

Each table file under `schemas/` carries:
- YAML front-matter (database, type, partition keys, S3 location, last-synced timestamp)
- a typed columns table
- enum-like value distributions (for low-cardinality string columns)
- an inferred JSON path tree (for varchar columns that hold JSON)
- the full `SHOW CREATE` DDL
- a `<!-- HUMAN NOTES BELOW -->` marker — anything below it is preserved across re-syncs

## How Claude uses this repo

When you invoke Claude Code in this directory, it reads `CLAUDE.md`, then locates relevant tables by grepping `schemas/INDEX.md` and `semantics/`. It reads the relevant table file(s), drafts SQL that respects the conventions documented there (partition filters, JSON extraction, view-over-raw preference), and validates against Athena via the MCP server (`explain_query` then `run_query` with a small `max_rows` cap) before returning final SQL.

The MCP server enforces the safety guarantees so you can let Claude run real queries without worry:
- only `SELECT / WITH / SHOW / DESCRIBE / EXPLAIN` accepted; DML/DDL rejected by token match
- multiple-statement payloads rejected
- workgroup + S3 output location pinned by config (not tool args)
- per-query timeout + bytes-scanned cap
- sensitive columns redacted before rows reach the model

## Initial setup

### 1. Clone and create a virtualenv

```bash
git clone https://github.com/ug911/athena-agent.git
cd athena-agent
python3 -m venv .venv
.venv/bin/pip install -r scripts/requirements.txt
```

### 2. AWS credentials

The sync script and MCP server use `boto3`'s default credential chain. Either:
- export `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` / `AWS_SESSION_TOKEN`, or
- set `AWS_PROFILE` to a profile in `~/.aws/credentials`, or
- use SSO / `aws-vault` / instance role — anything boto3 understands.

The IAM principal needs read access to Athena (`StartQueryExecution`, `GetQueryExecution`, `GetQueryResults`, `StopQueryExecution`), Glue catalog read (`GetDatabase`, `GetTable`), and read+write on the S3 bucket configured as `output_location`. **Use a read-only workgroup if your org supports it** — the MCP server rejects DML/DDL itself, but defense in depth never hurts.

### 3. Configure the warehouse

```bash
cp scripts/config.example.yaml scripts/config.yaml
# edit scripts/config.yaml — fill in region, workgroup, S3 results bucket,
# and the list of databases under each layer (raw / processed / views).
```

`scripts/config.yaml` is gitignored.

### 4. Run the initial schema sync

```bash
.venv/bin/python scripts/sync_schemas.py
```

This walks every database in your config, runs `SHOW TABLES` / `DESCRIBE` / `SHOW CREATE`, samples 200 rows per table for JSON inference, and writes one Markdown file per table. Expect a few minutes and a few GB scanned for a mid-size warehouse.

Useful flags:
- `--no-sample` — schema-only, skip the JSON sampling (much faster, no row reads)
- `--use-cache` — reuse `.cache/samples/` from a prior run instead of re-querying Athena
- `--cache-only` — only render tables that already have a cached sample
- `--layer processed` / `--database X` / `--table Y` — narrow the scope
- `--scrub` — re-redact existing markdown without hitting Athena (use after expanding the sensitive-name list in the script)

### 5. Connect the MCP server in Claude Code

`.mcp.json` is already wired up — when you run `claude` in this directory it will spawn `scripts/athena_mcp_server.py` via the venv. The first run inside Claude will prompt you to approve the server.

Confirm with a quick test query: ask Claude "list databases". It should call `list_databases()` via MCP.

## Redaction policy

Sampling reads raw rows from Athena, which means sensitive values can land in committed Markdown unless they're scrubbed. `sync_schemas.py` applies four layers of redaction:

1. **Sensitive leaf-name match** — exact + substring lists covering passwords, the token family, secrets, API keys, login PINs, emails, phone numbers, gov-id fields, and personal-name fields (`displayname`, `fullname`, `firstname`, `student_name`, etc.).
2. **Path-aware** — bare `name` is redacted only when nested under a person-bearing parent (`participants[].name`, `users[].name`, `students[].name` …). Preserves entity names like `class.name`, `institute.name`, `file.filename`. The walker propagates the outer column name as path context so a top-level `participants` array correctly cascades to its child `name`.
3. **Value-pattern** — JWTs, Google OAuth refresh tokens, AWS access keys, AWS account IDs in ARNs, S3 bucket paths, Google API keys, Slack / GitHub / Stripe tokens, plain emails, international phone numbers. Catches credentials embedded under non-sensitive leaf names (e.g. a JWT inside `query_string`).
4. **Final pass over rendered markdown** — catches credential / bucket / account-id strings sourced from DDL or YAML front-matter that the JSON walker never touches (e.g. `LOCATION 's3://<bucket>/...'`).

The MCP server has its own runtime redaction set (`loginpin, phonenumber, email, password, token, secret, apikey`, plus anything in `$ATHENA_REDACT_COLS`) that fires on query results before they reach the model. **Note**: the MCP guard matches on **output column name**, so when pivoting form/survey answers into wide columns, name them `reg_email_addr`, `reg_contact_number` style — not `email` / `phone_number` — or they'll be redacted to `[REDACTED]` before you see them.

If you discover a new leak class, add the leaf name or value pattern to the constants at the top of `sync_schemas.py` and re-run with `--scrub` to fix the existing markdown without re-querying Athena.

## Source-of-truth (Mongoose) schemas

The Athena warehouse is fed from MongoDB via the `wise/backend-api` repo's Mongoose schemas. To capture the *de jure* schema (what the application code declares), `scripts/sync_backend_api.py` static-parses each `models/*.js` and writes one Markdown per collection under `schemas/source/mongo/`, with nested sub-schemas resolved into a flat path tree, refs / enums / indexes preserved, and a candidate Athena table name suggested.

```bash
.venv/bin/python scripts/sync_backend_api.py --backend-api ~/Documents/wise/backend-api
```

No Mongo connection is required and no values are sampled — only field names and types are read from source — so the redaction policy that protects `sync_schemas.py` does not apply here.

The intended downstream uses are: (a) diffing against the inferred Athena schema to find extraction gaps, (b) confirming canonical join keys, and (c) sanity-checking field-name conventions when writing SQL.

### Gap report — find extraction debt

```bash
.venv/bin/python scripts/compare_schemas.py
```

Diffs each Mongo collection against its Athena counterpart and writes one report per collection under `schemas/_gaps/<collection>.md`, plus an `INDEX.md` ranked by missing-field count. Each report lists fields declared in the Mongoose schema but absent from Athena (extraction debt — widen the lake or note the field as JSON-only inside an existing varchar) and fields in Athena that aren't in Mongo any more (renamed / deprecated). Field-path matching normalizes case and underscores so `studentAttendance` (Mongo) matches `student_attendance` (Athena).

### Usage scan — which models are hot, which joins matter

```bash
.venv/bin/python scripts/scan_usage.py --backend-api ~/Documents/wise/backend-api
```

Statically scans `controllers/`, `services/`, `repositories/`, `workers/`, and `helpers/` for `<Model>.<query-method>` calls and `.populate(...)` chains. Patches each `schemas/source/mongo/<collection>.md` with a `## Usage` section showing query-method counts, populate fields (the strongest hint for "what JOINs matter in Athena"), and top call sites. Also writes `semantics/usage_patterns.md` with a global ranking and the most-populated fields across the codebase.

## Updating the knowledge base

- **Schema regen**: `python scripts/sync_schemas.py` — idempotent. Anything below `<!-- HUMAN NOTES BELOW -->` in each table file is preserved across runs, so add hand-written notes there.
- **Dependency graph regen**: `python scripts/extract_deps.py` — rebuilds `semantics/dependencies.md` and the join hints at the bottom of `semantics/joins.md` by parsing view DDLs.
- **Hand-curated joins**: edit the top section of `semantics/joins.md` directly. Verified joins go above the auto-extracted ones.
- **Glossary**: edit `semantics/glossary.md` whenever a business term needs disambiguation.
- **Vetted SQL**: when a non-trivial query worked, drop it into `examples/<short-name>.sql` with a one-line `-- intent:` comment.

When Claude finishes a non-trivial task and learns something non-obvious about the data, ask it to fold the lesson into the relevant table's human-notes section, the glossary, or `joins.md`. The repo gets sharper over time without manual upkeep.

## Cache hygiene

`sync_schemas.py` writes raw, unredacted samples to `.cache/samples/*.json.gz` for fast re-renders. The cache is gitignored, but the raw values still sit on local disk. After a sync that touches sensitive tables, consider:

```bash
rm -rf .cache/samples/
```

Re-runs will repopulate it; the redactor catches sensitive values on the way out into Markdown either way.
