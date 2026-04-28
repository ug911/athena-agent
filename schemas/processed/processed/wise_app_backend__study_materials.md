---
database: processed
table: wise_app_backend__study_materials
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/study_materials/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:17:17+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__study_materials`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `userid` | `string` |  |
| `name` | `string` |  |
| `description` | `string` |  |
| `type` | `string` |  |
| `classid` | `string` |  |
| `youtubeurl` | `string` |  |
| `subtype` | `string` |  |
| `resources` | `string` |  |
| `createdat` | `string` |  |
| `attachments` | `string` |  |
| `comments` | `string` |  |
| `__v` | `string` |  |
| `file` | `string` |  |
| `lastcommentedat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `type`: `video (×88)`, `file (×64)`, `folder (×48)`
- `subtype`: `youtube (×14)`, `hls_video (×2)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `5f394eeb62ef4c3c7c7b7ee3`, `5f6041f7d5bb2bf94f10e6b2`, `5f6045861c52d1b0a2b0818e`

### `userid`

- `$oid` — `string`  e.g. `5f12d7d088cd370409e738ec`, `5f4f7dc565d1d75c36c881a8`, `5f4f7dc565d1d75c36c881a8`

### `classid`

- `$oid` — `string`  e.g. `5f1c100abeaf861a4dfb009c`, `5f5f5cd1d5bb2b517d10d124`, `5f5f5cd1d5bb2b517d10d124`

### `resources`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `607db60155f19c0007951145`, `63725bcb1b28716ceb26155e`, `607ee26f79c4c38406a54f13`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1617703985862`, `1668438987702`, `1608904716636`
    - `date` — `string`  e.g. `06/04/2021`, `25/12/2020`, `20/04/2021`
    - `description` — `string`
    - `file` — `object`
      - `_id` — `object`
        - `$oid` — `string`  e.g. `606c34455bff25d09c765c2f`, `632968df78167e331592169e`, `5fe5f00c55a390d326c9d4b6`
      - `filename` — `string`  e.g. `sony_liv_.gif`, `6645_Stonks.png`, `images - 2020-11-03T211258.024.jpeg`
      - `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/5faf5f54b1d6b2af7625`, `https://files.wiseapp.live/upload_files/5f24052520955e1aff46`, `https://files.wiseapp.live/upload_files/5f24052520955e1aff46`
      - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`
      - `s3key` — `string`  e.g. `upload_files/5faf5f54b1d6b2af7625db2d/upload_c5ccfa08-dfa3-4`, `upload_files/5f24052520955e1aff464606/upload_c81a3b1e-9b73-4`, `upload_files/5f24052520955e1aff464606/upload_8d1007e3-69ca-4`
      - `size` — `object`
        - `$numberint` — `string`  e.g. `1683433`, `23176`, `35177`
      - `type` — `string`  e.g. `image`, `image`, `image`
    - `name` — `string`  e.g. `sony_liv_.gif`, `6645_Stonks.png`, `images - 2020-11-03T211258.024.jpeg`
    - `subtype` — `string`  e.g. `youtube`, `youtube`
    - `time` — `string`  e.g. `10:13 AM`, `01:58 PM`, `02:17 PM`
    - `type` — `string`  e.g. `file`, `file`, `file`
    - `youtubeurl` — `string`  e.g. `https://youtu.be/U3s8w8IFXzA`, `https://youtu.be/FTv1MaSzv-k`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1597591260000`, `1600143863109`, `1600144774105`

### `attachments`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `606c34455bff25d09c765c2f`, `5fe5f00c55a390d326c9d4b6`
    - `filename` — `string`  e.g. `sony_liv_.gif`, `images - 2020-11-03T211258.024.jpeg`
    - `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/5faf5f54b1d6b2af7625`, `https://files.wiseapp.live/upload_files/5f24052520955e1aff46`
    - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`
    - `s3key` — `string`  e.g. `upload_files/5faf5f54b1d6b2af7625db2d/upload_c5ccfa08-dfa3-4`, `upload_files/5f24052520955e1aff464606/upload_8d1007e3-69ca-4`
    - `size` — `object`
      - `$numberint` — `string`  e.g. `1683433`, `35177`
    - `type` — `string`  e.g. `image`, `image`

### `comments`



### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `file`

- `_id` — `object`
  - `$oid` — `string`  e.g. `606ae5ca5b206302cb9c613d`, `606af8341bdbdd62adc86121`, `606af8341bdbdd37e7c86125`
- `filename` — `string`  e.g. `Screenshot_2021-04-05-14-40-52-791_com.wise.app.staging.jpg`, `Selfi_docs.pdf`, `Hey_23_12_2020_09_47_PM.xlsx`
- `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/604f4689f25ce044d319`, `https://files.wiseapp.live/upload_files/604f4689f25ce044d319`, `https://files.wiseapp.live/upload_files/604f4689f25ce044d319`
- `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`
- `s3key` — `string`  e.g. `upload_files/604f4689f25ce044d319b0df/upload_132fea23-f98d-4`, `upload_files/604f4689f25ce044d319b0df/upload_8a8f4012-a928-4`, `upload_files/604f4689f25ce044d319b0df/upload_4d41b9b6-1540-4`
- `size` — `object`
  - `$numberint` — `string`  e.g. `224785`, `125958`, `6725`
- `type` — `string`  e.g. `image`, `pdf`, `file`
- `videoindexurl` — `string`  e.g. `https://files.wiseapp.live/upload_files/5f24052520955e1aff46`, `https://files.wiseapp.live/upload_files/5f24052520955e1aff46`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__study_materials`(
  `_id` string, 
  `userid` string, 
  `name` string, 
  `description` string, 
  `type` string, 
  `classid` string, 
  `youtubeurl` string, 
  `subtype` string, 
  `resources` string, 
  `createdat` string, 
  `attachments` string, 
  `comments` string, 
  `__v` string, 
  `file` string, 
  `lastcommentedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/study_materials/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_011820_00088_3bkz5', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
