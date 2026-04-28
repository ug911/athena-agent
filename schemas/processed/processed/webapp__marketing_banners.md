---
database: processed
table: webapp__marketing_banners
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/webapp/marketing_banners/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:13:07+00:00'
sampled_rows: 200
---

# `processed.webapp__marketing_banners`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `template_id` | `string` |  |
| `user_id` | `string` |  |
| `image_url` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `69e9a5c5d9f03300019d83cd`, `69e8e335d9f03300019d8383`, `69e0c3e1d6f848000130c7b0`

### `template_id`

- `$oid` — `string`  e.g. `5fe1fee15bb98b36f02e0776`, `5fe1fee15bb98b36f02e0776`, `5fe1e559c3d253016cc07ca3`

### `user_id`

- `$oid` — `string`  e.g. `641a0f2e6f9c1a86202dcf5b`, `641a0f2e6f9c1a86202dcf5b`, `641a0f2e6f9c1a86202dcf5b`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1776920005130`, `1776870197207`, `1776337889767`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1776920005130`, `1776870197207`, `1776337889767`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.webapp__marketing_banners`(
  `_id` string, 
  `template_id` string, 
  `user_id` string, 
  `image_url` string, 
  `updated_at` string, 
  `created_at` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/webapp/marketing_banners/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_010727_00016_ymvhh', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
