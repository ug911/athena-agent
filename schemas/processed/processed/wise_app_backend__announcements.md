---
database: processed
table: wise_app_backend__announcements
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/announcements/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:13:45+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__announcements`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `disablecommenting` | `string` |  |
| `pinneddiscussion` | `string` |  |
| `poll` | `string` |  |
| `polldata` | `string` |  |
| `title` | `string` |  |
| `description` | `string` |  |
| `date` | `string` |  |
| `time` | `string` |  |
| `userid` | `string` |  |
| `classid` | `string` |  |
| `attachments` | `string` |  |
| `createdat` | `string` |  |
| `comments` | `string` |  |
| `__v` | `string` |  |
| `lastcommentedat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `disablecommenting`: `false (×176)`, `true (×1)`
- `pinneddiscussion`: `false (×179)`
- `poll`: `false (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `5f251e1aaa382f6247e4a1c9`, `5f2661a5aa382f6247e4a40a`, `5f266c7eaa382f6247e4a429`

### `userid`

- `$oid` — `string`  e.g. `5f12d7d088cd370409e738ec`, `5f24052520955e1aff464606`, `5f12d7d088cd370409e738ec`

### `classid`

- `$oid` — `string`  e.g. `5f1c100abeaf861a4dfb009c`, `5f24056820955e1aff464608`, `5f1c100abeaf861a4dfb009c`

### `attachments`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `5f251e1aaa382f6247e4a1cb`, `5f34e91477cbda743088e021`, `5fe5bc10431bea8eb80e7078`
    - `filename` — `string`  e.g. `IMG-20200801-WA0006.jpg`, `image-9a539bfc-5841-4e63-840f-cb7f3f3e3cc9.jpg`, `JPEG_20201225_154631_7890301319085513433.jpg`
    - `path` — `string`  e.g. `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`, `https://files.wiseapp.live/upload_files/5f24052520955e1aff46`
    - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`
    - `s3key` — `string`  e.g. `upload_files/5f24052520955e1aff464606/upload_7bd7b5b6-bf76-4`, `upload_files/5f5b0247277e936f5b27f797/upload_72671bae-d157-4`, `upload_files/5f5b0247277e936f5b27f797/upload_ad8677a6-d20a-4`
    - `size` — `object`
      - `$numberint` — `string`  e.g. `24654`, `743403`, `3648474`
    - `type` — `string`  e.g. `image`, `image`, `image`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1596268058082`, `1596350885199`, `1596353662444`

### `comments`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `5f251ecaaa382f6247e4a1cf`, `5f251f0aaa382f6247e4a1d2`, `5f252562aa382f6247e4a208`
    - `comment` — `string`  e.g. `Khair Mubarak Sir`, `Khair mubarak sir `, `Ap ko bhi Eid Mubarak sir`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1596268234109`, `1596268298802`, `1596269922887`
    - `deleted` — `bool`  e.g. `true`, `false`, `false`
    - `deletedby` — `string`  e.g. `teacher`, `self`, `teacher`
    - `edited` — `bool`  e.g. `false`, `false`, `false`
    - `editedat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1596268234109`, `1596268298802`, `1596269922887`
    - `userid` — `object`
      - `$oid` — `string`  e.g. `5f1eb423c291405be401d188`, `5f1c227fbeaf861a4dfb00aa`, `5f1cfa01beaf861a4dfb01a1`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `lastcommentedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1604331655749`, `1598449815856`, `1598800333155`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__announcements`(
  `_id` string, 
  `disablecommenting` string, 
  `pinneddiscussion` string, 
  `poll` string, 
  `polldata` string, 
  `title` string, 
  `description` string, 
  `date` string, 
  `time` string, 
  `userid` string, 
  `classid` string, 
  `attachments` string, 
  `createdat` string, 
  `comments` string, 
  `__v` string, 
  `lastcommentedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/announcements/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003109_00205_4ccuf', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
