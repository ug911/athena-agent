---
collection: "SessionFeedbackSubmission"
athena_table: "wise_app_backend__session_feedback_submission"
mongo_field_count: 16
athena_field_count: 26
matched: 11
coverage_pct: 68.8
last_diffed: "2026-09-08T08:05:41+00:00"
---

# Schema gap: `SessionFeedbackSubmission` ↔ `processed.wise_app_backend__session_feedback_submission`

- **Mongo source**: [`src/models/SessionFeedbackSubmission.js`](../source/mongo/SessionFeedbackSubmission.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__session_feedback_submission.md`](../processed/processed/wise_app_backend__session_feedback_submission.md)
- **Coverage**: 11/16 Mongo fields are present in Athena (**68.8%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `unauthUserId` | `String` |  |  |
| `answers[].questionText` | `String` |  |  |
| `answers[].type` | `String` |  | required |
| `answers[].options` | `Object` |  |  |
| `answers[].answer` | `String` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `sessionid.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `rating.$numberint` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `metadata.unauthusername` | `string` | JSON path |
