---
canonical: processed
table: webapp__marketing_templates
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/webapp/marketing_templates/
format: INPUTFORMAT
partition_keys: []
schema_parity: drift
last_synced: '2026-08-11T13:19:43+00:00'
sampled_rows: 181
sampled_region: in
---

# `processed.webapp__marketing_templates`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |
| `NA` | `processed_na` |

_⚠ Schema parity: **drift** — see Region drift section below._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `archived` | `string` |  |
| `html_template` | `string` |  |
| `preview_image` | `string` |  |
| `image_height` | `string` |  |
| `image_width` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `template_variables` | `string` |  |
| `target` | `string` |  |
| `category` | `string` |  |

## Region drift

### `IN` (processed) vs `NA` (processed_na)

- Only in `IN`: `archived`, `category`, `html_template`, `image_height`, `image_width`, `preview_image`, `target`, `template_variables`
- Only in `NA`: `amount`, `charged_at`, `currency`, `payee_user_id`, `payer_user_id`, `payment_transaction_id`, `payment_type`, `payout_id`, `payout_succeeded`, `payout_triggered`, `razorpay_order_id`, `razorpay_payment_id`, `status`

## Enum-like columns

_String columns with ≤20 distinct values in 181 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `archived`: `false (×99)`, `true (×82)`
- `target`: `all (×130)`, `teacher (×43)`, `student (×8)`
- `category`: `greeting (×72)`, `marketing (×69)`, `motivational (×21)`, `session (×5)`, `test (×5)`, `assessment (×5)`, `entity_test (×1)`, `entity_assessment (×1)`, `entity_generic_upsc (×1)`, `testing (×1)`

## Inferred JSON structure

_Inferred from 181 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6076588a6268e508b124b515`, `62517ce374db6f0098e7663a`, `62260e0ad5e0de009ae8293e`

### `image_height`

- `$numberint` — `string`  e.g. `360`, `360`, `360`

### `image_width`

- `$numberint` — `string`  e.g. `360`, `360`, `360`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1681404650085`, `1680093155028`, `1678085530425`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1681404650085`, `1680093155028`, `1678085530425`

### `template_variables`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `6076588a6268e508b124b516`, `62517ce374db6f0098e7663b`, `62260e0ad5e0de009ae8293f`
    - `char_limit` — `object`
      - `$numberint` — `string`  e.g. `20`, `25`, `25`
    - `default_value` — `string`  e.g. `How to start preparing for UPSC?`, `Live Session`, `by`
    - `display_name` — `string`  e.g. `[REDACTED]`
    - `name` — `string`  e.g. `user_name`, `user_name`, `user_name`
    - `type` — `string`  e.g. `TEXT`, `TEXT`, `TEXT`

## DDL

### `IN` (processed)

```sql
CREATE EXTERNAL TABLE `processed.webapp__marketing_templates`(
  `_id` string, 
  `archived` string, 
  `html_template` string, 
  `preview_image` string, 
  `image_height` string, 
  `image_width` string, 
  `updated_at` string, 
  `created_at` string, 
  `template_variables` string, 
  `target` string, 
  `category` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/webapp/marketing_templates/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_011533_00016_ujnsn', 
  'trino_version'='0.215-24619-g93e00a8')
```

### `NA` (processed_na)

```sql
CREATE EXTERNAL TABLE `processed_na.webapp__marketing_templates`(
  `_id` string, 
  `status` string, 
  `payment_type` string, 
  `payer_user_id` string, 
  `payee_user_id` string, 
  `payment_transaction_id` string, 
  `amount` string, 
  `currency` string, 
  `payout_triggered` string, 
  `payout_succeeded` string, 
  `updated_at` string, 
  `created_at` string, 
  `razorpay_order_id` string, 
  `charged_at` string, 
  `razorpay_payment_id` string, 
  `payout_id` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed_na/webapp/marketing_templates/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_004432_00026_fcqix', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
