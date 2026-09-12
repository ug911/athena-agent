---
canonical: processed
table: wise_app_backend__registration_form_submission
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/registration_form_submission/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:27:40+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__registration_form_submission`

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
| `instituteid` | `string` |  |
| `userid` | `string` |  |
| `__v` | `string` |  |
| `answers` | `string` |  |
| `createdat` | `string` |  |
| `status` | `string` |  |
| `updatedat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `status`: `SUBMITTED (×137)`, `PARTIALLY_SUBMITTED (×63)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `65b8e2aeab16cf246ea915d3`, `65b9b1d86ea2901f59157f5f`, `65b9d5136ea2901f591bba2b`

### `instituteid`

- `$oid` — `string`  e.g. `63a4008dc8d767a361f9bc95`, `6594f8f7771359ce61357154`, `6594f8f7771359ce61357154`

### `userid`

- `$oid` — `string`  e.g. `5f15aca19aa2c74eba09a31f`, `65a1fe0e97e08648ba6a8d0b`, `65a87487c5adb13810d13dab`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `answers`

  - `[]` — `object`
    - `answer` — `string`  e.g. `Abhijeettt`, `[REDACTED-PHONE]`, `https://files.wiseapp.live/upload_files/5f15aca19aa2c74eba09`
    - `questionid` — `string`  e.g. `user_name`, `user_phone_number`, `user_profile_picture`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1706615470217`, `1706668504566`, `1706677523177`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1729167191767`, `1729874998399`, `1708564594754`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_012709_00061_zh2g4', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
