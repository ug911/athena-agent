---
collection: "LiveClassDiscussion"
athena_table: "wise_app_backend__live_class_discussion"
mongo_field_count: 14
athena_field_count: 34
matched: 14
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `LiveClassDiscussion` ↔ `processed.wise_app_backend__live_class_discussion`

- **Mongo source**: [`src/models/LiveClassDiscussion.js`](../source/mongo/LiveClassDiscussion.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__live_class_discussion.md`](../processed/processed/wise_app_backend__live_class_discussion.md)
- **Coverage**: 14/14 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `upvoted.[]` | `string` | JSON path |
| `insightid.$oid` | `string` | JSON path |
| `replies.[]` | `object` | JSON path |
| `replies.[]._id` | `object` | JSON path |
| `replies.[]._id.$oid` | `string` | JSON path |
| `replies.[].createdat` | `object` | JSON path |
| `replies.[].createdat.$date` | `object` | JSON path |
| `replies.[].createdat.$date.$numberlong` | `string` | JSON path |
| `replies.[].updatedat` | `object` | JSON path |
| `replies.[].updatedat.$date` | `object` | JSON path |
| `replies.[].updatedat.$date.$numberlong` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
