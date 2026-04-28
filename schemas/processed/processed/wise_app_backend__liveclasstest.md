---
database: processed
table: wise_app_backend__liveclasstest
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/LiveClassTest/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:16:15+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__liveclasstest`

## Columns

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

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `title`: `News Pod Quiz (×113)`, `General Knowledge about Wildlife (×37)`, `Are you a wise consumer? (×25)`, `Do you know?  (×7)`, `Untitled Quiz (×4)`, `NEWSPOD QUIZ (×4)`, `What did you comprehend? (×4)`, `Sample Quiz (×2)`, `9/16/24 (×1)`, `Probability Class Test-1 (×1)`, `Probality Class-2 quiz 1 (×1)`, `Probability Class-2 CBSE pattern quiz 2 (×1)`
- `showresults`: `false (×98)`, `true (×45)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `66a20e7f6bfdd671ede8885f`, `66a20eca6cf386174ab6a11a`, `66a20ede012a123a467aaed1`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1721896575522`, `1721896650499`, `1721896670166`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1721896647264`, `1721896652725`, `1721896671378`

### `insightid`

- `$oid` — `string`  e.g. `66a20e629f3b500dd8829608`, `66a20e629f3b500dd8829608`, `66a20e629f3b500dd8829608`

### `tags`

  - `[]` — `string`  e.g. `uuid_11001`, `uuid_110010`, `uuid_11001`

### `visibletags`

  - `[]` — `string`  e.g. `Wild_Animals`, `Birds`, `Sea_Animals`

### `endsat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1721896647257`, `1721896652718`, `1721896671373`

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
  'trino_query_id'='20260428_005732_00106_b23hv', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
