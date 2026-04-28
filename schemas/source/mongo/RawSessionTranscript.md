---
collection: "RawSessionTranscript"
model: "RawSessionTranscript"
source_file: "src/models/RawSessionTranscript.js"
field_count: 7
last_synced: "2026-04-28T10:58:23+00:00"
---

# `RawSessionTranscript` (Mongo collection)

- **Model**: `RawSessionTranscript`
- **Source**: [`src/models/RawSessionTranscript.js`](../../../src/models/RawSessionTranscript.js)
- **Athena counterpart**: try `processed.wise_app_backend__raw_session_transcript` or `processed.wise_app_backend__rawsessiontranscript` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ sessionId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`fileSchema`, `rawSessionTranscriptSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `sessionId` | `ObjectId` | `zoom` |  | required |  |  |
| `files[]` | `<fileSchema>` |  |  |  |  |  |
| `files[].url` | `String` |  |  | required |  |  |
| `files[].partIndex` | `Number` |  |  |  |  |  |
| `files[].sessionIndex` | `Number` |  |  |  |  |  |
| `files[].meetingUUID` | `String` |  |  |  |  |  |
| `files[].file` | `attachmentSchema` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
