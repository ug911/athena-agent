---
collection: "Chat"
model: "Chat"
source_file: "src/models/Chat.js"
field_count: 7
last_synced: "2026-04-28T10:58:23+00:00"
---

# `Chat` (Mongo collection)

- **Model**: `Chat`
- **Source**: [`src/models/Chat.js`](../../../src/models/Chat.js)
- **Athena counterpart**: try `processed.wise_app_backend__chat` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ instituteId: 1, chatWithId: 1, classId: 1 }, { unique: true }]`
- `[{ instituteId: 1, participants: 1 }]`
- `[{ classId: 1 }]`

## Local sub-schemas referenced

`chatSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `instituteId` | `ObjectId` |  |  | required |  |  |
| `classId` | `ObjectId` | `class` |  |  |  |  |
| `chatWithId` | `ObjectId` | `user` |  | required |  |  |
| `chatType` | `String` |  | CHAT_TYPE_INSTITUTE, CHAT_TYPE_CLASSROOM | required |  |  |
| `participants` | `Array<ObjectId>` | `user` |  |  |  |  |
| `unreadCounts` | `Map` |  |  |  |  |  |
| `lastMessageTimestamp` | `Date` |  |  |  |  |  |

## Usage (from backend-api)

_17 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.find` × 4
- `.deleteMany` × 3
- `.aggregate` × 3
- `.findOneAndUpdate` × 3
- `.findOne` × 2
- `.create` × 1
- `.updateMany` × 1

### Top call sites

- `src/services/chatService.js` × 11
- `src/services/DemoAccountService.js` × 3
- `src/services/classroomService.js` × 2
- `src/workers/dataTransferWorker.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
