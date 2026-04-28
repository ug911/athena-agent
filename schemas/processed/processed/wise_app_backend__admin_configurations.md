---
database: processed
table: wise_app_backend__admin_configurations
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/admin_configurations/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:13:40+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__admin_configurations`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `user_id` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `groups` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `627ba5d73e9f980001bd87cc`, `623aaf4e3d8b0a0001376694`, `623a09c94ebe3d00012c631e`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1652270550990`, `1648013134172`, `1647970761785`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1652270550990`, `1648013134172`, `1647970761785`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__admin_configurations`(
  `_id` string, 
  `user_id` string, 
  `updated_at` string, 
  `created_at` string, 
  `groups` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/admin_configurations/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003019_00007_qzsna', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
