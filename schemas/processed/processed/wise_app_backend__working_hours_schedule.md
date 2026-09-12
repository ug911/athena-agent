---
canonical: processed
table: wise_app_backend__working_hours_schedule
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/working_hours_schedule/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:30:15+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__working_hours_schedule`

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
| `userid` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `slots` | `string` |  |
| `timezone` | `string` |  |
| `updatedat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `timezone`: `Asia/Kolkata (×187)`, `America/Toronto (×4)`, `Asia/Dubai (×2)`, `America/Los_Angeles (×1)`, `Indian/Mahe (×1)`, `Asia/Colombo (×1)`, `America/Chicago (×1)`, `Asia/Singapore (×1)`, `America/Managua (×1)`, `America/New_York (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `65cb51f46ea2901f591675f8`, `65cb5f7c6ea2901f591ab1bd`, `65cb60386ea2901f591aef45`

### `instituteid`

- `$oid` — `string`  e.g. `64cb564b2ce363bc62187ede`, `62824b360f4c8e0007795099`, `64dcc496132b0b00199c19e3`

### `userid`

- `$oid` — `string`  e.g. `651d7dcd8ef8e6992078cad4`, `622885116725d175be434e6a`, `64dcc3f2cacfaa35815f90c8`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1707823604729`, `1707827068383`, `1707827256988`

### `slots`

  - `[]` — `object`
    - `day` — `string`  e.g. `Sunday`, `Monday`, `Tuesday`
    - `endtime` — `string`  e.g. `20:00`, `20:00`, `20:00`
    - `starttime` — `string`  e.g. `17:00`, `17:00`, `17:00`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1707823888574`, `1716812725487`, `1758728172551`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_013254_00007_cseqh', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
