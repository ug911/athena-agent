---
canonical: processed
table: wise_app_backend__classroom_fees
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/ClassroomFee/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:22:19+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__classroom_fees`

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
| `classid` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `paymentoptions` | `string` |  |
| `metadata` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `624b04a3db8952a1051dba2d`, `6254379a5def3f05aee3d981`, `62d27c9e1f216d881fd8da4a`

### `classid`

- `$oid` — `string`  e.g. `624b045339d53f6400c320de`, `6093c1e9efaf930c03a17ee4`, `62d27c9e1848b4fcb1689955`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1649083555752`, `1649686426772`, `1657961630203`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1649083555752`, `1649686426772`, `1657961630203`

### `paymentoptions`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `62d123216f0c72d2fbad4fec`, `62d1232283bc207346ee1c70`, `62d27c9e84b5c899da21d2f3`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1657873185592`, `1657873186076`, `1657961630203`
    - `installments` — `array<object>`
      - `[].installments[]` — `object`
        - `_id` — `object`
          - `$oid` — `string`  e.g. `62d123216f0c72151dad4fed`, `62d1232283bc209d5cee1c71`, `62d27c9e84b5c830f721d2f4`
        - `amount` — `object`
          - `currency` — `string`  e.g. `INR`, `INR`, `INR`
          - `value` — `object`
            - `$numberint` — `string`  e.g. `3000`, `1000`, `100000`
        - `chargeafterdays` — `object`
          - `$numberint` — `string`  e.g. `0`
        - `dueafterdays` — `object`
          - `$numberint` — `string`  e.g. `0`, `0`, `50`
        - `dueon` — `object`
          - `$date` — `object`
            - `$numberlong` — `string`  e.g. `1648771200000`, `1648771200000`, `1657929600000`
        - `index` — `object`
          - `$numberint` — `string`  e.g. `0`, `0`, `1`
        - `starton` — `object`
          - `$date` — `object`
            - `$numberlong` — `string`  e.g. `1647475200000`, `1647475200000`, `1656633600000`
    - `timezone` — `string`  e.g. `Asia/Kolkata`
    - `totalamount` — `object`
      - `currency` — `string`  e.g. `INR`, `INR`, `INR`
      - `value` — `object`
        - `$numberint` — `string`  e.g. `3000`, `1000`, `100000`
    - `type` — `string`  e.g. `UPFRONT`, `UPFRONT`, `UPFRONT`
    - `updatedat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1657873185592`, `1657873186076`, `1657961630203`

### `metadata`

- `migrated` — `bool`  e.g. `true`, `true`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__classroom_fees`(
  `_id` string, 
  `classid` string, 
  `createdat` string, 
  `updatedat` string, 
  `paymentoptions` string, 
  `metadata` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/ClassroomFee/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_003224_00007_cdip5', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
