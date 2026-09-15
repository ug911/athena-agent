# Do rsvpStatus / NOT_INVITED persist on ENDED sessions, what writes `offline:true` participant rows, and is there a fact for per-session rsvpStatus?

- **id:** 0e46179b-455a-408f-82cf-b73c15479405   **from:** group-sessions-admin   **depth:** 0   **utc:** 20260915T135438Z

## Question

Context: group-sessions-admin, tenant thinktankjr (NA host, institute 69b84f3c99b41087144ba02e). Session 6a3e9e395835b929f323aed0 (class 6a159be63e6d2516d2fcb799, 2026-09-15 00:30Z, ENDED).
Three questions about the Wise platform's session `participants` array, answered from platform/lake knowledge (do not query raw lake_cdc):
1. On an ENDED session, Wise's single-session endpoint returns a participant row for student 6a15a04feff9b8dd3eba82d8 with duration 0 AND rsvpStatus "NOT_INVITED" (rsvpDetails.markedAt 2026-09-11T15:40:40Z). Does Wise keep per-session rsvpStatus on the participants row permanently after the session ends, i.e. is reading rsvpStatus off an ENDED session's participants reliable? Is NOT_INVITED the per-session "remove learner from this session" action (as opposed to removing the learner from the classroom), and does classroom-level removal produce any marker on past sessions?
2. Same session: student 6a15a199eff9b8dd3ebb3182 ("Kiaansh") has a participants row with offline:true, duration 3695 = exactly start_time..end_time, and a separate row named "Kiaansh K." with no wiseUserId, a user_email, duration 3395, firstEntryTime 5 min after start. What produces an `offline: true` participant row (teacher manual attendance? auto-mark?) and is the "Kiaansh K." row the actual Zoom join that Wise failed to credit because the display name differs?
3. Is there a fact table (not raw CDC) that lists per-session rsvpStatus / NOT_INVITED rows, so I can count, for institute 69b84f3c99b41087144ba02e, ENDED sessions since 2026-08-01 that have a NOT_INVITED participant? If none, say so.

## Answer

Answered from backend-api source (`~/Documents/wise/backend-api`, HEAD `944758eb6`, 2026-09-10) and the v3 fact builder (`wise-analytics-portal/marts/wise_marts/facts_v3.py`). No lake query was run.

## Q1 — rsvpStatus on ENDED sessions

**Yes, `rsvpStatus` survives the session ending and is reliable to read off an ENDED session. `rsvpDetails` is not — it is purged ~30 days after the session.**

- **Written only pre-session.** `markSessionRsvpStatus` (`src/services/sessionService.js:1554-1570`) matches the session with `meetingStatus: {$in: meetingStatuses}` where `meetingStatuses` defaults to `[UPCOMING]`, or `[UPCOMING, IN_PROGRESS]` when called from the institute endpoint (`InstituteController.js:1820`, `allowInProgressSession: true`). A write against an ENDED session silently matches zero documents. So a NOT_INVITED you see on an ENDED session was set *before* the session ran — consistent with your `markedAt 2026-09-11` on a 2026-09-15 session.
- **Explicitly carried forward at attendance capture.** `captureAttendance` rebuilds the whole `participants[]` from Zoom, then `carryForwardParticipantFields` (`meetingAttendanceService.js:78-90`) copies `credits`, `rsvpStatus`, `rsvpDetails` from the previous array onto the new row **keyed by `wiseUserId`**. The absent-student row for 6a15a04f… comes from `absentClassStudents` (`meetingAttendanceService.js:243-244`: every `classroom.joinedRequest` member without a Zoom match gets `duration: 0, inMeetingDuration: 0`) and then inherits the NOT_INVITED. That is exactly the row you observed.
- **`rsvpDetails` is TTL-cleaned; `rsvpStatus` is not.** `clearExpiredRsvpDetails` (`sessionService.js:1654-1661`, scheduled from `periodicChecksWorker.js:76`) runs `$unset participants.$[].rsvpDetails` on ENDED sessions whose `start_time` is 30–32 days old. `rsvpStatus` has no expiry anywhere in the codebase. **Rule: on ENDED sessions, trust `rsvpStatus`; treat `rsvpDetails.markedAt/markedBy` as present only for ~30 days.**

**Three ways an rsvp row can be lost at capture (edge cases, not the normal path):**
1. Student removed from the classroom's `joinedRequest` *before* attendance capture → not in `absentClassStudents`, so no new row to carry onto; the NOT_INVITED row disappears.
2. Zoom returned **zero** participants → `absentClassStudents` is `[]` by construction (`!presentParticipants.length ? []`), `participants` becomes `[]`, all rsvp rows gone.
3. Class archived at capture time → `participants: []` (`meetingAttendanceService.js:37`).
4. Classroom with >150 joined students (`MAX_ALL_PARTICIPANT_THRESHOLD`) → duration-0 rows are dropped unless the user already had a row (which a NOT_INVITED student does, so they survive).

**Is NOT_INVITED the per-session "remove learner from this session" action? Yes.** The only writers are:
- `POST /institutes/:instituteId/classes/:classId/rsvpStatuses` and the student-side `POST /classes/:classId/rsvpStatuses`, body `updates[]: {studentId, sessionId, status ∈ ATTENDING|NOT_ATTENDING|NOT_INVITED}` (`institute.params.js:878-890`, `student.params.js:283`). Per (session, student). Only `classType === LIVE` classrooms; student must be in `joinedRequest`; ≤500 updates per call.
- `applyStudentEnrollmentRsvp` (`sessionService.js:1521`) at **enrollment** time, when the enrol payload carries `rsvp: {defaultAttending, exceptions[]}` — it fans NOT_INVITED across every UPCOMING/IN_PROGRESS session of the class (not the exceptions). So a bulk of NOT_INVITED rows sharing one `markedAt` usually means "enrolled with defaultAttending=false", not a teacher hand-picking sessions.
- `buildRsvpParticipants` at session **creation** (`sessionService.js:362-369`) seeds non-billable rows when a session is created with `rsvpParticipants`.

Semantics: NOT_INVITED and NOT_ATTENDING are both **non-billable** (`Session.isBillableRsvpStatus`, `Session.js:219`) and hide the session from the student's PAST list (`getRsvpVisibleSessionQuery`, `sessionService.js:475-479`). NOT_INVITED additionally makes the session **bookable** by the student (`getBookableSessionsForStudent`, `sessionService.js:1637-1643`) and does *not* send the "not attending" notification. So NOT_INVITED = "excluded from this occurrence, may opt in"; NOT_ATTENDING = "declined this occurrence".

**Does classroom-level removal mark past sessions? No.** `removeStudentFromClass` → `unassignStudentToClassroom` → `leaveOrRemoveFromClassroom` (`classroomAdmissionService.js:97+`) touches `ClassParticipant`, `InstituteParticipant`, and pushes `{userId, type: REMOVED|LEFT}` onto `Classroom.deletedStudents` (capped at last 1,000). It never writes to the `zoom` collection. Past sessions keep whatever `participants[]` they had. The only classroom-level marker is `class.deletedStudents[]`; the only per-session marker is `rsvpStatus`.

## Q2 — `offline: true` rows and the "Kiaansh K." duplicate

**`offline: true` on a participant row = teacher manual attendance, applied at capture time. Your reading of the duplicate is right: "Kiaansh K." is the real Zoom join that failed name-matching.**

- On every online session start, `initializeManualAttendance` (`meetingAttendanceService.js:278-288`, enqueued from `meetingService.js:220`) creates a `ManualAttendance` doc with one row per ACCEPTED student. The teacher's UI calls `POST /teacher/classes/:classId/sessions/:sessionId/manualAttendance` with `{wiseUserId, action: mark_present|mark_absent}` (`TeacherController.js:526-560`), which sets `present` and **`manual: true`** on that row. Only allowed before `attendanceRecorded`.
- At capture, `updateParticipantsWithManualAttendance` (`meetingAttendanceService.js:127-152`) takes rows with `manual: true` and, for `present`, force-assigns `duration = floor(session.duration/1000)`, `inMeetingDuration` same, `firstEntryTime = session.start_time`, `lastExitTime = session.end_time`, `relative/absolutePercentAttendance = 100`, `offline: true`. For absent: all zeros, `offline: true`. It matches the target row by `p.wiseUserId == manualParticipant.userId` — so it lands on the **absent-student row** (wiseUserId present, duration 0), not on the unmatched Zoom row. `duration 3695 = start..end` exactly is the fingerprint of this path. **No auto-mark exists**: `manual: true` is set only by that teacher endpoint.
- The other `offline: true` writers (`TeacherController.js:2002-2014` `markAttendance` for `type: OFFLINE` sessions, and `sessionService.js:385/932`) are for offline-type sessions and don't apply to this ENDED online session.
- **Why "Kiaansh K." is a separate row with no `wiseUserId`.** Zoom participants are matched by `getParticipantMatchKey` (`meetingAttendanceService.js:331-339`): first `customer_key` of the form `<classNumber|NA>…_<24-hex userId>` (set when the join goes through Wise's join flow), else `zoomCompatibleName(display name)` looked up against `zoomCompatibleName(user.name)` of the teacher + `joinedRequest`. `zoomCompatibleName` (`meetingService.js:44-46`) trims to 59 chars, `+`→space, strips chars outside `[A-Za-z0-9.-_ ()]`; it does **no** prefix/first-name matching. "Kiaansh K." ≠ "Kiaansh", and no customer_key → no match → the row is stored with `name`, `user_email`, `duration 3395`, real `firstEntryTime`, and **no `wiseUserId`** (`meetingAttendanceService.js:235-239`). The teacher then saw Kiaansh as absent and marked them present manually — producing the paired rows you see. The 5-minute-late `firstEntryTime` and 3395 s on the unmatched row are the true attendance; the 3695 s on the `offline:true` row is synthetic.
- Note `ManualAttendance` has a **2-day TTL** (`ManualAttendance.js:6`, `expireAfterSeconds: 172800`), so the source doc is gone from Mongo (and, since CDC mirrors deletes, from `lake_cdc.wise_app_backend__manualattendance`) within 48 h. The only durable trace is the `offline: true` flag on the session row.

## Q3 — fact table for per-session rsvpStatus

**No. No curated table carries `rsvpStatus`, and none carries `offline`.** Specifically:

- `lake_cdc.session_participant_facts_v3` (`facts_v3.py:239-292`) unnests `participants[]` but projects only `wiseUserId, name, user_email, inMeetingDuration, isTeacher`. `rsvpStatus`, `rsvpDetails`, `offline`, `duration` are not read. **Worse for your use: `attended = a.student_id IS NOT NULL` with no duration predicate** (`facts_v3.py:274`) — so a NOT_INVITED row with duration 0, and every ordinary absent-student row (duration 0), yields `attended = true, attend_minutes = 0`. Do not use `attended` from that fact to mean "was present"; use `attend_minutes > 0`. This is a defect worth raising with the facts owner.
- `lake_cdc.session_facts_v3` is session grain, no participant detail.
- `processed_na.zoom_attendance` (daily) has `student_duration / student_attendance / student_isteacher` only — no rsvp, no offline flag.
- `processed_na.wise_app_backend__zoom.participants` is the raw JSON varchar (daily dump), not a fact.

So the count you want ("ENDED sessions since 2026-08-01 for institute 69b84f3c… with ≥1 NOT_INVITED participant") is **not answerable from a fact today**. It is a "fact needed" per COMPACT §4: add `rsvp_status` (varchar), `is_offline_marked` (boolean) and raw `duration` to `session_participant_facts_v3`'s `attend` CTE — three more `json_extract_scalar`s on a path the builder already unnests, no new source, no new grain. Until then the only source is the raw `participants[]` JSON, which you have said you will not query; if someone does a bounded investigation, filter `institute_id`-scoped session ids first and unnest only those (the fact gives the session-id list cheaply), never a fleet-wide unnest.

## Confidence

- Q1 **high**: all writers of `rsvpStatus` enumerated by grep, the `meetingStatus` guard and the carry-forward are both explicit, and the 30-day `rsvpDetails` purge is a scheduled job. The four loss paths are read directly from `captureAttendance`. Not verified against production data for this session.
- Q2 **high** on mechanism (single writer of `manual:true`; synthetic-duration constants match your row exactly; name matcher is exact-match after sanitising). **Medium** that "Kiaansh K." is the *same person* — inferred from name + timing; the row carries a `user_email` the backend never links to the user, so I cannot prove identity from platform state.
- Q3 **high**: read the fact SQL end to end; both the missing columns and the `attended` defect are in the source.
- Caveat for all three: working-tree source at `944758eb6`; the NA deployed commit was not confirmed (same limit as ask `8dc4d5eb`).

## What I would check next

1. For this session, confirm the pairing via the daily dump (`processed_na.wise_app_backend__zoom`, `_id = '6a3e9e395835b929f323aed0'`): `participants[].user_email` on the "Kiaansh K." row vs `processed_na.user.email` for 6a15a199… — one row, one session, cheap, and it settles the identity question.
2. Raise with the facts owner: (a) `attended` should be `attend_minutes > 0` (or `duration > 0`); (b) add `rsvp_status`, `is_offline_marked`, `duration_seconds` to `session_participant_facts_v3`. That single change makes your Q3 count a one-liner: `count_if(rsvp_status = 'NOT_INVITED') > 0` grouped by session, `WHERE institute_id = … AND session_date >= date '2026-08-01'`.
3. If you need the count before the fact lands, ask for a bounded backfill through the gate (`bin/request-do.sh`), scoped to the session ids from `session_facts_v3` for the institute — not a raw scan.
4. Confirm the NA deployed commit of backend-api if any of this gates a product decision.

## Evidence

backend-api (`~/Documents/wise/backend-api`, HEAD `944758eb6`, read-only):
- `src/models/Session.js:24-27,44-64,219-221` — RSVP enum, `participantsSchema` (`offline`, `rsvpStatus`, `rsvpDetails{markedBy,markedAt}`), `isBillableRsvpStatus`, `getParticipantByUserId`.
- `src/services/sessionService.js:362-369` (`buildRsvpParticipants`), `:475-479` (`getRsvpVisibleSessionQuery`), `:1500-1519` (`updateSessionRsvpStatuses`, LIVE-only, joinedRequest check, meetingStatus filter), `:1521-1535` (`applyStudentEnrollmentRsvp`), `:1537-1551` (`dispatchRsvpUpdates`), `:1554-1600` (`markSessionRsvpStatus` — `meetingStatus $in meetingStatuses` guard, $set/$push, billing trigger, NOT_ATTENDING notification), `:1637-1651` (`getBookableSessionsForStudent`), `:1654-1661` (`clearExpiredRsvpDetails`, 30–32 d, ENDED, $unset rsvpDetails only).
- `src/workers/periodicChecksWorker.js:76` — `clearExpiredRsvpDetails` scheduled.
- `src/params/institute.params.js:878-890`, `src/params/student.params.js:283`, `src/routes/instituteRouter.js:256`, `src/routes/studentRouter.js:166`, `src/controllers/InstituteController.js:1814-1826` — the rsvp endpoints.
- `src/services/meetingAttendanceService.js:18` (threshold 150), `:20-76` (`captureAttendance`: archived → `participants: []`; carry-forward; threshold filter), `:78-90` (`carryForwardParticipantFields` keyed by wiseUserId), `:127-152` (`updateParticipantsWithManualAttendance`: `manual` filter, present/absent constants incl. `offline: true`, match by wiseUserId), `:165-250` (`saveRawAttendanceAndGetParticipantsData`: name/customer_key matching, unmatched rows keep `user_email` and no wiseUserId, `absentClassStudents` only when presentParticipants non-empty), `:278-288` (`initializeManualAttendance`), `:331-339` (`getParticipantMatchKey`).
- `src/services/meetingService.js:44-46` (`zoomCompatibleName`), `:220` (enqueue initializeManualAttendance).
- `src/models/ManualAttendance.js` — `manual` flag, TTL 172800 s.
- `src/controllers/TeacherController.js:526-560` (`markManualAttendance` sets `present` + `manual:true`), `:748-765` (`removeStudentFromClass`), `:2002-2014` (OFFLINE-type `markAttendance`).
- `src/services/instituteAdmissionService.js:168` → `src/services/classroomAdmissionService.js:97-115` — removal writes ClassParticipant/InstituteParticipant/`Classroom.deletedStudents`; grep `Session\.` in that path → none.

wise-analytics-portal (`~/Documents/wise/wise-analytics-portal`, read-only):
- `marts/wise_marts/facts_v3.py:218-292` — `_participants_base()`: `attend` CTE projects wiseUserId/name/user_email/inMeetingDuration/isTeacher only; `attended = a.student_id IS NOT NULL` (line ~274); no rsvp/offline/duration.
- `grep -rn -i "rsvp|not_invited|offline" marts/wise_marts/` → only a docstring hit.

athena-agent: `schemas/processed/processed/zoom_attendance.md` column list (no rsvp/offline); `schemas/source/mongo/zoom.md:47-60` (participants sub-schema, predates rsvp fields — schema doc is stale on `rsvpStatus`/`rsvpDetails`).

No Athena query was run (caller asked for platform knowledge, not lake queries).

## Gotcha

1. **`session_participant_facts_v3.attended` is "has a participants row", not "was present."** Every enrolled student gets a duration-0 row whenever anyone attended, so `attended` is true for absentees and NOT_INVITED students alike. Use `attend_minutes > 0`. Any consumer already using `attended` for attendance is overcounting — this contradicts COMPACT §4's canonical query (`count_if(attended)`), which should be corrected once the fact is fixed.
2. **`rsvpStatus` is permanent but `rsvpDetails` evaporates at 30 days** on ENDED sessions. A "who removed this student and when" audit on older sessions will find only the status.
3. **A session with zero Zoom attendance wipes every rsvp row** at capture (`absentClassStudents` is `[]` when nothing was present). Counting NOT_INVITED over ENDED sessions therefore undercounts sessions nobody joined.
4. **Zoom name matching is exact after sanitising** — "Kiaansh K." vs "Kiaansh" is a miss. The unmatched row carries the real attendance; the teacher's manual mark produces a second, synthetic full-duration `offline:true` row on the wiseUserId. Both rows coexist; per-student minutes summed across them would double count.
5. `schemas/source/mongo/zoom.md` predates the RSVP fields — do not treat it as the complete participants sub-schema.
