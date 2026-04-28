---
database: processed
table: wise_app_backend__entity_interaction
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/entity_interaction/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:14:52+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__entity_interaction`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `classid` | `string` |  |
| `entityid` | `string` |  |
| `userid` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `views` | `string` |  |
| `markedcompleted` | `string` |  |
| `markedcompletedon` | `string` |  |
| `profile` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `markedcompleted`: `true (×156)`, `false (×12)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6463568200656a0bb336aeb1`, `64646ba700656a0bb3754e91`, `64646ba900656a0bb3754ed2`

### `classid`

- `$oid` — `string`  e.g. `6463559c73240d281d18e23f`, `6463634df7c11b63c741cb26`, `6463634df7c11b63c741cb26`

### `entityid`

- `$oid` — `string`  e.g. `646355bb8a6da828f0576ac3`, `64636360f7c11b3bb741cb53`, `646363878d3d594dfb2beb3b`

### `userid`

- `$oid` — `string`  e.g. `63917fa313c287d3a0a03efc`, `6200f1e9df223de403f26533`, `6200f1e9df223de403f26533`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1684231810410`, `1684302759938`, `1684302761332`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1684231905314`, `1684308385815`, `1688127657467`

### `views`

- `$numberint` — `string`  e.g. `9`, `19`, `5`

### `markedcompletedon`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1708507383559`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__entity_interaction`(
  `_id` string, 
  `classid` string, 
  `entityid` string, 
  `userid` string, 
  `__v` string, 
  `createdat` string, 
  `updatedat` string, 
  `views` string, 
  `markedcompleted` string, 
  `markedcompletedon` string, 
  `profile` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/entity_interaction/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003202_00007_65tyf', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
