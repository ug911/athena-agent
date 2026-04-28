---
database: processed
table: wise_app_backend__working_hours_schedule
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/working_hours_schedule/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:18:03+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__working_hours_schedule`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `instituteid` | `string` |  |
| `userid` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `slots` | `string` |  |
| `timezone` | `string` |  |
| `updatedat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `timezone`: `Asia/Kolkata (×187)`, `America/Toronto (×4)`, `Asia/Dubai (×2)`, `America/Los_Angeles (×1)`, `America/Chicago (×1)`, `Asia/Singapore (×1)`, `America/Managua (×1)`, `America/New_York (×1)`, `Indian/Mahe (×1)`, `Asia/Colombo (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `65cb51f46ea2901f591675f8`, `65cb69296ea2901f591e57b7`, `65cb69e56ea2901f591e8928`

### `instituteid`

- `$oid` — `string`  e.g. `64cb564b2ce363bc62187ede`, `64dcc496132b0b00199c19e3`, `639b0a09b5984d6d06fa7dc0`

### `userid`

- `$oid` — `string`  e.g. `651d7dcd8ef8e6992078cad4`, `65afacec45b8bc2521cc19fa`, `5f12d7d088cd370409e738ec`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1707823604729`, `1707829545959`, `1707829733383`

### `slots`

  - `[]` — `object`
    - `day` — `string`  e.g. `Sunday`, `Monday`, `Tuesday`
    - `endtime` — `string`  e.g. `20:00`, `20:00`, `20:00`
    - `starttime` — `string`  e.g. `17:00`, `17:00`, `17:00`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1707823888574`, `1707829659473`, `1707829733383`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__working_hours_schedule`(
  `_id` string, 
  `instituteid` string, 
  `userid` string, 
  `__v` string, 
  `createdat` string, 
  `slots` string, 
  `timezone` string, 
  `updatedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/working_hours_schedule/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_012212_00061_6i3qz', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
