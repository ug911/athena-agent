---
database: processed
table: wise_app_backend__tags
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/tags/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:17:21+00:00'
sampled_rows: 6
---

# `processed.wise_app_backend__tags`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `type` | `string` |  |
| `tag` | `string` |  |
| `searchterm` | `string` |  |

## Inferred JSON structure

_Inferred from 6 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `60588251627829fd60b8abd2`, `605882c3627829fd60b8abd6`, `605882dd627829fd60b8abd7`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__tags`(
  `_id` string, 
  `type` string, 
  `tag` string, 
  `searchterm` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/tags/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_011830_00034_gvz55', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
