---
collection: "RegistrationFormSubmission"
athena_table: "wise_app_backend__registration_form_submission"
mongo_field_count: 6
athena_field_count: 19
matched: 4
coverage_pct: 66.7
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `RegistrationFormSubmission` ↔ `processed.wise_app_backend__registration_form_submission`

- **Mongo source**: [`src/models/RegistrationFormSubmission.js`](../source/mongo/RegistrationFormSubmission.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__registration_form_submission.md`](../processed/processed/wise_app_backend__registration_form_submission.md)
- **Coverage**: 4/6 Mongo fields are present in Athena (**66.7%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `classId` | `ObjectId` | `class` |  |
| `sessionId` | `ObjectId` | `zoom` |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `instituteid.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `answers.[]` | `object` | JSON path |
| `answers.[].answer` | `string` | JSON path |
| `answers.[].questionid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
