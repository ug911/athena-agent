---
database: processed
table: wise_app_backend__zoomrecordings
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/zoomRecordings/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:18:17+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__zoomrecordings`

## Columns

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

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `5ffc54ca62f3dd8063b6d88a`, `60095e652e17bd807a482432`, `60096bdf5e9d6cb8badfeddf`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1610372298157`, `1611226725142`, `1611230175768`

### `recordings`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `5ffc54ccdb29d900071e5082`, `60095e783aecac00093b9d2a`, `60096be69cd88200073746d1`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1610372207000`, `1611221821000`, `1611227317000`
    - `duration` — `object`
      - `$numberint` — `string`  e.g. `43`, `4266`, `2029`
    - `filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/sessi`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/sessi`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/sessi`
    - `filesize` — `object`
      - `$numberint` — `string`  e.g. `1444824`, `196507930`, `43907264`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `zoomobjectid`

- `$oid` — `string`  e.g. `60240aad3b2178b36e174d48`, `602689a0c1ed0161a6e79eb9`, `6027df6208a8072cdebb607f`

### `classid`

- `$oid` — `string`  e.g. `5f816738c7d380f4b59e90eb`, `601d41a8690ab040f1537186`, `5f6f656348df0955b6c7bb05`

### `userid`

- `$oid` — `string`  e.g. `5f6e97177d7d965f091e69d0`, `600f9f2a13635f57ba58f06e`, `5f6e97177d7d965f091e69d0`

## DDL

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
  'trino_query_id'='20260428_013316_00007_mwvhi', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
