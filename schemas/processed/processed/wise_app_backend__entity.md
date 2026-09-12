---
canonical: processed
table: wise_app_backend__entity
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/entity/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:23:02+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__entity`

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
| `entityid` | `string` |  |
| `__v` | `string` |  |
| `classid` | `string` |  |
| `createdat` | `string` |  |
| `entitysubtype` | `string` |  |
| `entitytype` | `string` |  |
| `sortkey` | `string` |  |
| `archived` | `string` |  |
| `metadata` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `entitysubtype`: `SCHEDULED (×187)`, `AD_HOC (×7)`, `FILE (×2)`, `video (×2)`, `DISCUSSION (×1)`
- `entitytype`: `SESSION (×194)`, `RESOURCE (×4)`, `TEST (×1)`, `DISCUSSION (×1)`
- `archived`: `false (×168)`, `true (×25)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `637f25299a6196165f4362bb`, `637f2547b056c63eb93688c2`, `637f25b64aef7fb801458c45`

### `entityid`

- `$oid` — `string`  e.g. `637f2529438fb09d1f6933db`, `637f2547438fb0eb876933e3`, `637f2583e5de0500010c5ef4`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `classid`

- `$oid` — `string`  e.g. `5f24056820955e1aff464608`, `5f24056820955e1aff464608`, `5f24056820955e1aff464608`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1669276969465`, `1669276999430`, `1669277110000`

### `sortkey`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1669287600000`, `1669276999430`, `1669277110000`

### `metadata`

- `subtype` — `string`  e.g. `youtube`, `youtube`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__entity`(
  `_id` string, 
  `entityid` string, 
  `__v` string, 
  `classid` string, 
  `createdat` string, 
  `entitysubtype` string, 
  `entitytype` string, 
  `sortkey` string, 
  `archived` string, 
  `metadata` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/entity/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_003322_00016_dgq2k', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
