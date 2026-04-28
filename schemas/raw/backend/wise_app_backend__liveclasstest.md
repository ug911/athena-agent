---
database: backend
table: wise_app_backend__liveclasstest
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/LiveClassTest
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:07:57+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__liveclasstest`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `insightid` | `string` | from deserializer |
| `title` | `string` | from deserializer |
| `tags` | `string` | from deserializer |
| `visibletags` | `string` | from deserializer |
| `endsat` | `string` | from deserializer |
| `submissions` | `string` | from deserializer |
| `showresults` | `string` | from deserializer |
| `questions` | `string` | from deserializer |
| `agendaid` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__liveclasstest`(
  `_id` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `insightid` string COMMENT 'from deserializer', 
  `title` string COMMENT 'from deserializer', 
  `tags` string COMMENT 'from deserializer', 
  `visibletags` string COMMENT 'from deserializer', 
  `endsat` string COMMENT 'from deserializer', 
  `submissions` string COMMENT 'from deserializer', 
  `showresults` string COMMENT 'from deserializer', 
  `questions` string COMMENT 'from deserializer', 
  `agendaid` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/LiveClassTest'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1743015807')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
