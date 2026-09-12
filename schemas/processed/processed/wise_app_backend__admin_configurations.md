---
canonical: processed
table: wise_app_backend__admin_configurations
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/admin_configurations/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:20:43+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__admin_configurations`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |
| `NA` | `processed_na` |

_Schema parity: **identical** across regions._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `user_id` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `groups` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `627ba5d73e9f980001bd87cc`, `623aaf4e3d8b0a0001376694`, `623a09c94ebe3d00012c631e`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1652270550990`, `1648013134172`, `1647970761785`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1652270550990`, `1648013134172`, `1647970761785`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_003453_00007_ancak', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
