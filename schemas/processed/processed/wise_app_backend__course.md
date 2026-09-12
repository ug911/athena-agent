---
canonical: processed
table: wise_app_backend__course
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/course/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:22:43+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__course`

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
| `coursetype` | `string` |  |
| `classroomids` | `string` |  |
| `instituteid` | `string` |  |
| `title` | `string` |  |
| `coursecovers` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |
| `subtitle` | `string` |  |
| `description` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `coursetype`: `LIVE (×183)`, `RECORDED (×17)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6374f8b3ae0cf40a22f52790`, `6374ff7fef0e3c82a31e7e92`, `637506b07a6fe5500c48ad5c`

### `classroomids`

  - `[]` — `object`
    - `$oid` — `string`  e.g. `6374f8b3ae0cf40edcf5278f`, `6374ff7fef0e3c26a01e7e91`, `6375000300eac6f3815a11c8`

### `instituteid`

- `$oid` — `string`  e.g. `6374f8b3ae0cf43d91f5278e`, `6374ff7fef0e3cb1391e7e90`, `637506b07a6fe53e8a48ad5a`

### `coursecovers`



### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1668610227966`, `1668611967797`, `1668613808449`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1668610227966`, `1668612100027`, `1668613808449`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__course`(
  `_id` string, 
  `coursetype` string, 
  `classroomids` string, 
  `instituteid` string, 
  `title` string, 
  `coursecovers` string, 
  `createdat` string, 
  `updatedat` string, 
  `__v` string, 
  `subtitle` string, 
  `description` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/course/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_003428_00016_xsq88', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
