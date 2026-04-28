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

## Usage (from backend-api)

_7 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.updateOne` × 3
- `.findOne` × 2
- `.create` × 1
- `.aggregate` × 1

### Top call sites

- `src/services/sessionAIDataService.js` × 7

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
