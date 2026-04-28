---
collection: "RawZoomAttendance"
athena_table: "wise_app_backend__raw_zoom_attendance"
mongo_field_count: 6
athena_field_count: 37
matched: 6
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `RawZoomAttendance` ↔ `processed.wise_app_backend__raw_zoom_attendance`

- **Mongo source**: [`src/models/RawZoomAttendance.js`](../source/mongo/RawZoomAttendance.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__raw_zoom_attendance.md`](../processed/processed/wise_app_backend__raw_zoom_attendance.md)
- **Coverage**: 6/6 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `participants.[]` | `object` | JSON path |
| `participants.[]._id` | `string` | JSON path |
| `participants.[].attentiveness_score` | `string` | JSON path |
| `participants.[].customer_key` | `string` | JSON path |
| `participants.[].duration` | `object` | JSON path |
| `participants.[].duration.$numberint` | `string` | JSON path |
| `participants.[].failover` | `bool` | JSON path |
| `participants.[].groupid` | `string` | JSON path |
| `participants.[].inmeetingduration` | `object` | JSON path |
| `participants.[].inmeetingduration.$numberint` | `string` | JSON path |
| `participants.[].join_time` | `string` | JSON path |
| `participants.[].leave_time` | `string` | JSON path |
| `participants.[].name` | `string` | JSON path |
| `participants.[].participant_user_id` | `string` | JSON path |
| `participants.[].status` | `string` | JSON path |
| `participants.[].user_email` | `string` | JSON path |
| `participants.[].user_id` | `string` | JSON path |
| `sessionid.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `totalrecords.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
