---
database: processed
table: wise_app_backend__pollvote
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/pollvote/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:16:25+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__pollvote`

## Columns

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

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `answer`: `A (×99)`, `B (×89)`, `C (×8)`, `E (×2)`, `D (×2)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6182aafd1bfea56817e2cc00`, `6182b0510237606d39157ae4`, `6182b0949d5d752b2faa314e`

### `pollid`

- `$oid` — `string`  e.g. `6182aa7b26d85d30ccfdb81d`, `6182afaf1e35063537b306a3`, `6182aade02376075b4153356`

### `userid`

- `$oid` — `string`  e.g. `5f8584769d2846d453284a63`, `5f12d7d088cd370409e738ec`, `5f7eb96821bf334707fe7e76`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1635953405560`, `1635954769689`, `1635954836071`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1635953405560`, `1635954769689`, `1635954836071`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

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
  'trino_query_id'='20260428_010747_00167_3idnc', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
