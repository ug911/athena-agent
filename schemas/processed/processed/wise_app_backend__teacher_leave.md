---
database: processed
table: wise_app_backend__teacher_leave
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/teacher_leave/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:17:25+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__teacher_leave`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `instituteid` | `string` |  |
| `userid` | `string` |  |
| `type` | `string` |  |
| `starttime` | `string` |  |
| `endtime` | `string` |  |
| `reason` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `type`: `FULL (×121)`, `HALF (×79)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `65cb69fc8cd15a775c387921`, `65cb6c1d3db6358fff390751`, `65cdacd0cb57e0e1fb858dc1`

### `instituteid`

- `$oid` — `string`  e.g. `639b0a09b5984d6d06fa7dc0`, `639b0a09b5984d6d06fa7dc0`, `646357316c7cce316b175c03`

### `userid`

- `$oid` — `string`  e.g. `5f12d7d088cd370409e738ec`, `61f6301747457264686aed2f`, `6200f1e9df223de403f26533`

### `starttime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1709231400000`, `1709145000000`, `1708021800000`

### `endtime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1709317799999`, `1709231399999`, `1708108199999`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1707829756222`, `1707830301019`, `1707977936499`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1707829756222`, `1707830301019`, `1707977936499`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__teacher_leave`(
  `_id` string, 
  `instituteid` string, 
  `userid` string, 
  `type` string, 
  `starttime` string, 
  `endtime` string, 
  `reason` string, 
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
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/teacher_leave/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_011853_00016_ww2kv', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
