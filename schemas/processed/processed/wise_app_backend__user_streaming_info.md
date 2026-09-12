---
canonical: processed
table: wise_app_backend__user_streaming_info
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/UserStreamingInfo/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:29:21+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__user_streaming_info`

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
| `userid` | `string` |  |
| `streamingusage` | `string` |  |
| `totalstreamedgbs` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `62dcb5b01f216d881f799465`, `62dcb5b01f216d881f799484`, `62dcb5b01f216d881f79949a`

### `userid`

- `$oid` — `string`  e.g. `60b660012809a900f05106f4`, `607e9da70fa3d7788648d865`, `60b747c2df81d0fe2dcff600`

### `streamingusage`

  - `[]` — `object`
    - `consumedmbs` — `object`
      - `$numberint` — `string`  e.g. `31009`, `47813`, `32749`
    - `date` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1656633600000`, `1659312000000`, `1661990400000`
    - `remaininggbs` — `object`
      - `$numberdouble` — `string`  e.g. `48.607421875`, `49.9072265625`, `49.98828125`
      - `$numberint` — `string`  e.g. `50`, `50`, `0`
    - `uniquerequestips` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `uniquestreamedvideos` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`

### `totalstreamedgbs`

- `$numberdouble` — `string`  e.g. `384.037109375`, `0.376953125`, `7.3837890625`
- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1658631600266`, `1658631600268`, `1658631600274`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1785543001302`, `1785543001302`, `1785543001302`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_013207_00007_qr4yf', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
