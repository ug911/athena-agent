---
collection: "SessionCredit"
athena_table: "wise_app_backend__session_credit"
mongo_field_count: 8
athena_field_count: 21
matched: 6
coverage_pct: 75.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `SessionCredit` ↔ `processed.wise_app_backend__session_credit`

- **Mongo source**: [`src/models/SessionCredit.js`](../source/mongo/SessionCredit.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__session_credit.md`](../processed/processed/wise_app_backend__session_credit.md)
- **Coverage**: 6/8 Mongo fields are present in Athena (**75.0%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `Institute` |  |
| `metadata` | `<inline-schema>` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `credit.$numberdouble` | `string` | JSON path |
| `credit.$numberint` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `assignedby.$oid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
