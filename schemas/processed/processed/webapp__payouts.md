---
database: processed
table: webapp__payouts
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/webapp/payouts/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:13:25+00:00'
sampled_rows: 200
---

# `processed.webapp__payouts`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `status` | `string` |  |
| `currency` | `string` |  |
| `user_id` | `string` |  |
| `payout_account_id` | `string` |  |
| `amount` | `string` |  |
| `amount_metadata` | `string` |  |
| `payout_metadata` | `string` |  |
| `updated_at` | `string` |  |
| `created_at` | `string` |  |
| `razorpay_payout_id` | `string` |  |
| `charged_at` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `status`: `processed (×197)`, `failed (×3)`
- `currency`: `INR (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `69ef90347e9f1c000786b8c7`, `69ef90347e9f1c000786b8c6`, `69ef90347e9f1c000786b8c5`

### `user_id`

- `$oid` — `string`  e.g. `658a4aa59e3651f30527edd9`, `60829972a706e317a3e1d558`, `68ecbef3b9932c954a59df74`

### `payout_account_id`

- `$oid` — `string`  e.g. `69b7fff5fa0c76000164d2ef`, `689c3087b93ef10001128a91`, `6982e735624652000197d197`

### `amount`

- `$numberint` — `string`  e.g. `116415`, `97402`, `460200`

### `amount_metadata`

- `original_amount` — `object`
  - `$numberint` — `string`  e.g. `119400`, `99900`, `472000`
- `payout_amount` — `object`
  - `$numberint` — `string`  e.g. `116415`, `97402`, `460200`
- `transaction_fee` — `object`
  - `$numberint` — `string`  e.g. `2985`, `2498`, `11800`
- `transaction_fee_percent` — `object`
  - `$numberdouble` — `string`  e.g. `2.5`, `2.5`, `2.5`

### `payout_metadata`

- `account_type` — `string`  e.g. `bank_account`, `bank_account`, `bank_account`
- `masked_account` — `string`  e.g. `XXXX8170`, `XXXX5420`, `XXXX3478`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777307705557`, `1777307706031`, `1777307705569`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777307700878`, `1777307700575`, `1777307700523`

### `charged_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1777307400000`, `1777307400000`, `1777307400000`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.webapp__payouts`(
  `_id` string, 
  `status` string, 
  `currency` string, 
  `user_id` string, 
  `payout_account_id` string, 
  `amount` string, 
  `amount_metadata` string, 
  `payout_metadata` string, 
  `updated_at` string, 
  `created_at` string, 
  `razorpay_payout_id` string, 
  `charged_at` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/webapp/payouts/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_010724_00142_zm6vs', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
