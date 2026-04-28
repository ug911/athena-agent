---
database: backend
table: wise_app_backend__premium_order
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/wise-app-backend/PremiumOrder
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:08:08+00:00'
sampled_rows: 0
---

# `backend.wise_app_backend__premium_order`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `status` | `string` | from deserializer |
| `licensecount` | `string` | from deserializer |
| `userid` | `string` | from deserializer |
| `startsfrom` | `string` | from deserializer |
| `endsat` | `string` | from deserializer |
| `amount` | `string` | from deserializer |
| `createdat` | `string` | from deserializer |
| `updatedat` | `string` | from deserializer |
| `type` | `string` | from deserializer |
| `plantype` | `string` | from deserializer |
| `premiumplan` | `string` | from deserializer |
| `billingperiod` | `string` | from deserializer |
| `plandisplayname` | `string` | from deserializer |
| `planmetadata` | `string` | from deserializer |
| `premiumplantype` | `string` | from deserializer |
| `renewson` | `string` | from deserializer |
| `__v` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.wise_app_backend__premium_order`(
  `_id` string COMMENT 'from deserializer', 
  `status` string COMMENT 'from deserializer', 
  `licensecount` string COMMENT 'from deserializer', 
  `userid` string COMMENT 'from deserializer', 
  `startsfrom` string COMMENT 'from deserializer', 
  `endsat` string COMMENT 'from deserializer', 
  `amount` string COMMENT 'from deserializer', 
  `createdat` string COMMENT 'from deserializer', 
  `updatedat` string COMMENT 'from deserializer', 
  `type` string COMMENT 'from deserializer', 
  `plantype` string COMMENT 'from deserializer', 
  `premiumplan` string COMMENT 'from deserializer', 
  `billingperiod` string COMMENT 'from deserializer', 
  `plandisplayname` string COMMENT 'from deserializer', 
  `planmetadata` string COMMENT 'from deserializer', 
  `premiumplantype` string COMMENT 'from deserializer', 
  `renewson` string COMMENT 'from deserializer', 
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
  's3://[REDACTED-BUCKET]/production/wise-app-backend/PremiumOrder'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1770302149')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
