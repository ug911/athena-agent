---
collection: "study materials"
athena_table: "wise_app_backend__study_materials"
mongo_field_count: 25
athena_field_count: 64
matched: 18
coverage_pct: 72.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `study materials` ↔ `processed.wise_app_backend__study_materials`

- **Mongo source**: [`src/models/Resource.js`](../source/mongo/study_materials.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__study_materials.md`](../processed/processed/wise_app_backend__study_materials.md)
- **Coverage**: 18/25 Mongo fields are present in Athena (**72.0%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `resources[].link` | `String` |  |  |
| `resources[].metadata` | `Object` |  |  |
| `link` | `String` |  |  |
| `disableCommenting` | `Boolean` |  |  |
| `public` | `Boolean` |  |  |
| `thumbnail` | `String` |  |  |
| `metadata` | `Object` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `attachments` | `string` | column |
| `_id.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `resources.[]` | `object` | JSON path |
| `resources.[]._id` | `object` | JSON path |
| `resources.[]._id.$oid` | `string` | JSON path |
| `resources.[].createdat.$date` | `object` | JSON path |
| `resources.[].createdat.$date.$numberlong` | `string` | JSON path |
| `resources.[].date` | `string` | JSON path |
| `resources.[].file._id` | `object` | JSON path |
| `resources.[].file._id.$oid` | `string` | JSON path |
| `resources.[].file.filename` | `string` | JSON path |
| `resources.[].file.path` | `string` | JSON path |
| `resources.[].file.s3filepath` | `string` | JSON path |
| `resources.[].file.s3key` | `string` | JSON path |
| `resources.[].file.size` | `object` | JSON path |
| `resources.[].file.size.$numberint` | `string` | JSON path |
| `resources.[].time` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `attachments.[]` | `object` | JSON path |
| `attachments.[]._id` | `object` | JSON path |
| `attachments.[]._id.$oid` | `string` | JSON path |
| `attachments.[].filename` | `string` | JSON path |
| `attachments.[].path` | `string` | JSON path |
| `attachments.[].s3filepath` | `string` | JSON path |
| `attachments.[].s3key` | `string` | JSON path |
| `attachments.[].size` | `object` | JSON path |
| `attachments.[].size.$numberint` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `file._id` | `object` | JSON path |
| `file._id.$oid` | `string` | JSON path |
| `file.filename` | `string` | JSON path |
| `file.path` | `string` | JSON path |
| `file.s3filepath` | `string` | JSON path |
| `file.s3key` | `string` | JSON path |
| `file.size` | `object` | JSON path |
| `file.size.$numberint` | `string` | JSON path |
| `file.videoindexurl` | `string` | JSON path |
