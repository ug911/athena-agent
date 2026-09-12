---
canonical: processed
table: wise_app_backend__user_2007
type: table
layer: processed
regions:
  na: processed_na
location: s3://[REDACTED-BUCKET]/backup_na/2026_07_20_00_10/wise-app-backend/user
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:29:07+00:00'
sampled_rows: 200
sampled_region: na
---

# `processed.wise_app_backend__user_2007`

## Region availability

| Region | Athena database |
| --- | --- |
| `NA` | `processed_na` |

_Only present in **NA**._

## Columns (NA)

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

_String columns with ≤20 distinct values in 200 sampled rows from `NA`. Distribution shown as `value (×count)`._

- `namespace`: `jhmi (×81)`, `wise (×76)`, `online (×6)`, `bluelearning (×6)`, `usmonkey (×5)`, `wise-demo (×5)`, `jmcg-maths-mentors (×4)`, `radical-reading (×3)`, `la-dame-atelier-d-une-sa (×2)`, `mr-johns-test-prep (×2)`, `abhijeettest (×1)`, `testus-insitute (×1)`, `nyctestprep (×1)`, `telostutors (×1)`, `rjinstitute (×1)`, `bible-academy (×1)`, `geography-study-of-ear (×1)`, `jonathanpovey (×1)`, `write-in (×1)`, `experience-house (×1)`
- `block`: `false (×199)`
- `profile`: `student (×126)`, `teacher (×70)`, `parent (×4)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `NA` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `601cccadac6b3b85b94c4412`, `6720dc21bfeca179d1c77fcb`, `6720dfecec51d33f822dcb2f`

### `activesessions`



### `publicprofile`

- `gradesteaching` — `array<unknown>`
- `ispublic` — `bool`  e.g. `false`, `false`, `false`
- `marketingtemplates` — `array<unknown>`
- `subdomainscreated` — `object`
  - `$numberdouble` — `string`  e.g. `0.0`
  - `$numberint` — `string`  e.g. `0`, `0`, `0`
- `subjects` — `array<unknown>`
- `teachinglanguages` — `array<unknown>`
- `teachingpreference` — `object`
  - `offline` — `bool`  e.g. `false`, `false`, `false`
  - `online` — `bool`  e.g. `false`, `false`, `false`
- `testimonials` — `array<unknown>`

### `premiumconfig`

- `licensed` — `bool`  e.g. `false`, `false`, `false`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1593561600000`, `1730206753738`, `1730207724048`

### `notificationtokens`

  - `[]` — `object`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1757517067933`, `1771151365909`, `1758136748954`
    - `platform` — `string`  e.g. `ios`, `ios`, `android`
    - `projectid` — `string`  e.g. `wise-ios-wl`, `wise-ios-wl`
    - `sessionid` — `object`
      - `$oid` — `string`  e.g. `68b957bb0f4b56c8d25dce2b`, `6991a00485c7cd376451afac`, `68ac74bad6506c2fd3d23931`
    - `token` — `string`  e.g. `[REDACTED]`
    - `type` — `string`  e.g. `push`, `push`, `push`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `lastloggedinon`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1770102651763`, `1773236041058`, `1730271889267`

### `acquiredby`

- `$oid` — `string`  e.g. `6720dfecec51d33f822dcb2f`, `6720dfecec51d33f822dcb2f`, `6720dfecec51d33f822dcb2f`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1722004955066`, `1770102651764`, `1773236041058`

### `identities`

  - `[]` — `object`
    - `identifier` — `string`  e.g. `0000000000`, `l65IEl25eyd9LaZJjr1Z8yGdD4t1`, `BKiVmsxA66NJDyJu7xyzYFGwuDM2`
    - `provider` — `string`  e.g. `PHONE_NUMBER`, `FIREBASE_ID`, `FIREBASE_ID`
    - `providermetadata` — `object`
      - `displayname` — `string`  e.g. `[REDACTED]`
      - `email` — `string`  e.g. `[REDACTED]`
      - `photourl` — `string`  e.g. `https://lh3.googleusercontent.com/a/ACg8ocLled_WCPCc8kcJc7ZP`, `https://lh3.googleusercontent.com/a/ACg8ocLi4fnU8OQ-d135yK1G`, `https://lh3.googleusercontent.com/a/ACg8ocIQtcb2OedlEMRh0HIH`
      - `providerid` — `string`  e.g. `google.com`, `google.com`, `google.com`
      - `uid` — `string`  e.g. `100888751102816993238`, `110057832020426446726`, `104536673218797560117`

### `referrer`

- `$oid` — `string`  e.g. `6720dfecec51d33f822dcb2f`, `6720dfecec51d33f822dcb2f`, `649fac64593b3e2bfda31e85`

### `sessions`

  - `[]` — `object`
    - `_id` — `object`
      - `$oid` — `string`  e.g. `6887244f9d3c53c07080fd59`, `6887244f0a96b8fa87ad6c71`, `69819f7b08abd85de904fbf1`
    - `createdat` — `object`
      - `$date` — `object`
        - `$numberlong` — `string`  e.g. `1753687119424`, `1753687119647`, `1770102651715`
    - `deviceid` — `string`  e.g. `8fd3cb14-cbe9-4bb0-9d1a-76a6638216e4`, `8fd3cb14-cbe9-4bb0-9d1a-76a6638216e4`, `8fd3cb14-cbe9-4bb0-9d1a-76a6638216e4`
    - `devicename` — `string`  e.g. `Chrome Mac OS`, `Chrome Mac OS`, `Chrome Mac OS`
    - `identity` — `string`  e.g. `FIREBASE_ID`, `FIREBASE_ID`, `FIREBASE_ID`
    - `ip` — `string`  e.g. `106.213.80.160`, `106.213.80.160`, `122.171.16.218`
    - `platform` — `string`  e.g. `web`, `web`, `web`
    - `token` — `string`  e.g. `[REDACTED]`

### `settings`

- `allowlicenseoverage` — `bool`  e.g. `false`, `false`, `false`
- `timezone` — `string`  e.g. `Asia/Kolkata`, `Asia/Kolkata`, `America/New_York`

### `parentid`

- `$oid` — `string`  e.g. `68596db304b8dbd4b0efbf52`, `685a742304b8dbd4b00c45e4`, `685c2aca04b8dbd4b0401133`

## DDL


```sql
CREATE EXTERNAL TABLE `processed_na.wise_app_backend__user_2007`(
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
  's3://[REDACTED-BUCKET]/backup_na/2026_07_20_00_10/wise-app-backend/user'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'transient_lastDdlTime'='1785415932', 
  'trino_query_id'='20260730_003938_00061_7d5fs', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
