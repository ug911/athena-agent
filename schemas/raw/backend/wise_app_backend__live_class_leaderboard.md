---
database: backend
table: wise_app_backend__live_class_leaderboard
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/live_class_leaderboard
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:07:46+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__live_class_leaderboard`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `insightid` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `pointstable` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__live_class_leaderboard`(
  `_id` string COMMENT 'from deserializer', 
  `insightid` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `pointstable` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/live_class_leaderboard'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1709549846')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
