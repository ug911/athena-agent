---
canonical: processed
table: webapp__registered_interests
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/webapp/registered_interests/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:20:24+00:00'
sampled_rows: 49
sampled_region: in
---

# `processed.webapp__registered_interests`

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
| `phone_number` | `string` |  |
| `registered_for` | `string` |  |
| `name` | `string` |  |
| `email` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 49 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `registered_for`: `zoom_licensing (×49)`

## Inferred JSON structure

_Inferred from 49 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `600941932144700001161102`, `6007044891793b00017d0f59`, `600595dd91793b00017d0f18`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1611219347812`, `1611072584888`, `1610978781995`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1611219347812`, `1611072584888`, `1610978781995`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.webapp__registered_interests`(
  `_id` string, 
  `phone_number` string, 
  `registered_for` string, 
  `name` string, 
  `email` string, 
  `updated_at` string, 
  `created_at` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/webapp/registered_interests/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_012537_00115_y5m75', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
