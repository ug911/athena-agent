---
database: backend
table: webapp__payout_accounts
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/webapp/payout_accounts
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:05:13+00:00'
sampled_rows: 0
---

# `backend.webapp__payout_accounts`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `vpa` | `string` | from deserializer |
| `account_type` | `string` | from deserializer |
| `payout_user_id` | `string` | from deserializer |
| `razorpay_fund_account_id` | `string` | from deserializer |
| `updated_at` | `string` | from deserializer |
| `created_at` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.webapp__payout_accounts`(
  `_id` string COMMENT 'from deserializer', 
  `vpa` string COMMENT 'from deserializer', 
  `account_type` string COMMENT 'from deserializer', 
  `payout_user_id` string COMMENT 'from deserializer', 
  `razorpay_fund_account_id` string COMMENT 'from deserializer', 
  `updated_at` string COMMENT 'from deserializer', 
  `created_at` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/webapp/payout_accounts'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1641895731')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
