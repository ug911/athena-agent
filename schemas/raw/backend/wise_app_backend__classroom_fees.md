---
database: backend
table: wise_app_backend__classroom_fees
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/ClassroomFee
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:06:16+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__classroom_fees`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `classid` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `paymentoptions` | `string` | from deserializer |
| `metadata` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__classroom_fees`(
  `_id` string COMMENT 'from deserializer', 
  `classid` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `paymentoptions` string COMMENT 'from deserializer', 
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
  's3://[REDACTED-BUCKET]/production/wise-app-backend/ClassroomFee'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1659965013')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
