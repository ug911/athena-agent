---
database: processed
table: wise_app_backend__assignments
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/assignments/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:13:50+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__assignments`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `disablecommenting` | `string` |  |
| `topic` | `string` |  |
| `submissiondate` | `string` |  |
| `userid` | `string` |  |
| `submissiontime` | `string` |  |
| `description` | `string` |  |
| `maxmarks` | `string` |  |
| `attachments` | `string` |  |
| `classid` | `string` |  |
| `solutions` | `string` |  |
| `submission` | `string` |  |
| `createdat` | `string` |  |
| `comments` | `string` |  |
| `__v` | `string` |  |
| `submitby` | `string` |  |
| `starttime` | `string` |  |
| `criteria` | `string` |  |
| `public` | `string` |  |
| `thumbnail` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `5f2405b520955e1aff46460a`, `5f2405c520955e1aff46460e`, `5f258bc2aa382f6247e4a327`

### `userid`

- `$oid` — `string`  e.g. `5f12d7d088cd370409e738ec`, `5f24052520955e1aff464606`, `5f12d7d088cd370409e738ec`

### `maxmarks`

- `$numberint` — `string`  e.g. `10`, `50`, `10`

### `attachments`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `5f24077920955e1aff464611`, `5f591911277e93308727cf21`, `5f258bc2aa382f6247e4a329`
    - `filename` — `string`  e.g. `Screenshot_20200731-171959~2.jpg`, `upload_661fb6a1-d887-456a-aa25-b18bb9e1da12.jpg`, `Screenshot_20200801-210400.jpg`
    - `path` — `string`  e.g. `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`
    - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`
    - `s3key` — `string`  e.g. `upload_files/5f24052520955e1aff464606/upload_aee7935e-2a7f-4`, `upload_files/5f12d7d088cd370409e738ec/upload_3aed3cec-6779-4`, `upload_files/5f12d7d088cd370409e738ec/upload_63287cf5-bbd2-4`
    - `size` — `object`
      - `$numberint` — `string`  e.g. `37535`, `67555`, `41815`
    - `type` — `string`  e.g. `image`, `image`, `image`

### `classid`

- `$oid` — `string`  e.g. `5f1c100abeaf861a4dfb009c`, `5f24056820955e1aff464608`, `5f1c100abeaf861a4dfb009c`

### `solutions`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `60f3c5378a7b6c2ca112f07c`, `5f424d7aa5302b121ee0027b`, `5f899e6fa883a2f8edf8e3eb`
    - `attachments` — `array<object>`
      - `[].attachments[]` — `object`
        - `_id` — `object`
          - `$oid` — `string`  e.g. `60f3c5378a7b6c771d12f07d`, `5f424d7aa5302b73c5e0027c`, `5f424d7aa5302b5b95e0027d`
        - `filename` — `string`  e.g. `IMG-20210718-WA0003.jpg`, `IMG-20200823-WA0013.jpg`, `IMG-20200823-WA0012.jpg`
        - `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/5f1d6518beaf861a4dfb`, `https://files.wiseapp.live/upload_files/5f1cfa01beaf861a4dfb`, `https://files.wiseapp.live/upload_files/5f1cfa01beaf861a4dfb`
        - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`
        - `s3key` — `string`  e.g. `upload_files/5f1d6518beaf861a4dfb0241/upload_964c7b57-18a5-4`, `upload_files/5f1cfa01beaf861a4dfb01a1/upload_597f7a8e-c215-4`, `upload_files/5f1cfa01beaf861a4dfb01a1/upload_cd8184eb-4ba6-4`
        - `size` — `object`
          - `$numberint` — `string`  e.g. `233874`, `55071`, `66911`
        - `type` — `string`  e.g. `image`, `image`, `image`
    - `studentid` — `object`
      - `$oid` — `string`  e.g. `5f1d6518beaf861a4dfb0241`, `5f1cfa01beaf861a4dfb01a1`, `5f15aca19aa2c74eba09a31f`

### `submission`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `5f240b2e20955e1aff464632`, `5f240d7420955e1aff46463c`, `5f240fda20955e1aff464643`
    - `answer` — `string`
    - `attachments` — `array<object>`
      - `[].attachments[]` — `object`
        - `_id` — `object`
          - `$oid` — `string`  e.g. `5f240b2e20955e1aff464633`, `5f240d7420955e1aff46463d`, `5f240fda20955e1aff464644`
        - `filename` — `string`  e.g. `IMG_20200731_174422.jpg`, `IMG_20200731_175223.jpg`, `20200731_180259-1.jpg`
        - `path` — `string`  e.g. `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`
        - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`
        - `s3key` — `string`  e.g. `upload_files/5f115343008e2d63eeedbe0e/upload_9245317c-d6ae-4`, `upload_files/5f12d7d088cd370409e738ec/upload_70232ad2-4c2d-4`, `upload_files/5f15aca19aa2c74eba09a31f/upload_07c293be-0735-4`
        - `size` — `object`
          - `$numberint` — `string`  e.g. `3375925`, `1359540`, `836176`
        - `type` — `string`  e.g. `image`, `image`, `image`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1596304162248`, `1596304162249`, `1596304162249`
    - `feedback` — `string`  e.g. `You were supposed to find mode`, `Correct`, `good`
    - `feedbackfiles` — `array<unknown>`
    - `feedbackrecordings` — `array<object>|array<unknown>`
      - `[].feedbackrecordings[]` — `object`
        - `_id` — `object`
          - `$oid` — `string`  e.g. `5f6c1af968936244bd4f5751`, `5f6b5510cea49b09e457752c`, `5f5cbc38609997045b9b7d1b`
        - `filename` — `string`  e.g. `sound.mp3`, `sound.mp3`, `sound.mp3`
        - `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/5f12d7d088cd370409e7`, `https://files.wiseapp.live/upload_files/5f12d7d088cd370409e7`, `https://files.wiseapp.live/upload_files/5f24052520955e1aff46`
        - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3.ap-south-1.amazonaws.com/uploa`
        - `s3key` — `string`  e.g. `upload_files/5f12d7d088cd370409e738ec/upload_fb6dbbc8-a91f-4`, `upload_files/5f12d7d088cd370409e738ec/upload_eb65e028-b915-4`, `upload_files/5f24052520955e1aff464606/upload_be599853-3a4f-4`
        - `size` — `object`
          - `$numberint` — `string`  e.g. `102296`, `127896`, `68597`
        - `type` — `string`  e.g. `audio`, `audio`, `audio`
    - `getmark` — `object`
      - `$numberint` — `string`  e.g. `2`, `9`, `45`
    - `gradedat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1600920313234`, `1600869648184`, `1599912869136`
    - `markedassolution` — `bool`  e.g. `false`, `false`, `false`
    - `studentid` — `object`
      - `$oid` — `string`  e.g. `5f1da9e4beaf861a4dfb02f3`, `5f1d55c3beaf861a4dfb0213`, `5f1d2e5ebeaf861a4dfb01eb`
    - `submissionstatus` — `string`  e.g. `submitted`, `graded`, `submitted`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1595779200000`, `1595779200000`, `1596296130737`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `submitby`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1596477600000`, `1626631200000`, `1596564000000`

### `starttime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1595779200000`, `1595779200000`, `1596296130737`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__assignments`(
  `_id` string, 
  `disablecommenting` string, 
  `topic` string, 
  `submissiondate` string, 
  `userid` string, 
  `submissiontime` string, 
  `description` string, 
  `maxmarks` string, 
  `attachments` string, 
  `classid` string, 
  `solutions` string, 
  `submission` string, 
  `createdat` string, 
  `comments` string, 
  `__v` string, 
  `submitby` string, 
  `starttime` string, 
  `criteria` string, 
  `public` string, 
  `thumbnail` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/assignments/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003043_00007_wf6tg', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
