---
database: processed
table: wise_app_backend__feestructure
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/feeStructure/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:15:03+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__feestructure`

## Columns

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

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `active`: `true (×200)`
- `type`: `RECURRING (×113)`, `ONE_TIME (×87)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `602e452cbb70506637ba67f5`, `602f3291a702b61e8798443d`, `602f3a77279efe2a24acc3e2`

### `classid`

- `$oid` — `string`  e.g. `5f24056820955e1aff464608`, `5f9ae91fa21ae213c20462c4`, `5f5224a857ea8c52b1528151`

### `userid`

- `$oid` — `string`  e.g. `5f24052520955e1aff464606`, `5f12d7d088cd370409e738ec`, `5f15aca19aa2c74eba09a31f`

### `amount`

- `currency` — `string`  e.g. `INR`, `INR`, `INR`
- `value` — `object`
  - `$numberint` — `string`  e.g. `10000`, `1000`, `300000`

### `startdate`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1612176280361`, `1612182048628`, `1612193707515`

### `enddate`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1638316800000`, `1638361248628`, `1627776000000`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1613645100440`, `1613705873416`, `1613707895272`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1632461917662`, `1648966245464`, `1628274195699`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

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
  'trino_query_id'='20260428_003543_00079_htseq', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
