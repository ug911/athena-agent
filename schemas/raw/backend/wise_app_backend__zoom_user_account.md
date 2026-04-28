---
database: backend
table: wise_app_backend__zoom_user_account
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/zoom_user_account
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:10:02+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__zoom_user_account`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `ownerid` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `zoomaccountid` | `string` | from deserializer |
| `zoomuserid` | `string` | from deserializer |
| `lastmeetingstartedon` | `string` | from deserializer |
| `licensed` | `string` | from deserializer |
| `accountassignedto` | `string` | from deserializer |
| `metadata` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__zoom_user_account`(
  `_id` string COMMENT 'from deserializer', 
  `ownerid` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `zoomaccountid` string COMMENT 'from deserializer', 
  `zoomuserid` string COMMENT 'from deserializer', 
  `lastmeetingstartedon` string COMMENT 'from deserializer', 
  `licensed` string COMMENT 'from deserializer', 
  `accountassignedto` string COMMENT 'from deserializer', 
  `metadata` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/zoom_user_account'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1709549983')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
