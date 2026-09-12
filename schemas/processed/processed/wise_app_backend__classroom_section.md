---
canonical: processed
table: wise_app_backend__classroom_section
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/classroom_section/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:22:35+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__classroom_section`

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
| `sortkey` | `string` |  |
| `name` | `string` |  |
| `entities` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `65facb5e56cc197e4868e6d8`, `65fae73e9a41ad45fa44cc02`, `65fb2e81c435b160e0fe153b`

### `classid`

- `$oid` — `string`  e.g. `64eeeb0eff3b0606f4871eaf`, `65e809f03a487963f65e8b83`, `6585aa0fef6a94765e7b4154`

### `sortkey`

- `$numberint` — `string`  e.g. `2`, `5`, `2`

### `entities`

  - `[]` — `object`
    - `entityid` — `object`
      - `$oid` — `string`  e.g. `65facb7440f45fa9ea23230c`, `65fae75a552e381ba42115a0`, `65fb2e974f8c0a53a9245083`
    - `entitytype` — `string`  e.g. `RESOURCE`, `RESOURCE`, `RESOURCE`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1710934878062`, `1710942014097`, `1710960257724`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1710934900690`, `1710942042792`, `1710960305950`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__classroom_section`(
  `_id` string, 
  `classid` string, 
  `sortkey` string, 
  `name` string, 
  `entities` string, 
  `createdat` string, 
  `updatedat` string, 
  `__v` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/classroom_section/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_003250_00007_5ej78', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
