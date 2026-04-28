---
collection: "assignments"
athena_table: "wise_app_backend__assignments"
mongo_field_count: 45
athena_field_count: 97
matched: 32
coverage_pct: 71.1
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `assignments` ↔ `processed.wise_app_backend__assignments`

- **Mongo source**: [`src/models/Assessment.js`](../source/mongo/assignments.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__assignments.md`](../processed/processed/wise_app_backend__assignments.md)
- **Coverage**: 32/45 Mongo fields are present in Athena (**71.1%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `criteria[].title` | `String` |  | required |
| `submission[].textAnswer` | `String` |  |  |
| `submission[].criteriaFeedback[]` | `<criteriaFeedbackSchema>` |  |  |
| `submission[].criteriaFeedback[].criteriaId` | `ObjectId` |  | required |
| `submission[].criteriaFeedback[].marks` | `Number` |  | required |
| `submission[].submissionFile` | `<googleDocFileSchema>` |  |  |
| `submission[].submissionFile.fileId` | `String` |  | required |
| `submission[].submissionFile.name` | `String` |  | required |
| `lastCommentedAt` | `Date` |  |  |
| `pending` | `Boolean` |  |  |
| `googleDocFile` | `<googleDocFileSchema>` |  |  |
| `googleDocFile.fileId` | `String` |  | required |
| `googleDocFile.name` | `String` |  | required |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `maxmarks.$numberint` | `string` | JSON path |
| `attachments.[]` | `object` | JSON path |
| `attachments.[]._id` | `object` | JSON path |
| `attachments.[]._id.$oid` | `string` | JSON path |
| `attachments.[].filename` | `string` | JSON path |
| `attachments.[].path` | `string` | JSON path |
| `attachments.[].s3filepath` | `string` | JSON path |
| `attachments.[].s3key` | `string` | JSON path |
| `attachments.[].size` | `object` | JSON path |
| `attachments.[].size.$numberint` | `string` | JSON path |
| `attachments.[].type` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `solutions.[]` | `object` | JSON path |
| `solutions.[]._id` | `object` | JSON path |
| `solutions.[]._id.$oid` | `string` | JSON path |
| `solutions.[].attachments.[].attachments[]._id` | `object` | JSON path |
| `solutions.[].attachments.[].attachments[]._id.$oid` | `string` | JSON path |
| `solutions.[].attachments.[].attachments[].filename` | `string` | JSON path |
| `solutions.[].attachments.[].attachments[].path` | `string` | JSON path |
| `solutions.[].attachments.[].attachments[].s3filepath` | `string` | JSON path |
| `solutions.[].attachments.[].attachments[].s3key` | `string` | JSON path |
| `solutions.[].attachments.[].attachments[].size` | `object` | JSON path |
| `solutions.[].attachments.[].attachments[].size.$numberint` | `string` | JSON path |
| `solutions.[].attachments.[].attachments[].type` | `string` | JSON path |
| `solutions.[].studentid.$oid` | `string` | JSON path |
| `submission.[]` | `object` | JSON path |
| `submission.[]._id` | `object` | JSON path |
| `submission.[]._id.$oid` | `string` | JSON path |
| `submission.[].attachments.[].attachments[]._id` | `object` | JSON path |
| `submission.[].attachments.[].attachments[]._id.$oid` | `string` | JSON path |
| `submission.[].attachments.[].attachments[].filename` | `string` | JSON path |
| `submission.[].attachments.[].attachments[].path` | `string` | JSON path |
| `submission.[].attachments.[].attachments[].s3filepath` | `string` | JSON path |
| `submission.[].attachments.[].attachments[].s3key` | `string` | JSON path |
| `submission.[].attachments.[].attachments[].size` | `object` | JSON path |
| `submission.[].attachments.[].attachments[].size.$numberint` | `string` | JSON path |
| `submission.[].attachments.[].attachments[].type` | `string` | JSON path |
| `submission.[].createdat.$date` | `object` | JSON path |
| `submission.[].createdat.$date.$numberlong` | `string` | JSON path |
| `submission.[].feedbackrecordings.[].feedbackrecordings[]._id` | `object` | JSON path |
| `submission.[].feedbackrecordings.[].feedbackrecordings[]._id.$oid` | `string` | JSON path |
| `submission.[].feedbackrecordings.[].feedbackrecordings[].filename` | `string` | JSON path |
| `submission.[].feedbackrecordings.[].feedbackrecordings[].path` | `string` | JSON path |
| `submission.[].feedbackrecordings.[].feedbackrecordings[].s3filepath` | `string` | JSON path |
| `submission.[].feedbackrecordings.[].feedbackrecordings[].s3key` | `string` | JSON path |
| `submission.[].feedbackrecordings.[].feedbackrecordings[].size` | `object` | JSON path |
| `submission.[].feedbackrecordings.[].feedbackrecordings[].size.$numberint` | `string` | JSON path |
| `submission.[].feedbackrecordings.[].feedbackrecordings[].type` | `string` | JSON path |
| `submission.[].getmark.$numberint` | `string` | JSON path |
| `submission.[].gradedat.$date` | `object` | JSON path |
| `submission.[].gradedat.$date.$numberlong` | `string` | JSON path |
| `submission.[].studentid.$oid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `submitby.$date` | `object` | JSON path |
| `submitby.$date.$numberlong` | `string` | JSON path |
| `starttime.$date` | `object` | JSON path |
| `starttime.$date.$numberlong` | `string` | JSON path |
