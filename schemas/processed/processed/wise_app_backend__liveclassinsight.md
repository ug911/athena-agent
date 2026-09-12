---
canonical: processed
table: wise_app_backend__liveclassinsight
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/liveclassinsight/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:26:04+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__liveclassinsight`

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

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6492d75bd20ce0f147342e12`, `6492dd8bd20ce0f14735cfa0`, `6492e430d20ce0f147379c42`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1687344987156`, `1687346571377`, `1687348272297`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1687346843223`, `1687346799879`, `1687350741094`

### `starttime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1687344987153`, `1687346571374`, `1687348272295`

### `endtime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1687346843221`, `1687346799879`, `1687350741094`

### `sessionid`

- `$oid` — `string`  e.g. `6492d75952e7306a98471924`, `6492dd894101ff42d256d60a`, `6492e42e4101ff2abe56ef2c`

### `userid`

- `$oid` — `string`  e.g. `646b3e6300656a0bb3d65e8e`, `646b3e4700656a0bb3d63e0b`, `646b441200656a0bb3d78ad7`

### `userratings`

  - `[]` — `object`
    - `comment` — `string`  e.g. `Great session! Please share more polls.`, `Great session. Please ask more MCQs`, `it was amazing.`
    - `rating` — `object`
      - `$numberint` — `string`  e.g. `4`, `10`, `10`
    - `userid` — `string`  e.g. `64716a24f17d1d6787736d4a`, `637db5ae5d97ca7a012a3881`, `U3R1ZGVudA==`

### `participants`

  - `[]` — `object`
    - `attendanceduration` — `object`
      - `$numberint` — `string`  e.g. `1856033`, `1758399`, `228491`
    - `attentiveduration` — `object`
      - `$numberint` — `string`  e.g. `0`, `336359`, `0`
    - `clientuserid` — `string`  e.g. `16778240`, `16795648`, `16778240`
    - `name` — `string`  e.g. `[REDACTED]`
    - `platform` — `string`  e.g. `UNKNOWN`, `WEB`, `UNKNOWN`
    - `speakingduration` — `object`
      - `$numberint` — `string`  e.g. `791433`, `1112185`, `0`
    - `type` — `string`  e.g. `host`, `cohost`, `host`
    - `userid` — `string`  e.g. `646b3e6300656a0bb3d65e8e`, `64739cd1f17d1d6787deb4d1`, `646b3e4700656a0bb3d63e0b`
    - `videoonduration` — `object`
      - `$numberint` — `string`  e.g. `0`, `0`, `0`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_011147_00250_83526', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
