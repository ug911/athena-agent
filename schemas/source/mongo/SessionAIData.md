---
collection: "SessionAIData"
model: "SessionAIData"
source_file: "src/models/SessionAIData.js"
field_count: 6
last_synced: "2026-04-28T10:58:23+00:00"
---

# `SessionAIData` (Mongo collection)

- **Model**: `SessionAIData`
- **Source**: [`src/models/SessionAIData.js`](../../../src/models/SessionAIData.js)
- **Athena counterpart**: try `processed.wise_app_backend__session_a_i_data` or `processed.wise_app_backend__sessionaidata` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ sessionId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`revisionNoteSchema`, `sessionAIDataSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `sessionId` | `ObjectId` | `zoom` |  | required |  |  |
| `status` | `String` |  | <VALID_SESSION_AI_DATA_STATUSES> | required |  |  |
| `revisionNotes[]` | `<revisionNoteSchema>` |  |  |  |  |  |
| `revisionNotes[].title` | `String` |  |  |  |  |  |
| `revisionNotes[].content` | `String` |  |  |  |  |  |
| `quizIds` | `Array<ObjectId>` | `announcements` |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
