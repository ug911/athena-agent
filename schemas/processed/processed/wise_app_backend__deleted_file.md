---
canonical: processed
table: wise_app_backend__deleted_file
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/deleted_file/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:22:51+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__deleted_file`

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
| `deletedfroms3` | `string` |  |
| `file` | `string` |  |
| `entitytype` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `deletedfroms3`: `true (×200)`
- `entitytype`: `SESSION (×149)`, `RESOURCE (×34)`, `ASSESSMENT (×10)`, `DISCUSSION (×6)`, `TEST (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6a49127a8b3f0f7236a13385`, `6a4912bead774b3ffb06686d`, `6a4912c552943b48c6d20542`

### `file`

- `_id` — `object`
  - `$oid` — `string`  e.g. `6a49121922c9d57e21f52e6a`, `6a49125ca4dd66caf643f21b`, `6a4912848baf82080cf0fede`
- `filename` — `string`  e.g. `Entrepreneurship_Worksheet_Lesson5.pdf`, `Screenshot 2026-07-04 192958.png`, `Screenshot 2026-06-25 214923.png`
- `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/68e90291b9932c954a2e`, `https://files.wiseapp.live/upload_files/69d0e38898ee51775fcb`, `https://files.wiseapp.live/upload_files/69d0e38898ee51775fcb`
- `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`
- `s3key` — `string`  e.g. `upload_files/68e90291b9932c954a2e142d/upload_1a708775-7663-4`, `upload_files/69d0e38898ee51775fcb2b68/upload_a263cc69-df40-4`, `upload_files/69d0e38898ee51775fcb2b68/upload_3bd84d66-8554-4`
- `size` — `object`
  - `$numberint` — `string`  e.g. `3909`, `60264`, `35230`
- `type` — `string`  e.g. `pdf`, `image`, `image`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1783173754591`, `1783173822641`, `1783173829023`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1783821813641`, `1783821813648`, `1783821813641`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__deleted_file`(
  `_id` string, 
  `deletedfroms3` string, 
  `file` string, 
  `entitytype` string, 
  `__v` string, 
  `createdat` string, 
  `updatedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/deleted_file/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_003438_00061_8f8pv', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
