---
database: backend
table: wise_app_backend__session_ai_data
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/session_ai_data
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:08:48+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__session_ai_data`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `sessionid` | `string` | from deserializer |
| `revisionnotes` | `string` | from deserializer |
| `quizids` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__session_ai_data`(
  `_id` string COMMENT 'from deserializer', 
  `sessionid` string COMMENT 'from deserializer', 
  `revisionnotes` string COMMENT 'from deserializer', 
  `quizids` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
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
  's3://[REDACTED-BUCKET]/production/wise-app-backend/session_ai_data'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1773212712')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
