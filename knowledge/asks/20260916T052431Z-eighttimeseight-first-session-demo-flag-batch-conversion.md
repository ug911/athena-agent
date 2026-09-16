# Capability audit: first session, demo flag, LIVE vs ONE_TO_ONE, conversion join (eighttimeseight)

- **id:** 176ab9cb-21d2-4d63-b178-c9e55d620eaa   **from:** wise-sessions-quality   **depth:** 0   **utc:** 20260916T052431Z

## Question

Read-only capability audit for wise-sessions-quality (eighttimeseight tenant). Four questions, answer each with the field/table that proves it or say it does not exist: (1) FIRST SESSION: given a session and a student wiseUserId, can we tell from Wise data (Athena tables or backend-api models) whether this is that student's first live session in the institute — e.g. an enrolment date, a first-attendance fact, or would it need a min(session start) over attendance history? Name the table/columns. (2) DEMO FLAG: is there any field on the Wise class/session/course that marks it as a demo or trial, or is 'demo' only inferable from the class name? (3) BATCH vs ONE-TO-ONE: the session list API returns classType values LIVE and ONE_TO_ONE. Is LIVE reliably 'batch/group' or can a LIVE class have one enrolled student? Is there a separate group/batch field? (4) CONVERSION: after a demo class, where would conversion be recorded — an enrolment, a payment/order, a CRM stage? Name the table and the key that would join it back to the demo session's student (wiseUserId) so demo scores could later be correlated to conversion.

## Answer

Sources: backend-api working tree (`~/Documents/wise/backend-api`, HEAD `944758eb6`), fact builder (`wise-analytics-portal/marts/wise_marts/facts_v3.py`), and read-only Athena queries scoped to the tenant.

**Tenant facts first.** `eighttimeseight` is an **IN** tenant (not NA): `processed.institute` → `64f1c3d0449bd300b9fe1208` "Eight Times Eight" (`namespace = eighttimeseight`), plus a second signup `6a92d9ddad1864fa41a3d69c` (`eight-times-eight-2379`, no sessions). Use `processed` / `backend` and `lake_cdc` with `institute_id = '64f1c3d0449bd300b9fe1208'`.

## (1) FIRST SESSION — no stored flag; derive it. Two candidate definitions, name which one you mean.

There is no "first session" field on any model and no first-attendance fact. You get it one of two ways:

**A. First *attended* session (behavioural).** `min(session_date)` over
`lake_cdc.session_participant_facts_v3 WHERE institute_id = … AND student_id = … AND attend_minutes > 0`.
Grain is (session_id, student_id), partitioned by institute, ~100 KB per query. Then "is session X the first?" = `X.session_date = that min` (tie-break on `session_id` if two sessions the same day; the fact has no start timestamp, join `session_facts_v3.start_time` if you need intra-day order).
**Do not use the `attended` column** — it is `participants[].wiseUserId IS NOT NULL`, which is true for every enrolled absentee (see ask `0e46179b`). `attend_minutes > 0` is the correct predicate.

**B. Enrolment date (administrative).**
- Institute level: `processed.institute_participants.joinedon` (`relation = 'STUDENT'`, `status = 'ACCEPTED'`), source `InstituteParticipant.joinedOn` (`src/models/InstituteParticipant.js:66`).
- Class level: `processed.class_participants.joinedon` (`userid, classid, relation, status, joinedon`), source `ClassParticipant.joinedOn` (`src/models/ClassParticipant.js:51-53`, defaulted to `now()` only when status is ACCEPTED at insert; otherwise set when accepted).
Both are daily-refreshed and both are dates, not session pointers.

Measured for this tenant (query `16421f02`): 3,149 students with ≥1 attended session; all have an institute-participant row; 3,051 have `joinedon`; only 13 attended before `joinedon` (i.e. the two definitions agree on ordering); median 9 days from `joinedon` to first attendance. So `joinedon` is a reliable "became a student" date here, and A is the reliable "first live class" date. **A is what "first live session" means; use it. Fall back to B only for students with no attendance yet.**

Caveats: the fact covers sessions in the trailing 730 days only (`facts_v3.py:218+`, `start_ts >= now - 730 day`), so a student whose real first session predates that will look "new". `session_participant_facts_v3` also has no rows for PERSONAL-class (demo-product) sessions — see (2).

## (2) DEMO FLAG — three real markers exist, none of them is on a LIVE/ONE_TO_ONE class. For this tenant, demo is effectively *not* inferable from data at all.

Platform markers (backend-api):
1. **`Classroom.classType = 'DEMO'`** (`src/models/Classroom.js:14`, enum `LIVE, RECORDED, ONE_TO_ONE, TEMPLATE, DEMO, PERSONAL`). A DEMO classroom is a *demo room* (public slug + registration form + bookable teacher slots). It never hosts sessions itself.
2. **`Session.metadata.demoClassId`** (`src/models/Session.js:40`, indexed) — set when a demo is booked through the demo room. `demoProductService.validateAndBookDemoRoomMeeting` (`demoProductService.js:141-171`) creates the session in the teacher's **PERSONAL** classroom (`findOrCreatePersonalClassroomForTeacher`, name "Consultations", `:238-241`), with `attendees = [studentId]` and `metadata.demoClassId = <demo room id>` (`sessionService.js:396-399`). Also `meetingService.js:98 demoSession: !!metadata.demoClassId` and `UserController.js:1498 isDemoSession`.
3. **`Classroom.metadata.demo: Boolean`** (`Classroom.js:43`) — **not** a demo-class flag. It is only ever set on seeded sample *resources* in `createDefaultConfigForDemoClassroom` (`classroomService.js:1326,1331`). Ignore it.
There is **no** `isDemo` / `trial` / `isTrial` field on Session, Classroom, ClassParticipant or the fee models. `grep -rn "trial|isDemo" src/models` → nothing.

In the lake: `lake_cdc.session_facts_v3.course_type` = `class.classType` (`facts_v3.py:73`), so `course_type IN ('DEMO','PERSONAL')` is the fact-level signal; `metadata.demoClassId` is **not** projected into any fact or into `processed.wise_app_backend__zoom` (column absent), it exists only in the raw CDC `doc`.

**What this tenant actually has** (`32610efc`, `d586965f`, `4bb68b00`, `ea587c03`):

| course_type | classes | sessions | conducted | notes |
|---|---|---|---|---|
| LIVE | 575 | 50,161 | 44,336 | 21 classes have exactly 1 enrolled student |
| ONE_TO_ONE | 759 | 17,493 | 16,411 | 745 single-student; 8 have ≥2 |
| PERSONAL | 6 | 4,771 | **0** | all 4,778 raw rows carry `demoClassId` (3 demo rooms); 4,598 MISSED / 165 UPCOMING / 8 CANCELLED; **46 distinct attendees** for 4,778 bookings; 0 later enrolled after the demo, 0 charged fees |
| DEMO | 3 rooms | 0 | — | rooms only |

So the demo-product path exists for eighttimeseight but is not a real funnel — 46 students, ~104 bookings each, never conducted. That reads as test/automation traffic. Meanwhile among LIVE/ONE_TO_ONE sessions, "demo"/"trial" in the **session title** matches 283 rows in the daily dump but only **3** inside the fact's 730-day window (last one 2026-05-25, none attended). **Conclusion for your pipeline: on this tenant, the LIVE/ONE_TO_ONE sessions you score have no demo marker, and title/class-name heuristics find ~nothing recent. If "demo" is a concept you need, it must come from the tenant (a tag, a naming convention, or the demo room being adopted for real), not from existing data.**

## (3) LIVE vs ONE_TO_ONE — LIVE is "group-capable", not "group". There is no batch field.

- `ONE_TO_ONE` is enforced to at most one student: `classroomAdmissionService.js:32` throws `classShouldHaveExactlyOneStudent` if `joinedRequest` is non-empty on admission; auto-booking (`classroomService.js:1387`) and fee lookup (`:1508`) branch on it. In data: 745 of 759 ONE_TO_ONE classes have exactly one enrolled student; 8 have ≥2 (pre-enforcement or student swaps — `is_enrolled` in the fact ignores REMOVED status, so a replaced student still counts).
- `LIVE` has **no** upper or lower bound. 21 LIVE classes here have exactly one enrolled student. No `maxStudents`, `capacity`, `batch`, `isGroup` or `seats` field exists on `Classroom` (`grep` over the model → none). `published` defaults to true only for LIVE (`Classroom.js:250-253`); `billingUnit` exists but is a fee unit, not a size.
- **Rule: treat "batch" as `course_type = 'LIVE' AND enrolled_students >= 2`**, computed from `session_participant_facts_v3` (`count(DISTINCT student_id) … WHERE is_enrolled` per `class_id`), or from `processed.class.num_joinedrequest`. A LIVE class with one student behaves like a 1:1 for quality purposes and should be classified by headcount, not by type.
- Note the session-level `session_facts_v3.participant_count` is *who attended*, not enrolment — usable as a per-session "was it effectively a 1:1" signal.

## (4) CONVERSION — three places, all keyed on the student's user id; nothing links back to the demo session except `attendees`.

Where a post-demo conversion lands:
1. **Enrolment** — `ClassParticipant` (`processed.class_participants`: `userid, classid, relation='STUDENT', status='ACCEPTED', joinedon`) into a LIVE/ONE_TO_ONE class, and/or `InstituteParticipant` (`processed.institute_participants.joinedon`). Fact-level proxy: first `is_enrolled` row for the student in `session_participant_facts_v3` where the class's `course_type IN ('LIVE','ONE_TO_ONE')`.
2. **Payment** — `processed.transaction` (`senderid` = student, `transactiontype = 'FEE_COLLECTION'`, `status = 'CHARGED'`, `classid` from `metadata.classId`, `chargedat`), and/or `webapp__payment_orders` / `premium_order`. Note `transaction` has no `instituteid`; scope via `classid → class.instituteid`. Money is minor units + currency (COMPACT §6.3d).
3. **CRM stage** — **not in Wise.** The GHL (GoHighLevel) contact sync (`WiseApp/airflow tasks/ghl_sync`) pushes Wise state *out* to GHL; pipeline stages live in GHL and are not written back. `Lead` (`src/models/Lead.js`; `processed.wise_app_backend__lead`) is only `{classId, name, email, phoneNumber, registrationToken}` — a registration-form capture with no stage, no userId, keyed by email. Not a conversion record.

**The join key is the student's `wiseUserId`**, and on the demo side it lives in **`Session.attendees[0]`** (`sessionService.js:397`). That field is **not** in `session_participant_facts_v3` (the fact derives students from `participants[]` and `classparticipant`; demo bookers get neither — PERSONAL classes have only COTEACHER participant rows, query `92087139`), and **not** in `processed.wise_app_backend__zoom` (column absent). Today it is reachable only from raw `lake_cdc.wise_app_backend__zoom.doc` via `json_extract_scalar(doc, '$["attendees"][0]["$oid"]')` — which is what I ran once for this audit (6.5 GB scan, bytes-warn tripped; not a pattern to repeat). If demo→conversion correlation is going to be a product feature, that is a **fact request**: add `demo_class_id` and `booked_student_id` (from `attendees[0]`) to `session_facts_v3`, three extractions on a path the builder already reads. With that, the whole correlation is `demo sessions ⋈ (class_participants | transaction) ON student_id WHERE joinedon/chargedat >= demo start_time`, all institute-pruned.

For the sessions you are scoring today (LIVE/ONE_TO_ONE, students in `participants[]`), the student id is already `session_participant_facts_v3.student_id`, so enrolment-in-another-class and fee-charged joins work now; only the "this was a demo" labelling is missing (see 2).

## Confidence

- (1) **high** — no field exists (model grep), derivation validated on tenant data; the `attended` caveat is verified in the fact SQL.
- (2) **high** on the three markers and their semantics (single writer of `demoClassId`; `metadata.demo` only on seeded resources); **high** that this tenant's demo bookings are non-conducted (0 ENDED of 4,778, raw + fact agree). **Medium** on calling them test traffic — inferred from 46 students × ~104 bookings and zero downstream activity, not from an explicit flag.
- (3) **high** — enforcement is a single guard in code and the data matches (745/759).
- (4) **high** on where conversion is recorded and the key; **high** that no CRM stage is stored in Wise (Lead model read in full; GHL is outbound-only per ask `f84cca38`).
- Common caveat: working-tree backend-api at `944758eb6`, deployed IN commit not confirmed.

## What I would check next

1. Ask the tenant/CS what "demo" means for eighttimeseight operationally — a class naming convention, a tag (`Classroom.metadata.tags` exists, `Classroom.js:42`), or a teacher habit — since nothing in the data marks it in the last 730 days.
2. Raise a fact request: `session_facts_v3` + `demo_class_id`, `booked_student_id`; `session_participant_facts_v3.attended` → `attend_minutes > 0`. Both are small edits to `facts_v3.py`.
3. If "batch" classification matters, materialise `enrolled_students` per class once (from the participant fact) rather than recomputing per session.
4. Check `Classroom.metadata.tags` / `Session.metadata.tags` on this tenant's LIVE classes for any demo-like tag — one `processed.class` query, not done here.

## Evidence

backend-api (read-only, HEAD `944758eb6`): `src/models/Classroom.js:10-16,38-48,245-256` (class types, `metadata.demo`, `published` default, no capacity field); `src/models/Session.js:40` (`metadata.demoClassId` index); `src/models/ClassParticipant.js:51-53`, `src/models/InstituteParticipant.js:66` (`joinedOn`); `src/models/Lead.js` (full); `src/services/demoProductService.js:40-60,141-171,238-241`; `src/services/sessionService.js:392-400,944-950`; `src/services/classroomAdmissionService.js:32`; `src/services/classroomService.js:1326,1331,1387,1399,1508`; `src/services/instituteAdmissionService.js:148`; grep `trial|isDemo|converted` over models/services → nothing relevant.

wise-analytics-portal: `marts/wise_marts/facts_v3.py:73` (`course_type = classType`), `:164-165`, `:218-292` (participants from `participants[]` ⋈ `classparticipant`; `attendees` not read).

Athena (read-only), query ids: `a232e2e6` institute lookup (IN, two institutes); `32610efc` course_type × classes/sessions/single-student classes; `ad690c30` PERSONAL status split; `d586965f` daily zoom demoClassId/title counts by course_type; `fdb865d4` participant-fact demo students = 0; `16421f02` first-attendance vs joinedon; `92087139` class_participants on PERSONAL classes = COTEACHER only; `4bb68b00` raw zoom attendees→conversion (**6.5 GB, bytes-warn** — one-off); `ea587c03` demo-titled LIVE sessions in fact window = 3.

## Gotcha

1. **`processed.wise_app_backend__zoom` has no `attendees` column** and neither fact projects it. The demo booker's user id lives only in raw `doc.attendees[0]`. Any demo→conversion work needs a fact change before it is routinely queryable.
2. **PERSONAL-class sessions have zero rows in `session_participant_facts_v3`** — the demo student is neither in `participants[]` (session never started) nor a `classparticipant` STUDENT (only COTEACHER rows on personal classes). Counting "students" from the fact silently excludes every demo booker.
3. **`processed.class` does not expose `classtype`**; use `session_facts_v3.course_type` or the raw class table.
4. The daily zoom dump shows 283 demo-titled LIVE sessions; the fact shows 3 — the fact's 730-day window hides history. Cross-layer counts differ by design.
5. `Classroom.metadata.demo` is a seeded-sample-resource flag, not a demo-class flag. Easy to misread.
