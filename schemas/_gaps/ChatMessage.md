---
collection: "ChatMessage"
athena_table: "wise_app_backend__chatmessage"
mongo_field_count: 4
athena_field_count: 24
matched: 4
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `ChatMessage` ↔ `processed.wise_app_backend__chatmessage`

- **Mongo source**: [`src/models/ChatMessage.js`](../source/mongo/ChatMessage.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__chatmessage.md`](../processed/processed/wise_app_backend__chatmessage.md)
- **Coverage**: 4/4 Mongo fields are present in Athena (**100.0%**).

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
| `chatid.$oid` | `string` | JSON path |
| `senderid.$oid` | `string` | JSON path |
| `attachments.[]` | `object` | JSON path |
| `attachments.[]._id` | `object` | JSON path |
| `attachments.[]._id.$oid` | `string` | JSON path |
| `attachments.[].filename` | `string` | JSON path |
| `attachments.[].path` | `string` | JSON path |
| `attachments.[].s3filepath` | `string` | JSON path |
| `attachments.[].s3key` | `string` | JSON path |
| `attachments.[].size` | `object` | JSON path |
| `attachments.[].size.$numberint` | `string` | JSON path |
| `attachments.[].type` | `string` | JSON path |
