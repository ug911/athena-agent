---
database: processed
table: wise_app_backend__rawsessiontranscript
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/RawSessionTranscript/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:16:46+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__rawsessiontranscript`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `sessionid` | `string` |  |
| `files` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `69494ce328118f629e242809`, `69494ce328118f629e24284b`, `69494ce328118f629e242883`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1766411491140`, `1766411491417`, `1766411491704`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1766411491140`, `1766411491417`, `1766411491704`

### `sessionid`

- `$oid` — `string`  e.g. `69454b7ce353695b55035891`, `694939903fa46da441c5d7d9`, `69424d4c39fa4786ef6c582a`

### `files`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `69494ce319e084a0173a8e34`, `69494ce39f98373feacc7d4f`, `69494ce3ca7ee0f3e638c6ee`
    - `file` — `object`
      - `_id` — `object`
        - `$oid` — `string`  e.g. `69494ce319e084a0173a8e35`, `69494ce39f98373feacc7d50`, `69494ce3ca7ee0f3e638c6ef`
      - `filename` — `string`  e.g. `69454b7ce353695b55035891-transcript-1.1.vtt`, `694939903fa46da441c5d7d9-transcript-1.1.vtt`, `69424d4c39fa4786ef6c582a-transcript-1.1.vtt`
      - `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/64dcc3f2cacfaa35815f`, `https://files.wiseapp.live/upload_files/637337d92a5342426555`, `https://files.wiseapp.live/upload_files/67617929b05c620517c9`
      - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com//uplo`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com//uplo`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com//uplo`
      - `s3key` — `string`  e.g. `upload_files/64dcc3f2cacfaa35815f90c8/69454b7ce353695b550358`, `upload_files/637337d92a53424265555e17/694939903fa46da441c5d7`, `upload_files/67617929b05c620517c92f8c/69424d4c39fa4786ef6c58`
      - `type` — `string`  e.g. `text`, `text`, `text`
    - `meetinguuid` — `string`  e.g. `VHhGw1GnTzyR8oF/Ezl4Lg==`, `GeoI9VsMSkqpBip5TcrgdQ==`, `K+ADZ+ncTFeB+fwJvw/p0g==`
    - `partindex` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `sessionindex` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `url` — `string`  e.g. `https://files.wiseapp.live/upload_files/64dcc3f2cacfaa35815f`, `https://files.wiseapp.live/upload_files/637337d92a5342426555`, `https://files.wiseapp.live/upload_files/67617929b05c620517c9`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__rawsessiontranscript`(
  `_id` string, 
  `createdat` string, 
  `updatedat` string, 
  `sessionid` string, 
  `files` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/RawSessionTranscript/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_011739_00007_pxnkf', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
