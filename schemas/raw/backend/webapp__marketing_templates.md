---
canonical: backend
table: webapp__marketing_templates
type: table
layer: raw
regions:
  in: backend
  na: backend_na
location: s3://[REDACTED-BUCKET]/production/webapp/marketing_templates
format: INPUTFORMAT
partition_keys: []
schema_parity: drift
last_synced: '2026-08-11T13:04:04+00:00'
sampled_rows: 0
sampled_region: null
---

# `backend.webapp__marketing_templates`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `backend` |
| `NA` | `backend_na` |

_⚠ Schema parity: **drift** — see Region drift section below._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` | from deserializer |
| `archived` | `string` | from deserializer |
| `html_template` | `string` | from deserializer |
| `preview_image` | `string` | from deserializer |
| `image_height` | `string` | from deserializer |
| `image_width` | `string` | from deserializer |
| `updated_at` | `string` | from deserializer |
| `created_at` | `string` | from deserializer |
| `template_variables` | `string` | from deserializer |
| `target` | `string` | from deserializer |
| `category` | `string` | from deserializer |

## Region drift

### `IN` (backend) vs `NA` (backend_na)

- Only in `IN`: `archived`, `category`, `html_template`, `image_height`, `image_width`, `preview_image`, `target`, `template_variables`
- Only in `NA`: `amount`, `charged_at`, `currency`, `payee_user_id`, `payer_user_id`, `payment_transaction_id`, `payment_type`, `payout_id`, `payout_succeeded`, `payout_triggered`, `razorpay_order_id`, `razorpay_payment_id`, `status`

## DDL

### `IN` (backend)

```sql
CREATE EXTERNAL TABLE `backend.webapp__marketing_templates`(
  `_id` string COMMENT 'from deserializer', 
  `archived` string COMMENT 'from deserializer', 
  `html_template` string COMMENT 'from deserializer', 
  `preview_image` string COMMENT 'from deserializer', 
  `image_height` string COMMENT 'from deserializer', 
  `image_width` string COMMENT 'from deserializer', 
  `updated_at` string COMMENT 'from deserializer', 
  `created_at` string COMMENT 'from deserializer', 
  `template_variables` string COMMENT 'from deserializer', 
  `target` string COMMENT 'from deserializer', 
  `category` string COMMENT 'from deserializer')
ROW FORMAT SERDE 
  'org.openx.data.jsonserde.JsonSerDe' 
WITH SERDEPROPERTIES ( 
  'ignore.malformed.json'='true') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/production/webapp/marketing_templates'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1641895707')
```

### `NA` (backend_na)

```sql
CREATE EXTERNAL TABLE `backend_na.webapp__marketing_templates`(
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
  's3://[REDACTED-BUCKET]/production_na/webapp/marketing_templates'
TBLPROPERTIES (
  'compressionType'='gzip', 
  'transient_lastDdlTime'='1759754704')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
