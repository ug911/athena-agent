---
database: processed
table: wise_app_backend__live_class_agendas_25_oct
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/backup/2024_10_25_00_01/wise-app-backend/live_class_agendas
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:15:58+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__live_class_agendas_25_oct`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `title` | `string` |  |
| `description` | `string` |  |
| `agendaitems` | `string` |  |
| `instituteid` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `65534d56ad19b127f9996ac6`, `65534dba85fafb1ebba04a22`, `65534e5784e27d883f1931fb`

### `agendaitems`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `65534d56ad19b1112f996ac7`, `65534dba85fafbffe0a04a23`, `65534dba85fafbb521a04a24`
    - `data` — `object`
      - `correctanswers` — `array<string>`
        - `[].data.correctanswers[]` — `string`  e.g. `C`, `B`, `A`
      - `image` — `string`  e.g. `https://example.com/image.jpg`, `https://example.com/image.jpg`
      - `iswordcloud` — `bool`  e.g. `false`, `false`, `false`
      - `maxanswers` — `object`
        - `$numberint` — `string`  e.g. `1`, `1`, `1`
      - `options` — `object`
        - `a` — `object`
          - `text` — `string`  e.g. `2`, `1`, `Australia`
        - `b` — `object`
          - `text` — `string`  e.g. `3`, `2`, `West Indies`
        - `c` — `object`
          - `text` — `string`  e.g. `4`, `3`, `Pakistan`
        - `d` — `object`
          - `text` — `string`  e.g. `5`, `4`, `Sri Lanka`
        - `e` — `object`
          - `text` — `string`  e.g. `Windows Desktop`, `10+, don't even ASK how many... I'm a veteran.`, `⭐️ (1 star)`
      - `question` — `string`  e.g. `What is 2+2?`, `How many times has India won the World Cup?`, `Who has won most number of times?`
      - `questions` — `array<object>`
        - `[].data.questions[]` — `object`
          - `correctanswers` — `array<string>`
            - `[].data.questions[].correctanswers[]` — `string`  e.g. `B`, `C`, `C`
          - `image` — `string`  e.g. `https://files.wiseapp.live/proxy/18867d45576d8283d6fabb82406`, `https://files.wiseapp.live/proxy/18867d45576d8283d6fabb82406`, `https://files.wiseapp.live/proxy/18867d45576d8283d6fabb82406`
          - `iswordcloud` — `bool`  e.g. `false`, `false`, `false`
          - `markingscheme` — `object`
            - `correct` — `object`
              - `$numberint` — `string`  e.g. `1`, `1`, `1`
            - `incorrect` — `object`
              - `$numberdouble` — `string`  e.g. `-0.25`, `-0.25`, `-0.25`
          - `maxanswers` — `object`
            - `$numberint` — `string`  e.g. `1`, `1`, `1`
          - `options` — `object`
            - `a` — `object`
              - `image` — `string`  e.g. `https://files.wiseapp.live/proxy/18867d45576d8283d6fabb82406`, `https://files.wiseapp.live/proxy/18867d45576d8283d6fabb82406`, `https://files.wiseapp.live/proxy/18867d45576d8283d6fabb82406`
              - `text` — `string`  e.g. `<p>1</p>`, `1`, `1`
            - `b` — `object`
              - `image` — `string`  e.g. `https://files.wiseapp.live/proxy/18867d45576d8283d6fabb82406`, `https://files.wiseapp.live/proxy/18867d45576d8283d6fabb82406`, `https://files.wiseapp.live/proxy/18867d45576d8283d6fabb82406`
              - `text` — `string`  e.g. `<p>2</p>`, `2`, `2`
            - `c` — `object`
              - `image` — `string`  e.g. `https://files.wiseapp.live/proxy/18867d45576d8283d6fabb82406`, `https://files.wiseapp.live/proxy/18867d45576d8283d6fabb82406`, `https://files.wiseapp.live/proxy/18867d45576d8283d6fabb82406`
              - `text` — `string`  e.g. `<p>3</p>`, `3`, `3`
            - `d` — `object`
              - `image` — `string`  e.g. `https://files.wiseapp.live/proxy/18867d45576d8283d6fabb82406`, `https://files.wiseapp.live/proxy/18867d45576d8283d6fabb82406`, `https://files.wiseapp.live/proxy/18867d45576d8283d6fabb82406`
              - `text` — `string`  e.g. `<p>4</p>`, `4`, `4`
            - `e` — `object`
              - `text` — `string`  e.g. `<p>asdf</p>`
          - `question` — `string`  e.g. `<p>1</p>`, `What is the square root of 4?`, `What is the square root of 4?`
          - `questiontype` — `string`  e.g. `SINGLE_CORRECT_ANSWER`, `SINGLE_CORRECT_ANSWER`, `SINGLE_CORRECT_ANSWER`
          - `tags` — `array<string>|array<unknown>`
            - `[].data.questions[].tags[]` — `string`  e.g. `tag1`, `tag2`, `question_tag1`
          - `type` — `string`  e.g. `QUIZ`, `QUIZ`, `QUIZ`
          - `visibletags` — `array<string>|array<unknown>`
            - `[].data.questions[].visibletags[]` — `string`  e.g. `tag1`, `tag2`, `question_visible_tag1`
      - `questiontype` — `string`  e.g. `SINGLE_CORRECT_ANSWER`, `SINGLE_CORRECT_ANSWER`, `SINGLE_CORRECT_ANSWER`
      - `tags` — `array<string>|array<unknown>`
        - `[].data.tags[]` — `string`  e.g. `tag1`, `tag2`, `agenda_item_tag1`
      - `title` — `string`  e.g. `Untitled Quiz`, `Exit ticket 1`, `Exit ticket 1`
      - `type` — `string`  e.g. `QUIZ`, `QUIZ`, `QUIZ`
      - `visibletags` — `array<string>|array<unknown>`
        - `[].data.visibletags[]` — `string`  e.g. `tag1`, `tag2`, `agenda_item_visible_tag1`
    - `tags` — `array<string>|array<unknown>`
      - `[].tags[]` — `string`  e.g. `tag1`, `tag2`, `agenda_item_tag1`
    - `title` — `string`  e.g. `Where have you joined from?`, `Please switch on your camera`, `Mention 3 things which you have worked on since last standup`
    - `type` — `string`  e.g. `POLL`, `POLL`, `POLL`
    - `visibletags` — `array<string>|array<unknown>`
      - `[].visibletags[]` — `string`  e.g. `tag1`, `tag2`, `agenda_item_visible_tag1`

### `instituteid`

- `$oid` — `string`  e.g. `63a1a5256b4383002cf7710e`, `63a55b9e5a426e7e2ff5d7bd`, `63a1a5256b4383002cf77115`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1699958102947`, `1699958202985`, `1699958359027`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1699958102947`, `1699958202985`, `1699958359027`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__live_class_agendas_25_oct`(
  `_id` string, 
  `title` string, 
  `description` string, 
  `agendaitems` string, 
  `instituteid` string, 
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
  's3://[REDACTED-BUCKET]/backup/2024_10_25_00_01/wise-app-backend/live_class_agendas'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'presto_query_id'='20241108_012009_00052_qp4mi', 
  'presto_version'='0.215-21789-gf312cbf', 
  'totalSize'='-1', 
  'transactional'='false', 
  'transient_lastDdlTime'='1731047469')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
