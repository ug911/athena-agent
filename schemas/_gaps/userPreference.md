---
collection: "userPreference"
athena_table: "wise_app_backend__userpreference"
mongo_field_count: 5
athena_field_count: 12
matched: 2
coverage_pct: 40.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `userPreference` ↔ `processed.wise_app_backend__userpreference`

- **Mongo source**: [`src/models/userPreference.js`](../source/mongo/userPreference.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__userpreference.md`](../processed/processed/wise_app_backend__userpreference.md)
- **Coverage**: 2/5 Mongo fields are present in Athena (**40.0%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `posts[]` | `<postsSchema>` |  |  |
| `posts[].entityId` | `String` |  | required |
| `posts[].entityType` | `String` |  | required |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `registration.testing_module` | `object` | JSON path |
| `registration.testing_module.registered` | `bool` | JSON path |
| `registration.testing_module.registeredat` | `object` | JSON path |
| `registration.testing_module.registeredat.$date` | `object` | JSON path |
| `registration.testing_module.registeredat.$date.$numberlong` | `string` | JSON path |
