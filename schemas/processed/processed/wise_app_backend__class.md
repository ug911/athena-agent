---
database: processed
table: wise_app_backend__class
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/class/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:14:09+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__class`

## Columns

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

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `namespace`: `wise (×111)`, `zeal (×78)`, `vital (×4)`, `acadedge (×4)`, `nuqoosherah (×2)`, `rise (×1)`
- `archived`: `false (×200)`
- `disablereminder`: `false (×168)`
- `lockclassroom`: `false (×148)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `5f1c100abeaf861a4dfb009c`, `5f24056820955e1aff464608`, `5f4bbf9638a21be52f0b8e8d`

### `zoomlink`

- `join_url` — `string`  e.g. `https://zoom.us/j/99218613889?pwd=cXh4UDk3cUdkR1pWeEZkcHRHSl`
- `meetinguuid` — `string`  e.g. `T4gs2pu1QIafYi4P0kPQZw==`
- `mettingended` — `bool`  e.g. `true`, `true`, `true`
- `mettingid` — `string`  e.g. `99218613889`
- `password` — `string`  e.g. `[REDACTED]`
- `start_url` — `string`  e.g. `https://zoom.us/s/99218613889?zak=eyJ6bV9za20iOiJ6bV9vMm0iLC`
- `starttime` — `object`
  - `$date` — `object`
    - `$numberlong` — `string`  e.g. `1642399312083`, `1777279160826`, `1650368733094`
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



### `coteachers`

  - `[]` — `object`
    - `$oid` — `string`  e.g. `5f24052520955e1aff464606`, `61eacd6ad629f04e583b84ee`, `609faac6e4f4d71eb0672d1f`

### `timing`

  - `[]` — `object`
    - `day` — `string`  e.g. `Monday`, `Tuesday`, `Wednesday`
    - `from` — `string`  e.g. `09:00 AM`, `09:00 AM`, `09:00 AM`
    - `selected` — `bool`  e.g. `false`, `false`, `false`
    - `to` — `string`  e.g. `10:00 AM`, `10:00 AM`, `10:00 AM`

### `userid`

- `$oid` — `string`  e.g. `5f12d7d088cd370409e738ec`, `5f24052520955e1aff464606`, `5f4bbf3938a21ba5bd0b8e8b`

### `classnumber`

- `$numberint` — `string`  e.g. `930031639`, `327790671`, `173353960`

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
      - `$numberlong` — `string`  e.g. `1651123898550`, `1709372343859`, `1671556448199`
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
  - `$numberlong` — `string`  e.g. `1595674634835`, `1596196200489`, `1598799766775`

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
      - `$oid` — `string`  e.g. `6200f1e9df223de403f26533`, `5f154a7e88cd370409e739be`, `5f12d7d088cd370409e738ec`

### `instituteid`

- `$oid` — `string`  e.g. `61fb71e08a1e29d5377950c7`, `61f2d3edb05c886b68933877`, `628248251aac4d000792f1ad`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

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
  'trino_query_id'='20260428_002958_00007_xkyhq', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
