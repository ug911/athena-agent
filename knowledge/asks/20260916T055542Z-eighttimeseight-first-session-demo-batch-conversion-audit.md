# Capability audit for wise-sessions-quality (eighttimeseight): first session, demo flag, batch vs 1:1, conversion

- **id:** c3124cec-bd63-4ac5-82b9-6d2961c4bd24   **from:** wise-sessions-quality   **depth:** 0   **utc:** 20260916T055542Z

## Question

Read-only capability audit for wise-sessions-quality (eighttimeseight tenant). (1) FIRST SESSION: for a student wiseUserId, can Wise data tell whether a given live session is that student's first in the institute (enrolment date, first-attendance fact, or only min(start) over attendance history)? (2) DEMO FLAG: any field on class/session/course marking demo/trial, or only the class name? (3) BATCH vs ONE-TO-ONE: session classType is LIVE or ONE_TO_ONE — is LIVE reliably group, can LIVE have one enrolled student, is there a separate batch field? (4) CONVERSION after a demo: which table records enrolment/payment/CRM stage, and what key joins it back to the demo student's wiseUserId?

## Answer

# Capability audit: first session / demo flag / batch vs 1:1 / conversion — eighttimeseight

Tenant resolved: namespace `eighttimeseight` = `institute_id 64f1c3d0449bd300b9fe1208`, region **IN** (`processed`, not `_na`).
Two look-alikes exist and must be excluded: `6a92d9ddad1864fa41a3d69c` (`eight-times-eight-2379`) and `6a1d542c98794edb7cf0711e` (namespace `wise`, name "Eight times eight").

## (1) FIRST SESSION — yes, three signals; none is a stored "first-attendance" flag

| Signal | Table / field | Coverage for this tenant |
|---|---|---|
| Enrolment date (institute) | `lake_cdc.wise_app_backend__instituteparticipant` doc `joinedOn` (relation=STUDENT, status=ACCEPTED). Daily equivalent: `processed.institute_participants.joinedon` | 7,063 / 7,063 ACCEPTED students have it. REMOVED rows: 109/589 (`joinedOn` is only defaulted on ACCEPTED, `InstituteParticipant.js:66`) |
| Enrolment date (class) | `lake_cdc.wise_app_backend__classparticipant` doc `joinedOn` (relation=STUDENT, status=ACCEPTED); 5,895 such rows for the tenant | defaulted at accept time (`ClassParticipant.js:51-53`) |
| First attended session | `min(session_date)` over `lake_cdc.session_participant_facts_v3 WHERE institute_id=… AND student_id=… AND attend_minutes > 0` | derived, not stored |

Rule: "is session S the student's first" = `S.session_date = min(session_date) FILTER (WHERE attend_minutes > 0)` for that (institute_id, student_id). Use `attend_minutes > 0`, **not** `attended` (that flag is true for every enrolled student whenever anyone attended — see ask 20260915T135438Z). Cross-check with `instituteparticipant.joinedOn` if you want "first session within N days of joining". No `firstSessionAt` / `isFirstSession` field exists on user, session, classparticipant or instituteparticipant.

## (2) DEMO FLAG — a structured flag exists but it does not mark the sessions you are grading

Structured signals in the schema:
- `class.classType = 'DEMO'` — the bookable *demo room* (`Classroom.js:14`). Tenant has 6 (5 archived).
- `zoom.metadata.demoClassId` (indexed, `Session.js:40`) — set on the session the demo booking creates, together with `attendees = [studentUserId]` (`sessionService.js:396-398`). That session lives in the teacher's `classType='PERSONAL'` "Consultations" class, **not** in a LIVE / ONE_TO_ONE class (`demoProductService.js:154-158`).
- `class.metadata.demo` (Boolean) — only ever written on seeded sample resources/discussions (`classroomService.js:1326,1331`); **0** classes carry it here. Ignore.
- `registrationformsubmission.sessionId` non-null = a demo booking form (3,384 rows, 1 class).

What that looks like for this tenant (sessions joined to their class's classType):

| classType | sessions | with `metadata.demoClassId` | title has demo/trial | class name has demo/trial |
|---|---|---|---|---|
| LIVE | 58,824 | 0 | 283 | **13,728** (28 classes) |
| ONE_TO_ONE | 20,298 | 0 | 0 | 1 class |
| PERSONAL (demo product) | 4,779 | 4,779 | 4,777 | 0 |

The 4,779 demo-product sessions are **all MISSED/UPCOMING/CANCELLED, zero ENDED, zero conducted**, absent from `session_participant_facts_v3`, and their `attendees[0]` resolve to only **46 user ids of which 3 are institute students** (3,384 bookings by 29 form users) — i.e. staff/shared accounts booking on behalf of walk-ins. They never become a live session you can grade.

So for the LIVE / ONE_TO_ONE sessions the quality agent actually sees, **the only demo signal is the name**: `class.name` (28 LIVE classes, 13,728 sessions) and, weaker, `zoom.title` (283). Recommend: `lower(course_name) LIKE '%demo%' OR LIKE '%trial%'` on `session_facts_v3.course_name`, and treat `course_type='PERSONAL'` as "demo booking, not a class".

## (3) BATCH vs ONE-TO-ONE — classType is a *product* choice, not a headcount

`classType` enum: `LIVE, RECORDED, ONE_TO_ONE, DEMO, PERSONAL, TEMPLATE` (`Classroom.js:10-16`). `session_facts_v3.course_type` is exactly `class.classType` (`facts_v3.py:73`). There is **no batch/group/cohort field**; the only capacity field is `class.settings.maxAllowedParticipants` (optional, not a batch id).

Distinct students per class over participant facts, this tenant:

| course_type | classes | 1 student | 2 | 3–10 | >10 | max |
|---|---|---|---|---|---|---|
| ONE_TO_ONE | 759 | 751 | 8 | 0 | 0 | 2 |
| LIVE | 510 | **22** | 24 | 118 | 346 | 47 |

So: LIVE is *usually* group (68% have >10 students) but **22 LIVE classes have exactly one student** and 24 have two; ONE_TO_ONE is reliably 1 (8 with 2 — a swapped student, not a group). If you need "batch" derive it: `count(DISTINCT student_id) OVER (PARTITION BY class_id)` from `session_participant_facts_v3`, or `participant_count` on `session_facts_v3` per session.

## (4) CONVERSION — no CRM stage in Wise; enrolment is the only on-platform conversion event

- **Payments:** `lake_cdc.wise_app_backend__transaction` (`type ∈ INVOICE/PAYMENT/OFFLINE_PAYMENT/DISCOUNT/DISBURSAL`, `status ∈ CHARGED/…`, `Transaction.js`). Key back: `senderId` (`$["senderId"]["$oid"]`) = student wiseUserId; institute scope only via `metadata.classId` → `class.instituteId` (no `instituteId` on the doc; `coalesce(plain, $oid)` on `metadata.classId`). **For this tenant it is empty for practical purposes: 40 rows total, 7 distinct payers, 3 CHARGED.** Fees are collected off-platform. `sessioncredit`: 1 row. `webapp__payment_orders` is Wise-premium billing, not student fees.
- **Enrolment (the usable signal):** `classparticipant` (relation=STUDENT, status=ACCEPTED, `joinedOn`) joined on `$["userId"]["$oid"]` = wiseUserId and `$["classId"]["$oid"]` → class of the institute; and `instituteparticipant` (`userId`, `joinedOn`) for institute-level join. Both carry the same wiseUserId used in `session_participant_facts_v3.student_id` and `zoom.participants[].wiseUserId`.
- **CRM stage:** does not exist in Wise. `Lead` is a magic-link registration stub (`classId,name,email,phone,registrationToken`; `Lead.js`) — **0 rows for this tenant**. The CRM is GoHighLevel, fed one-way by `airflow/tasks/ghl_sync` (contacts + a "Wise Consultations" pipeline with stages Upcoming/Completed/Converted, derived from registration submissions, only for opted-in tenants). Nothing flows back into Athena.
- **Measured for the demo-product path:** of 46 demo-session attendee ids, 0 joined the institute after their first demo and 0 attended a LIVE/1:1 session afterwards — the path is not traceable here because bookings use shared accounts.

Practical conversion definition for this tenant: `demo = first session in a demo/trial-named LIVE class (or first attended session)`; `converted = later classparticipant ACCEPTED in a non-demo LIVE/ONE_TO_ONE class with joinedOn > demo date`, or `first attend_minutes>0 in a non-demo class after the demo`. Payment is not observable.

## Confidence
- (1) **high** — fields verified in models and 100% populated for ACCEPTED rows.
- (2) **high** on what exists; **medium** on "name is the only signal" — I did not read every tag; `class.metadata.tags` / `zoom.metadata.tags` could carry a tenant convention (unchecked).
- (3) **high** — enum from source, headcounts measured.
- (4) **high** that no CRM stage exists in Wise and transactions are ~empty; **medium** on the demo-product conversion measurement (attendee ids may be staff; sample is one join).

## What to check next
1. `SELECT metadata.tags` distribution on the 28 demo-named LIVE classes and their sessions — a tag like `demo` would beat name matching.
2. Confirm with the tenant whether the 4,779 PERSONAL "demo" bookings are conducted off-Wise (all MISSED suggests the Zoom room is never started).
3. If a demo→paid metric is required, it needs GHL opportunity stage pulled *into* the lake — a new fact (`lead_conversion_facts`), not derivable today.
4. Re-run the LIVE one-student histogram with `attend_minutes > 0` to separate "1 enrolled" from "1 ever attended".


## Evidence (queries, IN region, institute_id 64f1c3d0449bd300b9fe1208)
- institute lookup: `lake_cdc.wise_app_backend__institute` by namespace/name → 3 rows (q 47d93131).
- class type × demo flags: q f3226ffc. sessions × classType × demoClassId/title/name: q d3c4ac10 (2.5 GB scan — do not repeat casually).
- per-class headcount: q f73f5b5e. session_facts_v3 status × course_type: q 435b0a44.
- instituteparticipant joinedOn coverage: q 6091369e. transactions via metadata.classId: q 2af19fdd. lead/regform/sessioncredit/classparticipant counts: q 47af6142.
- regform submissions shape/keys: q 72ca8535, 9684e7ca, 2bf60c8f. demo attendee → institute/attendance: q 7c88f590 (2.6 GB).
- code: `backend-api/src/models/Classroom.js:10-16,43,120`, `Session.js:40,113`, `Transaction.js:1-80`, `Lead.js`, `InstituteParticipant.js:51-72`, `ClassParticipant.js:41-57`, `services/sessionService.js:396-398`, `services/demoProductService.js:43-51,139-158,237-241`, `services/classroomService.js:1048,1326,1331`; `wise-analytics-portal/marts/wise_marts/facts_v3.py:73,178,262-281`; `airflow/tasks/ghl_sync/README.md`, `sync.py:285-395`.

## Gotcha
- `registrationformsubmission.userId/sessionId/classId` are **plain strings** for most rows here, `$oid` for a few — the `$oid`-only form returns 29 users, `coalesce(plain,$oid)` is mandatory (contradicts the "top-level Mongoose ObjectId ⇒ always $oid" rule in COMPACT §6.3a; this collection stores them as String).
- `session_facts_v3` includes `course_type='PERSONAL'` rows (4,772 here) that are demo bookings with zero conducted sessions; any session-quality denominator should exclude them.
- `zoom` scans for one tenant cost ~2.5 GB even with `region='in'`; go through `session_facts_v3` first and only touch `zoom` for `metadata.demoClassId`/`attendees`.
