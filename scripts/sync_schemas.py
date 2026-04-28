#!/usr/bin/env python3
"""
sync_schemas.py — regenerate schemas/ from AWS Athena.

Glue is NOT used. All metadata comes from Athena queries:
  SHOW SCHEMAS, SHOW TABLES, SHOW VIEWS, DESCRIBE, SHOW CREATE TABLE/VIEW.

For configured layers (default: processed), we also pull a sample of recent rows
from each table and infer the structure of any string column that holds JSON.
This is essential because tables originate from MongoDB and often hide rich
structure inside a single varchar column.

Output: one markdown file per table at
  schemas/<layer>/<db>/<table>.md
Anything below the `<!-- HUMAN NOTES BELOW -->` marker is preserved across runs.
"""
from __future__ import annotations

import argparse
import gzip
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable

import boto3
import yaml

ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = ROOT / "schemas"
CACHE_DIR = ROOT / ".cache" / "samples"
HUMAN_MARKER = "<!-- HUMAN NOTES BELOW -->"
RECENCY_CANDIDATES = ["created_at", "updated_at", "event_time", "_ts", "ts", "created", "updated"]

# Patterns for keys that should collapse to a placeholder (Mongo objects often use ID-keyed maps).
ID_KEY_PATTERNS = [
    ("oid", re.compile(r"^[0-9a-f]{24}$")),
    ("uuid", re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I)),
    ("int", re.compile(r"^\d+$")),
]
ENUM_DISTINCT_THRESHOLD = 20
ENUM_MIN_SAMPLES = 10

# ---------------------------------------------------------------------------
# Redaction
# ---------------------------------------------------------------------------
#
# Sampling reads raw rows from Athena, which means sensitive values (API keys,
# OAuth refresh tokens, login PINs, emails, phone numbers, meeting passwords)
# can land in committed schema markdown unless we redact them here.
# This list mirrors the Athena MCP server's redaction set, plus the long-tail
# of credential-like field names we have observed in the warehouse.

SENSITIVE_LEAF_NAMES = frozenset({
    # auth
    "password", "passwd", "meetingpassword",
    "loginpin", "pin", "otp", "cvv",
    "token", "refreshtoken", "accesstoken", "idtoken", "id_token",
    "authtoken", "sessiontoken", "bearertoken", "jwt",
    "secret", "secretkey", "clientsecret", "apisecret",
    "apikey", "api_key", "appkey",
    "privatekey", "private_key", "sshkey",
    "credential", "credentials",
    # PII contact
    "email", "useremail", "user_email", "contactemail", "emailid", "mail",
    "phone", "phonenumber", "phone_number", "contactnumber",
    "mobilenumber", "mobile", "contactmobile", "whatsapp",
    "whatsappnumber", "whatsapp_number",
    # gov ids
    "ssn", "aadhaar", "aadhar", "panno", "panid", "pannumber",
    # personal names (exact matches — unambiguously PII regardless of context)
    "displayname", "display_name", "fullname", "full_name",
    "firstname", "first_name", "lastname", "last_name",
    "student_name", "student_name_zoom", "ct_name", "parent_name",
    "participant_name", "username", "user_name", "parentname",
    "studentname", "teachername", "ownername", "customer_name",
})

# For the bare leaf `name`: only redact when the path indicates a person
# (e.g. `participants[].name`, `users[].name`). This preserves legitimate
# entity names like `class.name`, `institute.name`, `file.filename`.
PERSON_NAME_PATH_HINTS = (
    "participant", "user", "student", "teacher", "attendee",
    "host", "member", "instructor",
)

# Substring matches catch compound names like "userPassword", "client_apikey",
# "google_refreshtoken". Keep this list short and unambiguous.
SENSITIVE_SUBSTRINGS = (
    "password", "passwd", "secret", "apikey", "privatekey",
    "refreshtoken", "accesstoken", "uploadtoken", "authtoken",
    "sessiontoken", "bearertoken", "credential", "loginpin",
)

REDACTED = "[REDACTED]"

# Value-pattern redaction. Catches credential-shaped strings regardless of
# the column / leaf name they live under (a JWT in a URL `query_string`,
# an AWS key in free-text comment, etc.). Order matters: more-specific
# patterns first so JWTs aren't double-replaced by generic substrings.
SECRET_VALUE_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    # JWT (header.payload.signature, all base64url)
    (re.compile(r"eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+"), "[REDACTED-JWT]"),
    # Google OAuth refresh token
    (re.compile(r"1//0[A-Za-z0-9_-]{30,}"), "[REDACTED-GOOGLE-OAUTH]"),
    # AWS access key id
    (re.compile(r"\b(?:AKIA|ASIA)[0-9A-Z]{16}\b"), "[REDACTED-AWS-KEY]"),
    # Google API key
    (re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"), "[REDACTED-GOOGLE-API-KEY]"),
    # Slack tokens
    (re.compile(r"\bxox[baprs]-[0-9A-Za-z-]{10,}\b"), "[REDACTED-SLACK]"),
    # GitHub tokens
    (re.compile(r"\bgh[pousr]_[0-9A-Za-z]{36,}\b"), "[REDACTED-GITHUB]"),
    (re.compile(r"\bgithub_pat_[0-9A-Za-z_]{20,}\b"), "[REDACTED-GITHUB]"),
    # Stripe live/test keys
    (re.compile(r"\bsk_(?:live|test)_[0-9A-Za-z]{24,}\b"), "[REDACTED-STRIPE]"),
    # Email address (catches PII landing under non-`email` leaf names like `identifier`)
    (re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"), "[REDACTED-EMAIL]"),
    # International phone number (with +CC). Conservative: requires the leading `+`.
    (re.compile(r"\+[0-9][0-9 \-]{8,15}[0-9]"), "[REDACTED-PHONE]"),
    # AWS account id inside an ARN
    (re.compile(r"(arn:aws[a-z-]*:[a-z0-9-]*:[a-z0-9-]*:)[0-9]{12}(:)"), r"\1[REDACTED-AWS-ACCT]\2"),
    # S3 bucket path. Skip the `your-...` placeholder used in the example config.
    (re.compile(r"s3://(?!your-)[a-zA-Z0-9.\-]+/"), "s3://[REDACTED-BUCKET]/"),
]


def redact_secret_patterns(s: str) -> str:
    """Replace any credential-shaped substring inside `s`. No-op if `s` is short / clean."""
    if not s or not isinstance(s, str):
        return s
    for pat, repl in SECRET_VALUE_PATTERNS:
        s = pat.sub(repl, s)
    return s


def is_sensitive_leaf(name: str | None) -> bool:
    """True if this column / JSON leaf name should have its sampled values redacted."""
    if not name:
        return False
    s = name.lower()
    if s in SENSITIVE_LEAF_NAMES:
        return True
    return any(sub in s for sub in SENSITIVE_SUBSTRINGS)


def _path_leaf(path: str) -> str:
    """Last segment of a JSON path (`a.b[].c` → `c`)."""
    return path.split(".")[-1].split("[]")[-1] or path


def is_personal_name_path(path: str, leaf: str | None = None) -> bool:
    """True if a bare `name` leaf appears under a person-bearing parent path
    (e.g. `participants[].name`, `users[].name`). Preserves entity names like
    `class.name`, `institute.name`, `file.filename`."""
    leaf = (leaf if leaf is not None else _path_leaf(path)).lower()
    if leaf != "name":
        return False
    p = path.lower()
    return any(hint in p for hint in PERSON_NAME_PATH_HINTS)


# ---------------------------------------------------------------------------
# Athena client wrapper
# ---------------------------------------------------------------------------

@dataclass
class AthenaClient:
    region: str
    workgroup: str
    output_location: str
    bytes_scanned: int = 0
    max_bytes: int = 0  # global budget

    def __post_init__(self) -> None:
        self._client = boto3.client("athena", region_name=self.region)

    def query(self, sql: str, database: str | None = None, max_bytes: int | None = None,
              timeout_s: int = 90) -> list[dict]:
        """Run a query, return rows as list[dict]. Honors a per-query bytes cap and timeout."""
        if self.max_bytes and self.bytes_scanned >= self.max_bytes:
            raise RuntimeError(f"Bytes-scanned budget exhausted ({self.bytes_scanned} >= {self.max_bytes})")

        kwargs: dict[str, Any] = {
            "QueryString": sql,
            "WorkGroup": self.workgroup,
            "ResultConfiguration": {"OutputLocation": self.output_location},
        }
        if database:
            kwargs["QueryExecutionContext"] = {"Database": database}

        qid = self._client.start_query_execution(**kwargs)["QueryExecutionId"]

        # Poll with timeout.
        start = time.time()
        while True:
            ex = self._client.get_query_execution(QueryExecutionId=qid)["QueryExecution"]
            state = ex["Status"]["State"]
            if state in ("SUCCEEDED", "FAILED", "CANCELLED"):
                break
            if time.time() - start > timeout_s:
                try:
                    self._client.stop_query_execution(QueryExecutionId=qid)
                except Exception:
                    pass
                raise RuntimeError(f"Query timeout ({timeout_s}s): {sql[:120]}")
            time.sleep(0.5)

        scanned = ex.get("Statistics", {}).get("DataScannedInBytes", 0) or 0
        self.bytes_scanned += scanned
        if max_bytes and scanned > max_bytes:
            # Log but don't fail; result is already there.
            print(f"  [warn] query scanned {scanned} > cap {max_bytes}", file=sys.stderr)

        if state != "SUCCEEDED":
            reason = ex["Status"].get("StateChangeReason", "")
            raise RuntimeError(f"Query failed ({state}): {reason}\nSQL: {sql[:200]}")

        return self._collect_rows(qid)

    def _collect_rows(self, qid: str) -> list[dict]:
        """Collect rows. Use ResultSetMetadata as header; strip first data row only
        if it echoes the header (Athena does this for SELECT but not for SHOW)."""
        paginator = self._client.get_paginator("get_query_results")
        header: list[str] | None = None
        rows: list[dict] = []
        first_page = True
        for page in paginator.paginate(QueryExecutionId=qid):
            rs = page["ResultSet"]
            data = rs["Rows"]
            if header is None:
                header = [c["Name"] for c in rs["ResultSetMetadata"]["ColumnInfo"]]
            if first_page and data:
                first_cells = [c.get("VarCharValue") for c in data[0]["Data"]]
                if first_cells == header:
                    data = data[1:]
                first_page = False
            for r in data:
                cells = [c.get("VarCharValue") for c in r["Data"]]
                rows.append(dict(zip(header, cells)))
        return rows


# ---------------------------------------------------------------------------
# JSON path inference
# ---------------------------------------------------------------------------

def _infer_type(v: Any) -> str:
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "bool"
    if isinstance(v, int):
        return "int"
    if isinstance(v, float):
        return "float"
    if isinstance(v, str):
        return "string"
    if isinstance(v, list):
        if not v:
            return "array<unknown>"
        inner = {_infer_type(x) for x in v[:10]}
        return f"array<{'|'.join(sorted(inner))}>"
    if isinstance(v, dict):
        return "object"
    return "unknown"


def _detect_id_key_pattern(d: dict) -> str | None:
    """If most keys of `d` look like IDs of one kind, return that kind's label, else None."""
    keys = [k for k in d.keys() if isinstance(k, str)]
    if len(keys) < 3:
        return None
    for label, pat in ID_KEY_PATTERNS:
        matches = sum(1 for k in keys if pat.match(k))
        if matches / len(keys) > 0.7:
            return label
    return None


def _walk(node: Any, path: str, acc: dict[str, dict], context_prefix: str = "") -> None:
    t = _infer_type(node)
    entry = acc.setdefault(path, {"types": set(), "examples": []})
    entry["types"].add(t)
    if isinstance(node, dict):
        # Per-row collapse is unreliable (small dicts in some rows fall below threshold and
        # leak literal keys into the merged tree). Always emit literal keys here; the
        # post-process `_collapse_id_siblings` collapses them based on the merged keyspace.
        for k, v in node.items():
            _walk(v, f"{path}.{k}" if path else k, acc, context_prefix)
    elif isinstance(node, list):
        for x in node[:5]:
            _walk(x, f"{path}[]", acc, context_prefix)
    else:
        if len(entry["examples"]) < 3 and node not in (None, ""):
            full_path = f"{context_prefix}.{path}" if context_prefix else path
            if is_sensitive_leaf(_path_leaf(path)) or is_personal_name_path(full_path):
                if REDACTED not in entry["examples"]:
                    entry["examples"].append(REDACTED)
            else:
                s = json.dumps(node) if not isinstance(node, str) else node
                s = redact_secret_patterns(s[:60])
                entry["examples"].append(s)


def _collapse_id_siblings(acc: dict[str, dict]) -> dict[str, dict]:
    """Post-process: if many sibling keys under the same parent path look like IDs,
    collapse them into a single `<oid>` / `<uuid>` / `<int>` placeholder. This catches
    ID-keyed maps that don't show enough keys per row to be detected during walk."""
    # Group leaf segments under each parent path.
    by_parent: dict[str, list[str]] = defaultdict(list)
    for path in list(acc.keys()):
        if not path:
            continue
        # Find parent and last segment (split on '.', but keep '[]' attached).
        if "." not in path:
            parent = ""
            leaf = path
        else:
            parent, leaf = path.rsplit(".", 1)
        # Don't bucket array placeholders or already-collapsed ones.
        if leaf == "" or leaf.startswith("<") or leaf.endswith("[]"):
            continue
        by_parent[parent].append(leaf)

    rewrites: dict[str, str] = {}  # old_path -> new_path
    for parent, leaves in by_parent.items():
        if len(leaves) < 3:
            continue
        for label, pat in ID_KEY_PATTERNS:
            matches = [l for l in leaves if pat.match(l)]
            if matches and len(matches) / len(leaves) > 0.7:
                placeholder = f"<{label}>"
                for l in matches:
                    old = f"{parent}.{l}" if parent else l
                    new = f"{parent}.{placeholder}" if parent else placeholder
                    rewrites[old] = new
                break

    if not rewrites:
        return acc

    new_acc: dict[str, dict] = {}
    # Helper: rewrite any path prefix that matches an old key.
    sorted_keys = sorted(rewrites.keys(), key=len, reverse=True)
    def rewrite(p: str) -> str:
        for old in sorted_keys:
            if p == old or p.startswith(old + "."):
                return rewrites[old] + p[len(old):]
        return p

    for path, entry in acc.items():
        new_path = rewrite(path)
        existing = new_acc.get(new_path)
        if existing is None:
            new_acc[new_path] = {"types": set(entry["types"]), "examples": list(entry["examples"])[:3]}
        else:
            existing["types"].update(entry["types"])
            for ex in entry["examples"]:
                if len(existing["examples"]) < 3 and ex not in existing["examples"]:
                    existing["examples"].append(ex)
    # Mark each collapsed parent with a map<...> type hint.
    for old, new in rewrites.items():
        parent = new.rsplit(".", 1)[0] if "." in new else ""
        if parent in new_acc:
            label = new.rsplit(".", 1)[-1].strip("<>")
            new_acc[parent]["types"].add(f"map<{label},_>")
    return new_acc


def infer_json_schema(values: Iterable[str], context_prefix: str = "") -> dict[str, dict] | None:
    """Try to parse each value as JSON; return merged path tree, or None if nothing parsed.

    `context_prefix` is the outer column name. It is **not** prepended to stored paths
    (the renderer shows paths relative to the column), but it IS used for sensitivity
    checks so that e.g. a column `participants` with array elements containing `name`
    triggers the path-aware person-name redactor."""
    acc: dict[str, dict] = {}
    parsed = 0
    for v in values:
        if not v or not isinstance(v, str):
            continue
        s = v.strip()
        if not (s.startswith("{") or s.startswith("[")):
            continue
        try:
            obj = json.loads(s)
        except (ValueError, json.JSONDecodeError):
            continue
        parsed += 1
        _walk(obj, "", acc, context_prefix)
    if parsed == 0:
        return None
    return _collapse_id_siblings(acc)


def render_json_tree(acc: dict[str, dict]) -> str:
    lines = []
    for path in sorted(acc.keys()):
        if not path:
            continue
        depth = path.count(".") + path.count("[]")
        indent = "  " * depth
        types = "|".join(sorted(t for t in acc[path]["types"] if t != "null"))
        nullable = " (nullable)" if "null" in acc[path]["types"] else ""
        examples = acc[path]["examples"]
        ex_str = f"  e.g. `{'`, `'.join(examples)}`" if examples else ""
        leaf = path.split(".")[-1].split("[]")[-1] or path
        lines.append(f"{indent}- `{leaf}` — `{types}`{nullable}{ex_str}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Markdown rendering with human-notes preservation
# ---------------------------------------------------------------------------

@dataclass
class TableDoc:
    layer: str
    database: str
    name: str
    kind: str  # "table" | "view"
    columns: list[tuple[str, str, str]] = field(default_factory=list)  # (name, type, comment)
    partition_keys: list[str] = field(default_factory=list)
    location: str | None = None
    fmt: str | None = None
    create_sql: str | None = None
    sampled_rows: int = 0
    inferred_json: dict[str, dict[str, dict]] = field(default_factory=dict)  # column -> path tree
    enums: dict[str, list[str]] = field(default_factory=dict)  # column -> ["value (×n)", ...]

    def path(self) -> Path:
        return SCHEMAS_DIR / self.layer / self.database / f"{self.name}.md"

    def render(self) -> str:
        front = {
            "database": self.database,
            "table": self.name,
            "type": self.kind,
            "layer": self.layer,
            "location": self.location,
            "format": self.fmt,
            "partition_keys": self.partition_keys,
            "last_synced": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "sampled_rows": self.sampled_rows,
        }
        out = ["---", yaml.safe_dump(front, sort_keys=False).strip(), "---", ""]
        out.append(f"# `{self.database}.{self.name}`")
        out.append("")
        out.append("## Columns")
        out.append("")
        out.append("| Column | Type | Notes |")
        out.append("| --- | --- | --- |")
        for c, t, note in self.columns:
            out.append(f"| `{c}` | `{t}` | {note or ''} |")
        out.append("")
        if self.partition_keys:
            out.append(f"**Partition keys:** {', '.join(f'`{k}`' for k in self.partition_keys)}")
            out.append("")
        if self.enums:
            out.append("## Enum-like columns")
            out.append("")
            out.append(f"_String columns with ≤{ENUM_DISTINCT_THRESHOLD} distinct values in {self.sampled_rows} sampled rows. Distribution shown as `value (×count)`._")
            out.append("")
            for col, vals in self.enums.items():
                out.append(f"- `{col}`: {', '.join(f'`{v}`' for v in vals)}")
            out.append("")
        if self.inferred_json:
            out.append("## Inferred JSON structure")
            out.append("")
            out.append(f"_Inferred from {self.sampled_rows} sampled rows on "
                       f"{datetime.now(timezone.utc).date()}. Not authoritative — values may be missing or have additional keys._")
            out.append("")
            for col, tree in self.inferred_json.items():
                out.append(f"### `{col}`")
                out.append("")
                out.append(render_json_tree(tree))
                out.append("")
        if self.create_sql:
            out.append("## DDL")
            out.append("")
            out.append("```sql")
            out.append(self.create_sql.strip())
            out.append("```")
            out.append("")
        out.append(HUMAN_MARKER)
        out.append("")
        out.append("<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->")
        out.append("")
        return "\n".join(out)


def write_doc(doc: TableDoc) -> None:
    p = doc.path()
    p.parent.mkdir(parents=True, exist_ok=True)
    new = doc.render()
    # Final value-pattern pass over the rendered markdown — catches credential
    # /bucket / account-id strings sourced from DDL or front-matter that the
    # JSON-walker never sees (e.g. `LOCATION 's3://<bucket>/...'`).
    new = "\n".join(redact_secret_patterns(line) for line in new.split("\n"))

    # Preserve any human notes from existing file.
    if p.exists():
        old = p.read_text()
        if HUMAN_MARKER in old:
            human = old.split(HUMAN_MARKER, 1)[1]
            new = new.split(HUMAN_MARKER, 1)[0] + HUMAN_MARKER + human

    p.write_text(new)


# ---------------------------------------------------------------------------
# Athena introspection helpers
# ---------------------------------------------------------------------------

def list_tables(client: AthenaClient, database: str) -> list[str]:
    # SHOW TABLES is parsed by Hive — backticks (or unquoted) are fine, double-quotes are not.
    rows = client.query(f"SHOW TABLES IN `{database}`")
    return [next(iter(r.values())) for r in rows if r]


def list_views(client: AthenaClient, database: str) -> set[str]:
    # SHOW VIEWS is parsed by Presto — double-quotes (or unquoted) are fine, backticks are not.
    try:
        rows = client.query(f'SHOW VIEWS IN "{database}"')
        return {next(iter(r.values())) for r in rows if r}
    except Exception as e:
        print(f"  [warn] SHOW VIEWS failed for {database}: {e}", file=sys.stderr)
        return set()


def describe(client: AthenaClient, database: str, table: str) -> tuple[list[tuple[str, str, str]], list[str]]:
    """Return (columns, partition_keys). DESCRIBE output: 'col_name' 'data_type' 'comment'."""
    # DESCRIBE is Hive-parsed.
    rows = client.query(f"DESCRIBE `{database}`.`{table}`")
    columns: list[tuple[str, str, str]] = []
    partitions: list[str] = []
    in_partition = False
    for r in rows:
        vals = list(r.values())
        first = (vals[0] or "").strip() if vals else ""
        if not first or first.startswith("#"):
            if "Partition" in first:
                in_partition = True
            continue
        # DESCRIBE in Athena returns lines like "col_name\tdata_type\tcomment"
        parts = re.split(r"\s{2,}|\t", first)
        if len(parts) < 2:
            parts = first.split(None, 2)
        name = parts[0].strip()
        dtype = parts[1].strip() if len(parts) > 1 else ""
        comment = parts[2].strip() if len(parts) > 2 else ""
        if in_partition:
            partitions.append(name)
        else:
            columns.append((name, dtype, comment))
    # Dedup partition keys that also appear in columns list (Athena lists them twice).
    return columns, partitions


def show_create(client: AthenaClient, database: str, table: str, kind: str) -> tuple[str | None, str | None, str | None]:
    """Return (full_ddl, s3_location, format) for a table; for views, ddl only."""
    keyword = "VIEW" if kind == "view" else "TABLE"
    try:
        # SHOW CREATE TABLE is Hive-parsed; SHOW CREATE VIEW is Presto-parsed.
        if keyword == "VIEW":
            rows = client.query(f'SHOW CREATE VIEW "{database}"."{table}"')
        else:
            rows = client.query(f"SHOW CREATE TABLE `{database}`.`{table}`")
    except Exception as e:
        print(f"  [warn] SHOW CREATE failed for {database}.{table}: {e}", file=sys.stderr)
        return None, None, None
    ddl = "\n".join(next(iter(r.values()), "") or "" for r in rows)
    location = None
    fmt = None
    m = re.search(r"LOCATION\s+'([^']+)'", ddl)
    if m:
        location = m.group(1)
    m = re.search(r"STORED AS\s+(\w+)", ddl, re.IGNORECASE)
    if m:
        fmt = m.group(1)
    elif "ROW FORMAT SERDE" in ddl:
        m = re.search(r"ROW FORMAT SERDE\s+'([^']+)'", ddl)
        if m:
            fmt = m.group(1).split(".")[-1]
    return ddl, location, fmt


# ---------------------------------------------------------------------------
# Sampling for JSON inference
# ---------------------------------------------------------------------------

def pick_recency_column(columns: list[tuple[str, str, str]], override: str | None) -> str | None:
    if override:
        return override
    names = {c[0].lower(): c[0] for c in columns}
    for cand in RECENCY_CANDIDATES:
        if cand in names:
            return names[cand]
    return None


def sample_rows(client: AthenaClient, database: str, table: str,
                limit: int, recency_col: str | None, max_bytes: int) -> list[dict]:
    # Strategy: try ORDER BY recency first if available (gives recent rows). On timeout,
    # fall back to plain LIMIT (no ORDER, no TABLESAMPLE — TABLESAMPLE BERNOULLI scans
    # too much on large tables).
    attempts: list[str] = []
    if recency_col:
        attempts.append(f'SELECT * FROM "{database}"."{table}" ORDER BY "{recency_col}" DESC LIMIT {limit}')
    attempts.append(f'SELECT * FROM "{database}"."{table}" LIMIT {limit}')
    for sql in attempts:
        try:
            return client.query(sql, max_bytes=max_bytes, timeout_s=60)
        except Exception as e:
            print(f"  [warn] sampling attempt failed for {database}.{table}: {e}", file=sys.stderr)
    return []


def infer_json_for_table(rows: list[dict], columns: list[tuple[str, str, str]]) -> dict[str, dict]:
    """Return {column_name: path_tree} for columns whose values look like JSON."""
    out: dict[str, dict] = {}
    json_candidate_types = {"string", "varchar", "char"}
    for cname, ctype, _ in columns:
        base = ctype.lower().split("(")[0]
        if base not in json_candidate_types:
            continue
        values = [r.get(cname) for r in rows]
        tree = infer_json_schema(values, context_prefix=cname)
        if tree:
            out[cname] = tree
    return out


def extract_enums(rows: list[dict], columns: list[tuple[str, str, str]]) -> dict[str, list[str]]:
    """For string columns whose sampled values have small distinct cardinality, return the values."""
    if len(rows) < ENUM_MIN_SAMPLES:
        return {}
    out: dict[str, list[str]] = {}
    string_types = {"string", "varchar", "char"}
    for cname, ctype, _ in columns:
        base = ctype.lower().split("(")[0]
        if base not in string_types:
            continue
        if is_sensitive_leaf(cname):
            continue
        vals = [r.get(cname) for r in rows]
        # Skip if mostly null, mostly JSON, or mostly long.
        non_null = [redact_secret_patterns(v) if isinstance(v, str) else v
                    for v in vals if v is not None and v != ""]
        if len(non_null) < ENUM_MIN_SAMPLES:
            continue
        if any(isinstance(v, str) and (v.startswith("{") or v.startswith("[")) for v in non_null[:5]):
            continue
        if sum(len(v) for v in non_null[:20] if isinstance(v, str)) / max(1, min(20, len(non_null))) > 60:
            continue
        counts = Counter(non_null)
        if len(counts) > ENUM_DISTINCT_THRESHOLD:
            continue
        # Reject high-cardinality / low-repeat columns (hashes, ids, free text).
        # Require at least 50% repeat rate AND that the most common value appears at least 3 times.
        if len(counts) / len(non_null) > 0.5:
            continue
        if counts.most_common(1)[0][1] < 3:
            continue
        out[cname] = [f"{v} (×{n})" for v, n in counts.most_common()]
    return out


# ---------------------------------------------------------------------------
# Sample caching
# ---------------------------------------------------------------------------

def cache_path(database: str, table: str) -> Path:
    return CACHE_DIR / f"{database}__{table}.json.gz"


def load_cached_sample(database: str, table: str) -> list[dict] | None:
    p = cache_path(database, table)
    if not p.exists():
        return None
    try:
        with gzip.open(p, "rt") as f:
            return json.load(f)
    except Exception:
        return None


def save_cached_sample(database: str, table: str, rows: list[dict]) -> None:
    p = cache_path(database, table)
    p.parent.mkdir(parents=True, exist_ok=True)
    with gzip.open(p, "wt") as f:
        json.dump(rows, f)


# ---------------------------------------------------------------------------
# Markdown scrubber (post-hoc redaction of already-written schema files)
# ---------------------------------------------------------------------------
#
# Use this when sample-derived sensitive values landed in committed markdown
# (before the redaction logic above existed). Operates on text only, no Athena
# access required.

# `- `colname`: ...` lines under "## Enum-like columns".
_ENUM_LINE = re.compile(r"^- `([^`]+)`:\s*(.+)$")
# Indented `- `leaf` — `type` ...  e.g. `v1`, ...` lines under "## Inferred JSON structure".
_JSON_LINE = re.compile(r"^(\s*)- `([^`]+)` — (.*?)(  e\.g\. .*)?$")


def scrub_markdown_file(path: Path) -> int:
    """Strip sampled values for sensitive column / JSON-leaf names AND
    credential-shaped substrings (JWTs, OAuth, AWS/GCP/Slack/GitHub/Stripe).

    Returns number of lines rewritten."""
    text = path.read_text()
    out: list[str] = []
    section = None  # "enum" | "json" | None
    json_column = ""  # currently parsing tree under "### `<col>`"
    # Stack of (indent_level, parent_leaf) so nested leaves get a full synthetic path.
    parent_stack: list[tuple[int, str]] = []
    changed = 0
    for line in text.split("\n"):
        if line.startswith("## Enum-like columns"):
            section = "enum"
            out.append(line)
            continue
        if line.startswith("## Inferred JSON structure"):
            section = "json"
            out.append(line)
            continue
        if line.startswith("## ") or line == HUMAN_MARKER:
            section = None
            json_column = ""
            out.append(line)
            continue

        # Track the current JSON column header so leaves can be path-aware.
        if section == "json" and line.startswith("### `"):
            m = re.match(r"^### `([^`]+)`", line)
            json_column = m.group(1).lower() if m else ""
            parent_stack.clear()
            out.append(line)
            continue

        # Always run value-pattern redaction first — catches credentials embedded
        # under non-sensitive leaf names (e.g. JWT inside `query_string`).
        rewritten = redact_secret_patterns(line)
        if rewritten != line:
            line = rewritten
            changed += 1

        if section == "enum":
            m = _ENUM_LINE.match(line)
            if m:
                col = m.group(1)
                if is_sensitive_leaf(col) or is_personal_name_path(col, col):
                    out.append(f"- `{col}`: `{REDACTED}`")
                    if rewritten == line:
                        changed += 1
                    continue

        if section == "json":
            m = _JSON_LINE.match(line)
            if m:
                indent, leaf, type_part, eg_part = m.groups()
                # Indent is 2 spaces per level in the renderer.
                indent_level = len(indent) // 2
                # Pop ancestors at this depth or deeper.
                while parent_stack and parent_stack[-1][0] >= indent_level:
                    parent_stack.pop()
                # Build a synthetic path: column header + ancestor stack + leaf.
                ancestors = [json_column] if json_column else []
                ancestors += [p for _, p in parent_stack]
                synthetic_path = ".".join(ancestors + [leaf])
                if eg_part and (is_sensitive_leaf(leaf) or is_personal_name_path(synthetic_path, leaf)):
                    out.append(f"{indent}- `{leaf}` — {type_part}  e.g. `{REDACTED}`")
                    if rewritten == line:
                        changed += 1
                    # Even though we redacted, this line is a leaf — don't push.
                    continue
                # If this entry has no examples it's an object/array parent;
                # push so deeper leaves can see it in their path.
                if not eg_part:
                    parent_stack.append((indent_level, leaf))

        out.append(line)

    if changed:
        path.write_text("\n".join(out))
    return changed


def scrub_all(root: Path) -> tuple[int, int]:
    """Scrub every .md under `root`. Returns (files_changed, lines_rewritten)."""
    files_changed = 0
    lines_rewritten = 0
    for p in sorted(root.rglob("*.md")):
        n = scrub_markdown_file(p)
        if n:
            files_changed += 1
            lines_rewritten += n
            print(f"  scrubbed {n} line(s) in {p.relative_to(ROOT)}")
    return files_changed, lines_rewritten


# ---------------------------------------------------------------------------
# Index
# ---------------------------------------------------------------------------

def write_index(docs: list[TableDoc]) -> None:
    by_layer: dict[str, list[TableDoc]] = defaultdict(list)
    for d in docs:
        by_layer[d.layer].append(d)
    out = ["# Athena Schema Index", "", f"_Last synced: {datetime.now(timezone.utc).isoformat(timespec='seconds')}_", ""]
    for layer in sorted(by_layer):
        out.append(f"## {layer}")
        out.append("")
        for d in sorted(by_layer[layer], key=lambda x: (x.database, x.name)):
            rel = d.path().relative_to(ROOT).as_posix()
            kind = "view" if d.kind == "view" else "table"
            out.append(f"- [`{d.database}.{d.name}`]({rel}) — {kind}")
        out.append("")
    (SCHEMAS_DIR / "INDEX.md").write_text("\n".join(out))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=str(Path(__file__).parent / "config.yaml"))
    ap.add_argument("--layer", help="Only sync this layer (e.g. processed)")
    ap.add_argument("--database", help="Only sync this database")
    ap.add_argument("--table", help="Only sync this table")
    ap.add_argument("--no-sample", action="store_true", help="Skip JSON sampling")
    ap.add_argument("--use-cache", action="store_true",
                    help="Reuse cached samples in .cache/samples/ instead of re-querying Athena")
    ap.add_argument("--cache-only", action="store_true",
                    help="Only process tables for which a cached sample already exists; never query for samples")
    ap.add_argument("--scrub", action="store_true",
                    help="Re-redact existing schema markdown in place (no Athena access). "
                         "Use after expanding the sensitive-name list or when sampled secrets "
                         "already leaked into committed files.")
    args = ap.parse_args()

    if args.scrub:
        files, lines = scrub_all(SCHEMAS_DIR)
        print(f"Scrubbed {lines} line(s) across {files} file(s).")
        return 0

    cfg_path = Path(args.config)
    if not cfg_path.exists():
        print(f"Config not found at {cfg_path}. Copy scripts/config.example.yaml and edit.", file=sys.stderr)
        return 2
    cfg = yaml.safe_load(cfg_path.read_text())

    client = AthenaClient(
        region=cfg["aws"]["region"],
        workgroup=cfg["aws"]["workgroup"],
        output_location=cfg["aws"]["output_location"],
        max_bytes=int(cfg.get("budget", {}).get("max_total_bytes_scanned", 0)),
    )

    sampling_cfg = cfg.get("sampling", {})
    sample_layers = set(sampling_cfg.get("enabled_layers", ["processed"]))
    rows_per_table = int(sampling_cfg.get("rows_per_table", 200))
    per_query_cap = int(sampling_cfg.get("max_bytes_scanned_per_query", 1 << 30))
    recency_overrides = sampling_cfg.get("recency_column_overrides", {}) or {}

    docs: list[TableDoc] = []

    for layer, dbs in (cfg.get("databases") or {}).items():
        if args.layer and layer != args.layer:
            continue
        for db in dbs or []:
            if args.database and db != args.database:
                continue
            print(f"== {layer}/{db} ==")
            tables = list_tables(client, db)
            views = list_views(client, db)
            for t in tables:
                if args.table and t != args.table:
                    continue
                kind = "view" if t in views else "table"
                print(f"  - {t} ({kind})")
                try:
                    cols, parts = describe(client, db, t)
                    ddl, loc, fmt = show_create(client, db, t, kind)
                except Exception as e:
                    print(f"    [skip] {e}", file=sys.stderr)
                    continue

                doc = TableDoc(
                    layer=layer, database=db, name=t, kind=kind,
                    columns=cols, partition_keys=parts,
                    location=loc, fmt=fmt, create_sql=ddl,
                )

                should_sample = (not args.no_sample) and kind == "table" and layer in sample_layers
                if should_sample:
                    rows: list[dict] | None = None
                    if args.use_cache or args.cache_only:
                        rows = load_cached_sample(db, t)
                    if rows is None and not args.cache_only:
                        rcol = pick_recency_column(cols, recency_overrides.get(f"{db}.{t}"))
                        rows = sample_rows(client, db, t, rows_per_table, rcol, per_query_cap)
                        if rows:
                            save_cached_sample(db, t, rows)
                    rows = rows or []
                    doc.sampled_rows = len(rows)
                    if rows:
                        doc.inferred_json = infer_json_for_table(rows, cols)
                        doc.enums = extract_enums(rows, cols)

                write_doc(doc)
                docs.append(doc)

    write_index(docs)
    print(f"\nDone. Bytes scanned: {client.bytes_scanned:,}. Wrote {len(docs)} table files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
