---
database: processed
table: wise_app_backend__userpreference
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/userPreference/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:17:47+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__userpreference`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `userid` | `string` |  |
| `__v` | `string` |  |
| `registration` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6002f0c93221122157a06c3f`, `600ec02e783bc9d316c64894`, `60129c8745a09bb70fc8787f`

### `userid`

- `$oid` — `string`  e.g. `5fbdef454538c2bd916752c3`, `5f89437bb60b31eeeab3f569`, `5fc5dfbb24e11002f689ed7f`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `registration`

- `testing_module` — `object`
  - `registered` — `bool`  e.g. `true`, `true`, `true`
  - `registeredat` — `object`
    - `$date` — `object`
      - `$numberlong` — `string`  e.g. `1610805449535`, `1611579438965`, `1611832455618`

## DDL

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
  'trino_query_id'='20260428_012152_00115_cpg22', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
