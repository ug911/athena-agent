# Build spec for the six ghl_sync facts: grain, columns, joins, traps, institute_id derivability

- **id:** 66ccf0d0-af1f-4e3a-9a61-f8f887c2f6e7   **from:** airflow   **depth:** 0   **utc:** 20260912T125324Z

## Question

airflow is building the missing facts for the ghl_sync read path and asked for data-model calls,
as a build spec not a survey: for each of institute_contact_dim, student_credit_balance_facts,
student_invoice_facts, registration_answer_facts, class_enrolment_facts and
parent_student_edge_dim — (a) exact grain, (b) column list with types, (c) source collections and
the join, (d) correctness traps, (e) whether `institute_id` is derivable and if not what it must
join through. Plus specific sub-questions: should institute_contact_dim hold status/relation as
columns or be pre-filtered to ACCEPTED STUDENT/TEACHER; do the `_v3` facts honour
`class.archived`/`deletedStudents`/`suspendedStudents`; is credit balance simply
sum(CREDIT)−sum(DEBIT) or is there a per-doc "remaining"; is `metadata.classId` the only path to
institute for transactions and what to do with absent/orphan classIds; is the `FEE_COLLECTION`
filter right and what are all the invoiceType values; should registration be long format and where
does option-code decoding belong; is class_enrolment_facts the right answer for course_tags; and is
`user.parentIds` the only parent edge — i.e. is a fact a faithful port of an incomplete edge, or
blocked on upstream capture. Finally: is counting upcoming per student in
session_participant_facts_v3 EXACTLY equal to today's formula (upcoming per class from
session_facts_v3 × ACCEPTED STUDENT enrolments)?

Full answer written to the ask's temp path; summary below.

## Answer

**Three of the caller's premises were wrong, two load-bearing — stated first per protocol §7.**

1. **`spf_v3` has no `is_upcoming`.** That column is on `session_facts_v3` only
   (`facts_v3.py:164`, `s.start_ts > current_timestamp`). On spf_v3 the only future test is
   `session_date >= current_date`, which is date-grained and counts sessions finished earlier today.
2. **`spf_v3.fee_amount` and `spf_v3.credits_consumed` are hardcoded `cast(NULL AS double)`**
   (`facts_v3.py` ~line 283); verified 0 non-null of 303,644 NA rows. I had earlier implied
   `credits_consumed` was usable — that was my error.
3. **The `FEE_COLLECTION` filter is on the wrong field** — see fact 3, the most serious finding.

**Self-correction:** I previously reported the parent edge was not derivable, having measured
`parentId` (singular). The real field is **`parentIds` (plural array)**: IN 16,323 users / 16,467
edges, NA 6,222 users / 6,423 edges. The edge exists; the fact is a **faithful port (i)**, not
blocked.

### 1. institute_contact_dim
Grain **(region, institute_id, user_id)**; `institute_id` derivable **directly** from
`instituteParticipant.instituteId`. Source `instituteparticipant ⋈ user` on `userId`.
**Keep `status` and `relation` as columns — do not pre-filter.** Three consumers need three
different filters (participants = ACCEPTED STUDENT/TEACHER; students-per-institute = STUDENT;
parents = PARENT), pre-filtering destroys PARENT (9,117 NA) and ADMIN (158 NA) rows that fact 6
needs, and filtering inside a bucket-pruned partition is free while pre-filtering is irreversible.
Traps: dirty set must union `__user` (a name/email change produces no participant row change);
reconcile must DELETE (lake_cdc physically removes deleted docs).

**Sub-question — do the `_v3` facts honour archived/deleted? NO, definitively.**
`grep -rn "archived|deletedStudents|suspendedStudents|hidden|published" marts/wise_marts/` → one
unrelated comment. The `classes` CTE is unfiltered. This does **not** affect institute_contact_dim
(institute-grained) but does bind `class_enrolment_facts`.
**Worse:** `facts_v3.py:253` builds enrolment as `classparticipant WHERE relation='STUDENT'` with
**no status filter**, and NA classparticipant is STUDENT/REMOVED **17,210** vs STUDENT/ACCEPTED
15,971 — **51.9% of NA STUDENT rows are REMOVED and counted as enrolled by `spf_v3.is_enrolled`.**
A pre-existing defect in spf_v3 affecting every consumer.

### 2. student_credit_balance_facts
Grain **(region, institute_id, user_id)** — **not** including class_id. `institute_id` derivable
directly. **There is no per-doc `remaining`**: exhaustive key-shape enumeration across both regions
gives exactly `__v, _id, assignedBy, classId?, createdAt, credit, instituteId, metadata?, note,
type, updatedAt, userId`. So `sum(CASE WHEN type='DEBIT' THEN -credit ELSE credit END)` — the
caller's current expression — **is correct**. Keep zero balances in the fact, drop them in the
consumer ("balance 0" ≠ "no credit record"). Traps: never dedupe by `_id` (each ledger row is a
distinct event); **`classId` absent on 1,412/6,226 NA rows (22.7%)**, which is why class_id must not
be in the grain; no `seed` rows exist so `credit` is uniformly plain (worth an assertion).

### 3. student_invoice_facts — contains the most serious finding
Grain **(region, institute_id, user_id, currency)** — currency in the key is mandatory.
`institute_id` **NOT derivable**; `metadata.classId → class.instituteId` is confirmed the only path
(transaction doc has no instituteId and no other institute-bearing field).

**🔴 The `FEE_COLLECTION` filter is on `metadata.invoiceType`, which is a strict subset of
top-level `transactionType`:**

| region | transactionType=FEE_COLLECTION | metadata.invoiceType=FEE_COLLECTION | dropped |
|---|---|---|---|
| in | 2,615,790 | 2,146,400 | **469,390 (17.9%)** |
| na | 52,925 | 26,189 | **26,736 (50.5%)** |

Rows matching metadata but not transactionType: **0 in both regions**. The dropped NA rows are real
fee transactions (transactionType=FEE_COLLECTION, classId present, statuses CHARGED/REJECTED/
OFFLINE_PAYMENT/INVOICE). **Filter on `doc.transactionType`.** Payouts are excluded either way, so
the caller's payout belief was right but incomplete.
Complete `metadata.invoiceType` set: `FEE_COLLECTION`, `TUTOR_PAYOUT`, `WISE_PREMIUM`, `NULL`.

**🔴 Money:** `amount = {"value": <plain | {"$numberInt"} | {"$numberDouble"}>, "currency":"ISO"}`.
`$.amount` and `$numberInt/Long/Decimal` directly under `amount` return NULL on **all 2,949,539
rows** — the value is one level deeper. Seed rows `$numberInt` (8 IN `$numberDouble`),
insert/update plain. **35 currencies in IN, 16 in NA** — store integer minor units + ISO code,
never a cross-currency sum.
**🟠 `metadata.classId` mixed-encoded:** plain on 2,760,425 IN / 86,225 NA, `$oid` on 131 IN / 3 NA.
Orphan classIds: inner-join for the fact **plus a monitored orphan counter** — silently dropping
money is the failure to avoid.

### 4. registration_answer_facts
Grain **(region, institute_id, user_id, question_id)** — **long, keyed on question_id not label.**
`institute_id` derivable directly from either doc (prefer the form's, assert agreement).
`fields[]` = `{questionId, questionText, required, type, options?, maxAllowedAnswers?}`;
`answers[]` = exactly `{questionId, answer}`.
**Long format** because question sets differ per institute and change over time — a wide fact would
need per-tenant schema changes. The institute's label set is then a cheap
`SELECT DISTINCT question_id, question_label` on the bucket-pruned partition.
**Option decoding belongs in the FACT.** `options` is a code→label **map**
(`{"1":"🎮 Gaming","2":"🎵 Listening to music",…}`, type POLL) and answers store only the opaque
code — measured values `"2"`, `"A"`, `"1"`, `"B"`. Undecoded, GHL receives `2` for "Hobbies".
Codes are not uniformly numeric, so decode by map lookup, never by int cast or array index.
Store both `answer_raw` and `answer_label`. `questionId` is a **slug** (`user_email`, `hxcdc6jh`),
never an ObjectId. Reuse `processed_na.student_registration_form`'s join logic but **not** its
output — it uses `CAST(json_extract(…) AS VARCHAR)` so answers come back as `"John"` with quotes.

### 5. class_enrolment_facts
**Confirmed the right answer; the caller's refusal to port course_tags to spf_v3 is correct**, for a
stronger reason than coverage: `spf_v3.is_enrolled` has no status filter (51.9% NA REMOVED), so
tags would include courses students were removed from. Coverage also bites — on thinktankjr,
**1,010 ACCEPTED (student,class) pairs exist but only 565 appear in spf_v3** (445 = 44% have no
sessions).
Grain **(region, institute_id, class_id, user_id)**; `institute_id` **NOT derivable** from
classparticipant — join through `class`. Columns include `course_name, subject, class_type,
relation, status, joined_on, is_active, class_archived, class_hidden, class_published`.
Carry status; compute `is_active`; expect and document deliberate disagreement with
`spf_v3.course_name`.

### 6. parent_student_edge_dim — (i) faithful port, NOT blocked
`user.parentIds` is the edge and is what `parents()` already reads. Grain
**(region, institute_id, parent_user_id, student_user_id)**. `institute_id` **NOT derivable** —
`parentIds` is a global user-level edge with no institute scope; attribute by joining the *student*
to `institute_contact_dim`. Build after fact 1. Elements uniformly `$oid`-wrapped (6,423/6,423 NA).
**The edge is incomplete: 5,087 distinct parents referenced vs 9,120 distinct PARENT
institute-participants (~44% orphaned).** A faithful port reproduces that; record provenance in an
`edge_source` column. Do not also fold in singular `parentId` without checking subset overlap —
that would be a behaviour change.

### Equivalence: `upcoming` — NOT equal, four differences, current formula more correct on three
Measured on thinktankjr (`69b84f3c99b41087144ba02e`, NA):

| measure | value |
|---|---|
| spf_v3 `is_enrolled AND session_date >= current_date` | 26,765 |
| restricted to ACCEPTED enrolments | 21,246 |
| **overcount from non-ACCEPTED** | **+5,519 (+26.0%)** |
| ACCEPTED pairs invisible to spf_v3 | 445 of 1,010 (44%) |

(1) enrolment status — spf_v3 overcounts +26.0%; (2) no `is_upcoming`, date-vs-timestamp counts
sessions finished earlier today; (3) session coverage — spf_v3's `sess` comes from the `zoom`
collection bounded to 730 days, so future sessions without a zoom doc are absent (shared by
session_facts_v3, so a wash between the formulas but both under-report vs `class.schedule`);
(4) far-future inflation affects both — 26,722 rows `>= current_date` vs 11,119 within 90 days.
**Recommendation: neither as-is.** Compute upcoming from `session_facts_v3.is_upcoming` bounded to
+90d × ACCEPTED non-archived enrolments from `class_enrolment_facts`. Swapping to spf_v3 trades a
216 MB scan for a 26% accuracy regression, failing the hard constraint.

**Build order:** institute_contact_dim → credit_balance → class_enrolment → registration_answer →
invoice (land the `transactionType` fix as a *separately declared* correction, or the diff will show
a 50% NA change with no attribution) → parent_edge.

**Confidence: high** on the filter grep, spf_v3 NULL columns, the transactionType subset
relationship, no-`remaining`, `parentIds` existence, classparticipant status distribution, money
encoding, and the thinktankjr numbers. **Medium** on the 44% parent-orphan rate (fleet-wide NA
comparison; some referenced parents may not be institute participants). **Low/unmeasured, flagged
not guessed:** the disagreement rate between `status='REMOVED'` and class-level
`deletedStudents`/`suspendedStudents` (decides `is_active`); the multi-select answer shape for the
20 NA `maxAllowedAnswers` fields; whether singular `parentId` is a subset of `parentIds`; and
whether `senderId` is always the student on FEE_COLLECTION rows (assumed, not verified).

**Check next:** (1) run today's `invoices()` with `transactionType` for 3 NA tenants and diff — if
values ~2×, that is a live correctness bug deserving its own ticket ahead of the optimisation;
(2) measure the deletedStudents/status disagreement; (3) enumerate multi-select answer shapes;
(4) verify `senderId` is always the student; (5) decide `spf_v3.is_enrolled`'s missing status filter
separately — it affects every consumer, not just ghl_sync, and must not ride along with this work.

## Evidence

Source read (wise-analytics-portal, read-only):
- `marts/wise_marts/facts_v3.py:164` — `is_upcoming` defined on session_facts_v3 only.
- `marts/wise_marts/facts_v3.py:218-292` — `_participants_base()`: `sess` from `zoom` bounded
  `start_ts >= current_timestamp - interval '730' day`; `enroll` = `classparticipant WHERE
  relation='STUDENT'` (line 253, **no status filter**); `fee_amount`/`credits_consumed` hardcoded
  `cast(NULL AS double)`; FULL OUTER JOIN attend×enrolled_sessions; final
  `JOIN classes cl ON cl.id = c.class_id`, `WHERE cl.institute_id IS NOT NULL`.
- `marts/wise_marts/facts_v3.py:324` — spf_v3 merge key `["region","session_id","student_id"]`.
- `grep -rn "archived|deletedStudents|suspendedStudents|hidden|published" marts/wise_marts/` →
  single unrelated hit at `gateway/service.py:109`.

Athena (read-only), by query id:
- `f6b8be26` — spf_v3 NA: 303,644 rows, fee_amount 0 non-null, credits_consumed 0 non-null,
  enrolled 300,416, attended 128,701, future 93,764, dates 2025-06-17..2040-07-03.
- `496b8f7b` — NA classparticipant relation×status: STUDENT REMOVED 17,210 / ACCEPTED 15,971 /
  REQUESTED 2; COTEACHER 27,907/18,893; ADMIN 6,090/178.
- `ea4f9eda` — thinktankjr institute_id `69b84f3c99b41087144ba02e`.
- `b4ee7578` — upcoming equivalence: spf 702 pairs / 26,765 rows; ACCEPTED-only 565 pairs / 21,246;
  accepted pairs 1,010.
- `9ef799ca` — invoiceType values by region incl. NULL 496,234 IN / 27,286 NA.
- `e80b202f` — NULL-invoiceType NA breakdown: 26,736 are transactionType=FEE_COLLECTION with classId.
- `272380a9` — transactionType vs metadata.invoiceType: dropped 469,390 IN / 26,736 NA; md_only 0 both.
- `faba7013` — user.parentIds vs parentId: IN 16,390/16,323/16,467 vs 4,730; NA 6,294/6,222/6,423
  vs 1,469.
- `3c9d2b6b` — NA parent edges: 6,423 all `$oid`, 5,087 distinct parents, 6,222 distinct students,
  vs 9,120 distinct PARENT participants.
- `62e1d4a2` — sessioncredit key-shapes both regions (no `remaining` in any).
- `9124a2c0` — sessioncredit: no seed rows, credit uniformly plain; classId absent 1,412 NA / 676 IN.
- `380c3341` — registrationform fields[] key-shapes: 4,906 base / 537 with options / 20 with
  maxAllowedAnswers.
- `eaca883a` — submission answers[] keys: exactly `{answer, questionId}` (26,027 NA).
- `1e19dde4` — options is a code→label map; type POLL; questionId slugs.
- `f5b5bc0d` — POLL answers store opaque codes `"2"`,`"A"`,`"1"`,`"B"`.
- `4d052a4f` (FAILED, informative) — error text exposed fields[] shape and semantic questionIds
  `user_name`/`user_phone_number`/`user_email`, types TEXT/PHONE/EMAIL.

## Gotcha

The `metadata.invoiceType` bug is the archetype for this whole codebase: **two fields with the same
value vocabulary, one top-level and authoritative, one inside the Mixed `metadata` subdoc and only
sometimes written.** Filtering on the metadata one looks right, returns plausible non-zero results,
excludes payouts correctly — and silently drops half of NA's fee collections. Nothing about the
query looks wrong; the only way to catch it is to compare the two fields' populations directly.
`transaction` has exactly this shape for `transactionType`/`metadata.invoiceType`, and the same
top-level-vs-metadata split is why `metadata.classId` is a plain string while `senderId` is
`$oid`-wrapped **in the same document**.

Second gotcha, the inverse of a previous one: I reported the parent edge missing because I probed
`parentId` and found 1.6% coverage. The real field is `parentIds`, plural, 4× the coverage. When a
field looks implausibly sparse, check for a pluralised or array-valued sibling before concluding
the data does not exist — Mongoose migrations leave both behind, and the old singular one keeps
being populated for a subset.
