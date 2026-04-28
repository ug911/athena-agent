---
database: backend
table: wise_app_backend__verification
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/verification
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:09:47+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__verification`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `attempts` | `string` | from deserializer |
| `resendcount` | `string` | from deserializer |
| `verified` | `string` | from deserializer |
| `phonenumber` | `string` | from deserializer |
| `resendwindow` | `string` | from deserializer |
| `expirytime` | `string` | from deserializer |
| `code` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `__v` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__verification`(
  `_id` string COMMENT 'from deserializer', 
  `attempts` string COMMENT 'from deserializer', 
  `resendcount` string COMMENT 'from deserializer', 
  `verified` string COMMENT 'from deserializer', 
  `phonenumber` string COMMENT 'from deserializer', 
  `resendwindow` string COMMENT 'from deserializer', 
  `expirytime` string COMMENT 'from deserializer', 
  `code` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
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
  's3://[REDACTED-BUCKET]/production/wise-app-backend/verification'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1626548430')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
