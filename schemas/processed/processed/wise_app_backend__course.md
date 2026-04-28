---
database: processed
table: wise_app_backend__course
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/course/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:14:38+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__course`

## Columns

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

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `coursetype`: `LIVE (×184)`, `RECORDED (×16)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `633bd8f7886a2c7cb7a542e1`, `633bf7a2e97c0b69288c6e10`, `633bf7e500570a822a78bcff`

### `classroomids`

  - `[]` — `object`
    - `$oid` — `string`  e.g. `633bd8f7886a2c4b02a542e0`, `633bf9ba00b94225c214e74a`, `633bf9d9163e4221f2d023f0`

### `instituteid`

- `$oid` — `string`  e.g. `633bd8f7886a2c68d7a542df`, `633bd8f7886a2c68d7a542df`, `633bd8f7886a2c68d7a542df`

### `coursecovers`

  - `[]` — `object`
    - `link` — `string`  e.g. `https://files.wiseapp.live/upload_files/633bd6286cdbb6357812`, `https://files.wiseapp.live/upload_files/6093c17ef339108cdb84`, `https://files.wiseapp.live/upload_files/6093c17ef339108cdb84`
    - `type` — `string`  e.g. `image`, `image`, `image`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1664866551129`, `1664874402713`, `1664874469157`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1664885448052`, `1664876901134`, `1664886453445`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

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
  'trino_query_id'='20260428_003109_00007_ekbd4', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
