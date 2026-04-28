---
collection: "RawSessionTranscript"
athena_table: "wise_app_backend__rawsessiontranscript"
mongo_field_count: 7
athena_field_count: 28
matched: 7
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `RawSessionTranscript` ↔ `processed.wise_app_backend__rawsessiontranscript`

- **Mongo source**: [`src/models/RawSessionTranscript.js`](../source/mongo/RawSessionTranscript.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__rawsessiontranscript.md`](../processed/processed/wise_app_backend__rawsessiontranscript.md)
- **Coverage**: 7/7 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `sessionid.$oid` | `string` | JSON path |
| `files.[]` | `object` | JSON path |
| `files.[]._id` | `object` | JSON path |
| `files.[]._id.$oid` | `string` | JSON path |
| `files.[].file._id` | `object` | JSON path |
| `files.[].file._id.$oid` | `string` | JSON path |
| `files.[].file.filename` | `string` | JSON path |
| `files.[].file.path` | `string` | JSON path |
| `files.[].file.s3filepath` | `string` | JSON path |
| `files.[].file.s3key` | `string` | JSON path |
| `files.[].file.type` | `string` | JSON path |
| `files.[].partindex.$numberint` | `string` | JSON path |
| `files.[].sessionindex.$numberint` | `string` | JSON path |
