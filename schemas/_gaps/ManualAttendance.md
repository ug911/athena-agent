---
collection: "ManualAttendance"
athena_table: "wise_app_backend__manualattendance"
mongo_field_count: 11
athena_field_count: 26
matched: 11
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `ManualAttendance` ↔ `processed.wise_app_backend__manualattendance`

- **Mongo source**: [`src/models/ManualAttendance.js`](../source/mongo/ManualAttendance.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__manualattendance.md`](../processed/processed/wise_app_backend__manualattendance.md)
- **Coverage**: 11/11 Mongo fields are present in Athena (**100.0%**).

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
| `participants.[]` | `object` | JSON path |
| `participants.[].firstentrytime.$date` | `object` | JSON path |
| `participants.[].firstentrytime.$date.$numberlong` | `string` | JSON path |
| `participants.[].lastexittime.$date` | `object` | JSON path |
| `participants.[].lastexittime.$date.$numberlong` | `string` | JSON path |
| `participants.[].userid.$oid` | `string` | JSON path |
