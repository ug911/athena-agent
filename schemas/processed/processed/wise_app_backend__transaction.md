---
canonical: processed
table: wise_app_backend__transaction
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/transaction/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:28:56+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__transaction`

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
| `metadata` | `string` |  |
| `senderid` | `string` |  |
| `receiverid` | `string` |  |
| `amount` | `string` |  |
| `type` | `string` |  |
| `status` | `string` |  |
| `note` | `string` |  |
| `createdat` | `string` |  |
| `transactiontype` | `string` |  |
| `__v` | `string` |  |
| `chargedat` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `type`: `INVOICE (×111)`, `PAYMENT (×55)`, `DISBURSAL (×15)`, `OFFLINE_PAYMENT (×12)`, `DISCOUNT (×7)`
- `status`: `CHARGED (×142)`, `CANCELLED (×23)`, `CREATED (×22)`, `REJECTED (×13)`
- `transactiontype`: `FEE_COLLECTION (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `602e452c669f02000768b485`, `602e452cd074c0000731b229`, `602e452ca84eb00007531bba`

### `metadata`

- `amount_metadata` — `object`
  - `original_amount` — `object`
    - `$numberint` — `string`  e.g. `4000`, `2500`, `1000`
  - `payout_amount` — `object`
    - `$numberint` — `string`  e.g. `4000`, `2500`, `1000`
  - `transaction_fee` — `object`
    - `$numberint` — `string`  e.g. `0`, `0`, `0`
  - `transaction_fee_percent` — `object`
    - `$numberint` — `string`  e.g. `0`, `0`, `0`
- `chargeon` — `object`
  - `$date` — `object`
    - `$numberlong` — `string`  e.g. `1612396800000`, `1612396800000`, `1612396800000`
- `classid` — `string`  e.g. `5f24056820955e1aff464608`, `5f24056820955e1aff464608`, `5f24056820955e1aff464608`
- `display` — `string`  e.g. `Paid using upi`, `Paid using upi`, `Paid using upi`
- `dueon` — `object`
  - `$date` — `object`
    - `$numberlong` — `string`  e.g. `1613645100471`, `1613645100474`, `1613645100480`
- `inactive` — `bool`  e.g. `true`, `true`, `true`
- `index` — `object` (nullable)
  - `$numberint` — `string`  e.g. `1`, `1`, `1`
- `installmentid` — `string`  e.g. `62d1229b2fb90574d5b1df3c`, `62d1229b2fb90574d5b1df3c`, `62d1229b2fb90574d5b1df3c`
- `invoicenumber` — `string`  e.g. `INV-0001`, `INV-0002`, `INV-0001`
- `invoicetype` — `string`  e.g. `FEE_COLLECTION`, `FEE_COLLECTION`, `FEE_COLLECTION`
- `migrate` — `bool`  e.g. `true`, `true`, `true`
- `migrated` — `bool`  e.g. `true`, `true`, `true`
- `paid` — `bool`  e.g. `false`, `true`, `false`
- `payment_ids` — `array<string>`
  - `payment_ids[]` — `string`  e.g. `602e52c7279efe76d9ac8c47`, `602f31aabb70506b51ba9aa3`, `602f3447bb70505ef5baa009`
- `payment_order_id` — `string`  e.g. `602f34482dc9aa0001ea4f90`, `602f346b2dc9aa0001ea4f92`, `602f3a972d031b000161fb9a`
- `paymentoptionid` — `string`  e.g. `62d1229b2fb9057a1cb1df3b`, `62d1229b2fb9057a1cb1df3b`, `62d1229b2fb9057a1cb1df3b`
- `payout_id` — `string`  e.g. `602f4cd8552d6b00064dceee`, `602f4cd8552d6b00064dceed`, `602f593c552d6b00064dcef1`
- `payout_metadata` — `object`
  - `account_type` — `string`  e.g. `bank_account`, `vpa`, `bank_account`
  - `masked_account` — `string`  e.g. `XXXX8932`, `mube****@okhdfcbank`, `XXXX3933`

### `senderid`

- `$oid` — `string`  e.g. `5f24052520955e1aff464606`, `5f24052520955e1aff464606`, `5f24052520955e1aff464606`

### `receiverid`

- `$oid` — `string`  e.g. `5f27aeb3aa382f6247e4a568`, `5f15aca19aa2c74eba09a31f`, `5f114ad25a61c636f00bc1d8`

### `amount`

- `currency` — `string`  e.g. `INR`, `INR`, `INR`
- `value` — `object`
  - `$numberint` — `string`  e.g. `100000`, `100000`, `100000`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1613645100471`, `1613645100474`, `1613645100480`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `chargedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1613645100471`, `1613645100474`, `1613645100480`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__transaction`(
  `_id` string, 
  `metadata` string, 
  `senderid` string, 
  `receiverid` string, 
  `amount` string, 
  `type` string, 
  `status` string, 
  `note` string, 
  `createdat` string, 
  `transactiontype` string, 
  `__v` string, 
  `chargedat` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/transaction/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_012641_00097_9qgt8', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
