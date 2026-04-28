---
database: processed
table: wise_app_backend__transaction
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/transaction/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:17:35+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__transaction`

## Columns

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

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `type`: `INVOICE (×110)`, `PAYMENT (×71)`, `DISCOUNT (×8)`, `OFFLINE_PAYMENT (×7)`, `DISBURSAL (×4)`
- `status`: `CHARGED (×80)`, `CREATED (×56)`, `CANCELLED (×56)`, `REJECTED (×8)`
- `transactiontype`: `FEE_COLLECTION (×165)`, `WISE_PREMIUM (×35)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `604dafb1704a3100a3247f5d`, `604e05a3704a310e09248eee`, `604e05b7d16731a07f5deee5`

### `metadata`

- `amount_metadata` — `object`
  - `original_amount` — `object`
    - `$numberint` — `string`  e.g. `1500`, `20500`, `400`
  - `payout_amount` — `object`
    - `$numberint` — `string`  e.g. `1500`, `20500`, `400`
  - `transaction_fee` — `object`
    - `$numberint` — `string`  e.g. `0`, `0`, `0`
  - `transaction_fee_percent` — `object`
    - `$numberint` — `string`  e.g. `0`, `0`, `0`
- `chargeon` — `object`
  - `$date` — `object`
    - `$numberlong` — `string`  e.g. `1614470400000`, `1614470400000`, `1614470400000`
- `classid` — `string`  e.g. `603e60c87cdf726c52828af4`, `604efa7377491e96907f6ee3`, `603e2e714d49b807d7ee926c`
- `classname` — `string`  e.g. `🙏 तैयारी जीत की Academy`, `🙏 तैयारी जीत की Academy`, `🙏 तैयारी जीत की Academy`
- `display` — `string`  e.g. `Paid using card`, `Paid using upi`, `Paid using upi`
- `dueon` — `object|string`  e.g. `2021-03-28T12:33:26.274Z`, `2021-03-28T12:33:29.352Z`, `2021-03-28T12:36:17.880Z`
  - `$date` — `object`
    - `$numberlong` — `string`  e.g. `1615736201578`, `1615792455239`, `1615796608489`
- `inactive` — `bool`  e.g. `true`, `true`, `true`
- `index` — `object` (nullable)
  - `$numberint` — `string`  e.g. `1`, `0`, `0`
- `installmentid` — `string`  e.g. `62d1229c2fb90595a5b1e02a`, `62d1229c20c71721e1654962`, `62d1229c4d5a73254088d716`
- `invoicenumber` — `string`  e.g. `INV-0001`, `INV-0010`, `INV-0012`
- `invoicetype` — `string`  e.g. `FEE_COLLECTION`, `FEE_COLLECTION`, `FEE_COLLECTION`
- `migrate` — `bool`  e.g. `true`, `true`, `true`
- `migrated` — `bool`  e.g. `true`, `true`, `true`
- `paid` — `bool`  e.g. `true`, `false`, `false`
- `payment_ids` — `array<string>`
  - `payment_ids[]` — `string`  e.g. `6052df4c2a36640082122077`, `605370722ac5af10670dda93`, `605371bb9a02ef57249ddbed`
- `payment_order_id` — `string`  e.g. `604dafb1155ed90001cee8aa`, `6050516ae839d2000179d34a`, `60532e8e4731490001cad8c3`
- `paymentoptionid` — `string`  e.g. `62d1229c2fb9050f26b1e029`, `62d1229c20c71778e8654961`, `62d1229c4d5a73202488d715`
- `payout_id` — `string`  e.g. `60538134a2ee98000748830a`, `6054d2b4df51c900061595a8`, `6050de34df51c900061595a4`
- `payout_metadata` — `object`
  - `account_type` — `string`  e.g. `bank_account`, `bank_account`, `bank_account`
  - `masked_account` — `string`  e.g. `XXXX3832`, `XXXX3832`, `XXXX1125`
- `plantype` — `string`  e.g. `MONTHLY`, `MONTHLY`, `MONTHLY`
- `reason_code` — `string`  e.g. `WISE_PREMIUM`, `WISE_PREMIUM`, `WISE_PREMIUM`
- `reversed` — `bool`  e.g. `true`, `true`, `true`
- `subject` — `string`  e.g. `Geography,polity and history`, `Geography,polity and history`, `Geography,polity and history`

### `senderid`

- `$oid` — `string`  e.g. `5f98222f5eb515bc46f56412`, `5f61a8e8d5bb2b3bcf1128b0`, `5f61a8e8d5bb2b3bcf1128b0`

### `receiverid`

- `$oid` — `string`  e.g. `601cccadac6b3b85b94c4412`, `5f60d29a1c52d12c3eb0a464`, `5f60d29a1c52d12c3eb0a464`

### `amount`

- `currency` — `string`  e.g. `INR`, `INR`, `INR`
- `value` — `object`
  - `$numberint` — `string`  e.g. `90000`, `20000`, `200000`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1615703985102`, `1615725987876`, `1615726007881`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `chargedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1615736201578`, `1614470400000`, `1614470400000`

## DDL

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
  'trino_query_id'='20260428_011832_00043_nvfw5', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
