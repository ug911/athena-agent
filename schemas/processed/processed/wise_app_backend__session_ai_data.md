---
database: processed
table: wise_app_backend__session_ai_data
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/session_ai_data/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:17:06+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__session_ai_data`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `sessionid` | `string` |  |
| `revisionnotes` | `string` |  |
| `quizids` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6996359eb46249215064a552`, `699635ad9ef6eaa92d9519fe`, `699636a1cdefe3f630b5bd76`

### `sessionid`

- `$oid` — `string`  e.g. `68b9b3790f1d469f0397878a`, `695bf31351067b0b0ac3cc1a`, `697f5d33458dce2fc646ccae`

### `revisionnotes`

  - `[]` — `object`
    - `content` — `string`  e.g. `Look at each term and find the largest number and letters th`, `After you choose the common outside part, divide each origin`, `If you have A^2 − B^2, factor as (A − B)(A + B). To apply th`
    - `title` — `string`  e.g. `Highest common factor (HCF) — take out what’s common`, `Why divide after factoring out the HCF`, `Difference of two squares — quick pattern`

### `quizids`

  - `[]` — `object`
    - `$oid` — `string`  e.g. `6996359eb46249215064a54c`, `6996359eb46249215064a54d`, `6996359eb46249215064a54e`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1771451806786`, `1771451821720`, `1771452065548`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1771451806786`, `1771451821720`, `1771452065548`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__session_ai_data`(
  `_id` string, 
  `sessionid` string, 
  `revisionnotes` string, 
  `quizids` string, 
  `createdat` string, 
  `updatedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/session_ai_data/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003058_00160_t59rj', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
