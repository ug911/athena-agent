---
database: processed
table: wise_app_backend__classroom_certificate
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/classroom_certificate/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:14:18+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__classroom_certificate`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `archived` | `string` |  |
| `certificateconfigid` | `string` |  |
| `classid` | `string` |  |
| `userid` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `randomtoken` | `string` |  |
| `updatedat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `archived`: `false (×170)`, `true (×30)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `64be7e512b5da616d968e4d4`, `64be7e54420c5935e3ae187d`, `64be7e542b52c597f03a92bd`

### `certificateconfigid`

- `$oid` — `string`  e.g. `64be7e4cfef5ecce32bcb9a3`, `64be7e4cfef5ecce32bcb9a3`, `64be7e4cfef5ecce32bcb9a3`

### `classid`

- `$oid` — `string`  e.g. `5f24056820955e1aff464608`, `5f24056820955e1aff464608`, `5f24056820955e1aff464608`

### `userid`

- `$oid` — `string`  e.g. `5f15aca19aa2c74eba09a31f`, `61f0024ced40594811698245`, `5f365e25f02b25bb4f7764ee`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1690205777808`, `1690205780279`, `1690205780974`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1690205777808`, `1690205780279`, `1690205780974`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__classroom_certificate`(
  `_id` string, 
  `archived` string, 
  `certificateconfigid` string, 
  `classid` string, 
  `userid` string, 
  `__v` string, 
  `createdat` string, 
  `randomtoken` string, 
  `updatedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/classroom_certificate/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003148_00007_g9pn6', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
