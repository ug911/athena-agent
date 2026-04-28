---
database: processed
table: wise_app_backend__lens_room_config
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/lens_room_config/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:15:51+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__lens_room_config`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `classid` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `polls` | `string` |  |
| `updatedat` | `string` |  |
| `feedbackconfig` | `string` |  |
| `leaderboardconfig` | `string` |  |
| `discussionconfig` | `string` |  |
| `allowzoomforhost` | `string` |  |
| `agendaids` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `allowzoomforhost`: `true (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `647845a7f17d1d6787cf9a70`, `647845a7f17d1d6787cf9a61`, `647845a7f17d1d6787cf9a6c`

### `classid`

- `$oid` — `string`  e.g. `6476e22a14d4153f5d7f6879`, `6476e2290c9272e7c0d06470`, `6476e22b4a7ed66af6257a35`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1685603750166`, `1685603750166`, `1685603750166`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1685603750166`, `1685603750166`, `1685603750166`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__lens_room_config`(
  `_id` string, 
  `classid` string, 
  `__v` string, 
  `createdat` string, 
  `polls` string, 
  `updatedat` string, 
  `feedbackconfig` string, 
  `leaderboardconfig` string, 
  `discussionconfig` string, 
  `allowzoomforhost` string, 
  `agendaids` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/lens_room_config/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_005829_00151_82qxy', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
