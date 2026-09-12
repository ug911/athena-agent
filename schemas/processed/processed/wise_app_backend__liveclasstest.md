---
canonical: processed
table: wise_app_backend__liveclasstest
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/LiveClassTest/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:26:13+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__liveclasstest`

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
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `insightid` | `string` |  |
| `title` | `string` |  |
| `tags` | `string` |  |
| `visibletags` | `string` |  |
| `endsat` | `string` |  |
| `submissions` | `string` |  |
| `showresults` | `string` |  |
| `questions` | `string` |  |
| `agendaid` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `title`: `News Pod Quiz (×113)`, `General Knowledge about Wildlife (×37)`, `Are you a wise consumer? (×25)`, `Do you know?  (×7)`, `Untitled Quiz (×4)`, `NEWSPOD QUIZ (×4)`, `What did you comprehend? (×4)`, `Sample Quiz (×2)`, `9/16/24 (×1)`, `Probability Class Test-1 (×1)`, `Probality Class-2 quiz 1 (×1)`, `Probability Class-2 CBSE pattern quiz 2 (×1)`
- `showresults`: `false (×98)`, `true (×45)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `66a20e7f6bfdd671ede8885f`, `66a23fd8ece34727a6f703d8`, `66a3211713195153cfb202ce`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1721896575522`, `1721909208927`, `1721966871753`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1721896647264`, `1721909356128`, `1721966975422`

### `insightid`

- `$oid` — `string`  e.g. `66a20e629f3b500dd8829608`, `66a23f579f3b500dd8968bd6`, `66a320d39f3b500dd8e1ba36`

### `tags`

  - `[]` — `string`  e.g. `uuid_11001`, `uuid_110010`, `uuid_11001`

### `visibletags`

  - `[]` — `string`  e.g. `Wild_Animals`, `Birds`, `Sea_Animals`

### `endsat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1721896647257`, `1721909275873`, `1721966950160`

### `submissions`

  - `[]` — `object`
    - `submittedat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1721909261872`, `1721966937250`, `1721967017631`
    - `userid` — `string`  e.g. `U3R1ZGVudA==`, `U3R1ZGVudA==`, `U3R1ZGVudA==`

### `questions`

  - `[]` — `object`
    - `$oid` — `string`  e.g. `66a20e7f6bfdd64612e88855`, `66a20e7f6bfdd6ae6ce88856`, `66a20e7f6bfdd66cd1e88857`

### `agendaid`

- `$oid` — `string`  e.g. `66a20dde51d6c19136e0a02d`, `66a20dde51d6c19136e0a02d`, `66a20dde51d6c19136e0a02d`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__liveclasstest`(
  `_id` string, 
  `createdat` string, 
  `updatedat` string, 
  `insightid` string, 
  `title` string, 
  `tags` string, 
  `visibletags` string, 
  `endsat` string, 
  `submissions` string, 
  `showresults` string, 
  `questions` string, 
  `agendaid` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/LiveClassTest/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_010130_00214_9yf3j', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
