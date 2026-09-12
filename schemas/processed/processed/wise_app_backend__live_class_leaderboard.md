---
canonical: processed
table: wise_app_backend__live_class_leaderboard
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/live_class_leaderboard/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:25:44+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__live_class_leaderboard`

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
| `insightid` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `pointstable` | `string` |  |
| `updatedat` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6433e05443e715be7e312673`, `6433e5f343e715be7e3282b8`, `6433e67085e8dbaa09141f8c`

### `insightid`

- `$oid` — `string`  e.g. `6433e01843e715be7e31198d`, `6433e5ea43e715be7e327fc0`, `6433e67043e715be7e32a5ef`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1681121364908`, `1681122803514`, `1681122928938`

### `pointstable`

  - `[]` — `object`
    - `pointsdistribution` — `object`
      - `attention` — `object`
        - `$numberint` — `string`  e.g. `0`, `14`, `0`
      - `bonus` — `object`
        - `$numberint` — `string`  e.g. `0`, `2`, `0`
      - `poll` — `object`
        - `$numberint` — `string`  e.g. `0`, `14`, `1`
      - `talktime` — `object`
        - `$numberint` — `string`  e.g. `0`, `0`, `0`
      - `video` — `object`
        - `$numberint` — `string`  e.g. `0`, `18`, `0`
    - `userid` — `string`  e.g. `637b62a31aeff37812fca17e`, `63809a4bfab7fa014d91fba2`, `637b2efbb83202bbf7505385`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1681121935053`, `1681125181202`, `1681122928938`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__live_class_leaderboard`(
  `_id` string, 
  `insightid` string, 
  `__v` string, 
  `createdat` string, 
  `pointstable` string, 
  `updatedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/live_class_leaderboard/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_010302_00061_eds4b', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
