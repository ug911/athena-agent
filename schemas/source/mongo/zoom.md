---
collection: "zoom"
model: "zoom"
source_file: "src/models/Session.js"
field_count: 86
last_synced: "2026-04-28T10:58:23+00:00"
---

# `zoom` (Mongo collection)

- **Model**: `zoom`
- **Source**: [`src/models/Session.js`](../../../src/models/Session.js)
- **Athena counterpart**: try `processed.wise_app_backend__zoom` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ classId: 1, meetingStatus: 1, archived: 1, start_time: 1 }]`
- `[{ start_time: 1 }]`
- `[{ 'metadata.ownerId': 1, start_time: 1 }]`
- `[{ userId: 1, start_time: 1 }]`
- `[{ 'metadata.demoClassId': 1 }]`

## Local sub-schemas referenced

`fileSchema`, `participantsSchema`, `recordingsSchema`, `sessionSchema`, `streamingDataSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `provider` | `String` |  | <VALID_SESSION_PROVIDERS> |  | PROVIDER_ZOOM |  |
| `mettingId` | `String` |  |  |  |  |  |
| `meetingUUID` | `String` |  |  |  |  |  |
| `attendanceRecorded` | `Boolean` |  |  |  | false |  |
| `mettingEnded` | `Boolean` |  |  |  | false |  |
| `meetingStarted` | `Boolean` |  |  |  | false |  |
| `start_url` | `String` |  |  |  |  |  |
| `join_url` | `String` |  |  |  |  |  |
| `timeZone` | `String` |  |  |  |  |  |
| `classId` | `ObjectId` | `class` |  |  |  |  |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `start_time` | `Date` |  |  |  |  |  |
| `end_time` | `Date` |  |  |  |  |  |
| `duration` | `Number` |  |  |  |  |  |
| `maxParticipantDuration` | `Number` |  |  |  |  |  |
| `participant` | `Number` |  |  |  |  |  |
| `participants[]` | `<participantsSchema>` |  |  |  |  |  |
| `participants[].user_id` | `String` |  |  |  |  |  |
| `participants[].wiseUserId` | `ObjectId` | `user` |  |  |  |  |
| `participants[].name` | `String` |  |  |  |  |  |
| `participants[].user_email` | `String` |  |  |  |  |  |
| `participants[].customerKey` | `String` |  |  |  |  |  |
| `participants[].duration` | `Number` |  |  |  |  |  |
| `participants[].inMeetingDuration` | `Number` |  |  |  |  |  |
| `participants[].relativePercentAttendance` | `Number` |  |  |  |  |  |
| `participants[].absolutePercentAttendance` | `Number` |  |  |  |  |  |
| `participants[].isTeacher` | `Boolean` |  |  |  |  |  |
| `participants[].offline` | `Boolean` |  |  |  |  |  |
| `participants[].firstEntryTime` | `Date` |  |  |  |  |  |
| `participants[].lastExitTime` | `Date` |  |  |  |  |  |
| `attendees` | `Array<ObjectId>` | `user` |  |  |  |  |
| `licensed` | `Boolean` |  |  |  | false |  |
| `comments` | `Array<commentsSchema>` |  |  |  |  |  |
| `lastCommentedAt` | `Date` |  |  |  |  |  |
| `disableCommenting` | `Boolean` |  |  |  | false |  |
| `metadata` | `Object` |  |  |  | {} |  |
| `public` | `Boolean` |  |  |  |  |  |
| `recordingShared` | `Boolean` |  |  |  |  |  |
| `recordingsCaptured` | `Boolean` |  |  |  |  |  |
| `recordingUnsharedAt` | `Date` |  |  |  |  |  |
| `thumbnail` | `String` |  |  |  |  |  |
| `offline` | `Boolean` |  |  |  |  |  |
| `location` | `String` |  |  |  |  |  |
| `archived` | `Boolean` |  |  |  | false |  |
| `scheduledStartTime` | `Date` |  |  |  |  |  |
| `scheduledEndTime` | `Date` |  |  |  |  |  |
| `title` | `String` |  |  |  |  |  |
| `description` | `String` |  |  |  |  |  |
| `privateNote` | `String` |  |  |  |  |  |
| `type` | `String` |  | TYPE_AD_HOC, TYPE_SCHEDULED, TYPE_OFFLINE, TYPE_PLACEHOLDER |  | TYPE_AD_HOC |  |
| `recordings[]` | `<recordingsSchema>` |  |  |  |  |  |
| `recordings[].type` | `String` |  | RECORD_TYPE_YOUTUBE, RECORD_TYPE_RECORDING, RECORD_TYPE_P… | required |  |  |
| `recordings[].url` | `String` |  |  | required |  |  |
| `recordings[].duration` | `Number` |  |  |  |  |  |
| `recordings[].sessionIndex` | `Number` |  |  |  |  |  |
| `recordings[].partIndex` | `Number` |  |  |  |  |  |
| `recordings[].file` | `<fileSchema>` |  |  |  |  |  |
| `recordings[].file.path` | `String` |  |  |  |  |  |
| `recordings[].file.filename` | `String` |  |  |  |  |  |
| `recordings[].file.s3Key` | `String` |  |  |  |  |  |
| `recordings[].file.s3FilePath` | `String` |  |  |  |  |  |
| `recordings[].file.subtype` | `String` |  |  |  |  |  |
| `recordings[].file.type` | `String` |  | file, video |  |  |  |
| `recordings[].file.size` | `Number` |  |  |  |  |  |
| `recordings[].file.duration` | `Number` |  |  |  |  |  |
| `rawRecordings[]` | `<recordingsSchema>` |  |  |  |  |  |
| `rawRecordings[].type` | `String` |  | RECORD_TYPE_YOUTUBE, RECORD_TYPE_RECORDING, RECORD_TYPE_P… | required |  |  |
| `rawRecordings[].url` | `String` |  |  | required |  |  |
| `rawRecordings[].duration` | `Number` |  |  |  |  |  |
| `rawRecordings[].sessionIndex` | `Number` |  |  |  |  |  |
| `rawRecordings[].partIndex` | `Number` |  |  |  |  |  |
| `rawRecordings[].file` | `<fileSchema>` |  |  |  |  |  |
| `rawRecordings[].file.path` | `String` |  |  |  |  |  |
| `rawRecordings[].file.filename` | `String` |  |  |  |  |  |
| `rawRecordings[].file.s3Key` | `String` |  |  |  |  |  |
| `rawRecordings[].file.s3FilePath` | `String` |  |  |  |  |  |
| `rawRecordings[].file.subtype` | `String` |  |  |  |  |  |
| `rawRecordings[].file.type` | `String` |  | file, video |  |  |  |
| `rawRecordings[].file.size` | `Number` |  |  |  |  |  |
| `rawRecordings[].file.duration` | `Number` |  |  |  |  |  |
| `streamingData` | `<streamingDataSchema>` |  |  |  |  |  |
| `streamingData.streamingKey` | `String` |  |  | required |  |  |
| `streamingData.streamingURL` | `String` |  |  | required |  |  |
| `streamingData.pageURL` | `String` |  |  | required |  |  |
| `meetingStatus` | `String` |  | <VALID_STATUSES> |  | STATUS_ENDED |  |
| `password` | `String` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
