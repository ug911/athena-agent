---
canonical: processed
table: zoom_attendance
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/zoom_attendance/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:31:33+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.zoom_attendance`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |
| `NA` | `processed_na` |

_Schema parity: **identical** across regions._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `class_id` | `string` |  |
| `class_name` | `string` |  |
| `subject` | `string` |  |
| `num_ct` | `bigint` |  |
| `ct_live` | `string` |  |
| `isownerzoom` | `string` |  |
| `ownerid` | `string` |  |
| `zoom_id` | `string` |  |
| `start_time` | `timestamp` |  |
| `end_time` | `timestamp` |  |
| `type` | `string` |  |
| `meetingstatus` | `string` |  |
| `duration` | `int` |  |
| `participant` | `int` |  |
| `student_id` | `string` |  |
| `student_name_zoom` | `string` |  |
| `student_isteacher` | `string` |  |
| `student_attendance` | `string` |  |
| `student_attendance_abs` | `string` |  |
| `student_duration` | `string` |  |
| `ct_name` | `string` |  |
| `ct_phone` | `string` |  |
| `ct_email` | `string` |  |
| `student_name` | `string` |  |
| `student_phone` | `string` |  |
| `student_email` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `class_id`: `60cfee44bef839e09882e6c3 (×200)`
- `class_name`: `Chaitanya Charitamrita:Shlokas (×200)`
- `subject`: `Shlokas  (×200)`
- `ct_live`: `60c6fcee0e0c3a0019fac4e2 (×200)`
- `isownerzoom`: `false (×170)`
- `ownerid`: `60c6fcee0e0c3a0019fac4e2 (×200)`
- `zoom_id`: `639bf1d35391852c3c07a21b (×30)`, `68eb7f2ae846e7654dfe6e14 (×24)`, `65ac9a2897479c4687d40564 (×21)`, `64bcc33d01212cb8e82557bb (×20)`, `67a6da9b74d677bd2e242cfd (×19)`, `6a7954176c6974f85252779e (×18)`, `656c00f9972f09ffe48be2be (×17)`, `67e8c8c6e072810b511f16ba (×13)`, `65da984877a03ca4e542b100 (×11)`, `6a40a35c885f3c6a39e151c9 (×11)`, `65f4f6d8ee96c076c7904522 (×8)`, `6896f25c47d3846f4ccf1d05 (×5)`, `65fce1097d5e5eead1879919 (×3)`
- `type`: `AD_HOC (×200)`
- `meetingstatus`: `ENDED (×200)`
- `student_isteacher`: `false (×29)`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.zoom_attendance`(
  `class_id` string, 
  `class_name` string, 
  `subject` string, 
  `num_ct` bigint, 
  `ct_live` string, 
  `isownerzoom` string, 
  `ownerid` string, 
  `zoom_id` string, 
  `start_time` timestamp, 
  `end_time` timestamp, 
  `type` string, 
  `meetingstatus` string, 
  `duration` int, 
  `participant` int, 
  `student_id` string, 
  `student_name_zoom` string, 
  `student_isteacher` string, 
  `student_attendance` string, 
  `student_attendance_abs` string, 
  `student_duration` string, 
  `ct_name` string, 
  `ct_phone` string, 
  `ct_email` string, 
  `student_name` string, 
  `student_phone` string, 
  `student_email` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/zoom_attendance/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_020926_00043_87xv7', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->

## Notes

- **Grain**: one row per `(zoom_id, participant)`. `zoom_id` ↔ `wise_app_backend__zoom._id` (already extracted). Session-level fields (`start_time`, `end_time`, `duration`, `participant`, `meetingstatus`, `type`) are denormalized and repeat across rows for the same session.
- **Use this for**: per-session attendance summaries, who attended what, attendance %, total student duration. Timestamps are already typed `timestamp` (no JSON parsing) — much cheaper than reading `wise_app_backend__zoom` directly. For session/license-level concurrency, prefer this with `SELECT DISTINCT zoom_id, start_time, end_time, ...`.
- **Does NOT have per-participant entry/exit timestamps.** Only aggregate `student_duration` (seconds) and `student_attendance` / `student_attendance_abs`. For live participant concurrency that respects entry/exit times, use `wise_app_backend__raw_zoom_attendance` (per-segment join/leave) or `wise_app_backend__zoom.participants[]` (collapsed single window per participant).
- **Filters out non-license-consuming sessions**: `type = 'OFFLINE'` and `meetingstatus IN ('CANCELLED','MISSED')` are not present here — missed sessions live in `zoom_missed_attendance`.
- **Tenant scoping**: no `namespace` column. Join via `zoom_attendance.class_id = class.class_id` to get `class.namespace`.
- **`student_isteacher`** reliably flags hosts/co-teachers vs students.
