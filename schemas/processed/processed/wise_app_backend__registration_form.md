---
database: processed
table: wise_app_backend__registration_form
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/registration_form/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:16:55+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__registration_form`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `instituteid` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `enabled` | `string` |  |
| `fields` | `string` |  |
| `settings` | `string` |  |
| `updatedat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `enabled`: `true (×189)`, `false (×11)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `689054b30862ffb62a349bc1`, `689055200862ffb62a34d48d`, `689073d10862ffb62a46541f`

### `instituteid`

- `$oid` — `string`  e.g. `684c18285e6aca98ad2c2b09`, `684c18285e6aca98ad2c2b09`, `689047b6c114a704a08ab273`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1754289331896`, `1754289440777`, `1754297297919`

### `fields`

  - `[]` — `object`
    - `options` — `object`
      - `a` — `string`  e.g. `Male`, `8`, `11+`
      - `b` — `string`  e.g. `Female`, `9`, `GCSE`
      - `c` — `string`  e.g. `Other`, `10`, `A-Levels`
      - `d` — `string`  e.g. `6`, `Degree Level`, `UG Courses(CLAT/IPMAT/CUET)`
      - `e` — `string`  e.g. `Other`, `Others`, `UG (CUET/IPMAT)`
    - `questionid` — `string`  e.g. `user_name`, `user_phone_number`, `user_email`
    - `questiontext` — `string`  e.g. `Name`, `Phone Number`, `Email`
    - `required` — `bool`  e.g. `true`, `true`, `true`
    - `type` — `string`  e.g. `TEXT`, `PHONE`, `EMAIL`

### `settings`

- `disableupdatingsubmission` — `bool`  e.g. `false`, `false`, `false`
- `requiredforstudents` — `bool`  e.g. `false`, `true`, `true`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1754289342241`, `1754289440777`, `1754297297919`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__registration_form`(
  `_id` string, 
  `instituteid` string, 
  `__v` string, 
  `createdat` string, 
  `enabled` string, 
  `fields` string, 
  `settings` string, 
  `updatedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/registration_form/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_011732_00160_vxg48', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
