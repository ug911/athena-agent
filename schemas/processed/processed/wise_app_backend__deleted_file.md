---
database: processed
table: wise_app_backend__deleted_file
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/deleted_file/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:14:42+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__deleted_file`

## Columns

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

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `deletedfroms3`: `true (×173)`, `false (×27)`
- `entitytype`: `ASSESSMENT (×110)`, `RESOURCE (×84)`, `TEST (×5)`, `DISCUSSION (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6968bc9dd6ed5a951f34713a`, `6971fbaa05b94f4e85e723d2`, `6971fcfff9cb9dd821862896`

### `file`

- `_id` — `object`
  - `$oid` — `string`  e.g. `6968a6ecd6ed5a951f317e35`, `6971f97537c880bb4c7c6977`, `6971fbaa8d10aafc914da5a8`
- `filename` — `string`  e.g. `Topical test c3.AlyciaYeo`, `Topical test c3.AlyciaYeo`, `Topical test c3.AlyciaYeo`
- `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/68ff44fe73035d4c18ee`, `https://files.wiseapp.live/upload_files/68ff44fe73035d4c18ee`, `https://files.wiseapp.live/upload_files/68ff44fe73035d4c18ee`
- `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`
- `s3key` — `string`  e.g. `upload_files/68ff44fe73035d4c18ee9e27/upload_bcac5570-973a-4`, `upload_files/68ff44fe73035d4c18ee9e27/upload_5bc7d415-3d09-4`, `upload_files/68ff44fe73035d4c18ee9e27/upload_e7ba84c1-38c5-4`
- `size` — `object`
  - `$numberint` — `string`  e.g. `1620255`, `1620255`, `1620255`
- `type` — `string`  e.g. `file`, `file`, `file`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1768471709191`, `1769077674737`, `1769078015775`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777256564442`, `1777256564442`, `1777256564441`

## DDL

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
  'trino_query_id'='20260428_003044_00034_78gv2', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
