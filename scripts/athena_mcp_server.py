#!/usr/bin/env python3
"""
Athena MCP server (read-only).

Exposes a small, hardened set of tools for Claude to introspect and query the
Athena warehouse described in this repo.

Safety guarantees:
  - Only SELECT / WITH / SHOW / DESCRIBE / EXPLAIN statements are accepted.
  - DML/DDL keywords (INSERT, UPDATE, DELETE, DROP, CREATE, ALTER, TRUNCATE,
    GRANT, REVOKE, MERGE, RENAME) are rejected by token match.
  - Multiple statements (additional `;` after the first) are rejected.
  - Workgroup and S3 output location are pinned via env / config — not tool args.
  - Per-query timeout (default 60s); query is cancelled on timeout.
  - Per-query bytes-scanned cap (logged in the response; Athena does not pre-cap).
  - Sensitive columns (loginpin, phonenumber, email, password, token, secret,
    apikey, plus anything in $ATHENA_REDACT_COLS) are replaced with [REDACTED]
    before rows are returned to the model.

Run as a stdio MCP server (configured via .mcp.json).
"""
from __future__ import annotations

import os
import re
import sys
import time
from pathlib import Path
from typing import Any

import boto3
import yaml
from mcp.server.fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = ROOT / "scripts" / "config.yaml"

if not CONFIG_PATH.exists():
    print(f"[athena-mcp] missing {CONFIG_PATH}", file=sys.stderr)
    sys.exit(2)

_cfg = yaml.safe_load(CONFIG_PATH.read_text())
REGION = os.getenv("AWS_REGION") or _cfg["aws"]["region"]
WORKGROUP = os.getenv("ATHENA_WORKGROUP") or _cfg["aws"]["workgroup"]
OUTPUT_LOCATION = os.getenv("ATHENA_OUTPUT_LOCATION") or _cfg["aws"]["output_location"]
QUERY_TIMEOUT_S = int(os.getenv("ATHENA_TIMEOUT_S", "60"))
PER_QUERY_BYTES_WARN = int(os.getenv("ATHENA_BYTES_WARN", str(2 * (1 << 30))))  # 2 GiB

REDACT_DEFAULT = {"loginpin", "phonenumber", "email", "password", "token", "secret", "apikey"}
_extra = os.getenv("ATHENA_REDACT_COLS", "")
REDACT = (REDACT_DEFAULT | {x.strip().lower() for x in _extra.split(",") if x.strip()})

# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

ALLOWED_FIRST = {"SELECT", "WITH", "SHOW", "DESCRIBE", "DESC", "EXPLAIN"}
DENY_TOKENS = re.compile(
    r"\b(?:INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|TRUNCATE|GRANT|REVOKE|MERGE|RENAME|VACUUM|ANALYZE|MSCK|UNLOAD)\b",
    re.I,
)
IDENT_RE = re.compile(r"^[A-Za-z_][\w]{0,127}$")


def _strip_comments(sql: str) -> str:
    sql = re.sub(r"--[^\n]*", "", sql)
    sql = re.sub(r"/\*.*?\*/", "", sql, flags=re.S)
    return sql.strip()


def _validate_sql(sql: str) -> str:
    s = _strip_comments(sql).rstrip(";").strip()
    if not s:
        raise ValueError("Empty query.")
    first = s.split(None, 1)[0].upper()
    if first not in ALLOWED_FIRST:
        raise ValueError(
            f"Only {sorted(ALLOWED_FIRST)} statements are allowed; got '{first}'."
        )
    if DENY_TOKENS.search(s):
        raise ValueError("Query contains a forbidden DML/DDL keyword.")
    if ";" in s:
        raise ValueError("Multiple statements are not allowed.")
    return s


def _check_ident(name: str, label: str) -> str:
    if not IDENT_RE.match(name):
        raise ValueError(f"Invalid {label}: {name!r}")
    return name


# ---------------------------------------------------------------------------
# Athena
# ---------------------------------------------------------------------------

_athena = boto3.client("athena", region_name=REGION)


def _start(sql: str) -> str:
    return _athena.start_query_execution(
        QueryString=sql,
        WorkGroup=WORKGROUP,
        ResultConfiguration={"OutputLocation": OUTPUT_LOCATION},
    )["QueryExecutionId"]


def _wait(qid: str, timeout_s: int) -> dict:
    start = time.time()
    while True:
        ex = _athena.get_query_execution(QueryExecutionId=qid)["QueryExecution"]
        state = ex["Status"]["State"]
        if state in ("SUCCEEDED", "FAILED", "CANCELLED"):
            return ex
        if time.time() - start > timeout_s:
            try:
                _athena.stop_query_execution(QueryExecutionId=qid)
            except Exception:
                pass
            raise TimeoutError(f"Query exceeded {timeout_s}s and was cancelled.")
        time.sleep(0.5)


def _fetch(qid: str, max_rows: int) -> list[dict]:
    paginator = _athena.get_paginator("get_query_results")
    out: list[dict] = []
    header: list[str] | None = None
    first_page = True
    for page in paginator.paginate(QueryExecutionId=qid):
        rs = page["ResultSet"]
        cols = [c["Name"] for c in rs["ResultSetMetadata"]["ColumnInfo"]]
        if header is None:
            header = cols
        rows = rs["Rows"]
        if first_page and rows:
            first_cells = [c.get("VarCharValue") for c in rows[0]["Data"]]
            if first_cells == header:
                rows = rows[1:]
            first_page = False
        for r in rows:
            cells = [c.get("VarCharValue") for c in r["Data"]]
            row = dict(zip(header, cells))
            for k in row:
                if k.lower() in REDACT:
                    row[k] = "[REDACTED]"
            out.append(row)
            if len(out) >= max_rows:
                return out
    return out


def _execute(sql: str, max_rows: int = 200, timeout_s: int = QUERY_TIMEOUT_S,
             validate: bool = True) -> dict:
    """Validate, start, wait, fetch. Returns rows + execution stats.

    `validate=False` is for internal calls that build SQL from sanitized identifiers
    (e.g. SHOW CREATE TABLE) and would otherwise trip the deny list.
    """
    if validate:
        sql = _validate_sql(sql)
    qid = _start(sql)
    ex = _wait(qid, timeout_s)
    state = ex["Status"]["State"]
    scanned = ex.get("Statistics", {}).get("DataScannedInBytes", 0) or 0
    if state != "SUCCEEDED":
        return {
            "ok": False,
            "state": state,
            "reason": ex["Status"].get("StateChangeReason", ""),
            "bytes_scanned": scanned,
            "query_id": qid,
        }
    rows = _fetch(qid, max_rows=max_rows)
    return {
        "ok": True,
        "rows": rows,
        "row_count": len(rows),
        "truncated": len(rows) >= max_rows,
        "bytes_scanned": scanned,
        "warn_bytes_exceeded": scanned > PER_QUERY_BYTES_WARN,
        "query_id": qid,
    }


# ---------------------------------------------------------------------------
# MCP tools
# ---------------------------------------------------------------------------

mcp = FastMCP("athena")


@mcp.tool()
def list_databases() -> list[str]:
    """List all Athena databases visible to the configured workgroup."""
    res = _execute("SHOW DATABASES", max_rows=500)
    if not res["ok"]:
        raise RuntimeError(f"{res['state']}: {res.get('reason')}")
    return [next(iter(r.values())) for r in res["rows"]]


@mcp.tool()
def list_tables(database: str) -> dict[str, list[str]]:
    """List tables and views in a database. Returns {'tables': [...], 'views': [...]}."""
    db = _check_ident(database, "database")
    t_res = _execute(f"SHOW TABLES IN `{db}`", max_rows=2000)
    if not t_res["ok"]:
        raise RuntimeError(f"{t_res['state']}: {t_res.get('reason')}")
    all_names = [next(iter(r.values())) for r in t_res["rows"]]
    try:
        v_res = _execute(f'SHOW VIEWS IN "{db}"', max_rows=2000)
        views = [next(iter(r.values())) for r in v_res["rows"]] if v_res["ok"] else []
    except Exception:
        views = []
    view_set = set(views)
    return {
        "tables": [n for n in all_names if n not in view_set],
        "views": views,
    }


@mcp.tool()
def describe_table(database: str, table: str) -> dict:
    """Return the column list and DDL for a table or view."""
    db = _check_ident(database, "database")
    tb = _check_ident(table, "table")
    desc = _execute(f"DESCRIBE `{db}`.`{tb}`", max_rows=2000)
    if not desc["ok"]:
        raise RuntimeError(f"{desc['state']}: {desc.get('reason')}")
    columns: list[dict] = []
    in_partition = False
    partitions: list[str] = []
    for r in desc["rows"]:
        first = (next(iter(r.values())) or "").strip()
        if not first or first.startswith("#"):
            if "Partition" in first:
                in_partition = True
            continue
        parts = re.split(r"\s{2,}|\t", first)
        if len(parts) < 2:
            parts = first.split(None, 2)
        name = parts[0].strip()
        dtype = parts[1].strip() if len(parts) > 1 else ""
        if in_partition:
            partitions.append(name)
        else:
            columns.append({"name": name, "type": dtype})

    # DDL: try VIEW first, fall back to TABLE. Identifiers are sanitized via _check_ident,
    # so we skip the deny-list validator (which would trip on the word CREATE).
    ddl = None
    for sql in (f'SHOW CREATE VIEW "{db}"."{tb}"',
                f"SHOW CREATE TABLE `{db}`.`{tb}`"):
        try:
            r = _execute(sql, max_rows=500, validate=False)
            if r["ok"]:
                ddl = "\n".join(next(iter(x.values()), "") or "" for x in r["rows"])
                break
        except Exception:
            continue
    return {"database": db, "table": tb, "columns": columns,
            "partition_keys": partitions, "ddl": ddl}


@mcp.tool()
def get_partitions(database: str, table: str, max_rows: int = 200) -> list[dict]:
    """List existing partitions of a table (most recent first)."""
    db = _check_ident(database, "database")
    tb = _check_ident(table, "table")
    res = _execute(f'SHOW PARTITIONS "{db}"."{tb}"', max_rows=max_rows)
    if not res["ok"]:
        raise RuntimeError(f"{res['state']}: {res.get('reason')}")
    # Return the partition strings sorted desc (best-effort lexicographic).
    parts = [next(iter(r.values())) for r in res["rows"]]
    parts.sort(reverse=True)
    return [{"partition": p} for p in parts[:max_rows]]


@mcp.tool()
def explain_query(sql: str) -> dict:
    """Run EXPLAIN on a query to validate it parses and inspect the plan. Does not execute the query."""
    inner = _validate_sql(sql)  # validates the inner statement
    return _execute(f"EXPLAIN {inner}", max_rows=500)


@mcp.tool()
def run_query(sql: str, max_rows: int = 200, timeout_s: int = QUERY_TIMEOUT_S) -> dict:
    """Run a read-only query (SELECT/WITH/SHOW/DESCRIBE/EXPLAIN). Returns up to `max_rows` rows.

    Sensitive columns (loginpin, phonenumber, email, password, token, secret, apikey)
    are redacted before being returned. Do NOT attempt to bypass redaction —
    request the data via aggregates instead.
    """
    if max_rows > 1000:
        max_rows = 1000
    if timeout_s > 300:
        timeout_s = 300
    return _execute(sql, max_rows=max_rows, timeout_s=timeout_s)


if __name__ == "__main__":
    mcp.run()
