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

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
