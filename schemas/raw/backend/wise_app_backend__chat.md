---
database: backend
table: wise_app_backend__chat
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/Chat
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:05:49+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__chat`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `instituteid` | `string` | from deserializer |
| `classid` | `string` | from deserializer |
| `chatwithid` | `string` | from deserializer |
| `chattype` | `string` | from deserializer |
| `participants` | `string` | from deserializer |
| `unreadcounts` | `string` | from deserializer |
| `lastmessagetimestamp` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__chat`(
  `_id` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `instituteid` string COMMENT 'from deserializer', 
  `classid` string COMMENT 'from deserializer', 
  `chatwithid` string COMMENT 'from deserializer', 
  `chattype` string COMMENT 'from deserializer', 
  `participants` string COMMENT 'from deserializer', 
  `unreadcounts` string COMMENT 'from deserializer', 
  `lastmessagetimestamp` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/Chat'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1743015733')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
