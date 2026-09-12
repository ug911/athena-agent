---
canonical: processed
table: wise_app_backend__raw_zoom_attendance
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/RawZoomAttendance/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:27:08+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__raw_zoom_attendance`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |
| `NA` | `processed_na` |

_Schema parity: **identical** across regions._

## Columns (IN)

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

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6a530b0dc43c79e7be5760c8`, `6a530b91c43c79e7be57abcf`, `6a530b93c43c79e7be57acb1`

### `participants`

  - `[]` — `object`
    - `_id` — `string`  e.g. `6a1576f5ef3a8423b0bc2443`, `67d81e4a1212d98ff5967d1c`, `68344bcdb213e9ac49975e85`
    - `attentiveness_score` — `string`
    - `customer_key` — `string`  e.g. `NA|U_68344bcdb213e9ac49975e85`, `NA|Z_69902aad24f94ab33fb636fd`, `NA|U_65d868629981243ddd1f5626`
    - `duration` — `object`
      - `$numberint` — `string`  e.g. `2020`, `2158`, `1546`
    - `failover` — `bool`  e.g. `false`, `false`, `false`
    - `groupid` — `string`  e.g. `voZoXlrPR56iDoyS5LfH9A`, `voZoXlrPR56iDoyS5LfH9A`, `voZoXlrPR56iDoyS5LfH9A`
    - `id` — `string`  e.g. `RPzbceAyTUahTKzfpt0duQ`, `qGHpGberQqexbg6iMPlkNQ`, `oMDOc0j2RjWC_bkLWjyZgw`
    - `inmeetingduration` — `object`
      - `$numberint` — `string`  e.g. `2020`, `2158`, `1546`
    - `join_time` — `string`  e.g. `2026-07-12T02:33:16Z`, `2026-07-12T02:52:29Z`, `2026-07-12T03:02:41Z`
    - `leave_time` — `string`  e.g. `2026-07-12T03:06:56Z`, `2026-07-12T03:28:27Z`, `2026-07-12T03:28:27Z`
    - `name` — `string`  e.g. `[REDACTED]`
    - `participant_user_id` — `string`  e.g. `RPzbceAyTUahTKzfpt0duQ`, `qGHpGberQqexbg6iMPlkNQ`, `oMDOc0j2RjWC_bkLWjyZgw`
    - `status` — `string`  e.g. `in_meeting`, `in_meeting`, `in_meeting`
    - `user_email` — `string`  e.g. `[REDACTED]`
    - `user_id` — `string`  e.g. `16778240`, `16795648`, `16796672`

### `sessionid`

- `$oid` — `string`  e.g. `6a52fce18992102b2abe9c2f`, `6a52edb89931b85c92b374c4`, `6a5298588992102b2ab72b39`

### `classid`

- `$oid` — `string`  e.g. `6a392f44bcf77fe1a3da6170`, `69f46f18eb43931953cd07ba`, `69902b2b444ac4ea90c8f9a8`

### `totalrecords`

- `$numberint` — `string`  e.g. `4`, `14`, `2`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1783827213512`, `1783827345428`, `1783827347371`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1783827213512`, `1783827345428`, `1783827347371`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_012830_00178_7sy8r', 
  'trino_version'='0.215-24619-g93e00a8')
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
