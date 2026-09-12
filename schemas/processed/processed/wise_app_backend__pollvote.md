---
canonical: processed
table: wise_app_backend__pollvote
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/pollvote/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:26:33+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__pollvote`

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
| `pollid` | `string` |  |
| `userid` | `string` |  |
| `answer` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `answer`: `A (×102)`, `B (×86)`, `C (×8)`, `E (×2)`, `D (×2)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6182aafd1bfea56817e2cc00`, `6182b0949d5d752b2faa314e`, `6182b09a0237601c54157e49`

### `pollid`

- `$oid` — `string`  e.g. `6182aa7b26d85d30ccfdb81d`, `6182aade02376075b4153356`, `6182aab10706d4bfc31fb009`

### `userid`

- `$oid` — `string`  e.g. `5f8584769d2846d453284a63`, `5f7eb96821bf334707fe7e76`, `5f7eb96821bf334707fe7e76`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1635953405560`, `1635954836071`, `1635954842783`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1635953405560`, `1635954836071`, `1635954842783`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__pollvote`(
  `_id` string, 
  `pollid` string, 
  `userid` string, 
  `answer` string, 
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
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/pollvote/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_011529_00025_8e75t', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
