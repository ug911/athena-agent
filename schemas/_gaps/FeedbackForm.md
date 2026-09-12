---
collection: "FeedbackForm"
athena_table: "wise_app_backend__feedback_form"
mongo_field_count: 9
athena_field_count: 24
matched: 9
coverage_pct: 100.0
last_diffed: "2026-09-08T08:05:41+00:00"
---

# Schema gap: `FeedbackForm` ↔ `processed.wise_app_backend__feedback_form`

- **Mongo source**: [`src/models/FeedbackForm.js`](../source/mongo/FeedbackForm.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__feedback_form.md`](../processed/processed/wise_app_backend__feedback_form.md)
- **Coverage**: 9/9 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `instituteid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `questions.[]` | `object` | JSON path |
| `questions.[]._id` | `object` | JSON path |
| `questions.[]._id.$oid` | `string` | JSON path |
| `questions.[].options.<int>` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
