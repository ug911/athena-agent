---
canonical: processed
table: wise_app_backend__zoomrecordings
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/zoomRecordings/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:30:56+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__zoomrecordings`

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
| `createdat` | `string` |  |
| `sessionid` | `string` |  |
| `recordings` | `string` |  |
| `__v` | `string` |  |
| `zoomobjectid` | `string` |  |
| `classid` | `string` |  |
| `userid` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `609b5b0fc36ae541d792a9a5`, `609b5d918c1bc3490c2cee53`, `609b5e31980e0c45894b3127`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1620794127301`, `1620794769128`, `1620794929740`

### `recordings`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `609b5b175a94a30007b51c77`, `609b5d954150aa00078bc33d`, `609b5d965a94a30007b51d00`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1620791561000`, `1620791801000`, `1620793572000`
    - `duration` — `object`
      - `$numberint` — `string`  e.g. `2412`, `315`, `537`
    - `filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/sessi`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/sessi`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/sessi`
    - `filesize` — `object`
      - `$numberint` — `string`  e.g. `68085040`, `12841608`, `35326219`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `zoomobjectid`

- `$oid` — `string`  e.g. `609b507cbf946e88143ffac9`, `609b4b48094d6e417a0f87cd`, `609b4c15ff485460ca9bbb64`

### `classid`

- `$oid` — `string`  e.g. `607ea95378a74bdabab02595`, `608d4b34685f5f1ba6452c6c`, `609220c859087015253b2d90`

### `userid`

- `$oid` — `string`  e.g. `607ea8cf3136381eea22eb34`, `600f9f2a13635f57ba58f06e`, `609220910449c6065ca25cb4`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__zoomrecordings`(
  `_id` string, 
  `createdat` string, 
  `sessionid` string, 
  `recordings` string, 
  `__v` string, 
  `zoomobjectid` string, 
  `classid` string, 
  `userid` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/zoomRecordings/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_014710_00052_pwset', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
