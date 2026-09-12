---
canonical: processed
table: wise_app_backend__lead
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/lead/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:24:44+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__lead`

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
| `classid` | `string` |  |
| `email` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `name` | `string` |  |
| `phonenumber` | `string` |  |
| `registrationtoken` | `string` |  |
| `updatedat` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `64c28d8119302e350d5cc3ed`, `64c28dd151349d081aae8334`, `64c28df687a88a7c8b649c7d`

### `classid`

- `$oid` — `string`  e.g. `64be2728e63baf454aca8bb1`, `64be2728e63baf454aca8bb1`, `64be2728e63baf454aca8bb1`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1690471809934`, `1690471889262`, `1690471926850`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1690471809934`, `1690471889262`, `1690471926850`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__lead`(
  `_id` string, 
  `classid` string, 
  `email` string, 
  `__v` string, 
  `createdat` string, 
  `name` string, 
  `phonenumber` string, 
  `registrationtoken` string, 
  `updatedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/lead/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_010330_00025_hfg9t', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
