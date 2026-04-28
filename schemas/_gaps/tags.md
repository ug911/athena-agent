---
collection: "tags"
athena_table: "wise_app_backend__tags"
mongo_field_count: 3
athena_field_count: 5
matched: 3
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `tags` ↔ `processed.wise_app_backend__tags`

- **Mongo source**: [`src/models/tags.js`](../source/mongo/tags.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__tags.md`](../processed/processed/wise_app_backend__tags.md)
- **Coverage**: 3/3 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
