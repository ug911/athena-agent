---
database: processed
table: wise_app_backend__classroom_certificate_config
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/classroom_certificate_config/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:14:22+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__classroom_certificate_config`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `archived` | `string` |  |
| `classid` | `string` |  |
| `templateid` | `string` |  |
| `variables` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `archived`: `false (×186)`, `true (×14)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `660b99a8c368df33f79eda0b`, `660b99e6b2addea24b6d08b4`, `660b9a5db2added6066d18b1`

### `classid`

- `$oid` — `string`  e.g. `65d07b5cf59827e9a4720977`, `65d07b5cf59827e9a4720977`, `65fe81ecbdd9c07e818a3f1a`

### `templateid`

- `$oid` — `string`  e.g. `64f06ed6d7c67c3c202469c2`, `64f06ed6d7c67c3c202469c2`, `64f06ed6d7c67c3c202469c2`

### `variables`

  - `[]` — `object`
    - `name` — `string`  e.g. `studentName`, `certificateNumber`, `issuedOn`
    - `style` — `string`  e.g. `position: absolute; width: 100%; font-weight: 500; font-fami`, `position: absolute; width: 100%; font-weight: 500; font-fami`, `position: absolute; width: 100%; font-weight: 500; font-fami`
    - `value` — `string`  e.g. `Your student name placement`, `12345`, `July of 2023`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1712036264156`, `1712036326373`, `1712036445656`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1712036264156`, `1712036326373`, `1712036445656`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__classroom_certificate_config`(
  `_id` string, 
  `archived` string, 
  `classid` string, 
  `templateid` string, 
  `variables` string, 
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
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/classroom_certificate_config/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_002953_00007_qg8n2', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
