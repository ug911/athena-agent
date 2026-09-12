---
canonical: processed
table: wise_app_backend__leaderboard
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/leaderboard/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:25:01+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__leaderboard`

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
| `instituteid` | `string` |  |
| `type` | `string` |  |
| `__v` | `string` |  |
| `alltimepointstable` | `string` |  |
| `createdat` | `string` |  |
| `monthlypointstable` | `string` |  |
| `updatedat` | `string` |  |
| `weeklypointstable` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `type`: `CLASSROOM (×157)`, `INSTITUTE (×43)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6564ae77b732fdc5abf50805`, `6564ae3cb732fd55e1f50800`, `6564ae50b732fda501f50801`

### `classid`

- `$oid` — `string`  e.g. `64e4aaa71c3b0dcd62f8cadf`, `6525b9f58edcd2c110a27aee`, `64ca1112bb17464f1c2399e8`

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
        - `$numberint` — `string`  e.g. `260`, `240`, `240`
    - `rank` — `object`
      - `$numberint` — `string`  e.g. `1`, `2`, `3`
    - `totalpoints` — `object`
      - `$numberint` — `string`  e.g. `260`, `240`, `240`
    - `userid` — `string`  e.g. `64a6c034adf297e4e63e9873`, `64b11b1ae3716ed5e5599709`, `64cb67a12fe6014d0068e6e2`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1701097079162`, `1701097020412`, `1701097039954`

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
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `testsubmission` — `object`
        - `$numberint` — `string`  e.g. `20`, `0`, `0`
    - `rank` — `object`
      - `$numberint` — `string`  e.g. `1`, `2`, `3`
    - `totalpoints` — `object`
      - `$numberint` — `string`  e.g. `20`, `0`, `0`
    - `userid` — `string`  e.g. `6a4deedc8962898b87f1cd85`, `64a158bc34563564f0c32508`, `61d3caaa9cd5aa109a192a84`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786324232917`, `1724202063120`, `1723251718339`

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
    - `userid` — `string`  e.g. `64a158bc34563564f0c32508`, `61d3caaa9cd5aa109a192a84`, `64a52ab52ba44d5a0e6e94a6`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_010220_00151_4p2yr', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
