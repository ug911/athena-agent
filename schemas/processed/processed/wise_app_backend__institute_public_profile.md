---
canonical: processed
table: wise_app_backend__institute_public_profile
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/institute_public_profile/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:24:23+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__institute_public_profile`

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

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `ispublic`: `true (×200)`
- `namespace`: `wise (×184)`, `susan (×2)`, `spellzee (×2)`, `pedagogyy (×2)`, `crgchess (×2)`, `rise (×1)`, `shambhala (×1)`, `vital (×1)`, `brolly (×1)`, `image_classes (×1)`, `topmate (×1)`, `maestrochess (×1)`, `reiga (×1)`
- `backgroundcolor`: `#101828 (×196)`, `#000000 (×1)`, `#FF7F50 (×1)`, `#025160 (×1)`, `#000 (×1)`
- `ctatext`: `Chat now (×198)`, `Contact now (×1)`, `Text us (×1)`
- `textcolor`: `#ffffff (×200)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `633bd8f7c5d2498cfb25ec77`, `634e92bd72da697d508fec5f`, `634fee7772da697d50da0c06`

### `instituteid`

- `$oid` — `string`  e.g. `633bd8f7886a2c68d7a542df`, `634e92bdebdb55cdc8fb77fc`, `634fee77459bbb0a7926783a`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1664866551138`, `1666093757186`, `1666182775098`

### `institutecovers`

  - `[]` — `object`
    - `link` — `string`  e.g. `https://files.wiseapp.live/upload_files/6093c17ef339108cdb84`, `https://files.wiseapp.live/upload_files/6347a646b97810432e11`, `https://files.wiseapp.live/upload_files/5f24052520955e1aff46`
    - `type` — `string`  e.g. `image`, `image`, `image`

### `publishedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1664866551135`, `1666093757182`, `1666182775093`

### `sections`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `633bd8f7886a2cc626a542e2`, `633bd8f7886a2c72b7a542e3`, `634e92bdebdb559ef3fb77ff`
    - `classids` — `array<object>|array<unknown>`
      - `[].classids[]` — `object`
        - `$oid` — `string`  e.g. `633bd8f7886a2c4b02a542e0`, `633bf9ba00b94225c214e74a`, `633bf9d9163e4221f2d023f0`
    - `courseids` — `array<object>|array<unknown>`
      - `[].courseids[]` — `object`
        - `$oid` — `string`  e.g. `6363c0de4c047754855336b4`, `6368ae86582508ab5ced3791`, `6383971e624beb345f03aba7`
    - `sectiontype` — `string`  e.g. `OTHER`, `ALL`, `OTHER`
    - `title` — `string`  e.g. `Featured Courses`, `All Courses`, `Featured Courses`

### `socialprofile`

- `email` — `string`  e.g. `[REDACTED]`
- `facebook` — `string`  e.g. `https://facebook.com/risewithrise`, `https://www.facebook.com/cmagc.hyderabad`, `https://www.facebook.com/wiseapplive`
- `instagram` — `string`  e.g. `https://instagram.com/risewithrise`, `https://www.instagram.com/cmagc.hyderabad/`, `https://www.instagram.com/wiseapplive/`
- `linkedin` — `string`  e.g. `https://www.linkedin.com/company/riseinstitute/`, `https://www.linkedin.com/company/cmagc/`, `https://www.linkedin.com/feed/?trk=nav_logo`
- `twitter` — `string`  e.g. `https://twitter.com/risewithrise`
- `website` — `string`  e.g. `https://twitter.com/cmagc_hyderabad`, `t.me/debadutta_official`
- `whatsapp` — `string`  e.g. `[REDACTED]`
- `youtube` — `string`  e.g. `https://www.youtube.com/c/risewithrise`, `https://www.youtube.com/channel/UCK5_KGP-tGBg6SQNVO9lyKQ`, `https://www.youtube.com/`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1707893662140`, `1777545260064`, `1687328540687`

### `subdomaincreated`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_003807_00043_5447u', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
