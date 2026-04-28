---
database: processed
table: wise_app_backend__classparticipant
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/classparticipant/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:14:13+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__classparticipant`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `userid` | `string` |  |
| `classid` | `string` |  |
| `relation` | `string` |  |
| `status` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |
| `joinedon` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `relation`: `STUDENT (×196)`, `ADMIN (×4)`
- `status`: `ACCEPTED (×185)`, `REMOVED (×15)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `61c0977736c602000b761b51`, `61c0977736c602000b761b56`, `61c0978d2734790007063d55`

### `userid`

- `$oid` — `string`  e.g. `5f5ef13f2757f75ccca9c85a`, `5f5c481d2ccd101589b6f0a0`, `5f24052520955e1aff464606`

### `classid`

- `$oid` — `string`  e.g. `5fb610bc6def216d702d32fa`, `5fb610bc6def216d702d32fa`, `5fb8ab8cc91e3444349dc781`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1640011639115`, `1640011639115`, `1640011661163`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1640011639115`, `1640011639115`, `1702968854907`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `joinedon`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1605767356946`, `1605767356946`, `1605938060744`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__classparticipant`(
  `_id` string, 
  `userid` string, 
  `classid` string, 
  `relation` string, 
  `status` string, 
  `createdat` string, 
  `updatedat` string, 
  `__v` string, 
  `joinedon` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/classparticipant/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_002952_00016_ygewu', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
