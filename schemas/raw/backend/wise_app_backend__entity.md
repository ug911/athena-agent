---
database: backend
table: wise_app_backend__entity
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/entity
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:06:34+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__entity`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `entityid` | `string` | from deserializer |
| `__v` | `string` | from deserializer |
| `classid` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `entitysubtype` | `string` | from deserializer |
| `entitytype` | `string` | from deserializer |
| `sortkey` | `string` | from deserializer |
| `archived` | `string` | from deserializer |
| `metadata` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__entity`(
  `_id` string COMMENT 'from deserializer', 
  `entityid` string COMMENT 'from deserializer', 
  `__v` string COMMENT 'from deserializer', 
  `classid` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `entitysubtype` string COMMENT 'from deserializer', 
  `entitytype` string COMMENT 'from deserializer', 
  `sortkey` string COMMENT 'from deserializer', 
  `archived` string COMMENT 'from deserializer', 
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
  's3://[REDACTED-BUCKET]/production/wise-app-backend/entity'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1709549732')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
