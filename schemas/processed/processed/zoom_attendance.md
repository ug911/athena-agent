---
database: processed
table: zoom_attendance
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/zoom_attendance/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:18:28+00:00'
sampled_rows: 200
---

# `processed.zoom_attendance`

## Columns

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

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `class_id`: `6854c5af6fa36cdb2ee32de3 (×200)`
- `class_name`: `THREE E TEACHER (×200)`
- `subject`: ` K8 School Staffroom Link - 3 to 5 Wing (×200)`
- `ct_live`: `673185642d8443c682174117 (×200)`
- `isownerzoom`: `false (×200)`
- `ownerid`: `66ed10ce1a7ba04e4467c482 (×200)`
- `zoom_id`: `696ee7167179451c42b7a28e (×48)`, `69324130ed869aa7fd7db1c4 (×30)`, `69d7a4817a1e450cd82c295d (×23)`, `690f1899bffc3be89c48f933 (×22)`, `68e60812acb5d5123c900a71 (×20)`, `6894473d76657e1ae96e7ae3 (×20)`, `692f9e7543cc4aee533af854 (×18)`, `691d800d5b064f1e93c20129 (×12)`, `69e75d75b4f8d4457764f6bb (×6)`, `697894c9cb33cd30a67b1b16 (×1)`
- `type`: `SCHEDULED (×200)`
- `meetingstatus`: `ENDED (×200)`
- `student_isteacher`: `false (×78)`

## DDL

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
  'trino_query_id'='20260428_015359_00151_c2mt8', 
  'trino_version'='0.215-24582-g0575ac4')
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
