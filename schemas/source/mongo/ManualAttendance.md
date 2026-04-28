---
collection: "ManualAttendance"
model: "ManualAttendance"
source_file: "src/models/ManualAttendance.js"
field_count: 11
last_synced: "2026-04-28T10:58:23+00:00"
---

# `ManualAttendance` (Mongo collection)

- **Model**: `ManualAttendance`
- **Source**: [`src/models/ManualAttendance.js`](../../../src/models/ManualAttendance.js)
- **Athena counterpart**: try `processed.wise_app_backend__manual_attendance` or `processed.wise_app_backend__manualattendance` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ sessionId: 1 }, { unique: true }]`
- `[{ createdAt: 1 }, { expireAfterSeconds: 172800 }]`

## Local sub-schemas referenced

`manualAttendanceSchema`, `participantSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `sessionId` | `ObjectId` | `zoom` |  | required |  |  |
| `participants[]` | `<participantSchema>` |  |  |  |  |  |
| `participants[].userId` | `ObjectId` | `user` |  |  |  |  |
| `participants[].userName` | `String` |  |  |  |  |  |
| `participants[].userProfilePicture` | `String` |  |  |  |  |  |
| `participants[].live` | `Boolean` |  |  |  | false |  |
| `participants[].present` | `Boolean` |  |  |  | false |  |
| `participants[].left` | `Boolean` |  |  |  |  |  |
| `participants[].firstEntryTime` | `Date` |  |  |  |  |  |
| `participants[].lastExitTime` | `Date` |  |  |  |  |  |
| `participants[].manual` | `Boolean` |  |  |  |  |  |

## Usage (from backend-api)

_12 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 7
- `.updateOne` × 4
- `.create` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `sessionId` × 1

### Top call sites

- `src/services/meetingAttendanceService.js` × 8
- `src/controllers/TeacherController.js` × 3
- `src/controllers/UserController.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
