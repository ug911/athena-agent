---
collection: "RawZoomAttendance"
model: "RawZoomAttendance"
source_file: "src/models/RawZoomAttendance.js"
field_count: 6
last_synced: "2026-04-28T10:58:23+00:00"
---

# `RawZoomAttendance` (Mongo collection)

- **Model**: `RawZoomAttendance`
- **Source**: [`src/models/RawZoomAttendance.js`](../../../src/models/RawZoomAttendance.js)
- **Athena counterpart**: try `processed.wise_app_backend__raw_zoom_attendance` or `processed.wise_app_backend__rawzoomattendance` — verify in `schemas/INDEX.md`.

## Local sub-schemas referenced

`rawZoomAttendanceSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `classId` | `ObjectId` | `class` |  |  |  |  |
| `meetingId` | `String` |  |  |  |  |  |
| `meetingUUID` | `String` |  |  |  |  |  |
| `sessionId` | `ObjectId` | `zoom` |  | required |  |  |
| `totalRecords` | `Number` |  |  |  |  |  |
| `participants` | `Array` |  |  |  |  |  |

## Usage (from backend-api)

_4 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 3
- `.updateOne` × 1

### Top call sites

- `src/services/meetingAttendanceService.js` × 3
- `src/controllers/UserController.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
