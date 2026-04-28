---
database: processed
table: wise_app_backend__verification
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/verification/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:17:58+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__verification`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `attempts` | `string` |  |
| `resendcount` | `string` |  |
| `verified` | `string` |  |
| `phonenumber` | `string` |  |
| `resendwindow` | `string` |  |
| `expirytime` | `string` |  |
| `code` | `string` |  |
| `createdat` | `string` |  |
| `__v` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `verified`: `true (×173)`, `false (×27)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `69e6c397fb018e2ab21b8e64`, `69e6c3a0c9acb8469549692c`, `69e6c3c0c9acb84695496b85`

### `attempts`

- `$numberint` — `string`  e.g. `1`, `1`, `1`

### `resendcount`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `resendwindow`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1776731151727`, `1776731160888`, `1776731192572`

### `expirytime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1776731211727`, `1776731220888`, `1776731252572`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1776731031728`, `1776731040889`, `1776731072572`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__verification`(
  `_id` string, 
  `attempts` string, 
  `resendcount` string, 
  `verified` string, 
  `phonenumber` string, 
  `resendwindow` string, 
  `expirytime` string, 
  `code` string, 
  `createdat` string, 
  `__v` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/verification/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_012212_00106_vbrfg', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
