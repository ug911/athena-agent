---
database: processed
table: wise_app_backend__user
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/user/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:17:39+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__user`

## Columns

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

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `block`: `false (×200)`
- `profile`: `student (×155)`, `teacher (×31)`, `parent (×14)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `698edfd4b0e4b23fd555566c`, `6982ac3f1b7926abce7d869f`, `6982ae81b57123bd1ba85059`

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
  - `$numberlong` — `string`  e.g. `1770971092139`, `1770171455067`, `1770172033087`

### `notificationtokens`

  - `[]` — `object`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1770971400838`, `1770470756616`, `1777124465158`
    - `platform` — `string`  e.g. `android`, `android`, `android`
    - `projectid` — `string`  e.g. `wise-ios-wl`, `wise-ios-wl`, `wise-ios-wl`
    - `sessionid` — `object`
      - `$oid` — `string`  e.g. `698ee1069cf02d744142ed3f`, `69873d60df66cd7ec510883c`, `69ecc33d94bc942cd1f48074`
    - `token` — `string`  e.g. `[REDACTED]`
    - `type` — `string`  e.g. `push`, `push`, `push`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `lastloggedinon`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1775406084301`, `1770190188863`, `1770172033105`

### `acquiredby`

- `$oid` — `string`  e.g. `65c9cb4799d4bfaa0c260207`, `63b2d8a693b4da8455eff514`, `63b2d8a693b4da8455eff514`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1775406084301`, `1770193087489`, `1770172033105`

### `identities`

  - `[]` — `object`
    - `identifier` — `string`  e.g. `gExGEbW83rdAQTCTObv3NFtbTxg2`, `[REDACTED-PHONE]`, `1770193087488_50c56077d8becac589a4efdad333a587`
    - `provider` — `string`  e.g. `FIREBASE_ID`, `PHONE_NUMBER`, `FIREBASE_ID`
    - `providermetadata` — `object`
      - `displayname` — `string`  e.g. `[REDACTED]`
      - `email` — `string`  e.g. `[REDACTED]`
      - `photourl` — `string`  e.g. `https://lh3.googleusercontent.com/a/ACg8ocJpfbdyuWudVffXEbEA`, `https://lh3.googleusercontent.com/a/ACg8ocKrAD7eBPro7Bn5cmF9`, `https://lh3.googleusercontent.com/a/ACg8ocIyrhqAGrqSQwwJvR-n`
      - `providerid` — `string`  e.g. `google.com`, `google.com`, `google.com`
      - `uid` — `string`  e.g. `117815359944378628780`, `103923077803116488031`, `117807382925236385181`

### `referrer`

- `$oid` — `string`  e.g. `65d868629981243ddd1f5626`, `68b97e5969bf3cf7e1f7aada`, `6801059fcdd211ec15a16a2d`

### `sessions`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `698edfd4d148845c8a3e0aa1`, `698ee1069cf02d744142ed3f`, `699070d2569e897dbc528699`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1770971092154`, `1770971398487`, `1771073746317`
    - `deviceid` — `string`  e.g. `fccd84d8-0bd4-4128-ada3-855836c4f915`, `c81a558e-6da0-4172-b5c7-f109821e90d6`, `fccd84d8-0bd4-4128-ada3-855836c4f915`
    - `devicename` — `string`  e.g. `Chrome Android`, `Unknown`, `Chrome Android`
    - `identity` — `string`  e.g. `FIREBASE_ID`, `FIREBASE_ID`, `DIRECT_LOGIN_LINK`
    - `ip` — `string`  e.g. `122.170.195.214`, `122.170.195.214`, `117.99.249.107`
    - `platform` — `string`  e.g. `web`, `android`, `web`
    - `token` — `string`  e.g. `[REDACTED]`

### `settings`

- `sessionsettings` — `object`
  - `advanceslotbookingbuffer` — `object`
    - `$numberint` — `string`  e.g. `60`, `60`, `2880`
  - `allowonlyconsecutiveslotbooking` — `bool`  e.g. `true`, `true`, `true`
  - `blockedadjacentslotbuffer` — `object`
    - `$numberint` — `string`  e.g. `30`, `60`, `5`
- `timezone` — `string`  e.g. `Asia/Kolkata`, `Asia/Kolkata`, `Asia/Kolkata`

## DDL

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
  'trino_query_id'='20260428_011905_00061_iuhsy', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
