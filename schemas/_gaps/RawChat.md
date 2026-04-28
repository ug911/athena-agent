---
collection: "RawChat"
athena_table: "wise_app_backend__raw_chat"
mongo_field_count: 7
athena_field_count: 19
matched: 3
coverage_pct: 42.9
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `RawChat` ↔ `processed.wise_app_backend__raw_chat`

- **Mongo source**: [`src/models/RawChat.js`](../source/mongo/RawChat.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__raw_chat.md`](../processed/processed/wise_app_backend__raw_chat.md)
- **Coverage**: 3/7 Mongo fields are present in Athena (**42.9%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `files[]` | `<fileSchema>` |  |  |
| `files[].sessionIndex` | `Number` |  |  |
| `files[].meetingUUID` | `String` |  |  |
| `files[].file` | `attachmentSchema` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `chats` | `string` | column |
| `_id.$oid` | `string` | JSON path |
| `sessionid.$oid` | `string` | JSON path |
| `chats.[]` | `object` | JSON path |
| `chats.[]._id` | `object` | JSON path |
| `chats.[]._id.$oid` | `string` | JSON path |
| `chats.[].partindex.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
