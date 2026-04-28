---
collection: "LiveClassTest"
athena_table: "wise_app_backend__liveclasstest"
mongo_field_count: 12
athena_field_count: 30
matched: 11
coverage_pct: 91.7
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `LiveClassTest` ↔ `processed.wise_app_backend__liveclasstest`

- **Mongo source**: [`src/models/LiveClassTest.js`](../source/mongo/LiveClassTest.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__liveclasstest.md`](../processed/processed/wise_app_backend__liveclasstest.md)
- **Coverage**: 11/12 Mongo fields are present in Athena (**91.7%**).

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
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `insightid.$oid` | `string` | JSON path |
| `tags.[]` | `string` | JSON path |
| `visibletags.[]` | `string` | JSON path |
| `endsat.$date` | `object` | JSON path |
| `endsat.$date.$numberlong` | `string` | JSON path |
| `submissions.[]` | `object` | JSON path |
| `submissions.[].submittedat.$date` | `object` | JSON path |
| `submissions.[].submittedat.$date.$numberlong` | `string` | JSON path |
| `questions.[]` | `object` | JSON path |
| `questions.[].$oid` | `string` | JSON path |
| `agendaid.$oid` | `string` | JSON path |
