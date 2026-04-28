---
collection: "SessionFeedbackSubmission"
athena_table: "wise_app_backend__session_feedback_submission"
mongo_field_count: 16
athena_field_count: 36
matched: 15
coverage_pct: 93.8
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `SessionFeedbackSubmission` ↔ `processed.wise_app_backend__session_feedback_submission`

- **Mongo source**: [`src/models/SessionFeedbackSubmission.js`](../source/mongo/SessionFeedbackSubmission.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__session_feedback_submission.md`](../processed/processed/wise_app_backend__session_feedback_submission.md)
- **Coverage**: 15/16 Mongo fields are present in Athena (**93.8%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `unauthUserId` | `String` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `sessionid.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `answers.[]` | `object` | JSON path |
| `answers.[]._id` | `object` | JSON path |
| `answers.[]._id.$oid` | `string` | JSON path |
| `answers.[].options.<int>` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `rating.$numberint` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `metadata.autosubmitted` | `bool` | JSON path |
| `creditsconsumed.$numberdouble` | `string` | JSON path |
| `creditsconsumed.$numberint` | `string` | JSON path |
