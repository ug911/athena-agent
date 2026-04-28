---
database: backend
table: webapp__payment_orders
type: table
layer: raw
location: s3://[REDACTED-BUCKET]/production/webapp/payment_orders
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:05:07+00:00'
sampled_rows: 0
---

# `backend.webapp__payment_orders`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `status` | `string` | from deserializer |
| `payment_type` | `string` | from deserializer |
| `payer_user_id` | `string` | from deserializer |
| `payee_user_id` | `string` | from deserializer |
| `payment_transaction_id` | `string` | from deserializer |
| `amount` | `string` | from deserializer |
| `currency` | `string` | from deserializer |
| `payout_triggered` | `string` | from deserializer |
| `payout_succeeded` | `string` | from deserializer |
| `updated_at` | `string` | from deserializer |
| `created_at` | `string` | from deserializer |
| `razorpay_order_id` | `string` | from deserializer |
| `charged_at` | `string` | from deserializer |
| `razorpay_payment_id` | `string` | from deserializer |
| `payout_id` | `string` | from deserializer |

## DDL

```sql
CREATE EXTERNAL TABLE `backend.webapp__payment_orders`(
  `_id` string COMMENT 'from deserializer', 
  `status` string COMMENT 'from deserializer', 
  `payment_type` string COMMENT 'from deserializer', 
  `payer_user_id` string COMMENT 'from deserializer', 
  `payee_user_id` string COMMENT 'from deserializer', 
  `payment_transaction_id` string COMMENT 'from deserializer', 
  `amount` string COMMENT 'from deserializer', 
  `currency` string COMMENT 'from deserializer', 
  `payout_triggered` string COMMENT 'from deserializer', 
  `payout_succeeded` string COMMENT 'from deserializer', 
  `updated_at` string COMMENT 'from deserializer', 
  `created_at` string COMMENT 'from deserializer', 
  `razorpay_order_id` string COMMENT 'from deserializer', 
  `charged_at` string COMMENT 'from deserializer', 
  `razorpay_payment_id` string COMMENT 'from deserializer', 
  `payout_id` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/webapp/payment_orders'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1641895720')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
