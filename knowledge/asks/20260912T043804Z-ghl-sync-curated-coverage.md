# ghl_sync's 9 per-tenant lake_cdc reads — which have a curated fact/dim equivalent, and does NA change anything?

- **id:** aa8d9768-56e7-47a4-b7da-7ea749ef40be   **from:** wise-ghl-admin   **depth:** 0
- **utc:** 20260912T043804Z

## Question

The Wise->GHL sync (WiseApp/airflow `tasks/ghl_sync/athena_source.py`, read-only to the
caller) reads nine datasets per tenant per run from `lake_cdc` raw tables: participants,
attended, upcoming, credits, invoices, parents, course_tags, registration-questions,
registration-submissions. Every query full-scans a lake_cdc table, `json_extract_scalar(doc,...)`
to pull fields, `row_number() OVER (PARTITION BY _id ORDER BY ts DESC)` for latest state,
then filters to one institute. No partition predicates and no `ts >` watermark anywhere.
DAG runs every 6h over ~23 tenants.

For each of the nine: (a) is there an existing curated fact or dim table, exact name;
(b) if it genuinely needs raw CDC, why; (c) the exact column to use as partition/watermark
predicate. Note `attended`/`upcoming` already use `session_participant_facts_v3` /
`session_facts_v3`. Tenant is on NA — does IN vs NA change table names or databases?
Rank recommendations by scan saved.

Caller explicitly barred escalating to the airflow expert (a previous identical ask,
f84cca38, timed out at 900s doing exactly that) and barred documenting the CDC pipeline.

## Answer

Full answer written to the caller and mirrored at
`/var/folders/t_/.../ask-aa8d9768-....md`. Summary of the durable findings:

**Eight of nine have a curated equivalent, and seven of them are not in `lake_cdc`** —
they are views / flattened Parquet in `processed` (IN) and `processed_na` (NA). `lake_cdc`
holds exactly four curated artefacts (`session_facts`, `session_facts_v3`,
`session_participant_facts`, `session_participant_facts_v3`) plus `exam_service__*` and
`webapp__*`; every `wise_app_backend__*` there is raw.

| dataset | curated source | scope predicate |
|---|---|---|
| participants | `processed_na.institute_participants` + `processed_na.user` | `instituteid` |
| parents | same two (fold into participants; `user.parentid` is the edge) | `instituteid` |
| attended | `lake_cdc.session_participant_facts_v3` (already used) | `institute_id` |
| upcoming | `session_facts_v3` + `processed_na.class_participants` | `institute_id` / `classid` |
| credits | `processed_na.wise_app_backend__session_credit` (no view) | via `classid`→class |
| invoices | `processed_na.wise_app_backend__transaction` + `processed_na.class` | `instituteid` |
| course_tags | `session_participant_facts_v3.course_name`, or `class`+`class_participants` | `institute_id` |
| registration (both) | `processed_na.student_registration_form` — **one view covers both queries** | `instituteid` |

**Measured scan, one tenant one run: ~2.69 GB today → ~6 MB curated (~450x).**
Per dataset: participants 848MB, parents 848MB, invoices 521MB, course_tags 483MB,
upcoming 181MB, registration 5.8MB, credits 1.4MB, attended 0.1MB.

**The one-word fix that beats everything else for effort:** `region` is the ONLY partition
key on every `lake_cdc.wise_app_backend__*` table (Iceberg, `PARTITIONED BY (region)`,
values `'in'`/`'na'`). No ghl_sync query filters it. Adding `region='na'` takes 2.69 GB →
~140 MB (19x) with zero restructuring — NA is 2-3% of the lake.

**`session_*_facts_v3` are `PARTITIONED BY (bucket(64, institute_id))`** — an equality
predicate on `institute_id` prunes to 1/64. `region` on those tables is a plain column and
prunes nothing.

**IN vs NA:** database name changes (`processed` → `processed_na`); **base table names are
identical**; views `transaction` and `registration_form_submission` exist on IN and are
**ABSENT on NA**. So invoices and registration-submissions must read the base tables
`wise_app_backend__transaction` / `wise_app_backend__registration_form_submission` to stay
region-symmetric. `lake_cdc` is one database for both regions.

**No usable watermark.** These queries want latest-state-per-`_id`; a `ts >` filter drops
every unchanged document, i.e. most of the roster. A watermark is only correct as a delta
unioned onto a full-state base — which is what `processed` already is.

**Freshness is the only real argument for raw.** `processed_na` max `updatedat` =
2026-09-11 while `lake_cdc` NA `ingested_at` = 2026-09-12 03:55 — daily dump vs continuous.
A 6-hourly DAG on a daily source returns identical data 3 runs in 4. Matters for invoices
and participants; irrelevant for course_tags, parents, registration, upcoming.

## Evidence

All figures measured live via the athena MCP on 2026-09-12, not inferred from `schemas/`
(which does not index `lake_cdc` at all).

- `list_tables('lake_cdc')` — only 4 curated `session_*facts*` tables; no other facts/dims.
- `list_tables('processed')` vs `list_tables('processed_na')` — base names identical;
  `transaction` and `registration_form_submission` views IN-only.
- `describe_table` on `lake_cdc.wise_app_backend__instituteparticipant` →
  `PARTITIONED BY (region)`, cols `_id, region, doc, op, ts, ingested_at`.
- `describe_table` on `session_facts_v3` / `session_participant_facts_v3` →
  `PARTITIONED BY (bucket(64, institute_id))`. spf_v3 carries `course_name`, `class_id`,
  `credits_consumed`, `fee_amount`, `student_name`, `student_email`, `is_enrolled`.
- `describe_table` on `processed_na.{institute_participants,user,class,class_participants,
  registration_form,student_registration_form}` — all `$oid`/`$date` already unwrapped.
- Scan measurements, `SELECT region, count(*), sum(length(doc)) ... GROUP BY region`:
  user 805 MB (IN 3.82M rows / NA 94,150), transaction 219 MB, class 302 MB,
  classparticipant 181 MB, instituteparticipant 43 MB, regsub 4.75 MB, regform 0.45 MB,
  sessioncredit 1.4 MB.
- Curated counterparts: participants+user join **780 KB** (query 03f30b8c);
  student_registration_form whole-institute **600 KB** (bb01ac9d);
  spf_v3 course tags **117 KB** (98a3734d); class+class_participants **1.6 MB** (04f1542c);
  transaction **2.7 MB** (1c5bc4f0).
- `relation` enum on `processed_na.institute_participants`: STUDENT 25,252 / PARENT 9,117 /
  TEACHER 2,155 / ADMIN 158 (b8d9345e, **1,969 bytes scanned**).
- course_tags equivalence on institute `69b84f3c99b41087144ba02e` (ThinkTank Jr):
  1,306 enrolment pairs vs 1,323 fact pairs, **36 enrolments absent from the fact (2.8%)**.
- Freshness: `processed_na.institute_participants` max `updatedat` 2026-09-11 vs
  `lake_cdc` NA `ingested_at` 2026-09-12 03:55 (8e4d782c).

## Gotcha

1. **`ts` on lake_cdc CDC tables is epoch SECONDS, not milliseconds.**
   `from_unixtime(ts/1000)` returns 1970-01-21. Use `from_unixtime(ts)`. Cost me a query.
2. **`metadata.classid` on `processed_na.wise_app_backend__transaction` is a PLAIN STRING,
   not `{"$oid": ...}`.** A `$.classid["$oid"]` path — the shape that works against the CDC
   `doc` — returns zero rows **silently**. I hit this directly. `amount` is
   `$.amount.value.$numberint` with `$.amount.currency` alongside.
3. **NA transactions include `metadata.invoicetype = 'TUTOR_PAYOUT'`.** If the existing
   invoices query does not exclude those, tutor payouts are being pushed to GHL as student
   invoices — a live correctness question independent of any table swap.
4. **`processed_na.institute_participants.relation` IS the role enum.** The `doc` JSON
   extraction for STUDENT/TEACHER is redundant work.
5. **`processed_na.student_registration_form` already joins questions to answers** — it
   collapses two of the nine queries into one.
6. **`session_participant_facts_v3.credits_consumed` is NOT the credit balance** — it is
   per-session consumption, not the CREDIT-minus-DEBIT ledger. Do not substitute it for
   the credits dataset.
7. **`schemas/` in this repo does not index `lake_cdc` at all**, which is why this question
   could not be answered from the knowledge base and needed live catalog calls. Worth a
   `scripts/config.yaml` addition.
