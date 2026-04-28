---
collection: "InstituteGroup"
athena_table: "wise_app_backend__institutegroup"
mongo_field_count: 3
athena_field_count: 12
matched: 3
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `InstituteGroup` ↔ `processed.wise_app_backend__institutegroup`

- **Mongo source**: [`src/models/InstituteGroup.js`](../source/mongo/InstituteGroup.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__institutegroup.md`](../processed/processed/wise_app_backend__institutegroup.md)
- **Coverage**: 3/3 Mongo fields are present in Athena (**100.0%**).

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
