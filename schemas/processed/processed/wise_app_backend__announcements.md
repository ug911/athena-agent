---
canonical: processed
table: wise_app_backend__announcements
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/announcements/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:20:54+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__announcements`

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

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `disablecommenting`: `false (×196)`, `true (×4)`
- `pinneddiscussion`: `false (×199)`, `true (×1)`
- `poll`: `false (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `5fae283af25e31eb5e36a578`, `5fae29ab3840210163eee0ee`, `5fae2cc8d8a79b03dc25ba95`

### `userid`

- `$oid` — `string`  e.g. `5f7c2c473351934e8f88c86a`, `5f7c2c473351934e8f88c86a`, `5f7c2c473351934e8f88c86a`

### `classid`

- `$oid` — `string`  e.g. `5f7c6c4620366b77282186c4`, `5f7c6c4620366b77282186c4`, `5f7c6c4620366b77282186c4`

### `attachments`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `5fb1050f701049e40554d027`, `5fb1050f7010492be254d028`, `5fb1050f70104959e154d029`
    - `filename` — `string`  e.g. `IMG_20201115_141644.jpg`, `IMG_20201115_141634.jpg`, `IMG_20201115_141622.jpg`
    - `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/5f5c481d2ccd101589b6`, `https://files.wiseapp.live/upload_files/5f5c481d2ccd101589b6`, `https://files.wiseapp.live/upload_files/5f5c481d2ccd101589b6`
    - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`
    - `s3key` — `string`  e.g. `upload_files/5f5c481d2ccd101589b6f0a0/upload_3bcc6bf7-c89d-4`, `upload_files/5f5c481d2ccd101589b6f0a0/upload_c2466fdd-9b94-4`, `upload_files/5f5c481d2ccd101589b6f0a0/upload_d8ccc885-f8fa-4`
    - `size` — `object`
      - `$numberint` — `string`  e.g. `3025478`, `2702152`, `3466267`
    - `type` — `string`  e.g. `image`, `image`, `image`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1605249082668`, `1605249451915`, `1605250248077`

### `comments`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `5fae28e3f25e317d6a36a5b7`, `5fae296b384021e7ebeee0bc`, `5fae296b3840212b64eee0bf`
    - `comment` — `string`  e.g. `Sender's address
Date
Adresis address
Subject
Content
Experi`, `Sender's address
Date
Name
Title
Institution
Personal inform`, `Cover letter

From
Address
Date
To address​
Greetings
Subjec`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1605249251434`, `1605249387367`, `1605249387904`
    - `deleted` — `bool`  e.g. `false`, `false`, `false`
    - `deletedby` — `string`  e.g. `self`, `self`, `self`
    - `editedat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1605249694124`, `1605249387367`, `1605249387904`
    - `userid` — `object`
      - `$oid` — `string`  e.g. `5f5c440924e451d37639e7de`, `5f5c39a72ccd106822b6ef44`, `5f5e30ee60999708669ba14d`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `lastcommentedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1605249859401`, `1605251278094`, `1605251410911`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_003312_00025_r7eaa', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
