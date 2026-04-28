---
collection: "Entity"
athena_table: "wise_app_backend__entity"
mongo_field_count: 9
athena_field_count: 18
matched: 8
coverage_pct: 88.9
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `Entity` ↔ `processed.wise_app_backend__entity`

- **Mongo source**: [`src/models/Entity.js`](../source/mongo/Entity.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__entity.md`](../processed/processed/wise_app_backend__entity.md)
- **Coverage**: 8/9 Mongo fields are present in Athena (**88.9%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `entitySecondaryId` | `String` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `entityid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `sortkey.$date` | `object` | JSON path |
| `sortkey.$date.$numberlong` | `string` | JSON path |
