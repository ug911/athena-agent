---
database: processed
table: zoom_missed_attendance
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/production/attendance_raw/zoom_missed_attendance/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:18:33+00:00'
sampled_rows: 200
---

# `processed.zoom_missed_attendance`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `class_id` | `string` |  |
| `class_name` | `string` |  |
| `subject` | `string` |  |
| `num_ct` | `bigint` |  |
| `ct_live` | `string` |  |
| `start_time` | `timestamp` |  |
| `end_time` | `timestamp` |  |
| `type` | `string` |  |
| `meetingstatus` | `string` |  |
| `ct_name` | `string` |  |
| `ct_phone` | `string` |  |
| `ct_email` | `string` |  |

## DDL

```sql
CREATE EXTERNAL TABLE `processed.zoom_missed_attendance`(
  `class_id` string, 
  `class_name` string, 
  `subject` string, 
  `num_ct` bigint, 
  `ct_live` string, 
  `start_time` timestamp, 
  `end_time` timestamp, 
  `type` string, 
  `meetingstatus` string, 
  `ct_name` string, 
  `ct_phone` string, 
  `ct_email` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/attendance_raw/zoom_missed_attendance/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'presto_query_id'='20240119_075439_00083_n2i8j', 
  'presto_version'='0.215-20406-gecd2ea2', 
  'totalSize'='-1', 
  'transactional'='false')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->

## Notes

- **Grain**: one row per missed session (no participants — the session never started). Complement to `zoom_attendance` (which has only sessions that ran).
- Use to count missed sessions, no-show analysis, etc. Do **not** include in license/concurrency calculations — missed sessions don't consume a license.
- Tenant scoping: join `class_id → class.class_id` for `namespace`.
