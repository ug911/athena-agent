---
canonical: processed
table: wise_app_backend__session_ai_data
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/session_ai_data/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:27:54+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__session_ai_data`

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
| `sessionid` | `string` |  |
| `revisionnotes` | `string` |  |
| `quizids` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

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

_From `IN` (processed)._

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
  'trino_query_id'='20260811_003340_00016_55app', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->

### What this is (and isn't)

- Holds **AI revision notes** (`revisionnotes`: JSON array of `{title, content}`) and **generated quiz ids**
  (`quizids`: JSON array of `$oid`) per session. It is *not* the meeting summary and *not* the transcript —
  those live in `wise_app_backend__rawzoomsummary` and `wise_app_backend__rawsessiontranscript` respectively.
- Keyed by `sessionid` (`$oid`) like its sibling AI tables. `quizids` points at quiz documents; this table
  does not carry the quiz content itself.
