---
collection: "Lead"
athena_table: "wise_app_backend__lead"
mongo_field_count: 5
athena_field_count: 16
matched: 5
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `Lead` ↔ `processed.wise_app_backend__lead`

- **Mongo source**: [`src/models/Lead.js`](../source/mongo/Lead.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__lead.md`](../processed/processed/wise_app_backend__lead.md)
- **Coverage**: 5/5 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
