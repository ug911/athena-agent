---
collection: "RawRecording"
athena_table: "wise_app_backend__raw_recording"
mongo_field_count: 8
athena_field_count: 24
matched: 7
coverage_pct: 87.5
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `RawRecording` ↔ `processed.wise_app_backend__raw_recording`

- **Mongo source**: [`src/models/RawRecording.js`](../source/mongo/RawRecording.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__raw_recording.md`](../processed/processed/wise_app_backend__raw_recording.md)
- **Coverage**: 7/8 Mongo fields are present in Athena (**87.5%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `expiresIn` | `Date` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `sessionid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `recordings.[]` | `object` | JSON path |
| `recordings.[]._id` | `object` | JSON path |
| `recordings.[]._id.$oid` | `string` | JSON path |
| `recordings.[].duration.$numberint` | `string` | JSON path |
| `recordings.[].partindex.$numberint` | `string` | JSON path |
| `recordings.[].sessionindex.$numberint` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
