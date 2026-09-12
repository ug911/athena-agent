# The six missing facts — design

Owner: **athena-agent** (data model). Implementation: **airflow**.
Written 2026-09-12. Under the rule: *raw `lake_cdc` is the landing zone; consumers read facts.*

## Conventions all six inherit

Copy the `_v3` pattern rather than inventing one — it is proven in production:

- **Iceberg**, PARQUET + ZSTD, `LOCATION s3://wise-atlas-data-lake/cdc/iceberg/lake_cdc/<table>/`
- **`PARTITIONED BY (bucket(64, institute_id))`** — the consumer's tenant filter becomes the
  partition filter. Measured effect on `session_participant_facts_v3`: `institute_id` predicate
  113 KB vs `region` predicate 577 MB, ~5,000×.
- **`region` is an ordinary column**, never the partition. `institute_id` is a globally unique
  ObjectId, so it is sufficient alone.
- **Every table carries `src_ts BIGINT` and `refreshed_at TIMESTAMP`.**
- **Watermark: `ingested_at`**, stored as a JSON object in S3 next to the existing one
  (`cdc/state/v3/session_sync.json`), *never* `ts` — `ts` is `0` on every `seed` row, so a `ts >`
  predicate silently excludes all pre-2026-06-11 history.
- **Incremental MERGE + rolling reconcile.** Reuse the v3 shape: dirty-set MERGE each pass, plus
  one of the 64 buckets fully recomputed per hour ⇒ every institute self-heals every ~2.7 days.
  This is what makes a missed change recoverable rather than permanent.
- **Set `vacuum_max_snapshot_age_seconds = 259200`** at create time. The `_v3` tables omit it and
  default to 7 days — an inconsistency worth not repeating.
- **Add each new table to `HOT_TABLES`** in `lake/athena_maintenance.py`. A table MERGEd every
  15 min generates small files; that is what the hot OPTIMIZE set is for.

**Extraction rule — per field, not per table.** Do not apply `$["x"]["$oid"]` uniformly. Top-level
Mongoose-typed ObjectIds are `$oid`-wrapped; ids nested inside `metadata` (a Mixed subdocument)
are usually plain strings **and sometimes both**. Always `coalesce(plain, oid)` and assert the
census invariant from `accuracy-proof.md` §B1.

---

## 1. `institute_contact_dim` — build this first

Closes three gaps at once (roster, contact details, students-per-institute) and unblocks
`parents()`. Highest value per unit of work.

- **Grain:** one row per **(institute_id, user_id)**
- **Source:** `__instituteparticipant` ⋈ `__user` on `userId`
- **Columns:** `region, institute_id, user_id, relation, status, joined_on, name, email, phone,
  parent_user_id, tags, additional_note, created_at, updated_at, src_ts, refreshed_at`
- **`relation` ∈ `STUDENT | PARENT | TEACHER | ADMIN`** (NA counts: 25,252 / 9,117 / 2,155 / 158).
  Keep `ADMIN` — the current sync drops it, and that should be a consumer-side choice.
- **Dirty set:** `ingested_at >` watermark on `__instituteparticipant` **or** `__user`. The user
  join means a name/email change must mark the row dirty — easy to miss, and it is the most
  visible field in GHL.
- **Reconcile:** rolling bucket recompute; delete rows whose `(institute_id, user_id)` no longer
  exists in `__instituteparticipant`. Deletes matter here — `lake_cdc` removes deleted rows, so
  the fact must delete too or it will retain departed members forever.
- **Note:** `phone`/`email` are PII. The fact is fine; be careful in ad-hoc queries — the MCP
  redacts on **output column name**, so keep those names.

## 2. `student_credit_balance_facts`

- **Grain:** one row per **(institute_id, user_id)**
- **Source:** `__sessioncredit` — a true ledger, one row per grant/consumption, 20,496 rows
  fleet-wide. Cheap.
- **Columns:** `region, institute_id, user_id, credits_granted, credits_debited, balance,
  last_txn_at, src_ts, refreshed_at`
- **Logic:** `type ∈ CREDIT | DEBIT`, `credit` positive in both ⇒
  `balance = SUM(credit WHERE CREDIT) − SUM(credit WHERE DEBIT)`.
  Verified NA: CREDIT 5,850 rows / 54,639.67, DEBIT 365 / 1,549.0.
- **Do not dedupe by `_id`** — every ledger row is a distinct event. The `row_number()` habit is
  actively wrong here.
- **`metadata.invoiceId` is a plain string** (3,543/3,543 NA), not `$oid`-wrapped. Carry it if we
  want credits↔invoices linkage, with the coalesce rule.
- **Check first:** `marts/wise_marts/sql/credits_ledger` already exists as a gateway report — the
  logic may be written and only needs materialising.

## 3. `student_invoice_facts`

The highest-cost raw table to remove from read paths (2.96M rows), and the one with the most
correctness landmines.

- **Grain:** one row per **(institute_id, user_id, currency)** — *not* per user. See money note.
- **Source:** `__transaction`, scoped to institute via `metadata.classId` → `__class.instituteId`
- **Columns:** `region, institute_id, user_id, currency, paid_minor, pending_minor,
  invoice_count, last_charged_at, src_ts, refreshed_at`
- **Three things that will break this if not designed in:**
  1. **`__transaction` has no `instituteId`.** Scope must be reached via `metadata.classId` →
     class. That indirection is exactly what the fact should absorb once, rather than every
     consumer re-deriving it.
  2. **`metadata.classId` is mixed-encoded** — plain string on 2,760,425 IN / 86,225 NA rows, but
     `$oid`-wrapped on 131 IN / 3 NA. Coalesce, or silently drop those rows.
  3. **Money is a nested object in minor units, multi-currency.**
     `amount = {"value": <int|{"$numberInt"}|{"$numberDouble"}>, "currency": "<ISO>"}`.
     Seed rows use `$numberInt` (8 IN rows `$numberDouble`); insert/update rows are plain numbers.
     **35 distinct currencies in IN, 16 in NA.** Store **integer minor units plus currency code**,
     and never emit a currency-blind total. A cross-currency sum is a wrong number that looks
     right — the worst failure mode we have.
- **Check first:** `marts/wise_marts/sql/transactions_report` exists as a gateway report.

## 4. `registration_answer_facts`

- **Grain:** one row per **(institute_id, user_id, question_id)**
- **Source:** `__registrationform.fields` (unnest) LEFT JOIN `__registrationformsubmission.answers`
  (unnest) on `institute_id + question_id`
- **Columns:** `region, institute_id, user_id, question_id, question_text, question_type,
  question_required, answer, status, submitted_at, src_ts, refreshed_at`
- **`processed_na.student_registration_form` already implements this join** — reuse its logic, but
  **not** its output: it uses `CAST(json_extract(...) AS VARCHAR)`, which returns JSON text
  *with surrounding quotes*, so `answer` comes back as `"John"`. The fact must store unquoted
  values (`json_extract_scalar`). Pushing the quoted form to GHL writes `"John"` into every
  custom field.
- **Naming:** do not name output columns `email` / `phonenumber` — the MCP redacts on output
  column name. Use `reg_email_addr` / `reg_contact_number` for pivoted answers.
- Small: 5,049 forms / 46,466 submissions fleet-wide.

## 5. `class_enrolment_facts`

Lower priority — only needed if enrolments with **no sessions yet** must be visible. Today
`session_participant_facts_v3.course_name` covers (student, class) pairs that have at least one
session, which is most of them.

- **Grain:** one row per **(institute_id, class_id, user_id)**
- **Source:** `__classparticipant` ⋈ `__class`
- **Columns:** `region, institute_id, class_id, user_id, course_name, relation, status, joined_on,
  is_active, src_ts, refreshed_at`
- **Must honour** `class.archived`, `hidden`, `published`, `deletedStudents`, `suspendedStudents`
  — otherwise we tag contacts with courses they were removed from. **Open question: whether the
  `_v3` facts already honour these. Confirm before building, or we will build a fact that
  disagrees with `session_participant_facts_v3` and have no way to say which is right.**

## 6. `parent_student_edge_dim` — **BLOCKED, needs an upstream capture change**

**This fact cannot be built from what the lake holds today.** That is a finding, not a delay.

Evidence:
- `__instituteparticipant` PARENT docs contain **no child reference whatsoever** — keys are
  `_id, createdAt, instituteId, joinedOn, linkedDevices, metadata, relation, status, updatedAt,
  userId`. Only 34 of 9,117 NA PARENT rows even carry a `metadata` key.
- `user.parentid` resolves for **1,469 of 94,130** NA users (~1.6%) against 9,117 PARENT
  participant rows — it explains at most a sixth of the parents.

So the edge is either app-side-only, or in a collection nobody has checked.

**Two steps, in order:**

1. **Locate it.** Unchecked candidates: `__entity` / `__entityinteraction` (both already
   referenced by ghl_sync — suggestive), `linkedDevices`, `__classparticipant.metadata`, or the
   `backend-api` Mongoose models. This is a bounded investigation, and I should do it before
   anyone designs the fact.
2. **If it genuinely is not persisted relationally**, the capture change is upstream in
   backend-api: persist the parent→child link as a first-class field — either
   `InstituteParticipant.childUserIds: [ObjectId]` on the PARENT row, or a dedicated
   `ParentStudentLink` collection `{parentUserId, studentUserId, instituteId, status}`. Either is
   picked up by CDC automatically once it exists, since the daemon watches the whole database.
   **That is a backend-api change — the application backend, which we do not own.** It goes to
   that team as a request, not to airflow.

**Until then:** whatever `parents()` emits today is incomplete, and we should say so rather than
optimise it. Do not port the current logic into a fact and thereby bless it.

---

## Build order

1. `institute_contact_dim` — unblocks the most, no new semantics
2. `student_credit_balance_facts` — small, self-contained, logic may already exist
3. `student_invoice_facts` — highest cost saving, highest care (money + mixed encoding)
4. `registration_answer_facts` — small, but fix the quoting defect
5. `class_enrolment_facts` — only after the archived/deleted question is answered
6. `parent_student_edge_dim` — after the edge is located; may need backend-api first

Each lands with its own capture-diff cycle per `accuracy-proof.md` §4.

## Open questions blocking design

1. **Where is the parent→student edge?** Blocks fact 6. I will take this.
2. **Do the `_v3` facts filter `class.archived` / `deletedStudents` / `suspendedStudents`?**
   Blocks fact 5 and affects course tags. Airflow can answer from `marts/` source.
3. **Do `credits_ledger` and `transactions_report` gateway SQL already encode facts 2 and 3?**
   Airflow to check before we design from scratch.
