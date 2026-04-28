---
collection: "EntityInteraction"
athena_table: "wise_app_backend__entity_interaction"
mongo_field_count: 9
athena_field_count: 23
matched: 7
coverage_pct: 77.8
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `EntityInteraction` ↔ `processed.wise_app_backend__entity_interaction`

- **Mongo source**: [`src/models/EntityInteraction.js`](../source/mongo/EntityInteraction.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__entity_interaction.md`](../processed/processed/wise_app_backend__entity_interaction.md)
- **Coverage**: 7/9 Mongo fields are present in Athena (**77.8%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `markedCovered` | `Boolean` |  |  |
| `metadata` | `Object` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `entityid.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `views.$numberint` | `string` | JSON path |
| `markedcompletedon.$date` | `object` | JSON path |
| `markedcompletedon.$date.$numberlong` | `string` | JSON path |
