---
canonical: processed
table: wise_app_backend__live_class_poll
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/live_class_poll/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:25:53+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__live_class_poll`

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
| `insightid` | `string` |  |
| `type` | `string` |  |
| `question` | `string` |  |
| `image` | `string` |  |
| `questiontype` | `string` |  |
| `options` | `string` |  |
| `maxanswers` | `string` |  |
| `correctanswers` | `string` |  |
| `votes` | `string` |  |
| `showresults` | `string` |  |
| `tempvotedusers` | `string` |  |
| `iswordcloud` | `string` |  |
| `agendaid` | `string` |  |
| `testid` | `string` |  |
| `tags` | `string` |  |
| `visibletags` | `string` |  |
| `updatedat` | `string` |  |
| `createdat` | `string` |  |
| `endsat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `type`: `POLL (×184)`, `QUIZ (×16)`
- `questiontype`: `SINGLE_CORRECT_ANSWER (×200)`
- `showresults`: `true (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `637b694d54224bfcf2b444ff`, `638094f3ffe800bf8a37e578`, `6384965766f1211b936dd911`

### `insightid`

- `$oid` — `string`  e.g. `637b68cca38aacf662a57f79`, `63808f6d3812375a5af9aa1e`, `6384963e3812375a5acc295c`

### `options`

- `a` — `object`
  - `text` — `string`  e.g. `👌 Amazing`, `A`, `A`
  - `votes` — `array<object>|array<unknown>`
    - `a.votes[]` — `object`
      - `timetaken` — `object`
        - `$numberint` — `string`  e.g. `2497`, `1832`, `3826`
      - `userid` — `string`  e.g. `637b6376745b6d666bac97bf`, `637b6376745b6d666bac97bf`, `637b6376745b6d666bac97bf`
- `b` — `object`
  - `text` — `string`  e.g. `👍 Ok`, `B`, `B`
  - `votes` — `array<object>|array<unknown>`
    - `b.votes[]` — `object`
      - `timetaken` — `object`
        - `$numberint` — `string`  e.g. `80283`, `7366`, `2506`
      - `userid` — `string`  e.g. `637b6376745b6d666bac97bf`, `637b6376745b6d666bac97bf`, `637b6376745b6d666bac97bf`
- `c` — `object`
  - `text` — `string`  e.g. `🐇 Too fast`, `C`, `C`
  - `votes` — `array<object>|array<unknown>`
    - `c.votes[]` — `object`
      - `timetaken` — `object`
        - `$numberint` — `string`  e.g. `2319`, `2760`, `17853`
      - `userid` — `string`  e.g. `637b6376745b6d666bac97bf`, `637b6376745b6d666bac97bf`, `637b6376745b6d666bac97bf`
- `d` — `object`
  - `text` — `string`  e.g. `🤔 Need help`, `D`, `D`
  - `votes` — `array<object>|array<unknown>`
    - `d.votes[]` — `object`
      - `timetaken` — `object`
        - `$numberint` — `string`  e.g. `219464`, `11708`, `273674`
      - `userid` — `string`  e.g. `632aac01f185a4b296b8f6cf`, `637dd0dc2d208b66307c06f3`, `63809a4bfab7fa014d91fba2`

### `maxanswers`

- `$numberint` — `string`  e.g. `1`, `1`, `1`

### `correctanswers`

  - `[]` — `string`  e.g. `A`, `B`, `C`

### `votes`

  - `[]` — `object`
    - `answer` — `string`  e.g. `C`, `C`, `B`
    - `answers` — `array<string>`
      - `[].answers[]` — `string`  e.g. `C`, `C`, `B`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1695665800255`, `1695665800322`, `1695665800607`
    - `timetaken` — `object`
      - `$numberint` — `string`  e.g. `2319`, `2760`, `80283`
    - `updatedat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1695665800255`, `1695665800322`, `1695665800607`
    - `userid` — `string`  e.g. `637b6376745b6d666bac97bf`, `637b6376745b6d666bac97bf`, `637b6376745b6d666bac97bf`
    - `votedcorrect` — `bool`  e.g. `true`, `false`, `false`

### `tempvotedusers`



### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1695665800255`, `1695665800240`, `1695665800187`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1669032269851`, `1669371123649`, `1669633623128`

### `endsat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1669032276529`, `1669375299794`, `1669633720434`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__live_class_poll`(
  `_id` string, 
  `insightid` string, 
  `type` string, 
  `question` string, 
  `image` string, 
  `questiontype` string, 
  `options` string, 
  `maxanswers` string, 
  `correctanswers` string, 
  `votes` string, 
  `showresults` string, 
  `tempvotedusers` string, 
  `iswordcloud` string, 
  `agendaid` string, 
  `testid` string, 
  `tags` string, 
  `visibletags` string, 
  `updatedat` string, 
  `createdat` string, 
  `endsat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/live_class_poll/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_010246_00124_wem67', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
