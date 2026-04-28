---
database: processed
table: wise_app_backend__temp_user
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/temp_user/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:17:30+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__temp_user`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `phonenumber` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `5f1824e1e571492283caffb6`, `5f2027e2c291405be401d319`, `5f203748ec928f7bf75f5e79`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__temp_user`(
  `_id` string, 
  `phonenumber` string, 
  `__v` string, 
  `createdat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/temp_user/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_011842_00034_tgzpf', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
