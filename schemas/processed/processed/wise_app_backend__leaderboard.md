---
database: processed
table: wise_app_backend__leaderboard
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/leaderboard/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:15:44+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__leaderboard`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `classid` | `string` |  |
| `instituteid` | `string` |  |
| `type` | `string` |  |
| `__v` | `string` |  |
| `alltimepointstable` | `string` |  |
| `createdat` | `string` |  |
| `monthlypointstable` | `string` |  |
| `updatedat` | `string` |  |
| `weeklypointstable` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `type`: `CLASSROOM (×157)`, `INSTITUTE (×43)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6564ae3cb732fd55e1f50800`, `6564ae50b732fda501f50801`, `6564ae77b732fdc5abf50805`

### `classid`

- `$oid` — `string`  e.g. `6525b9f58edcd2c110a27aee`, `64ca1112bb17464f1c2399e8`, `64e4aaa71c3b0dcd62f8cadf`

### `instituteid`

- `$oid` — `string`  e.g. `61fc06b54b31f9e992f780b5`, `61fc06b54b31f9e992f780b5`, `61fc06b54b31f9e992f780b5`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `alltimepointstable`

  - `[]` — `object`
    - `pointsdistribution` — `object`
      - `assessmentmarks` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `assessmentsubmission` — `object`
        - `$numberint` — `string`  e.g. `5`, `0`, `0`
      - `discussioncomment` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `lenspoints` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `pollvoting` — `object`
        - `$numberint` — `string`  e.g. `4`, `4`, `3`
      - `resourcecompletion` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `sessionduration` — `object`
        - `$numberint` — `string`  e.g. `0`, `129`, `207`
      - `sessionparticipation` — `object`
        - `$numberint` — `string`  e.g. `271`, `256`, `295`
      - `testmarks` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `testsubmission` — `object`
        - `$numberint` — `string`  e.g. `849`, `462`, `336`
    - `rank` — `object`
      - `$numberint` — `string`  e.g. `1`, `2`, `3`
    - `totalpoints` — `object`
      - `$numberint` — `string`  e.g. `1129`, `851`, `841`
    - `userid` — `string`  e.g. `61925c70f4ed6b0bb6952aaf`, `6515288812f43e5442ba7c9c`, `64398f8c7545a7d2da68c36e`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1701097020412`, `1701097039954`, `1701097079162`

### `monthlypointstable`

  - `[]` — `object`
    - `pointsdistribution` — `object`
      - `assessmentmarks` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `assessmentsubmission` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `discussioncomment` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `lenspoints` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `pollvoting` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `resourcecompletion` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `sessionduration` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `sessionparticipation` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `testmarks` — `object`
        - `$numberdouble` — `string`  e.g. `-0.0`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `testsubmission` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
    - `rank` — `object`
      - `$numberint` — `string`  e.g. `1`, `2`, `3`
    - `totalpoints` — `object`
      - `$numberint` — `string`  e.g. `0`, `0`, `0`
    - `userid` — `string`  e.g. `65366032aeaf18f5d577f61b`, `653fa57411313ba2af764c17`, `6531560c7a08cfeb852537c6`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1724202063120`, `1723251718339`, `1777252125265`

### `weeklypointstable`

  - `[]` — `object`
    - `pointsdistribution` — `object`
      - `assessmentmarks` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `assessmentsubmission` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `discussioncomment` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `lenspoints` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `pollvoting` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `resourcecompletion` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `sessionduration` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `sessionparticipation` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `testmarks` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `testsubmission` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
    - `rank` — `object`
      - `$numberint` — `string`  e.g. `1`, `2`, `3`
    - `totalpoints` — `object`
      - `$numberint` — `string`  e.g. `0`, `0`, `0`
    - `userid` — `string`  e.g. `65366032aeaf18f5d577f61b`, `653fa57411313ba2af764c17`, `6531560c7a08cfeb852537c6`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__leaderboard`(
  `_id` string, 
  `classid` string, 
  `instituteid` string, 
  `type` string, 
  `__v` string, 
  `alltimepointstable` string, 
  `createdat` string, 
  `monthlypointstable` string, 
  `updatedat` string, 
  `weeklypointstable` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/leaderboard/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_005732_00295_5gp8i', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
