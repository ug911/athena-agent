# COMPACT — Wise data platform

Curated digest for experts and workers querying the Wise Athena warehouse.
**Read this before you reason. Then `grep -ril "<keywords>" knowledge/asks/` for a past answer.**

Rewritten 2026-09-12 after a worker built a 6-hourly client sync against raw `lake_cdc` tables —
full scans, no partition pruning, every tenant scanned to serve one institute — because nothing
told it that curated facts existed.

---

# THE RULE

> **"It is wasteful to query the raw `lake_cdc` tables for anything. If a fact does not have it,
> we should figure out a way to build a fact."** — platform owner, 2026-09-12

**Raw CDC is the landing zone, not a data source.** Consumers read **facts**.
A missing fact is a **request to build one**, not a licence to scan CDC.

If you are about to write `json_extract_scalar(doc, ...)` in consumer code, stop. Either a fact
covers it (see the mapping below), or you have found a fact that needs building — say so and
escalate. The one legitimate exception is a deliberate, bounded backfill or investigation, and
even then apply the hygiene rules at the end of this document.

---

# 1. The layers

Five layers exist. Only two are for consumers.

| # | Layer | Where | What it is | Freshness | Consumer-safe? |
|---|---|---|---|---|---|
| 1 | **Staging** | `cdc_raw.changes_v1` | Append-only JSON change log as landed from Mongo. `ns, op, id, ts, batch_ts, doc`, partitioned `(region, batch)`, JsonSerDe over `s3://wise-atlas-data-lake/cdc/staging` | seconds–minutes | **NO** |
| 2 | **Landing (raw CDC)** | `lake_cdc.wise_app_backend__*` | Iceberg, MERGEd to **one row per `_id`** — latest state per document. `_id, region, doc, op, ts, ingested_at` | ~30 min observed | **NO** — the rule above |
| 3 | **Facts (curated)** | `lake_cdc.*_facts_v3` | Typed, joined, consumer-ready. Partitioned `bucket(64, institute_id)` | **~5 min observed** | **YES — read these** |
| 4 | **Analyst / BI** | `processed` (IN), `processed_na` (NA) | Daily CTAS tables + curated views. Typed columns, no JSON | **daily** (one full Mongo dump/day) | YES, if daily is acceptable |
| 5 | **Legacy / trap** | `proc_zoom.zoom_MM_DD` (~250 tables); `lake_cdc.session_facts`, `lake_cdc.session_participant_facts` (**v2, no suffix — still built!**) | one-table-per-day anti-pattern; v2 is `DROP TABLE` + full CTAS **every 2 h** and is **tenant-filtered** (inline `tenant_map` CTE = onboarded tenants only) | v2 ≤2 h, briefly **absent** mid-rebuild | **NO — do not use** |

### Freshness, stated correctly
| Layer | Assume | Contractual threshold |
|---|---|---|
| `lake_cdc` raw | **≤ 15 min** (typical 5–10) | daemon alerts past 900 s |
| `lake_cdc.*_facts_v3` | **~30–45 min**, worst case 60 | watermark <25 min pass, <60 warn, ≥60 fail |
| `processed*` | ~24 h | nightly |

**Raw is fresher than the facts** — the facts add a 15-min refresh cadence plus a ~7-min pass on
top of raw's lag. Observed 2026-09-12 04:25 UTC: v3 watermark **03:55:38** ⇒ 30 min behind.
That is a real consideration *only* if you need sub-30-minute data; it is **not** a licence to read
raw CDC for a job that runs hourly or slower. The rule at the top still governs.

**⚠ Do not use per-row `refreshed_at` as a freshness signal.** It is `current_timestamp` at merge
time and only moves for rows that were *dirty* or in this hour's reconcile bucket. A cold
institute's rows can carry a `refreshed_at` days old and still be perfectly correct. The
authoritative signal is the S3 watermark object (§5).

**v2 facts are a trap, not merely dead.** `session_facts` (54,330 rows) and
`session_participant_facts` (344,139) vs v3's 3,864,043 / 115,400,407 — and v2 is *still rebuilt
every 2 hours*, restricted to onboarded tenants, and **does not exist** during its
`DROP`+`CTAS` window. Always use the `_v3` suffix.

### Databases in the account
`cdc_raw` (staging) · `lake_cdc` (landing + facts) · `processed` / `processed_na` (analyst, IN/NA) ·
`backend` / `backend_na` (raw daily dump feeding processed) · `proc_zoom` (legacy) ·
`backend_paper` / `processed_paper` (paper trading/test — not production) ·
`control_map` (small control tables: date map, inactive-teacher lists — **not** a region map) ·
`toplyne`, `cdn_logs_db`, `elb_logs`, `sampledb`, `default` (peripheral).

---

# 2. Regions — IN vs NA

There are two Wise deployments. How region is expressed **depends on the layer**:

| Layer | How region is expressed | Predicate |
|---|---|---|
| `cdc_raw.changes_v1` | partition column | `region = 'na'` (+ a `batch` value — injected projection) |
| `lake_cdc.wise_app_backend__*` (raw) | **partition column** | `region = 'na'` |
| `lake_cdc.*_facts_v3` | **plain column**; partition is `institute_id` | `institute_id = '<oid>'` — do **not** filter by region |
| `processed` / `processed_na` | **database name** | swap the database |

Region values are lowercase **`'in'` / `'na'`** in `lake_cdc` and `cdc_raw`.

**Table names never change between regions in `lake_cdc`** — one table serves both. Only the
analyst layer swaps database. NA is small: ~2–4% of rows on the big tables, so `region='na'`
prunes 96–98%.

`institute_id` is a globally unique ObjectId, so on a fact table it is sufficient on its own;
adding `region` neither prunes nor harms. NA holds **146 of 811** institutes in `session_facts_v3`.

**A namespace is not a tenant key.** One client can own many namespaces (each signup mints a
`-NNNN` suffix: `corizo` → 19), and many unrelated customers share `namespace='wise'`. Namespaces
are also truncated to ~24 chars. Prefer `institute_id`. See
[[20260910T233546Z-host-backfill-review]] for the full treatment.

---

# 3. Table index

## 3a. The fact layer — what consumers should read

### `lake_cdc.session_participant_facts_v3` — **the workhorse**
- **Grain:** one row per **(session_id, student_id)**. Verified unique (303,537 / 303,537 in NA).
- **Rows:** 115,400,407 · **665 institutes** · **Partition:** `bucket(64, institute_id)`
- **Watermark:** `refreshed_at` (timestamp), `src_ts` (bigint)
- **Columns:** `region, session_id, institute_id, session_date, student_id, student_name,
  student_email, class_id, course_name, teacher_id, teacher_name, attended, attend_minutes,
  is_enrolled, fee_amount, credits_consumed, src_ts, refreshed_at`
- **Contains future sessions** (93,504 NA rows `>= current_date`, all `is_enrolled`), so it answers
  attendance *and* upcoming from one table.
- **Canonical query:**
  ```sql
  SELECT student_id,
         count_if(attended)                                    AS attended_count,
         count_if(session_date >= current_date
                  AND session_date < current_date + interval '90' day) AS upcoming_count
  FROM lake_cdc.session_participant_facts_v3
  WHERE institute_id = '<oid>'          -- bucket partition: prunes to 1/64
  GROUP BY student_id
  ```
- **Cost:** `institute_id` predicate → **113 KB**. `region='na'` instead → **577 MB**. ~5,000×.

### `lake_cdc.session_facts_v3` — session-level
- **Grain:** one row per **session_id** · **Rows:** 3,864,043 · **811 institutes**
- **Partition:** `bucket(64, institute_id)` · **Watermark:** `refreshed_at`, `src_ts`
- **Notable columns:** `status, is_upcoming, is_conducted, is_cancelled, is_missed, is_quality,
  start_time, end_time, duration_minutes, participant_count, course_name, course_subject,
  course_type, teacher_*, credits_charged, fee_amount, fee_currency, fee_status, fee_derived,
  payout_*, student_feedback, teacher_feedback, ai_summary*, ai_quiz*, live_test_*`
- Use for session/teacher/course analytics. For anything **per student**, use participant facts.

**⚠ Bound your future window on both.** Recurring schedules project absurdly far out:
fleet `max(session_date)` is **2052-10-21**. For one NA institute, 26,722 rows are
`>= current_date` but only **11,119** are within 90 days and **562** are beyond a year.
Unbounded "upcoming" overcounts by ~2.4×.

### Other curated tables in `lake_cdc`
`exam_service__tests` (331,103) · `exam_service__submissions` (7,837,259) ·
`webapp__payment_orders` (195,520) · `webapp__payouts` (7,792) · `webapp__payout_accounts` ·
`webapp__payout_users` · `webapp__teacher_payout_account` ·
`webapp__user_auto_charge_payment_methods` · `webapp__user_payment_gateway`.
*(Row counts confirmed; grain/partitioning NOT individually verified — INFERRED.)*

## 3b. Raw CDC landing tables — `lake_cdc.wise_app_backend__*`

~90 tables, all identical in shape: `_id` (plain hex string), `region` (**partition**), `doc`
(JSON), `op`, `ts` (epoch **seconds**, = ingest time), `ingested_at` (timestamp). Iceberg,
`vacuum_max_snapshot_age_seconds = 259200` (3 days).

**All hold exactly one row per `_id`** — verified on 7 tables:

| table | rows | distinct `_id` | `in` | `na` | NA share |
|---|---|---|---|---|---|
| `__classparticipant` | 4,449,156 | 4,449,156 | 4,362,969 | 86,195 | 1.9% |
| `__user` | 3,913,927 | — | 3,819,777 | 94,150 | 2.4% |
| `__transaction` | 2,958,504 | 2,958,504 | 2,870,066 | 88,454 | 3.0% |
| `__instituteparticipant` | 964,913 | 964,913 | 928,238 | 36,675 | 3.8% |
| `__class` | 430,174 | 430,174 | 417,563 | 12,617 | 2.9% |
| `__registrationformsubmission` | 46,466 | 46,466 | 41,734 | 4,732 | 10% |
| `__sessioncredit` | 20,496 | 20,496 | 14,282 | 6,214 | 30% |
| `__registrationform` | 5,049 | 5,049 | 3,985 | 1,064 | 21% |

Other tables present: `__entity`, `__entityinteraction`, `__event`, `__announcements`,
`__assignments`, `__classroomfee`, `__classroompublicprofile`, `__classroomsection`, `__contract`,
`__contractsubmission`, `__coupon`, `__feestructure`, `__institute`, `__institutegroup`,
`__institutelocations`, `__institutepublicprofile`, `__lead`, `__leaderboard`, `__liveclass*`,
`__manualattendance`, `__premiumorder`, `__raw*`, `__report`, `__session*`, `__study_materials`,
`__tags`, `__teacherleave`, `__teacherpublicprofile`, `__temp_user`, `__transaction`,
`__userpreference`, `__verification`, `__whitelabel`, `__zoom`, and more.

## 3c. Analyst layer — `processed` / `processed_na`

Daily. ~85 tables + ~34 views per region. Views worth knowing (NA names shown; identical in
`processed` for IN):

| View | What it gives | Grain |
|---|---|---|
| `institute_participants` | `userid, instituteid, status, joinedon, relation, tags` — `relation ∈ STUDENT/PARENT/TEACHER/ADMIN` | (institute, user) |
| `user` | `userid, name, phonenumber, email, namespace, config_namespace, parentid, licensed, …` | user |
| `institute` | `instituteid, ownerid, name, namespace, settings, metadata` | institute |
| `class`, `class_participants` | class + enrolment, typed | class / enrolment |
| `student_registration_form` | form questions **joined to** each student's answers — replaces a 2-query unnest | (institute, question, user) |
| `registration_form` | form definitions | form |
| `zoomers`, `zoomers_v2`, `zoomers_v3` | session/teacher activity (legacy lineage) | session |
| `ft_student_*`, `ft_teacher_*` | per-role feature tables | user |
| `tests`, `study_materials_flat_v3`, `liveclassinsight_details` | as named | varies |

**Relation counts (NA):** STUDENT 25,252 · PARENT 9,117 · TEACHER 2,155 · ADMIN 158.

**⚠ Two defects in this layer to know about:**
1. **`CAST(json_extract(...) AS VARCHAR)` keeps JSON quotes.** `student_registration_form.answer`
   returns `"John"`, not `John`. Same for `questiontext`. Strip them, or the quotes propagate
   downstream. `json_extract_scalar` is the correct function and these views do not use it.
2. **`processed.user.config_namespace` is always NULL** (0 / 3,818,378) because the source `config`
   column is NULL in both `processed` and `backend`. See [[20260910T233546Z-host-backfill-review]].

**Table names differ between layers.** `lake_cdc.wise_app_backend__sessioncredit` ↔
`processed_na.wise_app_backend__session_credit`; `__registrationformsubmission` ↔
`__registration_form_submission`. Do not assume a name ports across layers.

---

# 4. The mapping people actually need

For each common question: the right source today, and where a fact is missing.

| Question | Correct source | Status |
|---|---|---|
| **Sessions attended per student** | `session_participant_facts_v3` · `WHERE institute_id=… AND attended` | ✅ fact exists |
| **Upcoming sessions per student** | `session_participant_facts_v3` · `session_date` between today and +90d | ✅ fact exists — **do not** join raw `classparticipant` |
| **Course/class names per student** | `session_participant_facts_v3.course_name` (+ `class_id`) | ✅ mostly — misses enrolments with **no sessions yet** |
| **Sessions / teachers / fees per session** | `session_facts_v3` | ✅ fact exists |
| **Test results** | `exam_service__submissions` / `__tests` | ✅ (grain unverified) |
| **Payments (webapp)** | `webapp__payment_orders`, `webapp__payouts` | ✅ (grain unverified) |
| **Roster: who is STUDENT/TEACHER/PARENT in an institute** | — | ❌ **FACT NEEDED** |
| **Contact details (name/email/phone) per institute member** | — | ❌ **FACT NEEDED** |
| **Students per institute** | — | ❌ **FACT NEEDED** (facts only cover students *with sessions*) |
| **Credit balance per student** | — | ❌ **FACT NEEDED** |
| **Invoices: paid / pending per student** | — | ❌ **FACT NEEDED** |
| **Parent → student edges** | — | ❌ **FACT NEEDED + source unknown** |
| **Registration form answers per student** | — | ❌ **FACT NEEDED** (daily view exists) |

## The "fact needed" list

**1. `institute_contact_dim`** — serves roster, contact details, and students-per-institute (three
of the gaps at once; the single highest-value fact to build).
- Grain **(institute_id, user_id)** · `bucket(64, institute_id)`
- `relation, status, joined_on, name, email, phone, parent_user_id, tags, region, src_ts, refreshed_at`
- Today: `processed_na.institute_participants` ⋈ `processed_na.user`, but **daily**.

**2. `student_credit_balance_facts`** — grain **(institute_id, user_id)**;
`credits_granted, credits_debited, balance, last_txn_at`.
Ledger is `__sessioncredit`: `type ∈ CREDIT (NA: 5,850 rows, 54,639.67) / DEBIT (365, 1,549.0)`,
amounts positive in both → `balance = SUM(CREDIT) − SUM(DEBIT)`. Only 20,496 rows fleet-wide —
cheap to build.

**3. `student_invoice_facts`** — grain **(institute_id, user_id)**;
`paid_amount, pending_amount, currency, last_charged_at`.
`__transaction` doc has `amount, chargedAt, receiverId, senderId, status, transactionType, type`
and **no `instituteId`** — institute scope must be reached via `class`, exactly the indirection a
fact should absorb. 2.96M rows: the most valuable raw table to remove from read paths.

**4. `registration_answer_facts`** — grain **(institute_id, user_id, question_id)**;
`question_text, question_type, answer` (unquoted), `status, submitted_at`.
`processed_na.student_registration_form` already does the join, but daily and JSON-quoted.

**5. `parent_student_edge_dim`** — grain (institute_id, parent_user_id, student_user_id).
**⚠ Blocked: the source is unknown.** The edge is not in what anyone currently reads —
`__instituteparticipant` PARENT docs carry **no child reference** (keys: `_id, createdAt,
instituteId, joinedOn, linkedDevices, metadata, relation, status, updatedAt, userId`; only 34 of
9,117 NA PARENT rows even have `metadata`), and `user.parentid` covers just **1,469 of 94,130** NA
users against 9,117 PARENT rows. Unchecked candidates: `__entity`, `__entityinteraction`,
`linkedDevices`, or app-side-only state. **Ask the backend team before building.** Any current
parent report is probably incomplete.

**6. `class_enrolment_facts`** *(lower priority)* — grain (institute_id, class_id, user_id);
`course_name, status, joined_on, is_active`. Only needed if enrolments with zero sessions must be
visible. Should honour `class.archived / hidden / published / deletedStudents / suspendedStudents`.

---

# 5. How the CDC pipeline works

**Confirmed** by the `airflow` expert from producer source + live prod inspection
(2026-09-12 04:25 UTC) — ask `dbb5ef4e`. Two medium-confidence spots flagged.

**The producer is not the airflow repo.** It is `wise-analytics-portal`, deployed to the Airflow
EC2 box (`i-096a2b1318a84960a`, ap-south-1) at `/home/ssm-user/wise/wise-analytics-portal`. The
airflow repo only *consumes* `lake_cdc`.

```
Atlas analytics secondaries (IN cluster + NA cluster)
  │ pymongo watch() change stream — ONE DAEMON PER CLUSTER
  ▼ cdc/wise_cdc/daemon.py   [systemd: wise-cdc-in.service, wise-cdc-na.service]
  │   → gzip NDJSON spool on local disk (/var/lib/wise-cdc/<region>/spool, 5 GiB cap)
  │   → S3 s3://wise-atlas-data-lake/cdc/staging/region=<r>/batch=<b>/
  │      (= external table cdc_raw.changes_v1)
  ▼ Athena MERGE, one per namespace across all pending batches
  │   (daemon's own _sink_loop, 30 s retry; workgroup `wise-cdc`)
  │   → lake_cdc.wise_app_backend__<coll>   (Iceberg, latest-state)
  ▼ Cloud Run job `wise-facts-refresh`, Cloud Scheduler EVERY 15 MIN
      → MERGE into lake_cdc.session_facts_v3 / session_participant_facts_v3
```

## 5a. Capture
- **Change-stream tailer, not a batch job.** Watches dbs `wise-app-backend`, `exam-service`,
  `webapp`, excluding `.Chat` / `.ChatMessage`. Both services verified `active running`.
- Memory-capped so it can never take Airflow down: `MemoryHigh=768M`, `MemoryMax=1G`,
  `OOMScoreAdjust=500`, `CPUQuota=100%`.
- **Batch cut at 5000 events / 32 MiB / 300 s**, whichever first. That 300 s is the freshness floor.
- Resume token advances **only after** a successful S3 upload → sink failures cost a replay,
  never a gap.
- MERGE is deliberately **off** the consume path (inlining it made catch-up slower than realtime).

## 5b. Column semantics — read this before writing any CDC query
| column | meaning |
|---|---|
| `op` | change-stream `operationType` verbatim: `insert`, `update`, `replace`, `delete`. **`seed` is not a Mongo value** — it is hardcoded by the backfill MERGE. `replace` is materialized but rare. |
| `ts` | Mongo **clusterTime in whole seconds**. **`0` on every `seed` row** and on synthetic reconcile deletes. |
| `ingested_at` | when the CDC *batch was cut* — pipeline time, not event time. **This is the freshness column**, and what the v3 watermark uses. |
| `doc` | relaxed extended JSON of the post-image; **NULL for deletes**. Kept as STRING end-to-end for schema-drift immunity. |
| `_id` | plain hex string (already extracted). The clean join key. |

**Never use `ts` as a freshness signal or a global ordering key** — seed rows sit at `ts=0`, so
`ORDER BY ts DESC` buries all history and `WHERE ts > <watermark>` **silently excludes every seed
row**. Use `ingested_at`.

**`seed` provenance:** history predating the stream was loaded from the old `mongo_etl` S3 dump
(not from Mongo) with a literal `'seed'` op and `ts = 0`. Earliest `ingested_at` is 2026-06-11.

## 5c. Deletes ARE propagated — `lake_cdc` is a mirror, not a log
**Correction to a widely-held assumption (including my own earlier one).** You never see
`op='delete'` precisely *because* the MERGE physically removes the row:
```sql
WHEN MATCHED     AND s.op  = 'delete' THEN DELETE
WHEN NOT MATCHED AND s.op != 'delete' THEN INSERT
```
So a Mongo delete makes the `_id` **vanish** from `lake_cdc`. Consequences:
- `lake_cdc.wise_app_backend__*` is a **latest-state mirror**, never an audit trail. "Row absent"
  means "deleted or never existed" — you cannot tell which, and you cannot recover history.
- Two delete paths: live change-stream events, and **weekly reconcile** tombstones
  (`synthetic_delete()` for any `_id` in the lake but not in Mongo).
- Within a MERGE batch, ordering is
  `ROW_NUMBER() OVER (PARTITION BY id ORDER BY ts DESC, (op='delete') DESC, batch_ts DESC)` — a
  trailing delete beats a same-second update, and replays resolve deterministically.

## 5d. What builds the v3 facts
**Not an Airflow DAG and not on the Airflow box.** Cloud Run job `wise-facts-refresh` via Cloud
Scheduler **every 15 min**, running `marts/wise_marts/facts_v3.py --refresh`.

**Incremental, never a rebuild:**
1. Read the watermark target first (`max(ingested_at)` over source collections) so anything landing
   mid-pass is caught next pass.
2. Compute the dirty set — one `ingested_at > <watermark>` CTE per source (`zoom,
   classparticipant, sessionaidata, sessionaisummary, sessionfeedbacksubmission, liveclassinsight,
   liveclasstest, transaction, class, user, institute`) fanned out to `(region, session_id)`.
3. MERGE those slices into both tables; DELETE tombstoned sessions.
4. **Once per hour, rolling-reconcile one of the 64 institute buckets** from scratch ⇒ every
   institute is fully re-derived roughly every **2.7 days**. This is the self-healing floor.
5. Advance the watermark **last**, only on full success. MERGEs are idempotent.

**Watermark is a JSON object in S3**, not a column or table —
`s3://wise-atlas-data-lake/cdc/state/v3/session_sync.json`:
```json
{"watermark":"2026-09-12T03:55:38.000000","reconcile_bucket":40,"reconcile_hour":4,"saved_at":1789186685.7}
```
Measured pass cost 420 s (session_facts 92 s, participants 97 s, rolling reconcile 213 s) — which
is why the cadence is 15 min rather than the originally designed 5.
A full build is the explicit one-off `facts_v3.py --backfill <table> --yes`; a refresh with no
stored watermark merely *establishes* one, so an accidental full rebuild is impossible.

## 5e. Maintenance — and a live failure
`lake/athena_maintenance.py`, driven by **systemd timers on the Airflow box**, per table:
`OPTIMIZE lake_cdc.<t> REWRITE DATA USING BIN_PACK` then `VACUUM lake_cdc.<t>`.

| unit | scope | schedule | state 2026-09-12 04:25 UTC |
|---|---|---|---|
| `wise-iceberg-optimize@hot.timer` | 9 hot tables | daily **20:35 UTC** | healthy, last ran 2026-09-11 20:40 |
| `wise-iceberg-optimize@all.timer` | all `lake_cdc` tables | **Sun 21:30 UTC** | ⚠️ **`@all.service` FAILED — last success 2026-09-06; weekly all-table compaction has not run in ~6 days** |

Hot set includes `__zoom, __rawzoomattendance, __liveclassinsight, __transaction, __user, __event,
exam_service__submissions`, **plus both `_v3` fact tables** (a MERGE every 15 min is exactly the
small-file problem this cleans).

The v3 tables lack `vacuum_max_snapshot_age_seconds` because `backfill_ctas` doesn't set it — they
VACUUM at the Athena default (7 days) rather than the raw tables' 3. An inconsistency, not a bug.

**`lake/dags/*.json` are NOT deployed** (`iceberg_optimize_etl`, `wise_marts_etl`,
`cdc_reconcile_etl`, `cdc_shadow_diff_etl`). `airflow dags list` on prod has none of them. systemd
timers + Cloud Scheduler are the truth.

## 5f. Regions — two capture processes, unified downstream
- One daemon per Atlas cluster; `region` is a **static literal per config file**
  (`cdc/config/cdc_in.yaml` → `in`, `cdc_na.yaml` → `na`). Mongo URIs come from env var **names**
  `WISE_CDC_MONGO_URI_IN` / `WISE_CDC_MONGO_URI_NA`, sourced from a root-owned 0600
  `EnvironmentFile=/etc/wise-cdc/env`. *(Names only — never values.)*
- The literal is threaded through the MERGE, which validates it against `^[a-z]{2}$`, prunes the
  staging scan by `region`, and joins on `t._id = s.id AND t.region = '<r>'`. Hence **one shared
  Iceberg table per collection**, written by two daemons that can never collide on a key.
- Both daemons write the **same** bucket / database / workgroup; storage is ap-south-1 for both
  (NA is Mongo-side NA only).
- **Downstream v3 is region-agnostic**: `region` is an ordinary column, the dirty set is keyed
  `(region, session_id)`, one pass covers both. The split exists only at capture.

## 5g. Other things that exist (and one more trap)
- **v2 report caches in S3, not Athena:** `s3://wise-atlas-data-lake/reports/{report_id}/{run_ts}/
  tenant_id=<tid>/*.gz`, indexed in Firestore, presigned 12 h.
- **v3 serving is query-time, not materialized.** A Cloud Run **warehouse gateway**
  (`/query` with `report_id` + `institute_ids`) runs report SQL live against `session_facts_v3`.
  Report ids include `institute_daily`, `payouts`, `payouts_overall_by_instructor`, `sessions`,
  `session_detail`, course/instructor/1:1 analytics, plus an **Explore** tab of 20 grain×preset
  aggregates. Named SQL in `marts/wise_marts/sql/`: `credits_ledger, one_to_one_summary,
  payouts_disbursed, transactions_report, students_report, sessions_long, session_detail,
  session_facts_select, participants_select`. **None of these are tables** — they are gateway
  reports. Note `credits_ledger` and `transactions_report` already encode logic for two of our
  "fact needed" gaps; check them before designing those facts from scratch.
- **`processed.*` is still produced nightly** by the airflow repo's `mongo_etl` / `mongo_etl_v3`
  DAGs (both unpaused; `mongo_etl_v4`, `mongo_na_etl`, `mongo_etl_paper` paused).
  mongodump → bsondump → gzip → S3 → Athena CTAS. Non-Iceberg, full rebuild. `lake_cdc` was built
  to replace it and it remains the shadow-diff reference. Point consumers at `lake_cdc` facts.
- **BigQuery `wise_analytics.cdc_changes` / `cdc_state` were decommissioned 2026-06-14.** Ignore
  any doc mentioning them.

## 5h. Reliability history — state the SLA honestly
Both regions have gone dark before: `cdc: fix crash loop on ChangeStreamHistoryLost (IN dark 12
days)` and `healthcheck: catch the failure modes that hid a 12-day outage`. The design invariant is
that **any CDC failure degrades to "as fresh as the last reconcile", never to wrong data**. So the
honest SLA is **"minutes, backed by a weekly correctness floor"** — not "minutes, guaranteed".

## 5i. Still unconfirmed (medium confidence)
1. **The v3 refresher's trigger resource.** Established it is *not* on the Airflow box (no timer,
   no DAG); repo docs + healthcheck name Cloud Scheduler → Cloud Run `wise-facts-refresh` every
   15 min, and the 15-min cadence is confirmed empirically by the watermark. The GCP resource
   itself was not queried.
2. **What actually triggers the weekly reconcile and daily shadow-diff.** Their `lake/dags/*.json`
   are undeployed and no matching systemd timer exists. Since the weekly reconcile *is* the
   correctness floor, this is the gap most worth closing. It may be a design document rather than
   a running job.

# 6. Query hygiene

## 6.1 Always supply the partition predicate

| Table kind | Partition | Predicate |
|---|---|---|
| `lake_cdc.*_facts_v3` | `bucket(64, institute_id)` | `institute_id = '<oid>'` |
| `lake_cdc.wise_app_backend__*` | `region` | `region = 'na'` |
| `cdc_raw.changes_v1` | `region`, `batch` (injected) | `region='na' AND batch='<batch>'` — required |
| `processed*` | mostly none (views over CTAS) | swap database for region |

Measured on `session_participant_facts_v3` (115.4M rows): `institute_id` → **113 KB**;
`region='na'` → **577 MB**. On a fact, **region does not prune**. Use `institute_id`.

## 6.2 `row_number() OVER (PARTITION BY _id ORDER BY ts DESC)` is a NO-OP on `lake_cdc`

The idiom is right for an append-only log — which `cdc_raw.changes_v1` is. But
`lake_cdc.wise_app_backend__*` is the **MERGEd result**: `count(*) == count(DISTINCT _id)` on every
table checked. The window cannot eliminate a row; it forces a **full sort/shuffle of the whole
table before any filter applies**. Delete it; output is identical.

Nothing in the table name or columns (`op`, `ts` are present either way) tells you which you have.
**The test:** `SELECT count(*), count(DISTINCT _id) FROM <table>` — equal means no dedup needed.

```sql
-- WRONG: full shuffle, no pruning, and the window does nothing
SELECT * FROM (
  SELECT json_extract_scalar(doc,'$["userId"]["$oid"]') AS user_id,
         row_number() OVER (PARTITION BY _id ORDER BY ts DESC) rn
  FROM lake_cdc.wise_app_backend__instituteparticipant
) WHERE rn = 1

-- RIGHT (when CDC genuinely is the source): partition predicate, no window
SELECT json_extract_scalar(doc,'$["userId"]["$oid"]')      AS user_id,
       json_extract_scalar(doc,'$.relation')               AS relation
FROM lake_cdc.wise_app_backend__instituteparticipant
WHERE region = 'na'                                            -- partition
  AND json_extract_scalar(doc,'$["instituteId"]["$oid"]') = '<oid>'

-- RIGHT, incremental: use ingested_at, NOT ts (seed rows sit at ts = 0)
  AND ingested_at > TIMESTAMP '2026-09-12 03:55:38'
```

## 6.3 The three silent-failure traps in `doc`

These return **empty results, not errors** — the worst failure mode there is.

**(a) Every ObjectId is Extended JSON `{"$oid":"..."}`.**
```sql
json_extract_scalar(doc, '$.instituteId')             -- NULL. always. silently.
json_extract_scalar(doc, '$.instituteId.$oid')        -- ERROR: Invalid JSON path
json_extract_scalar(doc, '$["instituteId"]["$oid"]')  -- ✅ the only working form
```
A per-tenant query written the first way returns **zero rows** and reads as "this tenant has no
data". The bracket form is mandatory because `$oid` begins with `$`.
**This one is uniform across ops** — measured on `__class` NA: the bracket form resolves for
seed (4,001/4,049), update (8,122/8,137) and insert (431/431); the plain form for **none**. Relaxed
extended JSON still wraps ObjectIds, so unlike dates there is nothing to coalesce.
**The top-level `_id` column (outside `doc`) is already a plain hex string — use it as the join key.**

**(b) Date encoding differs *within the same table*, by `op`. This is the worst trap here.**
`seed` rows are **canonical** extended JSON; `insert`/`update` rows are **relaxed**. Measured on
`lake_cdc.wise_app_backend__class`, `region='na'`:

| `op` | rows | `$["createdAt"]["$date"]` (ISO string) | `$["createdAt"]["$date"]["$numberLong"]` |
|---|---|---|---|
| `update` | 8,137 | **8,137** | 0 |
| `insert` | 431 | **431** | 0 |
| `seed` | 4,049 | 0 | **4,049** |

So either path alone **silently drops a third of the table** — the ISO path loses all pre-CDC
history, the `$numberLong` path loses everything since 2026-06-11. **Always coalesce:**
```sql
coalesce(
  from_iso8601_timestamp(json_extract_scalar(doc,'$["createdAt"]["$date"]')),            -- insert/update
  from_unixtime(CAST(json_extract_scalar(doc,'$["createdAt"]["$date"]["$numberLong"]') AS BIGINT)/1000)  -- seed
) AS created_at
```
`airflow/tasks/ghl_sync/athena_source.py` already has `OID` / `NUM` / `AMT` helpers implementing
exactly this — reuse that pattern rather than reinventing it.
(`processed` / `backend` use `{"$date":{"$numberlong":…}}` — note **lowercase** `numberlong` there
vs camelCase `$numberLong` in `lake_cdc`. Paths do not port between layers.)

**(c) `doc` keys are camelCase; `processed` columns are lowercase.**
`instituteId, userId, classId, createdAt, chargedAt` vs `instituteid, userid`. Same silent NULL.

## 6.4 Bound future-dated windows
Recurring schedules project years out — fleet `max(session_date)` **2052-10-21**. Always bound:
`session_date >= current_date AND session_date < current_date + interval '90' day`.
Unbounded, one NA institute's "upcoming" was 26,722 rows vs 11,119 real ones (~2.4× overcount).

## 6.5 Cost sanity
- Fact + `institute_id`: **~100 KB** per tenant query. Fine at any cadence.
- Fact without it: **~600 MB**.
- Raw `__transaction` without `region`: **~700 MB+** per query.
- A 9-query × 23-tenant × 4-runs/day job is **828 executions/day**. At ~600 MB each that is
  ~500 GB/day scanned; with correct predicates it is a few hundred MB/day. That is the whole
  argument for the rule at the top of this file.
- Iceberg **metadata-only** queries are nearly free: `count(*)` and `GROUP BY <partition col>`
  came back in 0–25 KB. Use them to size a table before scanning it.

## 6.6 Review checklist
1. Is this consumer code reading raw CDC? → **it should read a fact; if none exists, say so.**
2. Partition predicate present, and the *right* one for the layer?
3. Any `row_number() … PARTITION BY _id` on `lake_cdc`? → delete it.
4. Every id path bracketed as `$["x"]["$oid"]`?
5. Future-dated window bounded?
6. Right region expression for the layer (partition vs database)?
7. Deleted rows: `lake_cdc` **removes** them (mirror, not a log) — you cannot see history, and
   "absent" is indistinguishable from "never existed".
8. Validate: `explain_query`, then `run_query` with a small `max_rows`, and read `bytes_scanned`.

---

# 7. MCP server (`athena`) — safety

Read-only: `SELECT / WITH / SHOW / DESCRIBE / EXPLAIN` only; DML/DDL rejected by token match;
multi-statement payloads rejected; workgroup + S3 output pinned by config; per-query timeout and
bytes-scanned cap. Tools: `list_databases`, `list_tables`, `describe_table`, `get_partitions`,
`explain_query`, `run_query`.

**Redaction matches OUTPUT column names**, not source columns: `loginpin, phonenumber, email,
password, token, secret, apikey` come back `[REDACTED]`. A pivoted column *aliased* `email` is
redacted even if the source is `answer` — when pivoting survey data, name outputs
`reg_email_addr` / `reg_contact_number`. Don't bypass; request aggregates.

**`doc` is not redacted** — it is one opaque varchar. Never `SELECT doc` wholesale when the
document contains contact details; extract the specific non-sensitive fields, or inspect
**key names only**:
```sql
SELECT array_join(array_sort(map_keys(CAST(json_parse(doc) AS MAP(VARCHAR,JSON)))), ', ')
FROM lake_cdc.wise_app_backend__user WHERE region='na' LIMIT 1
```

**This expert is `ask` only.** It reviews, explains, and documents. It never writes, deploys, or
pushes.

# 8. Credentials
boto3 default chain — `AWS_ACCESS_KEY_ID` / `AWS_SECRET_ACCESS_KEY` / `AWS_SESSION_TOKEN`, or
`AWS_PROFILE`, or SSO / instance role. `scripts/config.yaml` is gitignored.
**Names only, here and in every answer. Never a value.**

# 9. Repo layout
`schemas/INDEX.md` (generated TOC) · `schemas/{processed,raw,source,_gaps}/` (one `.md` per table:
front-matter with partition keys + S3 location, typed columns, enum distributions, inferred JSON
path tree, full DDL, and a `<!-- HUMAN NOTES BELOW -->` marker — **anything below it survives
re-sync**) · `semantics/{glossary,joins,dependencies}.md` · `examples/` (vetted SQL) ·
`knowledge/asks/` (one file per answered ask) · `scripts/sync_schemas.py` (idempotent regen).

⚠ `schemas/` documents the **`processed` / `backend`** layers. It does **not** yet cover
`lake_cdc` or the fact tables — this file is currently the only documentation of the fact layer.

# 10. Open questions
1. **Where is the parent→student edge persisted?** Blocks `parent_student_edge_dim`. Backend team.
   Unchecked candidates: `__entity`, `__entityinteraction`, `linkedDevices`, app-side-only state.
2. **`wise-iceberg-optimize@all.service` is in a FAILED state** — weekly all-table compaction has
   not succeeded since 2026-09-06. Someone should look. *(Reported by the airflow expert; not ours
   to fix.)*
3. **What actually triggers the weekly reconcile** (`wise-cdc-reconcile`)? It is the documented
   correctness floor, its DAG JSON is undeployed, and no systemd timer matches. If nothing runs it,
   the freshness contract in §5h needs restating.
4. **Confirm the Cloud Run / Cloud Scheduler resources** behind the v3 refresh
   (`gcloud scheduler jobs list --location=asia-south1`, `gcloud run jobs list`).
5. **Do the `_v3` facts honour `class.archived / hidden / deletedStudents / suspendedStudents`?**
   Affects course-tag and enrolment correctness.
6. **Does `session_participant_facts_v3` include enrolments with no sessions?** Evidence suggests
   no — that is the `course_tags` coverage gap.
7. **Grain and partitioning of `exam_service__*` and `webapp__*`** — row counts confirmed, shape
   not verified.
8. **Should `wise-marts.timer` still be enabled?** Every 2 h it drops and recreates the v2
   `session_facts` in the same schema consumers browse.
9. **Check `marts/wise_marts/sql/credits_ledger` and `transactions_report`** before designing
   `student_credit_balance_facts` / `student_invoice_facts` — the logic may already exist.
