---
database: backend
table: wise_app_backend__live_class_poll
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/live_class_poll
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:07:49+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__live_class_poll`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `insightid` | `string` | from deserializer |
| `type` | `string` | from deserializer |
| `question` | `string` | from deserializer |
| `image` | `string` | from deserializer |
| `questiontype` | `string` | from deserializer |
| `options` | `string` | from deserializer |
| `maxanswers` | `string` | from deserializer |
| `correctanswers` | `string` | from deserializer |
| `votes` | `string` | from deserializer |
| `showresults` | `string` | from deserializer |
| `tempvotedusers` | `string` | from deserializer |
| `iswordcloud` | `string` | from deserializer |
| `agendaid` | `string` | from deserializer |
| `testid` | `string` | from deserializer |
| `tags` | `string` | from deserializer |
| `visibletags` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `endsat` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__live_class_poll`(
  `_id` string COMMENT 'from deserializer', 
  `insightid` string COMMENT 'from deserializer', 
  `type` string COMMENT 'from deserializer', 
  `question` string COMMENT 'from deserializer', 
  `image` string COMMENT 'from deserializer', 
  `questiontype` string COMMENT 'from deserializer', 
  `options` string COMMENT 'from deserializer', 
  `maxanswers` string COMMENT 'from deserializer', 
  `correctanswers` string COMMENT 'from deserializer', 
  `votes` string COMMENT 'from deserializer', 
  `showresults` string COMMENT 'from deserializer', 
  `tempvotedusers` string COMMENT 'from deserializer', 
  `iswordcloud` string COMMENT 'from deserializer', 
  `agendaid` string COMMENT 'from deserializer', 
  `testid` string COMMENT 'from deserializer', 
  `tags` string COMMENT 'from deserializer', 
  `visibletags` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `endsat` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/live_class_poll'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1743512243')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
