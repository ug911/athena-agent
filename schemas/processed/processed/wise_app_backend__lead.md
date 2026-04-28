---
database: processed
table: wise_app_backend__lead
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/lead/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:15:37+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__lead`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `classid` | `string` |  |
| `email` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `name` | `string` |  |
| `phonenumber` | `string` |  |
| `registrationtoken` | `string` |  |
| `updatedat` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `64452ee8a3b1b6f2d15a051a`, `644a1349cee286d25ebe08ee`, `645b93b59e1a7f30173a819b`

### `classid`

- `$oid` — `string`  e.g. `64452c5e806af866c8b696a9`, `644a1247cee2864affbe074a`, `645b93449e1a7fd4c93a7f57`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1682255592508`, `1682576201894`, `1683723189197`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1682255889549`, `1682576201894`, `1683729621179`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__lead`(
  `_id` string, 
  `classid` string, 
  `email` string, 
  `__v` string, 
  `createdat` string, 
  `name` string, 
  `phonenumber` string, 
  `registrationtoken` string, 
  `updatedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/lead/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_005738_00142_p3eij', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
