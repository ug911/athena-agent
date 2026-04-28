---
database: backend
table: wise_app_backend__googlecalendarevent
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/GoogleCalendarEvent
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:06:48+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__googlecalendarevent`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `sessionid` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `starttime` | `string` | from deserializer |
| `endtime` | `string` | from deserializer |
| `title` | `string` | from deserializer |
| `description` | `string` | from deserializer |
| `googleeventid` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__googlecalendarevent`(
  `_id` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `sessionid` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `starttime` string COMMENT 'from deserializer', 
  `endtime` string COMMENT 'from deserializer', 
  `title` string COMMENT 'from deserializer', 
  `description` string COMMENT 'from deserializer', 
  `googleeventid` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/GoogleCalendarEvent'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1743015771')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
