---
collection: "PollVote"
athena_table: "wise_app_backend__pollvote"
mongo_field_count: 3
athena_field_count: 15
matched: 3
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `PollVote` ↔ `processed.wise_app_backend__pollvote`

- **Mongo source**: [`src/models/PollVote.js`](../source/mongo/PollVote.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__pollvote.md`](../processed/processed/wise_app_backend__pollvote.md)
- **Coverage**: 3/3 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `pollid.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
