---
canonical: processed
table: wise_app_backend__institute_leaderboard_config
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/institute_leaderboard_config/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:24:02+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__institute_leaderboard_config`

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
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `enabled` | `string` |  |
| `levels` | `string` |  |
| `pointconfigurations` | `string` |  |
| `updatedat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `enabled`: `true (×181)`, `false (×19)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6576e51cb4804505fe58ceeb`, `6576e8fc06d8bd6afd32f25a`, `6577016d68fca3b126ccee16`

### `instituteid`

- `$oid` — `string`  e.g. `64ba717f7c93a560ecedfe80`, `61f2d3edb05c886b68933877`, `62824a620fbfda0007be1a3a`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1702290716734`, `1702291708083`, `1702297965075`

### `levels`

  - `[]` — `object`
    - `index` — `object`
      - `$numberint` — `string`  e.g. `1`, `2`, `3`
    - `thresholdpoints` — `object`
      - `$numberint` — `string`  e.g. `1`, `5`, `20`
    - `title` — `string`  e.g. `Beginner`, `Learner`, `Intermediate`

### `pointconfigurations`

  - `[]` — `object`
    - `category` — `string`  e.g. `SessionParticipation`, `SessionDuration`, `ResourceCompletion`
    - `points` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1702465395988`, `1702981395423`, `1702305069231`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_003747_00025_9qvjx', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
