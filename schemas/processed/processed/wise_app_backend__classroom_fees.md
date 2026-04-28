---
database: processed
table: wise_app_backend__classroom_fees
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/ClassroomFee/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:14:27+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__classroom_fees`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `classid` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `paymentoptions` | `string` |  |
| `metadata` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `603bcfe17732af12be8e1250`, `603bd0c9f7e5383c4525a493`, `603b790bf7e5385cb425897b`

### `classid`

- `$oid` — `string`  e.g. `603bcf6be295055c488a42fd`, `603bd0b4430c4f765acb46a1`, `603b3dc3dcc5f021464c62a5`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1614532577326`, `1614532809818`, `1614510347305`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1614532577326`, `1614532809818`, `1614510347305`

### `paymentoptions`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `62d1229c59d78c89147c34d0`, `62d1229c8a155b1171f71cd9`, `62d1229c6fe8f1d16feb2b38`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1657873052468`, `1657873052471`, `1657873052464`
    - `installments` — `array<object>`
      - `[].installments[]` — `object`
        - `_id` — `object`
          - `$oid` — `string`  e.g. `62d1229c59d78c8f437c34d1`, `62d1229c59d78c8e1e7c34d2`, `62d1229c8a155b80fbf71cda`
        - `amount` — `object`
          - `currency` — `string`  e.g. `INR`, `INR`, `INR`
          - `value` — `object`
            - `$numberint` — `string`  e.g. `100000`, `100000`, `75000`
        - `dueon` — `object`
          - `$date` — `object`
            - `$numberlong` — `string`  e.g. `1614556800000`, `1617235200000`, `1612137600000`
        - `index` — `object`
          - `$numberint` — `string`  e.g. `1`, `2`, `0`
        - `starton` — `object`
          - `$date` — `object`
            - `$numberlong` — `string`  e.g. `1613260800000`, `1615939200000`, `1610841600000`
    - `totalamount` — `object`
      - `currency` — `string`  e.g. `INR`, `INR`, `INR`
      - `value` — `object`
        - `$numberint` — `string`  e.g. `200000`, `75000`, `1050000`
    - `type` — `string`  e.g. `INSTALLMENT`, `UPFRONT`, `INSTALLMENT`
    - `updatedat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1657873052468`, `1657873052471`, `1657873052464`

### `metadata`

- `migrated` — `bool`  e.g. `true`, `true`, `true`

## DDL

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
  'trino_query_id'='20260428_003145_00007_cwqi3', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
