---
database: backend
table: webapp__payout_users
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/webapp/payout_users
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:05:17+00:00'
sampled_rows: 0
---

# `backend.webapp__payout_users`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `razorpay_contact_id` | `string` | from deserializer |
| `user_id` | `string` | from deserializer |
| `updated_at` | `string` | from deserializer |
| `created_at` | `string` | from deserializer |
| `primary_payout_account_id` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.webapp__payout_users`(
  `_id` string COMMENT 'from deserializer', 
  `razorpay_contact_id` string COMMENT 'from deserializer', 
  `user_id` string COMMENT 'from deserializer', 
  `updated_at` string COMMENT 'from deserializer', 
  `created_at` string COMMENT 'from deserializer', 
  `primary_payout_account_id` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/webapp/payout_users'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1641895726')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
