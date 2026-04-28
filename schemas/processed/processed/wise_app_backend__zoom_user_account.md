---
database: processed
table: wise_app_backend__zoom_user_account
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/zoom_user_account/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:18:15+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__zoom_user_account`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `ownerid` | `string` |  |
| `userid` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `zoomaccountid` | `string` |  |
| `zoomuserid` | `string` |  |
| `lastmeetingstartedon` | `string` |  |
| `licensed` | `string` |  |
| `accountassignedto` | `string` |  |
| `metadata` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `zoomaccountid`: `me_BV0wwTd-ffgw-jFFfiw (×175)`, `pxCuuYC1QGKAdEvnLhBZBA (×9)`, `isSTEmLeT066ykLC2WW6Xw (×3)`, `_rWzNQqzQQqZMuxRmLyFxg (×2)`, `ku_zvMvGRfmyZC8ipuYzmQ (×2)`, `ijN2YSscR72FKgnPGcpNMQ (×1)`, `msZgspLoRMuAu0d0Ua_AQQ (×1)`, `C5CxfRtlROuIFBpdo6_SUg (×1)`, `P-IkZAJcSP6ATjMqUsIt-w (×1)`, `K7zxK7gZRxCbl2O2llwvXw (×1)`, `FYmj_AC_TESmY93U0kePFw (×1)`, `_0ef4TefTRObPAMMl3xfcw (×1)`, `KecjAZ8qS7eK6q5BUvWoKg (×1)`, `-UGbzn60SnmfHS_7HJx9wA (×1)`
- `licensed`: `false (×167)`, `true (×33)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `63fe734e2e1f43bd9a7ba5f3`, `63feab432e1f43bd9a840851`, `63fed5532e1f43bd9a8c4efd`

### `ownerid`

- `$oid` — `string`  e.g. `601cccadac6b3b85b94c4412`, `601cccadac6b3b85b94c4412`, `601cccadac6b3b85b94c4412`

### `userid`

- `$oid` — `string`  e.g. `61fa5bb80bd3b2dd3747e064`, `600f9f2a13635f57ba58f06e`, `62318a2c240aad0403b597b6`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1677620046029`, `1677634371058`, `1677645139629`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1715862676010`, `1715862676010`, `1715862676010`

### `lastmeetingstartedon`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1715846840420`, `1715859266827`, `1715842858021`

### `accountassignedto`

- `$oid` — `string`  e.g. `61fa5bb80bd3b2dd3747e064`, `600f9f2a13635f57ba58f06e`, `62318a2c240aad0403b597b6`

### `metadata`

- `adminbasic` — `bool`  e.g. `true`, `true`, `true`
- `disablestoprecording` — `bool`  e.g. `true`, `true`, `true`
- `preventdeletion` — `bool`  e.g. `true`, `true`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__zoom_user_account`(
  `_id` string, 
  `ownerid` string, 
  `userid` string, 
  `__v` string, 
  `createdat` string, 
  `updatedat` string, 
  `zoomaccountid` string, 
  `zoomuserid` string, 
  `lastmeetingstartedon` string, 
  `licensed` string, 
  `accountassignedto` string, 
  `metadata` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/zoom_user_account/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_013246_00007_kqtq8', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
