---
database: processed
table: wise_app_backend__session_credit
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/session_credit/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:17:09+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__session_credit`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `userid` | `string` |  |
| `credit` | `string` |  |
| `note` | `string` |  |
| `classid` | `string` |  |
| `assignedby` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |
| `type` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `type`: `CREDIT (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `655da8d18222f749ce95a36a`, `655f29be1179b53728c4e373`, `655f2d048e38817e87044f61`

### `userid`

- `$oid` — `string`  e.g. `5f154a7e88cd370409e739be`, `63ff140483e90f02d7534d92`, `609faac6e4f4d71eb0672d1f`

### `credit`

- `$numberdouble` — `string`  e.g. `0.5`
- `$numberint` — `string`  e.g. `20`, `10`, `20`

### `classid`

- `$oid` — `string`  e.g. `61f823f0b03d7c257ff2d123`, `655f29be1179b56a10c4e370`, `655f2d038e38815016044f5b`

### `assignedby`

- `$oid` — `string`  e.g. `5f15aca19aa2c74eba09a31f`, `5f15aca19aa2c74eba09a31f`, `5f933a68f0d0fe6aef7f3948`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1700636881996`, `1700735422204`, `1700736260090`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1760094068959`, `1760094068959`, `1760094066594`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__session_credit`(
  `_id` string, 
  `userid` string, 
  `credit` string, 
  `note` string, 
  `classid` string, 
  `assignedby` string, 
  `createdat` string, 
  `updatedat` string, 
  `__v` string, 
  `type` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/session_credit/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_011743_00043_p5pvy', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
