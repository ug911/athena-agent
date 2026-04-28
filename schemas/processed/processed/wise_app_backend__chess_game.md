---
database: processed
table: wise_app_backend__chess_game
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/chess_game/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:14:05+00:00'
sampled_rows: 54
---

# `processed.wise_app_backend__chess_game`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `status` | `string` |  |
| `classid` | `string` |  |
| `userid` | `string` |  |
| `player1` | `string` |  |
| `player2` | `string` |  |
| `starttime` | `string` |  |
| `player1token` | `string` |  |
| `player2token` | `string` |  |
| `viewtoken` | `string` |  |
| `history` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |
| `endreason` | `string` |  |
| `endtime` | `string` |  |
| `winner` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 54 sampled rows. Distribution shown as `value (×count)`._

- `status`: `ENDED (×54)`
- `endreason`: `ENDED_BY_TEACHER (×36)`, `RESIGNATION (×17)`, `CHECKMATE (×1)`
- `winner`: `p2 (×14)`, `p1 (×8)`

## Inferred JSON structure

_Inferred from 54 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6536567310d7f482052eaa81`, `653a1befd3d2e0de484c365c`, `653beda8528de61fcbc51aee`

### `classid`

- `$oid` — `string`  e.g. `64105682547ace83d3f30c8b`, `644b6359ed75cad94b4af6fc`, `653bebf7b85b7409a1573084`

### `player1`

- `name` — `string`  e.g. `Vishwas`, `Mubeen M`, `Ghazi`
- `playerid` — `string`  e.g. `632aac01f185a4b296b8f6cf`, `637b62a31aeff37812fca17e`, `653bebf7b85b748302573081`

### `player2`

- `name` — `string`  e.g. `VD`, `MM2`, `W`
- `playerid` — `string`  e.g. `VkQ=`, `TU0y`, `Vw==`

### `starttime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1698059891199`, `1698307055747`, `1698426280236`

### `history`

  - `[]` — `object`
    - `after` — `string`  e.g. `rnbqkbnr/pppppppp/8/8/3P4/8/PPP1PPPP/RNBQKBNR b KQkq - 0 1`, `rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1`, `rnbqkbnr/ppp1pppp/3p4/8/4P3/8/PPPP1PPP/RNBQKBNR w KQkq - 0 2`
    - `before` — `string`  e.g. `rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1`, `rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1`, `rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq - 0 1`
    - `color` — `string`  e.g. `w`, `w`, `b`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1702534965298`, `1702534968265`, `1702534971695`
    - `flags` — `string`  e.g. `b`, `b`, `n`
    - `from` — `string`  e.g. `d2`, `e2`, `d7`
    - `lan` — `string`  e.g. `d2d4`, `e2e4`, `d7d6`
    - `piece` — `string`  e.g. `p`, `p`, `p`
    - `san` — `string`  e.g. `d4`, `e4`, `d6`
    - `to` — `string`  e.g. `d4`, `e4`, `d6`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1698059891201`, `1698307055751`, `1698426280240`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1698059899226`, `1698307130693`, `1698427725483`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `endtime`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1698059899226`, `1698307130691`, `1698427725483`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__chess_game`(
  `_id` string, 
  `status` string, 
  `classid` string, 
  `userid` string, 
  `player1` string, 
  `player2` string, 
  `starttime` string, 
  `player1token` string, 
  `player2token` string, 
  `viewtoken` string, 
  `history` string, 
  `createdat` string, 
  `updatedat` string, 
  `__v` string, 
  `endreason` string, 
  `endtime` string, 
  `winner` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/chess_game/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003136_00197_77mqg', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
