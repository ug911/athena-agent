---
collection: "DeletedFile"
athena_table: "wise_app_backend__deleted_file"
mongo_field_count: 10
athena_field_count: 22
matched: 3
coverage_pct: 30.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `DeletedFile` ↔ `processed.wise_app_backend__deleted_file`

- **Mongo source**: [`src/models/DeletedFile.js`](../source/mongo/DeletedFile.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__deleted_file.md`](../processed/processed/wise_app_backend__deleted_file.md)
- **Coverage**: 3/10 Mongo fields are present in Athena (**30.0%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `failed` | `Boolean` |  |  |
| `error` | `String` |  |  |
| `skippedDeletion` | `Boolean` |  |  |
| `classId` | `ObjectId` | `class` |  |
| `entityId` | `ObjectId` |  |  |
| `deletedAt` | `Date` |  |  |
| `skipValidation` | `Boolean` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `file._id` | `object` | JSON path |
| `file._id.$oid` | `string` | JSON path |
| `file.filename` | `string` | JSON path |
| `file.path` | `string` | JSON path |
| `file.s3filepath` | `string` | JSON path |
| `file.s3key` | `string` | JSON path |
| `file.size` | `object` | JSON path |
| `file.size.$numberint` | `string` | JSON path |
| `file.type` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
