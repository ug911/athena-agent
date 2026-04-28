---
database: processed
table: wise_app_backend__registration_form_submission
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/registration_form_submission/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:16:59+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__registration_form_submission`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `instituteid` | `string` |  |
| `userid` | `string` |  |
| `__v` | `string` |  |
| `answers` | `string` |  |
| `createdat` | `string` |  |
| `status` | `string` |  |
| `updatedat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `status`: `SUBMITTED (×151)`, `PARTIALLY_SUBMITTED (×49)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `65d8a3f8e57d96b0dda65d34`, `65d8a428e57d96b0dda67040`, `65d8a4a9e57d96b0dda6a42c`

### `instituteid`

- `$oid` — `string`  e.g. `64f1c3d0449bd300b9fe1208`, `65852a16a2358f61efa542c8`, `65852a16a2358f61efa542c8`

### `userid`

- `$oid` — `string`  e.g. `656099ee3c63e0db2944d8c5`, `65d8a3e84236157db1f1ffc3`, `65d8a470423615773af20db6`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `answers`

  - `[]` — `object`
    - `answer` — `string`  e.g. `Abhijit`, `[REDACTED-EMAIL]`, `[REDACTED-PHONE]`
    - `questionid` — `string`  e.g. `user_name`, `user_email`, `user_phone_number`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1708696568005`, `1708696616654`, `1708696745807`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1708696568005`, `1708696616654`, `1708696745807`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__registration_form_submission`(
  `_id` string, 
  `instituteid` string, 
  `userid` string, 
  `__v` string, 
  `answers` string, 
  `createdat` string, 
  `status` string, 
  `updatedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/registration_form_submission/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_011751_00007_qfpzh', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
