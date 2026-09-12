---
canonical: processed
table: exam_service__submissions
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/exam-service/submissions/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:15:26+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.exam_service__submissions`

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

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `status`: `ABSENT (×152)`, `GRADED (×45)`, `VOID_RETAKEN (×2)`, `PENDING (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6a7a655c17b47e0001d686c7`, `6a7a6104cf2fac0001bf742b`, `6a7a5b0bcf2fac0001bf742a`

### `marks_obtained`

- `$numberdouble` — `string`  e.g. `0.0`, `194.35`, `0.0`
- `$numberint` — `string`  e.g. `0`, `0`, `10`

### `test_id`

- `$oid` — `string`  e.g. `66a063d85ac83600013f2184`, `66a063d85ac83600013f2184`, `68da618dcb8d9e0001a00d3e`

### `user_id`

- `$oid` — `string`  e.g. `683dac7bb213e9ac496b0b0f`, `683dac7bb213e9ac496b0b0f`, `65e6d6b33eebbeedb40957aa`

### `answers`

- `<oid>` — `string`  e.g. `a`, `d`, `c`

### `start_time`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786406236255`, `1786405124077`, `1786403595111`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786406236258`, `1786406232997`, `1786404238936`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786406236258`, `1786405124080`, `1786403595113`

### `end_time`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786405862754`, `1786404195111`, `1786400961257`

### `rank`

- `$numberint` — `string`  e.g. `1`, `1`, `1`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_001419_00070_drwmr', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
