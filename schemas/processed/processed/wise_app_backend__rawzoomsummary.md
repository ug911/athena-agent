---
database: processed
table: wise_app_backend__rawzoomsummary
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/RawZoomSummary/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:16:51+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__rawzoomsummary`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `sessionid` | `string` |  |
| `summaries` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `693bbfdbc05630afe596e711`, `693bbfddc05630afe596e81b`, `693bbfe5c05630afe596ed80`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1765523419744`, `1765523421402`, `1765523429280`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1765523419744`, `1765523421402`, `1765523429280`

### `sessionid`

- `$oid` — `string`  e.g. `693bbcae7a8b51d228a705b7`, `693bbc94af2de4e24f499dc2`, `6932fd4664462e176fa30101`

### `summaries`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `693bbfdbaf2de4e24f4a2083`, `693bbfdd72e8ff63aab2629a`, `693bbfe57a8b51d228a7781b`
    - `meetinguuid` — `string`  e.g. `zYCUlkeGTsqHkG/bbuhlFw==`, `sfNWaWinRHu2B+1myy7HKQ==`, `cVYh1ZZ3RlmyU/nctCHKpw==`
    - `summarydetails` — `array<object>|array<unknown>`
      - `[].summarydetails[]` — `object`
        - `label` — `string`  e.g. `No Man's Sky Success Acknowledgment`, `LEGO Batman and Game Awards`, `Printing Options and Pre-test Completion`
        - `summary` — `string`  e.g. `Aryoko expressed gratitude on behalf of the Hello Games team`, `Aryoko hosted a show featuring Batman and announced the upco`, `The meeting focused on clarifying printing options and discu`
    - `summaryoverview` — `string`  e.g. `Aryoko represented the Hello Games team to express gratitude`, `The meeting began with a discussion of printing options and `, `Leanne discussed Mass Life Science, but the details of the c`
    - `summarytitle` — `string`  e.g. `Meeting Summary for Shaima Mustafa Fawzi (International Scho`, `Meeting Summary for Aryoko Aditya Nugroho (International Sch`, `Meeting Summary for Jasmine Kaur (5 days/week, 45 mins)`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__rawzoomsummary`(
  `_id` string, 
  `createdat` string, 
  `updatedat` string, 
  `sessionid` string, 
  `summaries` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/RawZoomSummary/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_012947_00232_axhk6', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
