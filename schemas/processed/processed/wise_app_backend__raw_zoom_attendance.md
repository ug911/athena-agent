---
database: processed
table: wise_app_backend__raw_zoom_attendance
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/RawZoomAttendance/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:16:43+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__raw_zoom_attendance`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `participants` | `string` |  |
| `sessionid` | `string` |  |
| `classid` | `string` |  |
| `meetingid` | `string` |  |
| `meetinguuid` | `string` |  |
| `totalrecords` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `69c8b66f59c459d1a1c7aab6`, `69c8b6ae59c459d1a1c7f27e`, `69c8b6ca59c459d1a1c8119e`

### `participants`

  - `[]` — `object`
    - `_id` — `string`  e.g. `6532b01fbd119009e0f09d72`, `67c2ec94f6b7db0bcc7328c9`, `67c2ec94f6b7db0bcc7328c9`
    - `attentiveness_score` — `string`
    - `customer_key` — `string`  e.g. `NA|Z_69b635d524bc16482270b0f0`, `NA|Z_69b635d524bc16482270b0f0`, `NA|Z_69b635d524bc16482270b0f0`
    - `duration` — `object`
      - `$numberint` — `string`  e.g. `2656`, `19`, `2302`
    - `failover` — `bool`  e.g. `false`, `false`, `false`
    - `groupid` — `string`  e.g. `voZoXlrPR56iDoyS5LfH9A`, `voZoXlrPR56iDoyS5LfH9A`, `voZoXlrPR56iDoyS5LfH9A`
    - `id` — `string`  e.g. `0HzAt-voTTierJIXbn9DbA`, `NbqQkb-CRIu_i5Jyo1IaKw`, `1ldrAH7hQqiDdwPPJ-59OA`
    - `inmeetingduration` — `object`
      - `$numberint` — `string`  e.g. `2656`, `0`, `2302`
    - `join_time` — `string`  e.g. `2026-03-29T04:30:23Z`, `2026-03-29T04:35:57Z`, `2026-03-29T04:36:16Z`
    - `leave_time` — `string`  e.g. `2026-03-29T05:14:39Z`, `2026-03-29T04:36:16Z`, `2026-03-29T05:14:38Z`
    - `name` — `string`  e.g. `[REDACTED]`
    - `participant_user_id` — `string`  e.g. `0HzAt-voTTierJIXbn9DbA`, `NbqQkb-CRIu_i5Jyo1IaKw`, `1ldrAH7hQqiDdwPPJ-59OA`
    - `status` — `string`  e.g. `in_meeting`, `in_waiting_room`, `in_meeting`
    - `user_email` — `string`  e.g. `[REDACTED]`
    - `user_id` — `string`  e.g. `16778240`, `16794624`, `16795648`

### `sessionid`

- `$oid` — `string`  e.g. `69c8aadb311095a2a4073a49`, `69c8a8914480a9e27245016b`, `69c035ac7dcca283bdbca6fb`

### `classid`

- `$oid` — `string`  e.g. `68f44db787df59118428b39e`, `687c6aae85ec6c4d6cca123f`, `69589b3d890dacdc0e34787b`

### `totalrecords`

- `$numberint` — `string`  e.g. `3`, `5`, `9`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1774761583439`, `1774761646864`, `1774761674775`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1774761583439`, `1774761646864`, `1774761674775`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__raw_zoom_attendance`(
  `_id` string, 
  `participants` string, 
  `sessionid` string, 
  `classid` string, 
  `meetingid` string, 
  `meetinguuid` string, 
  `totalrecords` string, 
  `createdat` string, 
  `updatedat` string, 
  `__v` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/RawZoomAttendance/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_011646_00196_np4ns', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->

## Notes

- **Source-of-truth for per-participant join/leave segments.** Each row's `participants[]` carries multiple entries per attendee — one per rejoin. `wise_app_backend__zoom.participants[]` is built by aggregating these into a single `firstentrytime` / `lastexittime` window per attendee.
- **Use this table when**: you need true live-concurrency that accounts for rejoin gaps, per-segment durations, or join/leave event timing. Use `wise_app_backend__zoom.participants[]` (or `zoom_attendance`) when collapsed-window or session-summary stats are sufficient.
- **Time encoding gotcha.** `participants[].join_time` and `leave_time` are **ISO strings** (e.g. `'2026-03-28T01:30:42Z'`) — *not* the `$date.$numberlong` epoch-millis encoding used elsewhere in this dataset. Parse with `from_iso8601_timestamp(...)`.
- **Joins**:
  - `sessionid.$oid = wise_app_backend__zoom._id.$oid` (one zoom session → potentially many raw_zoom_attendance rows; `totalrecords` indicates segment count).
  - `classid.$oid = class.class_id`.
  - `participants[]._id` is the Wise user id (`user.userid`). `user_id` (no underscore prefix) is the Zoom-internal id, not the Wise user id.
- **No `isteacher` flag here.** That distinction is added when aggregating into `zoom.participants[]`. If you need to split students vs teachers from raw segments, join `participants[]._id` to `class.userid` / `class.coteachers` / `class.admins`, or pull `isteacher` from the aggregated `zoom.participants[]` for the same `(sessionid, participant_userid)`.
