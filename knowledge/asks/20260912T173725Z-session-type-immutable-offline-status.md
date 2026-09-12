# Can PUT change a session's type OFFLINE→SCHEDULED, what sets IN_PROGRESS for OFFLINE, and is there any provenance field?

- **id:** 8dc4d5eb-f8b9-46ec-ad81-0e5b7451fa41   **from:** group-sessions-admin   **depth:** 0   **utc:** 20260912T173725Z

## Question

Wise sessions API, NA host. (1) Can `PUT /teacher/classes/{classId}/sessions/{sessionId}` change an
existing session's type from OFFLINE (in-person) to SCHEDULED (live/online), and if so which field
name (`sessionType`? `type`? `offline`?) does it accept — or is type immutable after creation?
(2) For an OFFLINE session, what sets `meetingStatus` to IN_PROGRESS: automatic at
`scheduledStartTime`, or does the teacher/admin start it? (3) Does a session document carry any
`createdBy`/`updatedBy`/`source` field telling whether it was created via the vendor API vs the
dashboard?

Context: group-sessions-admin relinked a cover-up shell created as OFFLINE into a 'live' cover-up by
PUT-ing title/location/times only; the shell stayed OFFLINE.

## Answer

**(1) No — type is immutable via that endpoint. The field is `type`.**
`src/models/Session.js:132`: `type: { type: String, enum: [AD_HOC, SCHEDULED, OFFLINE,
PLACEHOLDER], default: AD_HOC }`. Not `sessionType`, not `offline`.
The `updateSession` Joi body schema (`src/params/teacher.params.js:725`) accepts exactly nine
fields — `scheduledStartTime, scheduledEndTime, title, location, description, streamingData,
disableCommenting, tags, workingHoursScheduleId` — and `SessionService.js:732` destructures only
those (plus `thumbnailUploadToken, autoThumbnail, userId, removeThumbnail, recordingShared,
privateNote`). `type` is never written on this path.

**Why it returned 200 and did nothing:** `src/helpers/validate.js:33` sets Joi `allowUnknown: true`
deliberately (documented in-file: v1 was permissive and strict mode "would break every endpoint
whose schema is a strict subset of what clients actually send"), with no `stripUnknown`. So an
unknown `type`/`sessionType`/`offline` key passes validation onto `req.body` and is then never
destructured — **accepted, 200, silently discarded.** No request against this endpoint can flip the
type.

**(2) Nothing — IN_PROGRESS is unreachable for OFFLINE. The question's two options are both wrong.**
`SessionService.updateSession`'s OFFLINE branch derives status purely from the clock **at write
time**:
```js
if (session.isTypeOffline()) {
  const isUpcoming = moment(offlineStart).isAfter();
  updateQuery = { ...updateQuery, start_time, end_time, duration,
    meetingStatus: isUpcoming ? STATUS_UPCOMING : STATUS_ENDED, mettingEnded: !isUpcoming };
}
```
Only `UPCOMING` or `ENDED`; no third branch. It is **not a scheduler** — an untouched OFFLINE row
does not transition on its own, so one whose start has passed can still read `UPCOMING` until next
written. IN_PROGRESS is set only by go-live paths (`meetingService.js:276` with `meetingStarted:
true`/`start_url`/`join_url`, and `DevAPIController.js:256`), both online-meeting flows unreachable
for OFFLINE.

Confirmed in production (`lake_cdc.wise_app_backend__zoom`), both regions:

| region | OFFLINE total | OFFLINE IN_PROGRESS | OFFLINE MISSED |
|---|---|---|---|
| in | 54,978 | **0** | **0** |
| na | 12,056 | **0** | **0** |

67,034 OFFLINE sessions, zero IN_PROGRESS and zero MISSED — both follow from the code. NA OFFLINE
splits ENDED 8,292 / UPCOMING 3,345 / CANCELLED 419 (CANCELLED comes from the cancellation path).
SCHEDULED does reach IN_PROGRESS (19) and MISSED (6,438); AD_HOC reaches IN_PROGRESS (2).

**(3) No provenance field exists.** `src/models/Session.js` has no `createdBy`, `updatedBy`,
`source`, `createdVia`, `origin`, `apiKey`, `vendor` or `integration`; the schema ends
`{ collection: 'zoom', timestamps: { createdAt: true, updatedAt: true } }` — timestamps only, no
actor or channel. Production: **0 occurrences of each across 4,419,438 session docs**. The vendor
path doesn't stamp anything either — `DevAPIController.js:252` creates with
`metadata: { paidUser, ownerId, isOwnerZoom, lensEnabled }`.

Weak indirect signals only (inference, not reliable): `metadata.lensEnabled`/`isOwnerZoom`,
`licensed: true`, and DevAPI's literal title `` `Something ${Math.random()}` `` — distinctive but
specific to that one endpoint. Real provenance needs a schema field added in backend-api; CDC would
pick it up automatically once written.

**For the relink:** the shell cannot become SCHEDULED via this endpoint at any spelling. Either
delete and recreate with `type: SCHEDULED` (subject to the create path accepting `type` — not
verified), or have backend-api add `type` to the whitelist. **Do not flip `type` directly in
Mongo:** the OFFLINE branch alone maintains `start_time`/`end_time`/`duration`/`mettingEnded` and
`meetingStatus` semantics differ, so a bare field flip leaves the document internally inconsistent.

**Confidence: high** on all three. (1) and (3) come from a Joi whitelist and a destructuring list,
both exhaustive by construction, with `allowUnknown` explicitly documented; (3) corroborated by
0/4,419,438 in production. (2) rests on two independent legs — no code branch can assign
IN_PROGRESS to an OFFLINE session, and 67,034 production rows contain none. **Limit:** I read the
working-tree source and did not confirm which commit is deployed to the NA host or whether NA runs
the same build as IN; the NA-inclusive data agreeing makes divergence unlikely but not excluded.
**Not verified:** whether any other endpoint accepts `type` — `updateSessionInBulk`
(`SessionService.js:882`) was not read, nor the create path's schema.

**Check next:** (1) read the session *create* param schema to confirm `type: SCHEDULED` is settable
at creation — that decides whether delete-and-recreate works, and I ran out of budget for it;
(2) read `updateSessionInBulk`; (3) confirm the deployed NA commit if this gates a production
change; (4) raise a `source`/`createdVia` enum with the backend-api team if provenance matters;
(5) note the codebase typos **`mettingEnded`** and **`mettingId`** (both sic) — filtering on the
correctly-spelled names silently matches nothing.

## Evidence

backend-api (`~/Documents/wise/backend-api`, read-only):
- `src/models/Session.js:13-14,132,136,189-190` — TYPE_/STATUS_ constants, `type` enum + default
  AD_HOC, `meetingStatus` enum default ENDED, `isTypeOffline()`.
- `src/models/Session.js:125-140` — full schema field list; ends `{ collection: 'zoom',
  timestamps: { createdAt: true, updatedAt: true } }`. No provenance fields.
- `grep -n "createdBy|updatedBy|source|createdVia|origin|apiKey|vendor|integration"
  src/models/Session.js` → **no matches**.
- `src/params/teacher.params.js:725-746` — `updateSession` body whitelist (9 fields).
- `src/routes/teacherRouter.js:428` — `.put(validate(teacherParams.updateSession),
  teacher.updateSession)`.
- `src/controllers/TeacherController.js:1940-1949` → `sessionService.updateSession(req)`.
- `src/services/SessionService.js:732-815` — destructuring list; OFFLINE branch computing
  meetingStatus from the clock; `updateQuery` assembly.
- `src/helpers/validate.js:17-33` — `allowUnknown: true`, `context: true`, no `stripUnknown`, with
  the in-file rationale.
- `src/services/meetingService.js:276`, `src/controllers/DevAPIController.js:248-262` — the only
  IN_PROGRESS setters; DevAPI create fields.

Athena (read-only), by query id:
- `d7851ba6` — NA `zoom` type × meetingStatus: OFFLINE ENDED 8,292 / UPCOMING 3,345 / CANCELLED 419
  and **no IN_PROGRESS row**; SCHEDULED ENDED 63,368 / UPCOMING 53,687 / CANCELLED 10,749 /
  MISSED 6,438 / IN_PROGRESS 19; AD_HOC ENDED 3,616 / IN_PROGRESS 2; PLACEHOLDER ENDED 267.
- `ebecdc5f` — both regions: OFFLINE 54,978 in / 12,056 na, `offline_in_progress` 0, `offline_missed`
  0; `createdBy` 0, `updatedBy` 0, `source` 0 over 4,419,438 docs. (2.2 GB scanned, bytes-warn
  tripped — unavoidable for a full-corpus key-existence check, but scope it next time.)

## Gotcha

`allowUnknown: true` without `stripUnknown` is the trap, and it is repo-wide, not specific to this
endpoint. Send a field the schema does not list and you get **`200 OK` with the field silently
discarded** — the API cannot distinguish "you used the wrong field name" from "it worked". Any
future ask of the form *"I PUT X and nothing happened"* should start at the param whitelist in
`src/params/*.params.js` and the service's destructuring line, which together are an exhaustive
statement of what an endpoint will actually honour.

Second, a false-dichotomy worth remembering: the caller asked whether IN_PROGRESS is set
automatically or by the teacher. The real answer was that the state is **unreachable** for that
session type. When both offered options are wrong, saying so is the whole value of the answer —
and here the code and 67,034 production rows agreed independently, which is the strongest form of
this kind of finding.
