---
collection: "ClassroomPublicProfile"
athena_table: "wise_app_backend__classroom_public_profile"
mongo_field_count: 9
athena_field_count: 19
matched: 5
coverage_pct: 55.6
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `ClassroomPublicProfile` ↔ `processed.wise_app_backend__classroom_public_profile`

- **Mongo source**: [`src/models/ClassroomPublicProfile.js`](../source/mongo/ClassroomPublicProfile.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__classroom_public_profile.md`](../processed/processed/wise_app_backend__classroom_public_profile.md)
- **Coverage**: 5/9 Mongo fields are present in Athena (**55.6%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `highlights` | `<highlightsSchema>` |  |  |
| `highlights.points` | `Array<String>` |  |  |
| `public` | `Boolean` |  |  |
| `reviews` | `Array<reviewSchema>` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `classcovers` | `string` | column |
| `_id.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `classcovers.[]` | `object` | JSON path |
| `classcovers.[].link` | `string` | JSON path |
| `classcovers.[].type` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
