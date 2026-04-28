---
collection: "Chat"
athena_table: "wise_app_backend__chat"
mongo_field_count: 7
athena_field_count: 24
matched: 7
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `Chat` ↔ `processed.wise_app_backend__chat`

- **Mongo source**: [`src/models/Chat.js`](../source/mongo/Chat.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__chat.md`](../processed/processed/wise_app_backend__chat.md)
- **Coverage**: 7/7 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `instituteid.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `chatwithid.$oid` | `string` | JSON path |
| `participants.[]` | `object` | JSON path |
| `participants.[].$oid` | `string` | JSON path |
| `unreadcounts.<oid>` | `object` | JSON path |
| `unreadcounts.<oid>.$numberint` | `string` | JSON path |
| `lastmessagetimestamp.$date` | `object` | JSON path |
| `lastmessagetimestamp.$date.$numberlong` | `string` | JSON path |
