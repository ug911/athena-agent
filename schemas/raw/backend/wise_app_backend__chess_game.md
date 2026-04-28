---
database: backend
table: wise_app_backend__chess_game
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/chess_game
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:05:56+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__chess_game`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `status` | `string` | from deserializer |
| `classid` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `player1` | `string` | from deserializer |
| `player2` | `string` | from deserializer |
| `starttime` | `string` | from deserializer |
| `player1token` | `string` | from deserializer |
| `player2token` | `string` | from deserializer |
| `viewtoken` | `string` | from deserializer |
| `history` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `endreason` | `string` | from deserializer |
| `endtime` | `string` | from deserializer |
| `winner` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__chess_game`(
  `_id` string COMMENT 'from deserializer', 
  `status` string COMMENT 'from deserializer', 
  `classid` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `player1` string COMMENT 'from deserializer', 
  `player2` string COMMENT 'from deserializer', 
  `starttime` string COMMENT 'from deserializer', 
  `player1token` string COMMENT 'from deserializer', 
  `player2token` string COMMENT 'from deserializer', 
  `viewtoken` string COMMENT 'from deserializer', 
  `history` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `endreason` string COMMENT 'from deserializer', 
  `endtime` string COMMENT 'from deserializer', 
  `winner` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/chess_game'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1709549399')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
