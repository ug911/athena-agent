---
collection: "RawChat"
model: "RawChat"
source_file: "src/models/RawChat.js"
field_count: 7
last_synced: "2026-04-28T10:58:23+00:00"
---

# `RawChat` (Mongo collection)

- **Model**: `RawChat`
- **Source**: [`src/models/RawChat.js`](../../../src/models/RawChat.js)
- **Athena counterpart**: try `processed.wise_app_backend__raw_chat` or `processed.wise_app_backend__rawchat` — verify in `schemas/INDEX.md`.

## Local sub-schemas referenced

`RawChatSchema`, `fileSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `sessionId` | `ObjectId` | `zoom` |  | required, unique |  |  |
| `files[]` | `<fileSchema>` |  |  |  |  |  |
| `files[].url` | `String` |  |  | required |  |  |
| `files[].partIndex` | `Number` |  |  |  |  |  |
| `files[].sessionIndex` | `Number` |  |  |  |  |  |
| `files[].meetingUUID` | `String` |  |  |  |  |  |
| `files[].file` | `attachmentSchema` |  |  |  |  |  |

## Usage (from backend-api)

_1 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 1

### Top call sites

- `src/controllers/UserController.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
