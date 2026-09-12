---
canonical: processed
table: webapp__payouts
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/webapp/payouts/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:20:17+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.webapp__payouts`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |
| `NA` | `processed_na` |

_Schema parity: **identical** across regions._

## Columns (IN)

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

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `status`: `processed (×200)`
- `currency`: `INR (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6a79fdb49b6926000791f237`, `6a74b7b44fe44f000736a2e4`, `6a6a2bb486cbfa0007776e58`

### `user_id`

- `$oid` — `string`  e.g. `60829972a706e317a3e1d558`, `60d308f4de6c0eaffe4827b0`, `6a69a791002fa65af6ef1ab9`

### `payout_account_id`

- `$oid` — `string`  e.g. `689c3087b93ef10001128a91`, `6890a1cf3c04d600013f9850`, `6a69af92b151c70001f5972e`

### `amount`

- `$numberint` — `string`  e.g. `341152`, `14625`, `975`

### `amount_metadata`

- `original_amount` — `object`
  - `$numberint` — `string`  e.g. `349900`, `15000`, `1000`
- `payout_amount` — `object`
  - `$numberint` — `string`  e.g. `341152`, `14625`, `975`
- `transaction_fee` — `object`
  - `$numberint` — `string`  e.g. `8748`, `375`, `25`
- `transaction_fee_percent` — `object`
  - `$numberdouble` — `string`  e.g. `2.5`, `2.5`, `2.5`

### `payout_metadata`

- `account_type` — `string`  e.g. `bank_account`, `bank_account`, `bank_account`
- `masked_account` — `string`  e.g. `XXXX5420`, `XXXX7396`, `XXXX8358`

### `updated_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786379705045`, `1786034105655`, `1785342905701`

### `created_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786379700400`, `1786034100472`, `1785342900456`

### `charged_at`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786379400000`, `1786033800000`, `1785342600000`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_011553_00007_7w9uz', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
