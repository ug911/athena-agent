---
database: processed
table: exam_service__submissions
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/exam-service/submissions/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:10:42+00:00'
sampled_rows: 200
---

# `processed.exam_service__submissions`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `status` | `string` |  |
| `marks_obtained` | `string` |  |
| `test_id` | `string` |  |
| `user_id` | `string` |  |
| `user_name` | `string` |  |
| `answers` | `string` |  |
| `start_time` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `end_time` | `string` |  |
| `rank` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `status`: `GRADED (×157)`, `ABSENT (×40)`, `PENDING (×3)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `69eff5d60a10cc000178211b`, `69eff0d2c57c5d0001121161`, `69efecd4fb9af90001d3ded6`

### `marks_obtained`

- `$numberdouble` — `string`  e.g. `0.0`, `0.0`, `6.0`

### `test_id`

- `$oid` — `string`  e.g. `669dca2174f0a400010cd1bc`, `670622faab8746000182b773`, `670f625edc4f3e0001734632`

### `user_id`

- `$oid` — `string`  e.g. `68aaf160dc426fe2bdb4a2c2`, `68c53a44ea9d48d390fc3655`, `68c53a44ea9d48d390fc3655`

### `answers`

- `<oid>` — `string`  e.g. `c`, `b`, `a`

### `start_time`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777333718859`, `1777332434437`, `1777331412788`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777333718863`, `1777333966359`, `1777332268824`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777333718863`, `1777332434440`, `1777331412791`

### `end_time`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777333934437`, `1777332268803`, `1777330916691`

### `rank`

- `$numberint` — `string`  e.g. `1`, `1`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.exam_service__submissions`(
  `_id` string, 
  `status` string, 
  `marks_obtained` string, 
  `test_id` string, 
  `user_id` string, 
  `user_name` string, 
  `answers` string, 
  `start_time` string, 
  `updated_at` string, 
  `created_at` string, 
  `end_time` string, 
  `rank` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/exam-service/submissions/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_001423_00036_zec9i', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
