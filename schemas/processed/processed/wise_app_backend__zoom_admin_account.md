---
database: processed
table: wise_app_backend__zoom_admin_account
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/zoom_admin_account/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:18:12+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__zoom_admin_account`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `userid` | `string` |  |
| `refreshtoken` | `string` |  |
| `zoomaccountid` | `string` |  |
| `accountnumber` | `string` |  |
| `email` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |
| `plantype` | `string` |  |
| `disabled` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `plantype`: `PRO (×191)`, `BASIC (×9)`
- `disabled`: `false (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `63f8b2037eb779515cf43d21`, `659cfb6545a66fc13d0ad1d5`, `65e7197f40cc0fcfdc7b21f8`

### `userid`

- `$oid` — `string`  e.g. `601cccadac6b3b85b94c4412`, `655604dee0a28c6bc79b0485`, `65ded8da14f878f9106c3dcc`

### `accountnumber`

- `$numberdouble` — `string`  e.g. `7.00944599E+09`, `5.087562481E+09`, `7.035772939E+09`
- `$numberint` — `string`  e.g. `110988842`, `50263251`, `50130211`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1677242883555`, `1704786789748`, `1709644159599`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1727696226679`, `1727423196228`, `1727662945146`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__zoom_admin_account`(
  `_id` string, 
  `userid` string, 
  `refreshtoken` string, 
  `zoomaccountid` string, 
  `accountnumber` string, 
  `email` string, 
  `createdat` string, 
  `updatedat` string, 
  `__v` string, 
  `plantype` string, 
  `disabled` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/zoom_admin_account/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_012236_00124_c3a83', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
