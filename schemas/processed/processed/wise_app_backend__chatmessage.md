---
database: processed
table: wise_app_backend__chatmessage
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/ChatMessage/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:14:03+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__chatmessage`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `chatid` | `string` |  |
| `senderid` | `string` |  |
| `message` | `string` |  |
| `attachments` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `67c5e19223d4838f444fcb16`, `67c5e1ccf08557977ca62cdf`, `67c5e1d7f08557977ca62e97`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1741021586557`, `1741021644869`, `1741021655151`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1741021586557`, `1741021644869`, `1741021655151`

### `chatid`

- `$oid` — `string`  e.g. `67c42fa7f6b7db0bcc0bea2f`, `67c2f581f6b7db0bcc78d122`, `67c2f581f6b7db0bcc78d122`

### `senderid`

- `$oid` — `string`  e.g. `65f430b95998990017e30f45`, `65f430b95998990017e30f45`, `65f430b95998990017e30f45`

### `attachments`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `67c6067c23d4838f4451edf8`, `67c6067c23d4838f4451edf9`, `67c60e86f68622f7afc0ff62`
    - `filename` — `string`  e.g. `IMG_3408.jpeg`, `IMG_3407.jpeg`, `JPEG_20250303_201802_3735521586248823369.jpg`
    - `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/67c1e7d9f6b7db0bcc00`, `https://files.wiseapp.live/upload_files/67c1e7d9f6b7db0bcc00`, `https://files.wiseapp.live/upload_files/67c20ba4f6b7db0bcc10`
    - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`
    - `s3key` — `string`  e.g. `upload_files/67c1e7d9f6b7db0bcc004805/upload_230defa2-6966-4`, `upload_files/67c1e7d9f6b7db0bcc004805/upload_4b59790c-7372-4`, `upload_files/67c20ba4f6b7db0bcc105e07/upload_37de6e90-0a9b-4`
    - `size` — `object`
      - `$numberint` — `string`  e.g. `2923552`, `2771220`, `917082`
    - `type` — `string`  e.g. `image`, `image`, `image`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__chatmessage`(
  `_id` string, 
  `createdat` string, 
  `updatedat` string, 
  `chatid` string, 
  `senderid` string, 
  `message` string, 
  `attachments` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/ChatMessage/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_002958_00007_cdkyw', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
