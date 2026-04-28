---
collection: "feeStructure"
athena_table: "wise_app_backend__feestructure"
mongo_field_count: 7
athena_field_count: 26
matched: 7
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `feeStructure` ↔ `processed.wise_app_backend__feestructure`

- **Mongo source**: [`src/models/FeeStructure.js`](../source/mongo/feeStructure.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__feestructure.md`](../processed/processed/wise_app_backend__feestructure.md)
- **Coverage**: 7/7 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `amount.currency` | `string` | JSON path |
| `amount.value` | `object` | JSON path |
| `amount.value.$numberint` | `string` | JSON path |
| `startdate.$date` | `object` | JSON path |
| `startdate.$date.$numberlong` | `string` | JSON path |
| `enddate.$date` | `object` | JSON path |
| `enddate.$date.$numberlong` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
