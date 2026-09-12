---
canonical: processed
table: wise_app_backend__registration_form
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/registration_form/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:27:32+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__registration_form`

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
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `enabled` | `string` |  |
| `fields` | `string` |  |
| `settings` | `string` |  |
| `updatedat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `enabled`: `true (×153)`, `false (×47)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `65b8e17eab16cf246ea8b8d9`, `65b8ec5dab16cf246eac4b0b`, `65b92f93ab16cf246ec4d496`

### `instituteid`

- `$oid` — `string`  e.g. `63a4008dc8d767a361f9bc95`, `646357316c7cce316b175c03`, `6594f8f7771359ce61357154`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1706615166736`, `1706617949193`, `1706635155004`

### `fields`

  - `[]` — `object`
    - `options` — `object`
      - `1` — `string`  e.g. `Aug 2026`
      - `2` — `string`  e.g. `Nov 2026`
      - `3` — `string`  e.g. `Feb 2027`
      - `4` — `string`  e.g. `May 2027`
      - `5` — `string`  e.g. `Aug 2027`
      - `6` — `string`  e.g. `Nov 2027`
      - `7` — `string`  e.g. `Not Decided`
      - `a` — `string`  e.g. `Male`, `Level I`, `4-6 Years`
      - `b` — `string`  e.g. `Female`, `Level II`, `7-9 Years`
      - `c` — `string`  e.g. `not prefer to say`, `Level III`, `10-14 Years`
      - `d` — `string`  e.g. `14-18 Years`, `7th`, `Fourth`
      - `e` — `string`  e.g. `18 and Above`, `VOCALS`, `Class 12`
    - `questionid` — `string`  e.g. `user_name`, `user_phone_number`, `user_email`
    - `questiontext` — `string`  e.g. `Name`, `Phone Number`, `Email`
    - `required` — `bool`  e.g. `true`, `true`, `true`
    - `type` — `string`  e.g. `TEXT`, `PHONE`, `EMAIL`

### `settings`

- `disableupdatingsubmission` — `bool`  e.g. `false`, `true`, `false`
- `required` — `bool`  e.g. `true`, `true`, `true`
- `requiredforstudents` — `bool`  e.g. `false`, `true`, `true`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1721371512112`, `1711089979617`, `1738335882700`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_012558_00025_xvt23', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
