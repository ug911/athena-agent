---
collection: "RawRecording"
model: "RawRecording"
source_file: "src/models/RawRecording.js"
field_count: 8
last_synced: "2026-04-28T10:58:23+00:00"
---

# `RawRecording` (Mongo collection)

- **Model**: `RawRecording`
- **Source**: [`src/models/RawRecording.js`](../../../src/models/RawRecording.js)
- **Athena counterpart**: try `processed.wise_app_backend__raw_recording` or `processed.wise_app_backend__rawrecording` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ sessionId: 1 }, { unique: true }]`
- `[{ expiresIn: 1 }, { expireAfterSeconds: 0 }]`

## Local sub-schemas referenced

`rawRecordingSchema`, `recordingsSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `sessionId` | `ObjectId` | `zoom` |  | required |  |  |
| `recordings[]` | `<recordingsSchema>` |  |  |  |  |  |
| `recordings[].type` | `String` |  | RECORDING, CHAT | required |  |  |
| `recordings[].url` | `String` |  |  | required |  |  |
| `recordings[].duration` | `Number` |  |  |  |  |  |
| `recordings[].sessionIndex` | `Number` |  |  |  |  |  |
| `recordings[].partIndex` | `Number` |  |  |  |  |  |
| `expiresIn` | `Date` |  |  |  |  |  |

## Usage (from backend-api)

_6 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 3
- `.updateOne` × 3

### Top call sites

- `src/workers/videoConversionWorker.js` × 3
- `src/controllers/UserController.js` × 1
- `src/controllers/TeacherController.js` × 1
- `src/controllers/LensController.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
