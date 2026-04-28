---
database: backend
table: wise_app_backend__vendorintegration
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/VendorIntegration
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:09:42+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__vendorintegration`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `settings` | `string` | from deserializer |
| `enabled` | `string` | from deserializer |
| `integrationtype` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__vendorintegration`(
  `_id` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `settings` string COMMENT 'from deserializer', 
  `enabled` string COMMENT 'from deserializer', 
  `integrationtype` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/VendorIntegration'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1743015864')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
