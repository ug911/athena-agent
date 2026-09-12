---
collection: "RegistrationForm"
athena_table: "wise_app_backend__registration_form"
mongo_field_count: 7
athena_field_count: 36
matched: 6
coverage_pct: 85.7
last_diffed: "2026-09-08T08:05:41+00:00"
---

# Schema gap: `RegistrationForm` ↔ `processed.wise_app_backend__registration_form`

- **Mongo source**: [`src/models/RegistrationForm.js`](../source/mongo/RegistrationForm.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__registration_form.md`](../processed/processed/wise_app_backend__registration_form.md)
- **Coverage**: 6/7 Mongo fields are present in Athena (**85.7%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `classId` | `ObjectId` | `class` |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `instituteid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `fields.[]` | `object` | JSON path |
| `fields.[].options` | `object` | JSON path |
| `fields.[].options.1` | `string` | JSON path |
| `fields.[].options.2` | `string` | JSON path |
| `fields.[].options.3` | `string` | JSON path |
| `fields.[].options.4` | `string` | JSON path |
| `fields.[].options.5` | `string` | JSON path |
| `fields.[].options.6` | `string` | JSON path |
| `fields.[].options.7` | `string` | JSON path |
| `fields.[].options.a` | `string` | JSON path |
| `fields.[].options.b` | `string` | JSON path |
| `fields.[].options.c` | `string` | JSON path |
| `fields.[].options.d` | `string` | JSON path |
| `fields.[].options.e` | `string` | JSON path |
| `fields.[].questionid` | `string` | JSON path |
| `fields.[].questiontext` | `string` | JSON path |
| `fields.[].required` | `bool` | JSON path |
| `fields.[].type` | `string` | JSON path |
| `settings.required` | `bool` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
