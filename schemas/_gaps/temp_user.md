---
collection: "temp_user"
athena_table: "wise_app_backend__temp_user"
mongo_field_count: 3
athena_field_count: 6
matched: 0
coverage_pct: 0.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `temp_user` ↔ `processed.wise_app_backend__temp_user`

- **Mongo source**: [`src/models/TempUser.js`](../source/mongo/temp_user.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__temp_user.md`](../processed/processed/wise_app_backend__temp_user.md)
- **Coverage**: 0/3 Mongo fields are present in Athena (**0.0%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `identifier` | `String` |  | required |
| `idType` | `String` |  | required |
| `metadata` | `Object` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `phonenumber` | `string` | column |
| `_id.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
