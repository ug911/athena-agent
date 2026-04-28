---
database: processed
table: wise_app_backend__liveclassinsight
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/liveclassinsight/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:16:13+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__liveclassinsight`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `meetingid` | `string` |  |
| `meetingpassword` | `string` |  |
| `meetinguuid` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `starttime` | `string` |  |
| `endtime` | `string` |  |
| `sessionid` | `string` |  |
| `userid` | `string` |  |
| `userratings` | `string` |  |
| `participants` | `string` |  |
| `__v` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `64869240f17d1d6787e3720a`, `6486b2dff17d1d6787e9c607`, `6486b649f17d1d6787ea7cad`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1686540864551`, `1686549215306`, `1686550089074`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1686541608456`, `1686549250797`, `1686550089074`

### `starttime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1686540864547`, `1686549215298`, `1686550089062`

### `endtime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1686541608455`, `1686549250796`, `1686555122689`

### `sessionid`

- `$oid` — `string`  e.g. `6486923e8d29f3e737bbb592`, `6486b2dd23f17ac433db9aa6`, `6486b646f88eaa9a1abd22e3`

### `userid`

- `$oid` — `string`  e.g. `646b441d00656a0bb3d797b6`, `646b3e4700656a0bb3d63de9`, `646b3e6000656a0bb3d65b96`

### `userratings`

  - `[]` — `object`
    - `comment` — `string` (nullable)  e.g. `good`, `Mob web comment `, `Android ckmmen`
    - `rating` — `object`
      - `$numberint` — `string`  e.g. `10`, `10`, `10`
    - `userid` — `string`  e.g. `64716a32f17d1d6787737a90`, `646b2d8a00656a0bb3d2d837`, `R2hhemk=`

### `participants`

  - `[]` — `object`
    - `attendanceduration` — `object`
      - `$numberint` — `string`  e.g. `738791`, `35465`, `3825420`
    - `attentiveduration` — `object`
      - `$numberint` — `string`  e.g. `0`, `0`, `0`
    - `clientuserid` — `string`  e.g. `16778240`, `16778240`, `16783360`
    - `customerkey` — `string`  e.g. `NA|M_644231da6b9fbf1b26ef32af`, `NA|Z_64775a2e6090414a9a6ad43b`, `NA|W_64775a36ef6d474dfa63ddbd`
    - `iszoomuser` — `bool`  e.g. `false`, `false`, `false`
    - `name` — `string`  e.g. `[REDACTED]`
    - `platform` — `string`  e.g. `UNKNOWN`, `UNKNOWN`, `WEB`
    - `speakingduration` — `object`
      - `$numberint` — `string`  e.g. `0`, `0`, `2385398`
    - `type` — `string`  e.g. `host`, `host`, `host`
    - `userid` — `string`  e.g. `646b441d00656a0bb3d797b6`, `646b3e4700656a0bb3d63de9`, `646b441700656a0bb3d79049`
    - `videoonduration` — `object`
      - `$numberint` — `string`  e.g. `0`, `0`, `0`
    - `zoomuserid` — `string`  e.g. `16778240`, `16787456`, `16788480`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__liveclassinsight`(
  `_id` string, 
  `meetingid` string, 
  `meetingpassword` string, 
  `meetinguuid` string, 
  `createdat` string, 
  `updatedat` string, 
  `starttime` string, 
  `endtime` string, 
  `sessionid` string, 
  `userid` string, 
  `userratings` string, 
  `participants` string, 
  `__v` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/liveclassinsight/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_010420_00241_wqv9q', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
