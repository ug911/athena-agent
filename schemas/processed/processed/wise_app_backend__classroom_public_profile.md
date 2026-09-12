---
canonical: processed
table: wise_app_backend__classroom_public_profile
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/classroom_public_profile/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:22:28+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__classroom_public_profile`

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
| `classid` | `string` |  |
| `__v` | `string` |  |
| `classcovers` | `string` |  |
| `createdat` | `string` |  |
| `description` | `string` |  |
| `subtitle` | `string` |  |
| `title` | `string` |  |
| `updatedat` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `645a7b38fb7e2ae52af813f1`, `645a7d42fb7e2ae52af87eb5`, `645a7d42fb7e2ae52af87ec6`

### `classid`

- `$oid` — `string`  e.g. `6347f137dda9ba2c7b286fb7`, `6371db5a96d4b8dd36c3a0b7`, `637b54eaaddbabe038d28cb5`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `classcovers`

  - `[]` — `object`
    - `link` — `string`  e.g. `https://files.wiseapp.live/upload_files/5f24052520955e1aff46`, `https://files.wiseapp.live/upload_files/6200f1e9df223de403f2`, `https://files.wiseapp.live/upload_files/6200f1e9df223de403f2`
    - `type` — `string`  e.g. `image`, `image`, `image`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1683651384445`, `1683651906144`, `1683651906144`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1683652692987`, `1683652696071`, `1683652696071`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__classroom_public_profile`(
  `_id` string, 
  `classid` string, 
  `__v` string, 
  `classcovers` string, 
  `createdat` string, 
  `description` string, 
  `subtitle` string, 
  `title` string, 
  `updatedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/classroom_public_profile/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_012810_00133_hff4p', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
