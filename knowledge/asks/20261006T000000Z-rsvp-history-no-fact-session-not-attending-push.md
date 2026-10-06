# Does any lake table retain pre-overwrite rsvpStatus/rsvpDetails history, and is there a notifications table for session_not_attending push sends?

- **id:** f61699a6-255d-4811-b02a-19d99ca80118   **from:** worker   **depth:** 0   **utc:** 20261006T000000Z

## Question

READ-ONLY question, NA region (namespace thinktankjr). Two Wise sessions on 2026-10-06: session
6a7c9a8afa631b452eaa3eb9 (learner 6a15a183eff9b8dd3ebb0fe4 'Medhansh', class
6a159be63e6d2516d2fcb78f) and session 6aaaf71d406060e55f022f5b (learner
6a15a183eff9b8dd3ebb1040 'Neil Rastogi', class 6aaaf6d128a9b01211fd3033). On each, the
learner's participants[] row had rsvpStatus NOT_ATTENDING shortly before the session start
(00:00Z / 01:00Z); an admin then set it back to ATTENDING at 2026-10-06T00:04:14Z / 01:05:16Z,
which overwrote participants[].rsvpDetails {markedBy, markedAt}. Need markedBy/markedAt and the
full rsvpStatus change history before the overwrite, for both. Does any lake table (CDC/history
of the sessions collection, or any processed table) retain those historical values? Also: is
there a notifications/push table with type session_not_attending (category SessionNotAttending,
entityId = sessionId) for those two session ids — return send timestamps. If nothing retains
it, say so plainly.

## Answer

**No lake table can reliably retrieve the pre-overwrite rsvp history for either session, and
no Athena/lake table holds `session_not_attending` push sends at all** — the second finding is
architectural (push notifications persist to DynamoDB, never touch Mongo, so CDC never sees
them), the first is a tooling gap, not a confirmed absence.

Checked, in order: `lake_cdc.wise_app_backend__zoom` (MERGEd latest-state mirror, no history —
confirms [[20260915T135438Z-participants-rsvp-offline-rows-no-fact]]); `*_facts_v3` (doesn't
carry rsvp columns at all); `processed_na.wise_app_backend__zoom` (daily dump, same overwrite
problem). The one genuinely append-only layer, `cdc_raw.changes_v1`, likely *does* still hold
the pre-overwrite `update` event (one row per Mongo change-stream op, never merged/deleted), but
Athena refuses to query it without a literal equality predicate on its `batch` partition
(verified live: `CONSTRAINT_VIOLATION` on injected-partition projection). `batch` is a random
per-flush token (`epoch_millis-uuid8`, from `wise_cdc/spool.py:new_batch_id()`), not a time
bucket, and there is no catalog mapping a time window to batch_ids reachable from SQL — only an
S3 key listing would give that, and I have no S3-listing tool here. So this is "cannot check",
not "checked and absent."

For `session_not_attending`: traced backend-api source —
`sessionService.js:1626` → `notificationService.sendSessionNotAttendingNotification` (category
`SessionNotAttending`, type `session_not_attending`, `entityId: session._id`) →
`pushNotificationWorker.js` → FCM send + `saveNotification()` → DynamoDB
`notifications_production` (30-day TTL via `expiresAt`), never Mongo. CDC only watches Mongo
dbs `wise-app-backend`/`exam-service`/`webapp`, so this is genuinely outside the warehouse by
design, not a missing fact.

Full write-up delivered to the caller at
`/var/folders/t_/6nh_x0m11hnb90b_663m19q40000gn/T//ask-f61699a6-255d-4811-b02a-19d99ca80118.md`.

## Evidence

- `mcp__athena__explain_query` on `cdc_raw.changes_v1` without a `batch` predicate → rejected,
  query id `eedb3b86-6007-4c83-9e2c-d8b061036da8`.
- `mcp__athena__describe_table(cdc_raw, changes_v1)` — DDL confirms `projection.batch.type=injected`.
- `~/Documents/wise/wise-analytics-portal/cdc/wise_cdc/spool.py:25-27` (`new_batch_id`),
  `cdc/wise_cdc/sinks/s3_athena.py:37-45` (staging key layout).
- `~/Documents/wise/backend-api`: `src/services/sessionService.js:1626`;
  `src/services/communications/notificationService.js:106,899-932`;
  `src/services/communications/pushNotificationService.js:24-49`;
  `src/workers/pushNotificationWorker.js` (full read); `src/bin/www.mjs:28` (`notifications_production`).
- `knowledge/COMPACT.md` §1, §5a, §5c, §6.1.

## Gotcha

`cdc_raw.changes_v1` is a true append-only audit log, unlike every other layer in this
warehouse — but its `batch` partition is an opaque random token with zero time index in SQL.
Nobody can honestly say "no history anywhere" for a Mongo-sourced field without first checking
whether they had S3-listing access to resolve batch_ids for this layer; absence of a result from
`lake_cdc`/`processed`/facts is not the same as absence from `cdc_raw.changes_v1`.
