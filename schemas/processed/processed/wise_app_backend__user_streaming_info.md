---
database: processed
table: wise_app_backend__user_streaming_info
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/UserStreamingInfo/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:17:43+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__user_streaming_info`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `userid` | `string` |  |
| `streamingusage` | `string` |  |
| `totalstreamedgbs` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `62f31f303d3514811f4fc61b`, `62f31f303d3514811f4fc760`, `62f31f303d3514811f4fc765`

### `userid`

- `$oid` — `string`  e.g. `62ef46e52592436ddb43b10f`, `60073f1382c8a2819586f471`, `62edeea561f32b6f7ccc6286`

### `streamingusage`

  - `[]` — `object`
    - `consumedmbs` — `object`
      - `$numberint` — `string`  e.g. `0`, `7622`, `27`
    - `date` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1659312000000`, `1659312000000`, `1661990400000`
    - `remaininggbs` — `object`
      - `$numberdouble` — `string`  e.g. `49.1689453125`, `49.99609375`, `49.9296875`
      - `$numberint` — `string`  e.g. `50`, `50`, `50`
    - `uniquerequestips` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `uniquestreamedvideos` — `object`
      - `$numberint` — `string`  e.g. `4`, `1`, `1`

### `totalstreamedgbs`

- `$numberdouble` — `string`  e.g. `16.40234375`, `0.00390625`, `0.8310546875`
- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1660100400451`, `1660100400480`, `1660100400480`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1775002206388`, `1775002206398`, `1775002206408`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__user_streaming_info`(
  `_id` string, 
  `userid` string, 
  `streamingusage` string, 
  `totalstreamedgbs` string, 
  `createdat` string, 
  `updatedat` string, 
  `__v` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/UserStreamingInfo/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_012150_00088_dk2yw', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
