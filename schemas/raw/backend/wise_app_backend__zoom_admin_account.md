---
database: backend
table: wise_app_backend__zoom_admin_account
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/zoom_admin_account
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:09:59+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__zoom_admin_account`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `refreshtoken` | `string` | from deserializer |
| `zoomaccountid` | `string` | from deserializer |
| `accountnumber` | `string` | from deserializer |
| `email` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `plantype` | `string` | from deserializer |
| `disabled` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__zoom_admin_account`(
  `_id` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `refreshtoken` string COMMENT 'from deserializer', 
  `zoomaccountid` string COMMENT 'from deserializer', 
  `accountnumber` string COMMENT 'from deserializer', 
  `email` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `plantype` string COMMENT 'from deserializer', 
  `disabled` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/zoom_admin_account'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1709549971')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
