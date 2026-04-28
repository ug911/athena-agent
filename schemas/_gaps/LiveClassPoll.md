---
collection: "LiveClassPoll"
athena_table: "wise_app_backend__live_class_poll"
mongo_field_count: 25
athena_field_count: 72
matched: 24
coverage_pct: 96.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `LiveClassPoll` ↔ `processed.wise_app_backend__live_class_poll`

- **Mongo source**: [`src/models/LiveClassPoll.js`](../source/mongo/LiveClassPoll.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__live_class_poll.md`](../processed/processed/wise_app_backend__live_class_poll.md)
- **Coverage**: 24/25 Mongo fields are present in Athena (**96.0%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `duration` | `Number` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `insightid.$oid` | `string` | JSON path |
| `options.a` | `object` | JSON path |
| `options.a.text` | `string` | JSON path |
| `options.a.votes.a.votes[].timetaken.$numberint` | `string` | JSON path |
| `options.b` | `object` | JSON path |
| `options.b.text` | `string` | JSON path |
| `options.b.votes.b.votes[].timetaken.$numberint` | `string` | JSON path |
| `options.c` | `object` | JSON path |
| `options.c.text` | `string` | JSON path |
| `options.c.votes.c.votes[].timetaken.$numberint` | `string` | JSON path |
| `options.d` | `object` | JSON path |
| `options.d.text` | `string` | JSON path |
| `options.d.votes.d.votes[].timetaken.$numberint` | `string` | JSON path |
| `maxanswers.$numberint` | `string` | JSON path |
| `correctanswers.[]` | `string` | JSON path |
| `votes.[]` | `object` | JSON path |
| `votes.[].createdat.$date` | `object` | JSON path |
| `votes.[].createdat.$date.$numberlong` | `string` | JSON path |
| `votes.[].timetaken.$numberint` | `string` | JSON path |
| `votes.[].updatedat.$date` | `object` | JSON path |
| `votes.[].updatedat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `endsat.$date` | `object` | JSON path |
| `endsat.$date.$numberlong` | `string` | JSON path |
