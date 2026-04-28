---
database: backend
table: wise_app_backend__chatmessage
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/ChatMessage
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:05:52+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__chatmessage`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `chatid` | `string` | from deserializer |
| `senderid` | `string` | from deserializer |
| `message` | `string` | from deserializer |
| `attachments` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__chatmessage`(
  `_id` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `chatid` string COMMENT 'from deserializer', 
  `senderid` string COMMENT 'from deserializer', 
  `message` string COMMENT 'from deserializer', 
  `attachments` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/ChatMessage'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1743015748')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
