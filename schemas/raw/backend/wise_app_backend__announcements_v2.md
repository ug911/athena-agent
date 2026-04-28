---
database: backend
table: wise_app_backend__announcements_v2
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/announcements
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:05:38+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__announcements_v2`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `disablecommenting` | `string` | from deserializer |
| `pinneddiscussion` | `string` | from deserializer |
| `poll` | `string` | from deserializer |
| `polldata` | `string` | from deserializer |
| `title` | `string` | from deserializer |
| `description` | `string` | from deserializer |
| `date` | `string` | from deserializer |
| `time` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `classid` | `string` | from deserializer |
| `attachments` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `comments` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `lastcommentedat` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__announcements_v2`(
  `_id` string COMMENT 'from deserializer', 
  `disablecommenting` string COMMENT 'from deserializer', 
  `pinneddiscussion` string COMMENT 'from deserializer', 
  `poll` string COMMENT 'from deserializer', 
  `polldata` string COMMENT 'from deserializer', 
  `title` string COMMENT 'from deserializer', 
  `description` string COMMENT 'from deserializer', 
  `date` string COMMENT 'from deserializer', 
  `time` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `classid` string COMMENT 'from deserializer', 
  `attachments` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `comments` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `lastcommentedat` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/announcements'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1641898560')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
