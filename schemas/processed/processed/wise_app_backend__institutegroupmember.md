---
canonical: processed
table: wise_app_backend__institutegroupmember
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/InstituteGroupMember/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:24:37+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__institutegroupmember`

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
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `groupid` | `string` |  |
| `type` | `string` |  |
| `memberid` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `type`: `CLASSROOM (×193)`, `STUDENT (×7)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `661d0f35ad2b60ded8f0bd34`, `661d0f36ad2b605df1f0bd5a`, `661d1302eafbf578ac696ba2`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1713180469145`, `1713180470033`, `1713181442490`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1713180469145`, `1713180470033`, `1713181442490`

### `groupid`

- `$oid` — `string`  e.g. `661d0f29eafbf513a668dc79`, `661d0f29eafbf513a668dc79`, `661d12f733faf3a94b528d04`

### `memberid`

- `$oid` — `string`  e.g. `619dee2b05daebcb4d3fcc76`, `6200f1e9df223de403f26533`, `639b112c6a879edef86f07fc`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__institutegroupmember`(
  `_id` string, 
  `createdat` string, 
  `updatedat` string, 
  `groupid` string, 
  `type` string, 
  `memberid` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/InstituteGroupMember/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_003743_00025_8gyay', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
