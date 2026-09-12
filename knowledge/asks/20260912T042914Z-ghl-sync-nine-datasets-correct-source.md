# For each of ghl_sync's nine datasets, what is the correct source — fact or raw CDC?

- **id:** f84cca38-c72b-4fa4-ab79-75ad847d30b7   **from:** wise-ghl-admin   **depth:** 0   **utc:** 20260912T042914Z

## Question

The Wise->GHL contact sync (`tasks/ghl_sync` in WiseApp/airflow) reads nine datasets per tenant
per run, almost all straight from raw `lake_cdc` tables with `json_extract_scalar` over the `doc`
column and `row_number() OVER (PARTITION BY _id ORDER BY ts DESC)` for latest state, with no
partition or watermark predicates anywhere. It runs every 6 hours across ~23 tenants, so it
appears to full-scan the lake for every tenant forever. Two of the nine (attended, upcoming)
already use `session_facts_v3` / `session_participant_facts_v3`, so the curated-vs-raw split is
inconsistent.

For EACH of the nine — participants, attended, upcoming, credits, invoices, parents, course_tags,
and registration (questions + submissions) — what is the CORRECT source? Concretely: (a) name the
curated fact/dim table that already covers it if one exists, (b) say which genuinely require raw
CDC and why, and (c) give the partition or watermark predicate that should be applied in either
case, with the actual column name. Also: does the IN vs NA split change any of these table names,
given this tenant is on NA?

Caller is read-only on `tasks/ghl_sync`; output is a written recommendation for the backend team.

## Answer

Answered under the platform owner's rule (2026-09-12): *"It is wasteful to query the raw lake_cdc
tables for anything. If a fact does not have it, we should figure out a way to build a fact."*
Raw CDC is the landing zone, not a source; a missing fact is a build request.

Full answer: see `knowledge/COMPACT.md` (the durable version) — summary of the verdicts:

| dataset | correct source | status |
|---|---|---|
| participants | `institute_contact_dim` | **FACT NEEDED** (interim: `processed_na.institute_participants`, daily) |
| attended | `lake_cdc.session_participant_facts_v3` | already correct |
| upcoming | `lake_cdc.session_participant_facts_v3` **alone** | fix: drop `session_facts_v3` + raw `classparticipant` join |
| credits | `student_credit_balance_facts` | **FACT NEEDED** (ledger genuinely CDC-only today) |
| invoices | `student_invoice_facts` | **FACT NEEDED** (transaction has no `instituteId`) |
| parents | `parent_student_edge_dim` | **FACT NEEDED + edge does not exist in CDC** |
| course_tags | `session_participant_facts_v3.course_name` | mostly covered; `class_enrolment_facts` if enrolment-without-sessions matters |
| registration (x2) | `registration_answer_facts` | **FACT NEEDED** (`processed_na.student_registration_form` does it in one query but is daily + JSON-quoted) |
| students per institute | `institute_contact_dim` | **FACT NEEDED** |

Key measured findings:

1. **`row_number() ... PARTITION BY _id` is a no-op.** All 7 raw tables have
   `count(*) == count(DISTINCT _id)` — merge-on-read Iceberg, one row per `_id`, not an
   append-only log. The window can never drop a row; it forces a full shuffle before filtering.
2. **The missing raw partition predicate is `region`** (`'in'`/`'na'`, lowercase). For NA it
   prunes 96–98%: classparticipant 86,195/4,449,156 (1.9%), transaction 88,454/2,958,504 (3.0%),
   class 2.9%, instituteparticipant 3.8%, registrationformsubmission 10%, registrationform 21%,
   sessioncredit 30%.
3. **Facts are `PARTITIONED BY (bucket(64, institute_id))`** — the tenant filter IS the partition
   filter. On `session_participant_facts_v3` (115.4M rows): `region='na'` → **577 MB**;
   `institute_id='<oid>'` → **113 KB**. ~5,000×. Never filter a fact by region.
4. **Freshness, corrected:** raw is ≤15 min; the `_v3` facts are **~30–45 min** behind (raw lag +
   15-min refresh + ~7-min pass; v3 watermark read 03:55:38 at wall clock 04:25). My first draft had
   this backwards — `refreshed_at` is merge time, not data time, and only moves for dirty/reconciled
   rows, so it is not a freshness signal. Irrelevant at a 6-hourly cadence either way.
5. **`session_participant_facts_v3` covers attended AND upcoming.** Grain verified unique at
   (session_id, student_id) — 303,537/303,537 in NA — and it holds future rows (93,504 NA,
   all `is_enrolled`). So `upcoming()` needs no raw join.
6. **Upcoming is ~2.4× overcounted today.** Recurring schedules project far out: one NA institute
   has 26,722 rows `>= current_date` but only 11,119 within 90 days, 562 beyond a year,
   `max(session_date)` 2040-05-23; fleet max 2052-10-21. Bound the window.
7. **Silent-failure traps in `doc`** (return empty, not errors): ObjectIds are `{"$oid":...}` so
   `json_extract_scalar(doc,'$.instituteId')` is always NULL and `'$.instituteId.$oid'` is a hard
   `Invalid JSON path` error — only `'$["instituteId"]["$oid"]'` works, and that form is **uniform
   across ops** (seed 4,001/4,049; update 8,122/8,137; insert 431/431; plain form 0 everywhere).
   The top-level `_id` column is already plain hex. **Dates, by contrast, vary by `op` within one
   table** — `seed` rows are canonical (`{"$date":{"$numberLong":…}}`), `insert`/`update` relaxed
   (`{"$date":"<ISO>"}`); on `__class` NA that is 4,049 vs 8,568 rows, so either path alone silently
   drops a third of the table. Coalesce both. `doc` keys are camelCase vs lowercase in `processed`,
   which uses lowercase `$numberlong`. Table names also differ across layers
   (`__sessioncredit` vs `__session_credit`).
   `ts` is epoch **seconds** and is **0 on every seed row** — use `ingested_at` as the watermark,
   never `ts`.
8. **Deletes DO arrive — I was wrong, corrected by the `airflow` expert (ask `dbb5ef4e`).** There is
   no `op='delete'` value *because* the MERGE physically removes the row
   (`WHEN MATCHED AND s.op='delete' THEN DELETE`). `lake_cdc` is a **latest-state mirror, not a
   log**: a Mongo delete makes the `_id` vanish. So removed students stop syncing — but absence
   generates no event and there is no history, so retiring GHL contacts needs a reconciliation diff.
   Weekly reconcile tombstones stragglers, so worst-case removal latency is ~a week.
9. **`parents()` is broken at the source.** PARENT `instituteparticipant` docs carry no child
   reference at all (keys: `_id, createdAt, instituteId, joinedOn, linkedDevices, metadata,
   relation, status, updatedAt, userId`; only 34 of 9,117 NA PARENT rows even have `metadata`),
   and `user.parentid` covers just 1,469 of 94,130 NA users vs 9,117 PARENT rows. The edge is not
   derivable from what the sync reads.
10. **IN/NA changes no `lake_cdc` table names** — region is a partition column on raw, a plain
    column on facts. Only the analyst layer swaps database (`processed` → `processed_na`).

**Confidence: high** on all measurements above. **Medium** on whether the facts honour
`class.archived`/`deletedStudents`/`suspendedStudents`, on fact refresh cadence (sample of two,
~9 min apart), and on course-tag completeness (my enrolment reconciliation returned 0 missing but
its enrolment side first came back empty due to the `$oid` trap). **Low/unknown:** where the
parent→student edge is persisted — did not inspect `entity`/`entityinteraction` in depth.
**Not verified by design:** I never read `tasks/ghl_sync/athena_source.py` (read-only to caller,
not supplied), so statements about what the queries *currently* do are inferred from the brief.

**Check next:** grep the file for `'$.'`-style id paths (if the bracket `$oid` form is missing,
that dataset is silently empty in production today); compare `bytes_scanned` before/after
`region='na'` to cost the 23 × 9 × 4/day = 828 daily executions; ask the airflow expert what
builds the `_v3` facts and whether archived-class filtering is applied; confirm delete semantics
with the backend team; decide whether `ADMIN` (158 NA rows) should be synced.

## Evidence

Prior ask reused: `knowledge/asks/20260910T233546Z-host-backfill-review.md` (lake_cdc is Iceberg
`PARTITIONED BY (region)`, values `in`/`na`, cols `_id, region, doc, op, ts, ingested_at`;
`op` has no delete).

Athena queries (read-only, via `athena` MCP), by query id:
- `2467e101` — count(*) vs count(DISTINCT _id) on 7 raw tables → all equal.
- `7107639f` — region row counts per raw table (25 KB scanned, Iceberg metadata).
- `describe_table` on `lake_cdc.session_facts_v3`, `session_participant_facts_v3` →
  `PARTITIONED BY (bucket(64, institute_id))`, `region` a plain column, `src_ts`, `refreshed_at`.
- `describe_table` on `lake_cdc.wise_app_backend__instituteparticipant` → `PARTITIONED BY (region)`.
- `510fb3f7` — participant-fact grain + future rows for NA (577 MB with `region='na'`).
- `0f951f1b` — same shape filtered by `institute_id` → 113 KB.
- `383976a7` — session_facts_v3 by region: in 665 institutes / na 146; max session_date 2052-10-21.
- `6e100573` — far-future inflation for one institute (26,722 vs 11,119 vs 562; max 2040-05-23).
- `2d570540` — cross-layer freshness: cdc na users 94,150 @ 03:55:38; processed_na 94,130;
  fact refreshed_at 04:20:15 UTC.
- `ac735ba1` — fact row counts 3,863,933 / 115,401,850; 811 / 665 institutes.
- `9b55ebff` — v1 facts are abandoned: `session_facts` 54,330 and `session_participant_facts`
  344,139 vs v3's 3.86M / 115.4M.
- `0ca029ca` — PARENT instituteparticipant doc key sets (no child reference).
- `850fb61b` — processed_na.user: 94,130 rows, 1,469 with `parentid`.
- `696a80be` — `processed_na.institute_participants.relation` → STUDENT 25,252 / PARENT 9,117 /
  TEACHER 2,155 / ADMIN 158.
- `35af104a` — sessioncredit type CREDIT 5,850 (54,639.67) / DEBIT 365 (1,549.0), NA.
- `34662aa2` — transaction doc keys (no `instituteId`).
- `7277185a`, `b33310f2`, `1bcc2925` — class / classparticipant / sessioncredit doc key sets
  (camelCase; class has `archived, hidden, published, deletedStudents, suspendedStudents`).
- `ba951ff6` (FAILED) — `'$.instituteId.$oid'` → `INVALID_FUNCTION_ARGUMENT: Invalid JSON path`.
- `bb14c0b9` — `{"$oid":...}` encoding; `json_extract_scalar(doc,'$.instituteId')` NULL vs
  `'$["instituteId"]["$oid"]'` correct; top-level `_id` already plain hex.
- `95517e6b` — dates are `{"$date":"2026-09-12T03:55:34.896Z"}`; `ts` is epoch **seconds**
  (1789185338 == ingested_at 03:55:38), i.e. CDC ingest time, usable as a watermark.
- `describe_table(processed_na, student_registration_form)` — view already unnests fields +
  answers and joins on instituteid+questionid; uses `CAST(JSON_EXTRACT(...) AS VARCHAR)` so values
  carry JSON quotes.
- `describe_table(processed_na, institute_participants)` — relation/status/tags view.
- `list_tables` on `processed_na`, `cdc_raw`, `proc_zoom`, `control_map`.

- `58620ba0` — per-`op` encoding split on `__class` NA: seed 4,049 rows canonical dates / ts=0;
  update 8,137 + insert 431 relaxed ISO dates; `$oid` bracket form works for all three ops.

Ask raised to the `airflow` expert and **answered** (id `dbb5ef4e`, depth 1, chain
wise-ghl-admin,athena-agent): producer is `wise-analytics-portal` (not the airflow repo), two
change-stream daemons on the Airflow EC2 box, batch cut at 5000 events/32 MiB/300 s, Iceberg MERGE
from the daemon's own sink loop; `_v3` facts built by Cloud Run `wise-facts-refresh` on Cloud
Scheduler every 15 min, incremental, watermarked by `s3://…/cdc/state/v3/session_sync.json`, with a
rolling reconcile of 1-of-64 institute buckets per hour; `OPTIMIZE`/`VACUUM` via systemd timers —
and **`wise-iceberg-optimize@all.service` is currently FAILED (no all-table compaction since
2026-09-06)**. It also corrected my delete premise. Folded into `knowledge/COMPACT.md` §5.

## Gotcha

The pattern that made this design look reasonable: `row_number() OVER (PARTITION BY _id ORDER BY
ts DESC)` is the textbook latest-state-from-CDC idiom, and it is exactly right for an append-only
change log — which `cdc_raw.changes_v1` is. But `lake_cdc.wise_app_backend__*` is **not** that
log; it is the MERGEd result, one row per `_id`. So the idiom is correct-looking, produces correct
output, and costs a full-table shuffle for nothing. Nothing about the table name or columns
(`op`, `ts`) tells you which of the two you are looking at — you have to compare `count(*)` to
`count(DISTINCT _id)`.

Second trap, worse because it fails silently in the other direction: `json_extract_scalar(doc,
'$.instituteId')` returns NULL rather than erroring, because the value is an object
`{"$oid":"..."}`. A per-tenant query written that way returns **zero rows** and looks like "this
tenant has no data" rather than "my JSON path is wrong". And the obvious fix, `'$.instituteId.$oid'`,
is a hard error — the only working form is bracketed: `'$["instituteId"]["$oid"]'`.
