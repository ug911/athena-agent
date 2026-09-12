---
canonical: processed
table: wise_app_backend__userpreference
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/userPreference/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:29:29+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__userpreference`

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
| `userid` | `string` |  |
| `__v` | `string` |  |
| `registration` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `5fa00229ee695513238e55d3`, `5fa0096aee695513238f27a5`, `5fa0a7fdee695513239ac272`

### `userid`

- `$oid` — `string`  e.g. `5f114ad25a61c636f00bc1d8`, `5f12d7d088cd370409e738ec`, `5f528ea7d95ad2443b8ef7b6`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `registration`

- `testing_module` — `object`
  - `registered` — `bool`  e.g. `true`, `true`, `true`
  - `registeredat` — `object`
    - `$date` — `object`
      - `$numberlong` — `string`  e.g. `1604549727520`, `1605159856150`, `1604364285953`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__userpreference`(
  `_id` string, 
  `userid` string, 
  `__v` string, 
  `registration` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/userPreference/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_013207_00007_24vzn', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
