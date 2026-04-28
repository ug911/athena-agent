---
database: backend
table: webapp__payouts
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/webapp/payouts
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:05:21+00:00'
sampled_rows: 0
---

# `backend.webapp__payouts`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `status` | `string` | from deserializer |
| `currency` | `string` | from deserializer |
| `user_id` | `string` | from deserializer |
| `payout_account_id` | `string` | from deserializer |
| `amount` | `string` | from deserializer |
| `amount_metadata` | `string` | from deserializer |
| `payout_metadata` | `string` | from deserializer |
| `updated_at` | `string` | from deserializer |
| `created_at` | `string` | from deserializer |
| `razorpay_payout_id` | `string` | from deserializer |
| `charged_at` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.webapp__payouts`(
  `_id` string COMMENT 'from deserializer', 
  `status` string COMMENT 'from deserializer', 
  `currency` string COMMENT 'from deserializer', 
  `user_id` string COMMENT 'from deserializer', 
  `payout_account_id` string COMMENT 'from deserializer', 
  `amount` string COMMENT 'from deserializer', 
  `amount_metadata` string COMMENT 'from deserializer', 
  `payout_metadata` string COMMENT 'from deserializer', 
  `updated_at` string COMMENT 'from deserializer', 
  `created_at` string COMMENT 'from deserializer', 
  `razorpay_payout_id` string COMMENT 'from deserializer', 
  `charged_at` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/webapp/payouts'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1641895699')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
