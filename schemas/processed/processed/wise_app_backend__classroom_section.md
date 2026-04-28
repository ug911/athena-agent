---
database: processed
table: wise_app_backend__classroom_section
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/classroom_section/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:14:34+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__classroom_section`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `classid` | `string` |  |
| `sortkey` | `string` |  |
| `name` | `string` |  |
| `entities` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6463559c455c4a5106d33797`, `646357326c7cce77b1175c09`, `646358096c7cce2d52175ee3`

### `classid`

- `$oid` — `string`  e.g. `6463559c73240d281d18e23f`, `646357316c7cce405c175c04`, `646357316c7cce405c175c04`

### `sortkey`

- `$numberint` — `string`  e.g. `1`, `1`, `2`

### `entities`

  - `[]` — `object`
    - `entityid` — `object`
      - `$oid` — `string`  e.g. `646355bb8a6da828f0576ac3`, `646dfaf40fded9486a4dfc66`, `646dfb8dff666ded5f04793e`
    - `entitytype` — `string`  e.g. `RESOURCE`, `RESOURCE`, `RESOURCE`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1684231580856`, `1684231986445`, `1684232201770`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1685430185202`, `1714030094686`, `1710783673414`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__classroom_section`(
  `_id` string, 
  `classid` string, 
  `sortkey` string, 
  `name` string, 
  `entities` string, 
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
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/classroom_section/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003123_00025_n9cwa', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
