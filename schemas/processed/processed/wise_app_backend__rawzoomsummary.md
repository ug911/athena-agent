---
canonical: processed
table: wise_app_backend__rawzoomsummary
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/RawZoomSummary/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:27:24+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__rawzoomsummary`

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
| `sessionid` | `string` |  |
| `summaries` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `69b129b813cc1073afefc55d`, `69b13aa913cc1073af01d1f3`, `69b129bc13cc1073afefca6e`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1773218232130`, `1773222569666`, `1773218236128`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1773218232189`, `1773222569680`, `1773221398351`

### `sessionid`

- `$oid` — `string`  e.g. `69b11cbf4a1aeef703f8f228`, `6992ced6ca0c44da2f9cf45e`, `6998147c512d5e87c7155283`

### `summaries`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `69b129b8ceab13003ba439e6`, `69b129b8e222ac24cb98d85e`, `69b13aa9e222ac24cb9c2c7e`
    - `meetinguuid` — `string`  e.g. `ENcNIUkKRgWyGspgZ2dmcg==`, `ENcNIUkKRgWyGspgZ2dmcg==`, `q70XS5qIShunSxybKTiXTg==`
    - `summarydetails` — `array<object>|array<unknown>`
      - `[].summarydetails[]` — `object`
        - `label` — `string`  e.g. `Presentation Team Assignments Discussion`, `Team PPT Presentation Surprise Planning`, `Student Behavior and Presentation Management`
        - `summary` — `string`  e.g. `The team discussed preparations for an upcoming presentation`, `The meeting focused on planning a surprise activity involvin`, `The meeting focused on managing student behavior and assigni`
    - `summaryoverview` — `string`  e.g. `The meeting primarily focused on planning a surprise present`, `The meeting primarily focused on planning a surprise present`, `In this tutoring session, Divya and Ava worked through math `
    - `summarytitle` — `string`  e.g. `Meeting Summary for Six G Teacher (Grade 6G April Batch 2025`, `Meeting Summary for Six G Teacher (Grade 6G April Batch 2025`, `Meeting Summary for Ava (3 days/week)`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_014247_00052_df3qm', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->

### AI summary availability

- **One row per (session, summary batch); `summaries` is a JSON array.** A row can exist with an empty array, so presence of a row is *not* proof a summary was generated. Gate on `summaries IS NOT NULL AND summaries <> '[]'`.
- Join to sessions on `json_extract_scalar(sessionid, '$["$oid"]') = zoomers_v3.zoom_id` (or `wise_app_backend__zoom._id` `$oid`).
- Sibling artifact tables keyed the same way: `wise_app_backend__rawsessiontranscript` (VTT transcript files) and
  `wise_app_backend__session_ai_data` (AI revision notes + generated quiz ids). All three are independent —
  a session can have any subset.
- Coverage as of Aug 2026: ~93% of IN tutors running 4+ sessions/week have summaries; transcripts lag
  (~86% in IN, materially lower in NA). Summary coverage > transcript coverage in both regions.
