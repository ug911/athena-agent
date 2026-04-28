---
database: processed
table: wise_app_backend__feedback_form
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/feedback_form/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:14:58+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__feedback_form`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `instituteid` | `string` |  |
| `profile` | `string` |  |
| `__v` | `string` |  |
| `commenttext` | `string` |  |
| `createdat` | `string` |  |
| `enabled` | `string` |  |
| `questions` | `string` |  |
| `updatedat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `profile`: `teacher (×200)`
- `enabled`: `false (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `695f49b92fe8ed393fd7989d`, `695f49b92fe8ed393fd79681`, `695f49b92fe8ed393fd79687`

### `instituteid`

- `$oid` — `string`  e.g. `628248260f4c8e000778edae`, `628248254b26fc00082a0955`, `628248254b26fc00082a0958`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1767852493979`, `1767852493960`, `1767852493961`

### `questions`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `695f49b92fe8ed393fd7989e`, `695f49b92fe8ed393fd7989f`, `695f49b92fe8ed393fd79682`
    - `questiontext` — `string`  e.g. `Topics covered`, `Comments`, `Topics covered`
    - `required` — `bool`  e.g. `false`, `false`, `false`
    - `type` — `string`  e.g. `SHORT_ANSWER`, `LONG_ANSWER`, `SHORT_ANSWER`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1767852493979`, `1767852493960`, `1767852493961`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__feedback_form`(
  `_id` string, 
  `instituteid` string, 
  `profile` string, 
  `__v` string, 
  `commenttext` string, 
  `createdat` string, 
  `enabled` string, 
  `questions` string, 
  `updatedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/feedback_form/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003452_00007_2kfcm', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
