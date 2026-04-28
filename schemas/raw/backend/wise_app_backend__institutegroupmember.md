---
database: backend
table: wise_app_backend__institutegroupmember
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/InstituteGroupMember
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:07:17+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__institutegroupmember`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `groupid` | `string` | from deserializer |
| `type` | `string` | from deserializer |
| `memberid` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__institutegroupmember`(
  `_id` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `groupid` string COMMENT 'from deserializer', 
  `type` string COMMENT 'from deserializer', 
  `memberid` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/InstituteGroupMember'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1743015798')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
