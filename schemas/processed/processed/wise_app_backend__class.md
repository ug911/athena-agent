---
canonical: processed
table: wise_app_backend__class
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/class/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:21:47+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__class`

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
| `namespace` | `string` |  |
| `zoomlink` | `string` |  |
| `pendingadmins` | `string` |  |
| `admins` | `string` |  |
| `pendingrequest` | `string` |  |
| `joinedrequest` | `string` |  |
| `coteacherrequests` | `string` |  |
| `coteachers` | `string` |  |
| `archived` | `string` |  |
| `disablereminder` | `string` |  |
| `lockclassroom` | `string` |  |
| `subject` | `string` |  |
| `timing` | `string` |  |
| `userid` | `string` |  |
| `name` | `string` |  |
| `classnumber` | `string` |  |
| `timingversion` | `string` |  |
| `schedule` | `string` |  |
| `settings` | `string` |  |
| `oldschedules` | `string` |  |
| `createdat` | `string` |  |
| `deletedstudents` | `string` |  |
| `suspendedstudents` | `string` |  |
| `instituteid` | `string` |  |
| `__v` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `namespace`: `wise (×95)`, `lifeskilllearnings (×31)`, `theiasakademia (×24)`, `ipec_eduserv (×23)`, `vital (×12)`, `eclass (×9)`, `rise (×4)`, `trice_prime (×1)`, `image_classes (×1)`
- `archived`: `false (×198)`, `true (×2)`
- `disablereminder`: `false (×177)`
- `lockclassroom`: `false (×38)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `5f1c100abeaf861a4dfb009c`, `5f24056820955e1aff464608`, `5f54433b3dcd1771696a371d`

### `zoomlink`

- `join_url` — `string`  e.g. `https://wise-live.zoom.us/j/91313748331?pwd=bTZEb0luZEJnay9W`
- `meetinguuid` — `string`  e.g. `SM/m/gQRQNK6DP2m3aNMsg==`
- `mettingended` — `bool`  e.g. `true`, `true`, `true`
- `mettingid` — `string`  e.g. `91313748331`
- `password` — `string`  e.g. `[REDACTED]`
- `registrationenabled` — `bool`  e.g. `false`
- `start_url` — `string`  e.g. `https://wise-live.zoom.us/s/91313748331?zak=eyJ0eXAiOiJKV1Qi`
- `starttime` — `object`
  - `$date` — `object`
    - `$numberlong` — `string`  e.g. `1642399312083`, `1778232882021`, `1627966976222`
- `timezone` — `string`  e.g. `Asia/Calcutta`

### `pendingadmins`



### `admins`

  - `[]` — `object`
    - `$oid` — `string`  e.g. `5f24052520955e1aff464606`, `5f12d7d088cd370409e738ec`, `5f114ad25a61c636f00bc1d8`

### `pendingrequest`

  - `[]` — `object`
    - `$oid` — `string`  e.g. `64106b41fabf6c0694aa3bc2`, `6416978fd312b74c9f1c7862`, `5f7aacbf5040a53bdf49b275`

### `joinedrequest`

  - `[]` — `object`
    - `$oid` — `string`  e.g. `5f1c18a1beaf861a4dfb00a0`, `5f1c227fbeaf861a4dfb00aa`, `5f1c231ebeaf861a4dfb00ae`

### `coteacherrequests`

  - `[]` — `object`
    - `$oid` — `string`  e.g. `60ead9f2c317317e6ed5e6b6`, `612fc2605f3a3b0217f4b1eb`, `5f4f7dc565d1d75c36c881a8`

### `coteachers`

  - `[]` — `object`
    - `$oid` — `string`  e.g. `5f24052520955e1aff464606`, `602d030e247f6042e1a49486`, `5ff1c342dc3e91fa95bc5130`

### `timing`

  - `[]` — `object`
    - `day` — `string`  e.g. `Monday`, `Tuesday`, `Wednesday`
    - `from` — `string`  e.g. `09:00 AM`, `09:00 AM`, `09:00 AM`
    - `selected` — `bool`  e.g. `false`, `false`, `false`
    - `to` — `string`  e.g. `10:00 AM`, `10:00 AM`, `10:00 AM`

### `userid`

- `$oid` — `string`  e.g. `5f12d7d088cd370409e738ec`, `5f24052520955e1aff464606`, `5f4f7dc565d1d75c36c881a8`

### `classnumber`

- `$numberint` — `string`  e.g. `930031639`, `327790671`, `590338605`

### `timingversion`

- `$numberint` — `string`  e.g. `2`, `2`, `1`

### `settings`

- `admissionsdisabled` — `bool`  e.g. `false`, `false`, `false`
- `autoaccept` — `bool`  e.g. `true`, `false`, `false`
- `disablescreencapture` — `bool`  e.g. `true`, `false`, `false`
- `disablestudentcomments` — `bool`  e.g. `true`, `false`, `false`
- `disablestudentdiscussions` — `bool`  e.g. `true`, `false`, `false`
- `disablewebsdk` — `bool`  e.g. `false`, `false`, `false`
- `lockafter` — `object`
  - `$numberint` — `string`  e.g. `0`, `0`, `0`
- `lockclassroom` — `bool`  e.g. `false`, `false`, `false`
- `magicjointokenconfig` — `object` (nullable)
  - `enabledon` — `object`
    - `$date` — `object`
      - `$numberlong` — `string`  e.g. `1651123898550`, `1709372343859`, `1655710818944`
  - `loginrequired` — `bool`  e.g. `false`, `false`, `false`
  - `registrationrequired` — `bool`  e.g. `false`, `false`, `false`
  - `token` — `string`  e.g. `[REDACTED]`
- `openclassroom` — `bool`  e.g. `false`, `false`, `false`
- `providecertification` — `bool`  e.g. `false`, `false`, `false`
- `validityindays` — `object`
  - `$numberint` — `string`  e.g. `-1`, `-1`, `-1`
- `videoplayrestriction` — `object`
  - `$numberint` — `string`  e.g. `-1`, `-1`, `-1`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1595674634835`, `1596196200489`, `1599357755520`

### `deletedstudents`

  - `[]` — `object`
    - `deletedon` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1625754638451`, `1625820906840`, `1628072798202`
    - `type` — `string`  e.g. `LEFT`, `LEFT`, `LEFT`
    - `userid` — `object`
      - `$oid` — `string`  e.g. `5f243ed620955e1aff464759`, `60cd690d06289c2b87e7925e`, `5f1c5ef1beaf861a4dfb0145`

### `suspendedstudents`

  - `[]` — `object`
    - `reason` — `string`  e.g. `SUSPEND`, `FEE_DELAY`, `FEE_DELAY`
    - `userid` — `object`
      - `$oid` — `string`  e.g. `6200f1e9df223de403f26533`, `61979952f87200bff5a3127c`, `6198ed10f83f2c5cae530341`

### `instituteid`

- `$oid` — `string`  e.g. `61fb71e08a1e29d5377950c7`, `61f2d3edb05c886b68933877`, `628248254b26fc00082a094e`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__class`(
  `_id` string, 
  `namespace` string, 
  `zoomlink` string, 
  `pendingadmins` string, 
  `admins` string, 
  `pendingrequest` string, 
  `joinedrequest` string, 
  `coteacherrequests` string, 
  `coteachers` string, 
  `archived` string, 
  `disablereminder` string, 
  `lockclassroom` string, 
  `subject` string, 
  `timing` string, 
  `userid` string, 
  `name` string, 
  `classnumber` string, 
  `timingversion` string, 
  `schedule` string, 
  `settings` string, 
  `oldschedules` string, 
  `createdat` string, 
  `deletedstudents` string, 
  `suspendedstudents` string, 
  `instituteid` string, 
  `__v` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/class/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_003453_00070_gqk5w', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
