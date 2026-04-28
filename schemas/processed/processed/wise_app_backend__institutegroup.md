---
database: processed
table: wise_app_backend__institutegroup
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/InstituteGroup/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:15:30+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__institutegroup`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `name` | `string` |  |
| `type` | `string` |  |
| `instituteid` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `type`: `LIVE (×149)`, `RECORDED (×51)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `661d0f29eafbf513a668dc79`, `661db3e79f37be5748ed6703`, `661db3ff3197465f2a42e14e`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1713180457529`, `1713222631856`, `1713222655373`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1713180457529`, `1713222631856`, `1713222655373`

### `instituteid`

- `$oid` — `string`  e.g. `63a4008dc8d767a361f9bc95`, `64ccca0ac5cac4002e2d53eb`, `64ccca0ac5cac4002e2d53eb`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__institutegroup`(
  `_id` string, 
  `createdat` string, 
  `updatedat` string, 
  `name` string, 
  `type` string, 
  `instituteid` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/InstituteGroup/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003527_00016_b4hh6', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
