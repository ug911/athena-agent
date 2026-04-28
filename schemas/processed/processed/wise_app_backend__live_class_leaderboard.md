---
database: processed
table: wise_app_backend__live_class_leaderboard
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/live_class_leaderboard/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:16:05+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__live_class_leaderboard`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `insightid` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `pointstable` | `string` |  |
| `updatedat` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

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
  'trino_query_id'='20260428_005849_00061_r82wb', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
