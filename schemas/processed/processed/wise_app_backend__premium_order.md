---
database: processed
table: wise_app_backend__premium_order
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/PremiumOrder/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:16:30+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__premium_order`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `status` | `string` |  |
| `licensecount` | `string` |  |
| `userid` | `string` |  |
| `startsfrom` | `string` |  |
| `endsat` | `string` |  |
| `amount` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `type` | `string` |  |
| `plantype` | `string` |  |
| `premiumplan` | `string` |  |
| `billingperiod` | `string` |  |
| `plandisplayname` | `string` |  |
| `planmetadata` | `string` |  |
| `premiumplantype` | `string` |  |
| `renewson` | `string` |  |
| `__v` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `status`: `ACTIVE (×125)`, `CANCELLED (×75)`
- `type`: `LICENSE (×200)`
- `plantype`: `MONTHLY (×137)`, `ANNUAL (×63)`
- `premiumplan`: `STARTUP (×200)`
- `billingperiod`: `MONTHLY (×105)`, `ANNUAL (×40)`
- `plandisplayname`: `Seat Based Plan (Online) (×145)`
- `premiumplantype`: `SEAT_BASED (×145)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `625e9e39f811960008aae9be`, `625e9f46caccd30008999357`, `625e9f4622e8be00093b54ca`

### `licensecount`

- `$numberint` — `string`  e.g. `1`, `1`, `1`

### `userid`

- `$oid` — `string`  e.g. `5f4bbf3938a21ba5bd0b8e8b`, `5f8472ba51918e3792bd645d`, `5f60d29a1c52d12c3eb0a464`

### `startsfrom`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1650326400000`, `1650326400000`, `1650326400000`

### `endsat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1652918400000`, `1652400000000`, `1675641600000`

### `amount`

- `currency` — `string`  e.g. `INR`, `INR`, `INR`
- `value` — `object`
  - `$numberint` — `string`  e.g. `75000`, `60000`, `732500`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1650368057203`, `1650368326951`, `1650368326955`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1769164102754`, `1769161002649`, `1769161002649`

### `planmetadata`

- `unitamount` — `object`
  - `currency` — `string`  e.g. `INR`, `INR`, `INR`
  - `value` — `object`
    - `$numberint` — `string`  e.g. `400000`, `400000`, `400000`
- `unitcount` — `object`
  - `$numberint` — `string`  e.g. `1`, `1`, `1`

### `renewson`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1652918400000`, `1652400000000`, `1675641600000`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__premium_order`(
  `_id` string, 
  `status` string, 
  `licensecount` string, 
  `userid` string, 
  `startsfrom` string, 
  `endsat` string, 
  `amount` string, 
  `createdat` string, 
  `updatedat` string, 
  `type` string, 
  `plantype` string, 
  `premiumplan` string, 
  `billingperiod` string, 
  `plandisplayname` string, 
  `planmetadata` string, 
  `premiumplantype` string, 
  `renewson` string, 
  `__v` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/PremiumOrder/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_011646_00061_6numw', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
