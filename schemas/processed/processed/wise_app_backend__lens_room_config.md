---
canonical: processed
table: wise_app_backend__lens_room_config
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/lens_room_config/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:25:18+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__lens_room_config`

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
| `classid` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `polls` | `string` |  |
| `updatedat` | `string` |  |
| `feedbackconfig` | `string` |  |
| `leaderboardconfig` | `string` |  |
| `discussionconfig` | `string` |  |
| `allowzoomforhost` | `string` |  |
| `agendaids` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `allowzoomforhost`: `true (×34)`, `false (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `642d424443e715be7e983046`, `642d42f343e715be7e985ac0`, `642d431a43e715be7e986410`

### `classid`

- `$oid` — `string`  e.g. `642d41c8275549b4e57bc16a`, `641d7cf275473ee2392faa18`, `63a1a5256b4383002cf77227`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1680687684396`, `1680687859249`, `1680687898202`

### `polls`

  - `[]` — `object`
    - `correctanswers` — `array<string>|array<unknown>`
      - `[].correctanswers[]` — `string`  e.g. `C`, `A`, `D`
    - `iswordcloud` — `bool`  e.g. `false`, `false`, `false`
    - `maxanswers` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `options` — `object`
      - `a` — `object`
        - `text` — `string`  e.g. `A`, `👌 Amazing`, `boht hi bdia hai.. mja agyaa
boht hi bdia hai.. mja agyaa`
      - `b` — `object`
        - `text` — `string`  e.g. `B`, `👍 Ok`, `boht hi bdia hai.. mja agyaaboht hi bdia hai.. mja agyaaboht`
      - `c` — `object`
        - `text` — `string`  e.g. `C`, `🐇 Too fast`, `boht hi bdia hai.. mja agyaaboht hi bdia hai.. mja agyaa`
      - `d` — `object`
        - `text` — `string`  e.g. `D`, `🤔 Need help`, `boht hi bdia hai.. mja agyaaboht hi bdia hai.. mja agyaaboht`
      - `e` — `object`
        - `text` — `string`  e.g. `iOS`, `All of them are using Lens`
    - `question` — `string`  e.g. `Mark your response`, `How is the session going?`, `kese lga ?
`
    - `questiontype` — `string`  e.g. `SINGLE_CORRECT_ANSWER`, `SINGLE_CORRECT_ANSWER`, `SINGLE_CORRECT_ANSWER`
    - `type` — `string`  e.g. `POLL`, `POLL`, `POLL`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1680688253077`, `1680687860920`, `1710783203524`

### `feedbackconfig`

- `enabled` — `bool`  e.g. `true`, `true`, `true`
- `question` — `string`  e.g. `How was it ?`, `How was today's session?`, `Please share your feedback`

### `leaderboardconfig`

- `configurations` — `array<object>`
  - `configurations[]` — `object`
    - `category` — `string`  e.g. `attention`, `talktime`, `video`
    - `criteria` — `string`  e.g. `streak`, `streak`, `streak`
    - `duration` — `object`
      - `$numberint` — `string`  e.g. `30`, `5`, `30`
    - `points` — `object`
      - `$numberint` — `string`  e.g. `2`, `1`, `1`
- `enabled` — `bool`  e.g. `true`, `true`, `true`
- `visibletoparticipants` — `bool`  e.g. `true`, `true`, `false`

### `discussionconfig`

- `allowanonymous` — `bool`  e.g. `true`, `false`, `false`
- `autoapproval` — `bool`  e.g. `true`, `true`, `true`
- `enabled` — `bool`  e.g. `true`, `true`, `true`

### `agendaids`

  - `[]` — `object`
    - `$oid` — `string`  e.g. `65701a06f93004180f4ad9de`, `67a0aabc65167438144a9285`, `67a0ab638e92d42a67814260`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__lens_room_config`(
  `_id` string, 
  `classid` string, 
  `__v` string, 
  `createdat` string, 
  `polls` string, 
  `updatedat` string, 
  `feedbackconfig` string, 
  `leaderboardconfig` string, 
  `discussionconfig` string, 
  `allowzoomforhost` string, 
  `agendaids` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/lens_room_config/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_010130_00160_jfadk', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
