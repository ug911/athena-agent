---
canonical: processed
table: wise_app_backend__institutegroup
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/InstituteGroup/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:24:29+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__institutegroup`

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
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `name` | `string` |  |
| `type` | `string` |  |
| `instituteid` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `type`: `LIVE (×148)`, `RECORDED (×52)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

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

_From `IN` (processed)._

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
  'trino_query_id'='20260811_003743_00097_g49vs', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
