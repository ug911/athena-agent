---
canonical: processed
table: wise_app_backend__user
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/user/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:29:03+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__user`

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
| `isadmin` | `string` |  |
| `activesessions` | `string` |  |
| `block` | `string` |  |
| `profilepicture` | `string` |  |
| `pendingrequest` | `string` |  |
| `joinedrequest` | `string` |  |
| `adminpendingrequest` | `string` |  |
| `adminrequest` | `string` |  |
| `publicprofile` | `string` |  |
| `premiumconfig` | `string` |  |
| `name` | `string` |  |
| `profile` | `string` |  |
| `phonenumber` | `string` |  |
| `config` | `string` |  |
| `createdat` | `string` |  |
| `notificationtokens` | `string` |  |
| `__v` | `string` |  |
| `lastloggedinon` | `string` |  |
| `acquiredby` | `string` |  |
| `referralcode` | `string` |  |
| `referrallink` | `string` |  |
| `zoomaccountid` | `string` |  |
| `zoomprefix` | `string` |  |
| `zoomuserid` | `string` |  |
| `lastmeetingstartedon` | `string` |  |
| `uuid` | `string` |  |
| `updatedat` | `string` |  |
| `identities` | `string` |  |
| `email` | `string` |  |
| `referrer` | `string` |  |
| `loginpin` | `string` |  |
| `sessions` | `string` |  |
| `settings` | `string` |  |
| `parentid` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `block`: `false (×200)`
- `profile`: `student (×179)`, `teacher (×16)`, `parent (×5)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `697a096eaf7fbc5ac858d657`, `697a0984af7fbc5ac858e8da`, `697a0999af7fbc5ac858ff8b`

### `publicprofile`

- `gradesteaching` — `array<unknown>`
- `ispublic` — `bool`  e.g. `false`, `false`, `false`
- `marketingtemplates` — `array<unknown>`
- `subdomainscreated` — `object`
  - `$numberint` — `string`  e.g. `0`, `0`, `0`
- `subjects` — `array<unknown>`
- `teachinglanguages` — `array<unknown>`
- `teachingpreference` — `object`
  - `offline` — `bool`  e.g. `false`, `false`, `false`
  - `online` — `bool`  e.g. `false`, `false`, `false`
- `testimonials` — `array<unknown>`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1769605486749`, `1769605508416`, `1769605529816`

### `notificationtokens`

  - `[]` — `object`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1770558742313`, `1769606014084`, `1769606160692`
    - `platform` — `string`  e.g. `android`, `ios`, `android`
    - `projectid` — `string`  e.g. `wise-ios-wl`, `whitelabel2-c27d7`, `wise-ios-wl`
    - `sessionid` — `object`
      - `$oid` — `string`  e.g. `698895146d88f1c24e54e590`, `697a0b7cdb625933f0f5a1ca`, `697a0c0ba142aaf08e11d0a7`
    - `token` — `string`  e.g. `[REDACTED]`
    - `type` — `string`  e.g. `push`, `push`, `push`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `lastloggedinon`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786248315306`, `1769606904468`, `1777474928363`

### `acquiredby`

- `$oid` — `string`  e.g. `64dcc3f2cacfaa35815f90c8`, `617ad86e5bed0c468fae3c09`, `64dcc3f2cacfaa35815f90c8`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1786248315306`, `1769606904468`, `1769605529832`

### `identities`

  - `[]` — `object`
    - `identifier` — `string`  e.g. `6461432`, `6342461`, `bmbUm2yIjIMUWLkeFYhox3GAYVh1`
    - `provider` — `string`  e.g. `VENDOR_USER_ID`, `VENDOR_USER_ID`, `FIREBASE_ID`
    - `providermetadata` — `object`
      - `displayname` — `string`  e.g. `[REDACTED]`
      - `email` — `string`  e.g. `[REDACTED]`
      - `photourl` — `string`  e.g. `https://lh3.googleusercontent.com/a/ACg8ocLynxUQzM9_YhjjL3Oi`, `https://lh3.googleusercontent.com/a/ACg8ocLoO1VCFDo7bsjuCwuS`, `https://lh3.googleusercontent.com/a/ACg8ocKKWSUCwrDslJ_mEc3U`
      - `providerid` — `string`  e.g. `google.com`, `google.com`, `google.com`
      - `uid` — `string`  e.g. `105923805156712991713`, `113716172055171011514`, `101345585819800858393`

### `referrer`

- `$oid` — `string`  e.g. `692067aac05630afe58d1388`, `692067aac05630afe58d1388`, `65c9cb4799d4bfaa0c260207`

### `sessions`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `6a75eb2a0339d6687e359252`, `6a75eb6c6cb961dd579663fd`, `6a75eb93e79f3e8291c90ac1`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1786112810658`, `1786112876325`, `1786112915601`
    - `deviceid` — `string`  e.g. `5e1f3353-8c90-4139-94a7-209719605dd5`, `c518a608-b876-45ec-9fda-0ddf2c7eaeea`, `c518a608-b876-45ec-9fda-0ddf2c7eaeea`
    - `devicename` — `string`  e.g. `Chrome WebView Android`, `Chrome Linux`, `Chrome Linux`
    - `identity` — `string`  e.g. `VENDOR_USER_ID`, `VENDOR_USER_ID`, `VENDOR_USER_ID`
    - `ip` — `string`  e.g. `122.170.223.81`, `122.170.223.81`, `122.170.223.81`
    - `platform` — `string`  e.g. `android`, `web`, `web`
    - `token` — `string`  e.g. `[REDACTED]`

### `settings`

- `timezone` — `string`  e.g. `Asia/Kolkata`, `Asia/Kolkata`, `Etc/GMT-3`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__user`(
  `_id` string, 
  `namespace` string, 
  `isadmin` string, 
  `activesessions` string, 
  `block` string, 
  `profilepicture` string, 
  `pendingrequest` string, 
  `joinedrequest` string, 
  `adminpendingrequest` string, 
  `adminrequest` string, 
  `publicprofile` string, 
  `premiumconfig` string, 
  `name` string, 
  `profile` string, 
  `phonenumber` string, 
  `config` string, 
  `createdat` string, 
  `notificationtokens` string, 
  `__v` string, 
  `lastloggedinon` string, 
  `acquiredby` string, 
  `referralcode` string, 
  `referrallink` string, 
  `zoomaccountid` string, 
  `zoomprefix` string, 
  `zoomuserid` string, 
  `lastmeetingstartedon` string, 
  `uuid` string, 
  `updatedat` string, 
  `identities` string, 
  `email` string, 
  `referrer` string, 
  `loginpin` string, 
  `sessions` string, 
  `settings` string, 
  `parentid` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/user/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_012910_00097_kgadn', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
