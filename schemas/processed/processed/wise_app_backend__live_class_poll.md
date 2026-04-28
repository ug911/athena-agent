---
database: processed
table: wise_app_backend__live_class_poll
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/live_class_poll/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:16:09+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__live_class_poll`

## Columns

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

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `type`: `POLL (×184)`, `QUIZ (×16)`
- `questiontype`: `SINGLE_CORRECT_ANSWER (×200)`
- `showresults`: `true (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `637b694d54224bfcf2b444ff`, `637b80cdd53d1d1506e3cf44`, `6380a7655cf4f46ac65d2920`

### `insightid`

- `$oid` — `string`  e.g. `637b68cca38aacf662a57f79`, `637b7fb8a38aacf662aaf44e`, `6380a75f3812375a5afe5741`

### `options`

- `a` — `object`
  - `text` — `string`  e.g. `👌 Amazing`, `👌 Amazing`, `A`
  - `votes` — `array<object>|array<unknown>`
    - `a.votes[]` — `object`
      - `timetaken` — `object`
        - `$numberint` — `string`  e.g. `3149`, `3673`, `2057`
      - `userid` — `string`  e.g. `6374d83e271de900dd26a83f`, `637f58f2d3e3e79a5a76a46c`, `637db5c7c08a217fd972d12b`
- `b` — `object`
  - `text` — `string`  e.g. `👍 Ok`, `👍 Ok`, `B`
  - `votes` — `array<object>|array<unknown>`
    - `b.votes[]` — `object`
      - `timetaken` — `object`
        - `$numberint` — `string`  e.g. `5312`, `6921`, `57781`
      - `userid` — `string`  e.g. `637f56cd28354456da9dcd65`, `637f2d37abf8c70bf7fd93f1`, `637b6376745b6d666bac97bf`
- `c` — `object`
  - `text` — `string`  e.g. `🐇 Too fast`, `🐇 Too fast`, `C`
  - `votes` — `array<object>|array<unknown>`
    - `c.votes[]` — `object`
      - `timetaken` — `object`
        - `$numberint` — `string`  e.g. `2319`, `2760`, `4981`
      - `userid` — `string`  e.g. `637b6376745b6d666bac97bf`, `637b6376745b6d666bac97bf`, `637b62a31aeff37812fca17e`
- `d` — `object`
  - `text` — `string`  e.g. `🤔 Need help`, `🤔 Need help`, `D`
  - `votes` — `array<object>|array<unknown>`
    - `d.votes[]` — `object`
      - `timetaken` — `object`
        - `$numberint` — `string`  e.g. `4893`, `55729`, `1770`
      - `userid` — `string`  e.g. `637b6376745b6d666bac97bf`, `637f58f2d3e3e79a5a76a46c`, `637b62a31aeff37812fca17e`

### `maxanswers`

- `$numberint` — `string`  e.g. `1`, `1`, `1`

### `correctanswers`

  - `[]` — `string`  e.g. `A`, `B`, `A`

### `votes`

  - `[]` — `object`
    - `answer` — `string`  e.g. `C`, `C`, `A`
    - `answers` — `array<string>`
      - `[].answers[]` — `string`  e.g. `C`, `C`, `A`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1695665800255`, `1695665800322`, `1695665800450`
    - `timetaken` — `object`
      - `$numberint` — `string`  e.g. `2319`, `2760`, `3149`
    - `updatedat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1695665800255`, `1695665800322`, `1695665800450`
    - `userid` — `string`  e.g. `637b6376745b6d666bac97bf`, `637b6376745b6d666bac97bf`, `6374d83e271de900dd26a83f`
    - `votedcorrect` — `bool`  e.g. `true`, `false`, `false`

### `tempvotedusers`



### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1695665800255`, `1695665800322`, `1695665800295`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1669032269851`, `1669038285177`, `1669375845760`

### `endsat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1669032276529`, `1669038291002`, `1669375853860`

## DDL

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
  'trino_query_id'='20260428_005803_00079_8syxc', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
