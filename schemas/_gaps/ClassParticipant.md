---
collection: "ClassParticipant"
athena_table: "wise_app_backend__classparticipant"
mongo_field_count: 10
athena_field_count: 19
matched: 5
coverage_pct: 50.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `ClassParticipant` ↔ `processed.wise_app_backend__classparticipant`

- **Mongo source**: [`src/models/ClassParticipant.js`](../source/mongo/ClassParticipant.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__classparticipant.md`](../processed/processed/wise_app_backend__classparticipant.md)
- **Coverage**: 5/10 Mongo fields are present in Athena (**50.0%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `metadata` | `<metadataSchema>` |  |  |
| `metadata.paymentOptionId` | `String` |  |  |
| `metadata.settleDues` | `Boolean` |  |  |
| `metadata.feesWaived` | `Boolean` |  |  |
| `metadata.payoutSettings` | `String` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `joinedon.$date` | `object` | JSON path |
| `joinedon.$date.$numberlong` | `string` | JSON path |
