---
canonical: processed
table: wise_app_backend__verification
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/verification/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:29:52+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__verification`

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

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `verified`: `true (×165)`, `false (×35)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6a713160e94a1b7d0e503133`, `6a7131921e1945fdebe8210e`, `6a7132132244b4f38bc29bdc`

### `attempts`

- `$numberint` — `string`  e.g. `0`, `1`, `1`

### `resendcount`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `resendwindow`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1785803224802`, `1785803274212`, `1785803403203`

### `expirytime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1785803284802`, `1785803334212`, `1785803463203`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1785803104802`, `1785803154213`, `1785803283203`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_013231_00007_asrqz', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
