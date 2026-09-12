---
canonical: processed
table: wise_app_backend__feedback_form
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/feedback_form/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:23:27+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__feedback_form`

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
| `instituteid` | `string` |  |
| `profile` | `string` |  |
| `__v` | `string` |  |
| `commenttext` | `string` |  |
| `createdat` | `string` |  |
| `enabled` | `string` |  |
| `questions` | `string` |  |
| `updatedat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `profile`: `teacher (×157)`, `student (×43)`
- `enabled`: `true (×112)`, `false (×88)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `651d723c4bf47cf403756099`, `651d723f6795b97028f8f957`, `651e4a395bbce22af581f54c`

### `instituteid`

- `$oid` — `string`  e.g. `639b0a09b5984d6d06fa7dc0`, `639b0a09b5984d6d06fa7dc0`, `62824adfdae35100075d1b7f`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1696428604911`, `1696428607241`, `1696483897719`

### `questions`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `6669639b8eab9a4fb0445099`, `6669639b8eab9a20c344509a`, `696de58cc7494115068d828b`
    - `options` — `map<int,_>|object`
      - `<int>` — `string`  e.g. `Class`, `Class`, `Class`
    - `questiontext` — `string`  e.g. `Topics covered`, `Comments`, `Topics covered`
    - `required` — `bool`  e.g. `false`, `false`, `false`
    - `type` — `string`  e.g. `SHORT_ANSWER`, `LONG_ANSWER`, `SHORT_ANSWER`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1718182811467`, `1718182814053`, `1768809868425`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_003718_00025_7wk6v', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
