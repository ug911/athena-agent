---
database: processed
table: wise_app_backend__lens_event
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/lens_event/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:15:47+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__lens_event`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `eventname` | `string` |  |
| `insightid` | `string` |  |
| `userid` | `string` |  |
| `eventpayload` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `eventname`: `POINTS_GIVEN (×200)`
- `userid`: `637f57f1c266ea8050b35606 (×41)`, `63809a4bfab7fa014d91fba2 (×32)`, `63b6c2416b3447561b408c00 (×25)`, `637db5c7c08a217fd972d12b (×21)`, `637b2efbb83202bbf7505385 (×19)`, `63a55b9e5a426eb62ff5d7bc (×13)`, `637f58f2d3e3e79a5a76a46c (×10)`, `637db5ae5d97ca7a012a3881 (×8)`, `63a349dcffa60222308f886a (×8)`, `6384cb5d679f553a2dd30200 (×7)`, `637f2d37abf8c70bf7fd93f1 (×6)`, `U3VtaXQgd2Vi (×6)`, `Ymg= (×3)`, `RmFsZ3VuaQ== (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6433e0a11b02798c5e680e55`, `6433e0a10c8757aa851b6bf2`, `6433e0a51b02793009680efa`

### `insightid`

- `$oid` — `string`  e.g. `6433e01843e715be7e31198d`, `6433e01843e715be7e31198d`, `6433e01843e715be7e31198d`

### `eventpayload`

- `category` — `string`  e.g. `poll`, `poll`, `poll`
- `criteria` — `string`  e.g. `streak`, `streak`, `streak`
- `points` — `object`
  - `$numberint` — `string`  e.g. `1`, `1`, `1`
- `pollid` — `string`  e.g. `6433e09e1df91e2d4d13a32d`, `6433e09e1df91e2d4d13a32d`, `6433e09e1df91e2d4d13a32d`
- `userid` — `string`  e.g. `637b2efbb83202bbf7505385`, `63b6c2416b3447561b408c00`, `63809a4bfab7fa014d91fba2`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1681121441064`, `1681121441224`, `1681121445174`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1681121441064`, `1681121441224`, `1681121445174`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__lens_event`(
  `_id` string, 
  `eventname` string, 
  `insightid` string, 
  `userid` string, 
  `eventpayload` string, 
  `createdat` string, 
  `updatedat` string, 
  `__v` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/lens_event/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_005849_00142_ae9vb', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
