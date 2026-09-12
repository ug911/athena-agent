---
canonical: processed
table: wise_app_backend__entity_interaction
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/entity_interaction/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:23:12+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__entity_interaction`

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

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `markedcompleted`: `true (×171)`, `false (×6)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `64646ba700656a0bb3754e91`, `64646ba900656a0bb3754ed2`, `64646caf00656a0bb375a054`

### `classid`

- `$oid` — `string`  e.g. `6463634df7c11b63c741cb26`, `6463634df7c11b63c741cb26`, `6463634df7c11b63c741cb26`

### `entityid`

- `$oid` — `string`  e.g. `64636360f7c11b3bb741cb53`, `646363878d3d594dfb2beb3b`, `64646c4904a3ee25512c1d82`

### `userid`

- `$oid` — `string`  e.g. `6200f1e9df223de403f26533`, `6200f1e9df223de403f26533`, `6200f1e9df223de403f26533`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1684302759938`, `1684302761332`, `1684303023270`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1684308385815`, `1688127657467`, `1685430186496`

### `views`

- `$numberint` — `string`  e.g. `19`, `5`, `3`

### `markedcompletedon`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1705898954530`, `1708507383559`, `1708675291335`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_003355_00007_y6t4r', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
