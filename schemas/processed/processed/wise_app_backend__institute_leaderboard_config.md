---
database: processed
table: wise_app_backend__institute_leaderboard_config
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/institute_leaderboard_config/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:15:17+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__institute_leaderboard_config`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `instituteid` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `enabled` | `string` |  |
| `levels` | `string` |  |
| `pointconfigurations` | `string` |  |
| `updatedat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `enabled`: `true (×160)`, `false (×40)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6576e241e2ce183f13abeaa0`, `6576e51cb4804505fe58ceeb`, `6576e8fc06d8bd6afd32f25a`

### `instituteid`

- `$oid` — `string`  e.g. `625578d2853c6f4420a99e8a`, `64ba717f7c93a560ecedfe80`, `61f2d3edb05c886b68933877`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1702289985743`, `1702290716734`, `1702291708083`

### `levels`

  - `[]` — `object`
    - `index` — `object`
      - `$numberint` — `string`  e.g. `1`, `2`, `3`
    - `thresholdpoints` — `object`
      - `$numberint` — `string`  e.g. `1`, `10`, `50`
    - `title` — `string`  e.g. `Beginner`, `Learner`, `Intermediate`

### `pointconfigurations`

  - `[]` — `object`
    - `category` — `string`  e.g. `SessionParticipation`, `SessionDuration`, `ResourceCompletion`
    - `points` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1761656505485`, `1702465395988`, `1702981395423`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__institute_leaderboard_config`(
  `_id` string, 
  `instituteid` string, 
  `__v` string, 
  `createdat` string, 
  `enabled` string, 
  `levels` string, 
  `pointconfigurations` string, 
  `updatedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/institute_leaderboard_config/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003548_00052_68n3s', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
