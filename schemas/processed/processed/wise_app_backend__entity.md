---
database: processed
table: wise_app_backend__entity
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/entity/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:14:47+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__entity`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `entityid` | `string` |  |
| `__v` | `string` |  |
| `classid` | `string` |  |
| `createdat` | `string` |  |
| `entitysubtype` | `string` |  |
| `entitytype` | `string` |  |
| `sortkey` | `string` |  |
| `archived` | `string` |  |
| `metadata` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `entitysubtype`: `AD_HOC (×181)`, `SCHEDULED (×9)`, `FILE (×5)`, `OFFLINE (×1)`, `DISCUSSION (×1)`, `LINK (×1)`
- `entitytype`: `SESSION (×191)`, `RESOURCE (×6)`, `TEST (×2)`, `DISCUSSION (×1)`
- `archived`: `false (×26)`, `true (×5)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6383905a0bd8695cd5e4a591`, `638391663812375a5aa391ae`, `6383970626069262b76e7caa`

### `entityid`

- `$oid` — `string`  e.g. `6383905af32540416fb7776c`, `637bba0b7f472530365805f3`, `6383970638129a2439b42943`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `classid`

- `$oid` — `string`  e.g. `63838e6d624bebda48039c46`, `637bb9c7b9f7ac02303cb6bc`, `638074246b0e96bcbbfaf5eb`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1669566554405`, `1669568642057`, `1669568262226`

### `sortkey`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1668011457460`, `1669568642022`, `1669568262226`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__entity`(
  `_id` string, 
  `entityid` string, 
  `__v` string, 
  `classid` string, 
  `createdat` string, 
  `entitysubtype` string, 
  `entitytype` string, 
  `sortkey` string, 
  `archived` string, 
  `metadata` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/entity/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003114_00097_khk45', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
