# Five thinktankjr ONE_TO_ONE classes with "no students" — never created, stuck pending, or ACCEPTED-then-REMOVED?

- **id:** dec9f2ce-c668-4485-84bc-189a19d137cd   **from:** worker   **depth:** 0   **utc:** 20261007T000000Z

## Question

READ-ONLY, NA region, namespace thinktankjr. For 5 ONE_TO_ONE classrooms (created via
`POST /teacher/addClass` with `student {_id}`) whose participants endpoint now lists no
students, determine per class+student whether the ClassParticipant row was never created,
created INVITED/REQUESTED and never accepted, or created ACCEPTED and later REMOVED (with
when) — plus the student's InstituteParticipant status/createdAt/updatedAt for thinktankjr.
Ask for a history/CDC table of status transitions if one exists.

## Answer

All 5 `ClassParticipant` rows exist today with `status=REMOVED` — none was "never created",
and none is provable/possible to be stuck INVITED/REQUESTED, because `ClassParticipant.status`
can only reach `REMOVED` by first passing through `ACCEPTED` (the pending-rejection path
deletes the row instead — `classroomAdmissionService.js:214/235/249`). This is a structural
guarantee from the single writer of `STATUS_REMOVED` in backend-api
(`classroomAdmissionService.js:210/231/243`), not an inference from timing.

Two distinct removal shapes, distinguished by whether the student's `InstituteParticipant`
also flipped to `REMOVED` within milliseconds of the `ClassParticipant` flip:
- **Class-only removal** (student still `ACCEPTED` at the institute today): class
  `6a3cc23cb0057fd9bfaa56f9` (Aarav), class `6a6c8e3afa993ad1d46b3114` (Anay Sharma).
- **Institute-level removal cascade** (`InstituteParticipant` REMOVED ~14s–31ms after
  `ClassParticipant`, matching `leaveOrRemoveFromInstitute`'s sequential walk over a user's
  classrooms): class `6a4ceb1e6434fae6d501ad7b` (Arya Panchal), class
  `6a5900cc900c759033db806b` (user later renamed "Deactivated User" via `softDeleteUser` —
  separate, unrelated event), class `6aab1c5828a9b01211fe987b` (Nyra M).

`class.deletedStudents[]` corroborated 3 of 5 (matching `type: REMOVED` + timestamp within
~10ms); it was unexpectedly **empty** for the other 2 despite the same code path pushing to it
unconditionally — flagged as an unresolved inconsistency, not used as a primary signal.

**No history/CDC table carries the full status-transition timeline for events this old.**
Checked `lake_cdc_log.wise_app_backend__classparticipant` directly (the per-change-event
pre-compaction buffer): `region='na'` currently holds only 719 rows, all `ingested_at` on
2026-10-07 (today) — a same-day buffer, not an archive. `cdc_raw.changes_v1` is the only
genuinely append-only layer, but is practically unqueryable without an S3 batch_id listing —
same structural blocker as [[20261006T000000Z-rsvp-history-no-fact-session-not-attending-push]].
So `createdAt`/`updatedAt` on the current merged row is the full extent of what this warehouse
can give for these transitions.

Full write-up with the per-student table delivered to
`/var/folders/t_/6nh_x0m11hnb90b_663m19q40000gn/T//ask-dec9f2ce-c668-4485-84bc-189a19d137cd.md`.

## Evidence

- `lake_cdc.wise_app_backend__classparticipant`, `__instituteparticipant`, `__class`, `__user`
  (all `region='na'`, filtered by explicit class/user ids) — current status, timestamps,
  `deletedStudents[]`, names.
- `lake_cdc_log.wise_app_backend__classparticipant` — confirmed empty of relevant history;
  `count(*)=719`, `min/max(ingested_at)` both 2026-10-07.
- `~/Documents/wise/backend-api`: `src/models/ClassParticipant.js:11-57`;
  `src/services/classroomAdmissionService.js:101-132,189-258`;
  `src/services/instituteAdmissionService.js:42-61,144-163,170-207,357-382`;
  `src/controllers/TeacherController.js:135-207`; `src/services/classroomService.js:1230-1256,1296-1306`.

## Gotcha

`joinedOn` on `ClassParticipant` is stamped on *every* status transition (REQUEST, INVITE,
ACCEPT, and REMOVE alike) — on a `REMOVED` row it equals the removal time, not the original
join time. Don't read it as "first accepted at". Same for `lake_cdc_log` as the previous rsvp
ask: it has the schema of a history log but in practice is a ~1-day compaction buffer — always
check `min(ingested_at)` before trusting it has reach back further than that.
