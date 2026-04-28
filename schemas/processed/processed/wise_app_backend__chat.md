---
database: processed
table: wise_app_backend__chat
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/Chat/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:14:00+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__chat`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `instituteid` | `string` |  |
| `classid` | `string` |  |
| `chatwithid` | `string` |  |
| `chattype` | `string` |  |
| `participants` | `string` |  |
| `unreadcounts` | `string` |  |
| `lastmessagetimestamp` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `chattype`: `CLASSROOM (×102)`, `INSTITUTE (×98)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `67c00c48f6b7db0bccf31d31`, `67c00c4ef6b7db0bccf32042`, `67c00c4ef6b7db0bccf32053`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1740639304815`, `1740639310104`, `1740639310268`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1740639305197`, `1740639310422`, `1743483927848`

### `instituteid`

- `$oid` — `string`  e.g. `655b3d81c327ce0025351d4c`, `655b3d81c327ce0025351d4c`, `63edd5a6a7f290704ee2224c`

### `classid`

- `$oid` — `string`  e.g. `66e014490b753c1e38a8aa39`, `66fbd319883b43ab05f3c5c8`, `6482cf7b27385167990c4e25`

### `chatwithid`

- `$oid` — `string`  e.g. `66e012ddd08d46625f41c7e3`, `66e012ddd08d46625f41c7e3`, `67172dd8cef0bf2270fadc56`

### `participants`

  - `[]` — `object`
    - `$oid` — `string`  e.g. `6659a908efdfab38cd36949b`, `66e012ddd08d46625f41c7e3`, `66e2cecc92b77f419623a497`

### `unreadcounts`

- `<oid>` — `object`
  - `$numberint` — `string`  e.g. `0`, `0`, `10`

### `lastmessagetimestamp`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1741592577633`, `1749060743129`, `1740641915340`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__chat`(
  `_id` string, 
  `createdat` string, 
  `updatedat` string, 
  `instituteid` string, 
  `classid` string, 
  `chatwithid` string, 
  `chattype` string, 
  `participants` string, 
  `unreadcounts` string, 
  `lastmessagetimestamp` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/Chat/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003048_00016_np32w', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
