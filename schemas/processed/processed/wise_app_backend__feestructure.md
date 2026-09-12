---
canonical: processed
table: wise_app_backend__feestructure
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/feeStructure/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:23:37+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__feestructure`

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
| `active` | `string` |  |
| `classid` | `string` |  |
| `userid` | `string` |  |
| `amount` | `string` |  |
| `type` | `string` |  |
| `startdate` | `string` |  |
| `enddate` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `__v` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `active`: `true (×200)`
- `type`: `RECURRING (×120)`, `ONE_TIME (×80)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `60791dc1cf462a387db36acf`, `60791fecdf27a27dade2f984`, `6079202d110db6fe0b8fd46b`

### `classid`

- `$oid` — `string`  e.g. `607918dfdf27a2da48e27ab6`, `60791fc7a587b9e7434769f1`, `60792016cf462ae055b38dfa`

### `userid`

- `$oid` — `string`  e.g. `607917dfa587b9933246dfd9`, `607913d2cf462a8cb6b2b0ac`, `607913d2cf462a8cb6b2b0ac`

### `amount`

- `currency` — `string`  e.g. `INR`, `INR`, `INR`
- `value` — `object`
  - `$numberint` — `string`  e.g. `50000`, `30000`, `30000`

### `startdate`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1617235200000`, `1617235200000`, `1617235200000`

### `enddate`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1638316800000`, `1625097600000`, `1619827200000`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1618550209262`, `1618550764581`, `1618550829979`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1618550209262`, `1618550764581`, `1618550829979`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__feestructure`(
  `_id` string, 
  `active` string, 
  `classid` string, 
  `userid` string, 
  `amount` string, 
  `type` string, 
  `startdate` string, 
  `enddate` string, 
  `createdat` string, 
  `updatedat` string, 
  `__v` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/feeStructure/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_003718_00025_njz3d', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
