---
database: processed
table: wise_app_backend__certificate_template
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/certificate_template/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:13:55+00:00'
sampled_rows: 3
---

# `processed.wise_app_backend__certificate_template`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `archived` | `string` |  |
| `htmltemplate` | `string` |  |
| `variables` | `string` |  |
| `previewimage` | `string` |  |
| `imagewidth` | `string` |  |
| `imageheight` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |

## Inferred JSON structure

_Inferred from 3 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `64be7cb920807f002d2afdf3`, `64be7cb920807f002d2afdf4`, `64f06ed6d7c67c3c202469c2`

### `variables`

  - `[]` — `object`
    - `charlimit` — `object|string`  e.g. `30`
      - `$numberint` — `string`  e.g. `50`, `50`, `50`
    - `defaultvalue` — `string`  e.g. `Indian Institute`, `Certificate`, `of completion`
    - `displayname` — `string`  e.g. `[REDACTED]`
    - `editable` — `bool|string`  e.g. `true`, `true`, `true`
    - `name` — `string`  e.g. `instituteName`, `title1`, `title2`
    - `stylable` — `bool`  e.g. `true`
    - `style` — `string`  e.g. `position: absolute; width:100%;font-weight: 500; font-family`
    - `type` — `string`  e.g. `TEXT`, `TEXT`, `TEXT`
    - `value` — `string`

### `imagewidth`

- `$numberint` — `string`  e.g. `1000`, `1000`, `1000`

### `imageheight`

- `$numberint` — `string`  e.g. `707`, `707`, `707`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1690205369159`, `1690205369160`, `1689840695798`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1690205369159`, `1690205369160`, `1689840695798`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__certificate_template`(
  `_id` string, 
  `archived` string, 
  `htmltemplate` string, 
  `variables` string, 
  `previewimage` string, 
  `imagewidth` string, 
  `imageheight` string, 
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
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/certificate_template/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003032_00025_ze542', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
