---
database: backend
table: wise_app_backend__transaction
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/transaction
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:09:16+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__transaction`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `metadata` | `string` | from deserializer |
| `senderid` | `string` | from deserializer |
| `receiverid` | `string` | from deserializer |
| `amount` | `string` | from deserializer |
| `type` | `string` | from deserializer |
| `status` | `string` | from deserializer |
| `note` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `transactiontype` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `chargedat` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__transaction`(
  `_id` string COMMENT 'from deserializer', 
  `metadata` string COMMENT 'from deserializer', 
  `senderid` string COMMENT 'from deserializer', 
  `receiverid` string COMMENT 'from deserializer', 
  `amount` string COMMENT 'from deserializer', 
  `type` string COMMENT 'from deserializer', 
  `status` string COMMENT 'from deserializer', 
  `note` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `transactiontype` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `chargedat` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/wise-app-backend/transaction'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1764921418')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
