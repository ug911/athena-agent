---
collection: "ClassroomSection"
athena_table: "wise_app_backend__classroom_section"
mongo_field_count: 12
athena_field_count: 20
matched: 6
coverage_pct: 50.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `ClassroomSection` ↔ `processed.wise_app_backend__classroom_section`

- **Mongo source**: [`src/models/ClassroomSection.js`](../source/mongo/ClassroomSection.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__classroom_section.md`](../processed/processed/wise_app_backend__classroom_section.md)
- **Coverage**: 6/12 Mongo fields are present in Athena (**50.0%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `entities[].public` | `Boolean` |  |  |
| `dripSettings` | `<dripSettingSchema>` |  |  |
| `dripSettings.enableDaysAfter` | `Number` |  |  |
| `dripSettings.enableOn` | `Date` |  |  |
| `sequentialLearning` | `Boolean` |  |  |
| `other` | `Boolean` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `sortkey.$numberint` | `string` | JSON path |
| `entities.[]` | `object` | JSON path |
| `entities.[].entityid.$oid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
