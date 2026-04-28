---
collection: "ChatMessage"
model: "ChatMessage"
source_file: "src/models/ChatMessage.js"
field_count: 4
last_synced: "2026-04-28T10:58:23+00:00"
---

# `ChatMessage` (Mongo collection)

- **Model**: `ChatMessage`
- **Source**: [`src/models/ChatMessage.js`](../../../src/models/ChatMessage.js)
- **Athena counterpart**: try `processed.wise_app_backend__chat_message` or `processed.wise_app_backend__chatmessage` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ chatId: 1, createdAt: -1 }]`

## Local sub-schemas referenced

`chatMessageSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `chatId` | `ObjectId` | `Chat` |  | required |  |  |
| `senderId` | `ObjectId` | `user` |  | required |  |  |
| `message` | `String` |  |  |  |  |  |
| `attachments` | `Array<attachmentSchema>` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
