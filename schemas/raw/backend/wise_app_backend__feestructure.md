---
database: backend
table: wise_app_backend__feestructure
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/feeStructure
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:06:45+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__feestructure`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `active` | `string` | from deserializer |
| `classid` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `amount` | `string` | from deserializer |
| `type` | `string` | from deserializer |
| `startdate` | `string` | from deserializer |
| `enddate` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `__v` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__feestructure`(
  `_id` string COMMENT 'from deserializer', 
  `active` string COMMENT 'from deserializer', 
  `classid` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `amount` string COMMENT 'from deserializer', 
  `type` string COMMENT 'from deserializer', 
  `startdate` string COMMENT 'from deserializer', 
  `enddate` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/feeStructure'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1626548271')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
