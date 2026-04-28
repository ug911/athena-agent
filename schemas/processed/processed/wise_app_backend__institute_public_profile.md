---
database: processed
table: wise_app_backend__institute_public_profile
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/institute_public_profile/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:15:26+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__institute_public_profile`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `instituteid` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `institutecovers` | `string` |  |
| `ispublic` | `string` |  |
| `namespace` | `string` |  |
| `publishedat` | `string` |  |
| `sections` | `string` |  |
| `socialprofile` | `string` |  |
| `subdomain` | `string` |  |
| `title` | `string` |  |
| `updatedat` | `string` |  |
| `description` | `string` |  |
| `backgroundcolor` | `string` |  |
| `ctatext` | `string` |  |
| `textcolor` | `string` |  |
| `subdomaincreated` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `ispublic`: `true (×200)`
- `namespace`: `wise (×198)`, `rise (×1)`, `shambhala (×1)`
- `backgroundcolor`: `#101828 (×199)`, `#000000 (×1)`
- `ctatext`: `Chat now (×199)`, `Contact now (×1)`
- `textcolor`: `#ffffff (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `633bd8f7c5d2498cfb25ec77`, `634d34e272da697d5045222e`, `634d361372da697d50456122`

### `instituteid`

- `$oid` — `string`  e.g. `633bd8f7886a2c68d7a542df`, `634d34e1e24c4e7e50816c6c`, `634d36136cb885bf06ce4771`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1664866551138`, `1666004193995`, `1666004499091`

### `institutecovers`

  - `[]` — `object`
    - `link` — `string`  e.g. `https://files.wiseapp.live/upload_files/6093c17ef339108cdb84`, `https://files.wiseapp.live/upload_files/5f24052520955e1aff46`, `https://cdn.wiseapp.live/images/institute-cover/15.png`
    - `type` — `string`  e.g. `image`, `image`, `image`

### `publishedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1664866551135`, `1666004193991`, `1666004499087`

### `sections`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `633bd8f7886a2cc626a542e2`, `633bd8f7886a2c72b7a542e3`, `634d34e1e24c4ee99f816c6f`
    - `classids` — `array<object>|array<unknown>`
      - `[].classids[]` — `object`
        - `$oid` — `string`  e.g. `633bd8f7886a2c4b02a542e0`, `633bf9ba00b94225c214e74a`, `633bf9d9163e4221f2d023f0`
    - `courseids` — `array<object>|array<unknown>`
      - `[].courseids[]` — `object`
        - `$oid` — `string`  e.g. `634e9c5047a3103383a73e22`, `6350c0ea5891cf755466a5ef`, `6351684a97d0e18b0f3cec26`
    - `sectiontype` — `string`  e.g. `OTHER`, `ALL`, `OTHER`
    - `title` — `string`  e.g. `Featured Courses`, `All Courses`, `Featured Courses`

### `socialprofile`

- `email` — `string`  e.g. `[REDACTED]`
- `facebook` — `string`  e.g. `https://facebook.com/risewithrise`, `https://www.facebook.com/objectiveiasonline`, `https://www.facebook.com/cmagc.hyderabad`
- `instagram` — `string`  e.g. `https://instagram.com/risewithrise`, `https://www.instagram.com/cmagc.hyderabad/`
- `linkedin` — `string`  e.g. `https://www.linkedin.com/company/riseinstitute/`, `https://www.linkedin.com/company/cmagc/`
- `twitter` — `string`  e.g. `https://twitter.com/risewithrise`
- `website` — `string`  e.g. `https://objectiveias.in`, `https://twitter.com/cmagc_hyderabad`
- `whatsapp` — `string`  e.g. `[REDACTED]`
- `youtube` — `string`  e.g. `https://www.youtube.com/c/risewithrise`, `https://www.youtube.com/c/OBJECTIVEIAS`, `https://www.youtube.com/channel/UCK5_KGP-tGBg6SQNVO9lyKQ`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1707893662140`, `1687328540687`, `1687328540687`

### `subdomaincreated`

- `$numberint` — `string`  e.g. `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__institute_public_profile`(
  `_id` string, 
  `instituteid` string, 
  `__v` string, 
  `createdat` string, 
  `institutecovers` string, 
  `ispublic` string, 
  `namespace` string, 
  `publishedat` string, 
  `sections` string, 
  `socialprofile` string, 
  `subdomain` string, 
  `title` string, 
  `updatedat` string, 
  `description` string, 
  `backgroundcolor` string, 
  `ctatext` string, 
  `textcolor` string, 
  `subdomaincreated` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/institute_public_profile/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003524_00052_awjvj', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
