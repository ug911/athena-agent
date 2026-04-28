---
collection: "TeacherLeave"
athena_table: "wise_app_backend__teacher_leave"
mongo_field_count: 6
athena_field_count: 22
matched: 6
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `TeacherLeave` ↔ `processed.wise_app_backend__teacher_leave`

- **Mongo source**: [`src/models/TeacherLeave.js`](../source/mongo/TeacherLeave.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__teacher_leave.md`](../processed/processed/wise_app_backend__teacher_leave.md)
- **Coverage**: 6/6 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `instituteid.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `starttime.$date` | `object` | JSON path |
| `starttime.$date.$numberlong` | `string` | JSON path |
| `endtime.$date` | `object` | JSON path |
| `endtime.$date.$numberlong` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
