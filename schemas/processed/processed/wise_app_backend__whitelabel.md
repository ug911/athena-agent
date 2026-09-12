---
canonical: processed
table: wise_app_backend__whitelabel
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/Whitelabel/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:30:05+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__whitelabel`

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
| `featureconfig` | `string` |  |
| `hostnames` | `string` |  |
| `adminuserids` | `string` |  |
| `displayconfig` | `string` |  |
| `namespace` | `string` |  |
| `apphash` | `string` |  |
| `__v` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `versionconfig` | `string` |  |
| `systemconfig` | `string` |  |
| `disabled` | `string` |  |
| `contactmobile` | `string` |  |
| `trialclassid` | `string` |  |
| `faqurl` | `string` |  |
| `privacypolicyurl` | `string` |  |
| `customauthconfig` | `string` |  |
| `defaultinstituteid` | `string` |  |
| `maxlogins` | `string` |  |
| `additionalconfig` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `disabled`: `false (×119)`, `true (×81)`

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `623c050d4e08e40022c593a7`, `623c050d4e08e40022c593ab`, `623c050d4e08e40022c593b0`

### `featureconfig`

- `adminuserids` — `array<string>|array<unknown>`
  - `adminuserids[]` — `string`  e.g. `60c6fcee0e0c3a0019fac4e2`, `6297567c258178a6a60ed2d8`, `6093c17ef339108cdb84dc7b`
- `cancreateclassrooms` — `bool`  e.g. `true`, `true`, `true`
- `disableapplelogin` — `bool`  e.g. `false`, `false`, `false`
- `disableemaillogin` — `bool`  e.g. `true`, `false`, `false`
- `disablefees` — `bool`  e.g. `true`, `false`, `false`
- `disablegooglelogin` — `bool`  e.g. `true`, `false`, `false`
- `disableparticipantunmute` — `bool`  e.g. `true`
- `disableparticipantvideo` — `bool`  e.g. `true`
- `disablephonelogin` — `bool`  e.g. `false`, `false`, `false`
- `disablewisebranding` — `bool`  e.g. `true`
- `enablecustomytplayer` — `bool`  e.g. `true`, `true`, `true`
- `enablejwtbasedlogin` — `bool`  e.g. `false`, `false`, `false`
- `enablelens` — `bool`  e.g. `true`, `true`, `true`
- `enablelenstroubleshoot` — `bool`  e.g. `true`
- `enableloginpin` — `bool`  e.g. `[REDACTED]`
- `enableparentportal` — `bool`  e.g. `true`, `true`, `true`
- `enablesociallogin` — `bool`  e.g. `true`, `true`, `true`

### `hostnames`

  - `[]` — `string`  e.g. `web.wiseapp.live`, `wl.wiseapp.live`, `web.wise.live`

### `adminuserids`

  - `[]` — `string`  e.g. `60c6fcee0e0c3a0019fac4e2`, `6297567c258178a6a60ed2d8`, `61cc05ac169ac8b26e8a55e1`

### `displayconfig`

- `androidappurl` — `string`  e.g. `https://play.google.com/store/apps/details?id=com.wise.app`, `https://play.google.com/store/apps/details?id=com.wise.pooja`, `https://play.google.com/store/apps/details?id=com.wise.pps`
- `appiconlink` — `string`  e.g. `https://firebasestorage.googleapis.com/v0/b/wise-leap-app.ap`, `https://firebasestorage.googleapis.com/v0/b/wise-leap-app.ap`, `https://firebasestorage.googleapis.com/v0/b/wise-leap-app.ap`
- `brandingfavicon` — `string`  e.g. `https://cdn.wiseapp.live/images/wise_favicon.png`, `https://cdn.wiseapp.live/whitelabel/madmonkey/madmonkey_logo`, `https://cdn.wiseapp.live/whitelabel/zug_zwang/zug_zwang_logo`
- `brandinglogo` — `string`  e.g. `https://cdn.wiseapp.live/images/wise-logo-white.svg`, `https://cdn.wiseapp.live/whitelabel/vital/app_logo.png`, `https://cdn.wiseapp.live/whitelabel/pooja/pooja_logo.png`
- `brandingname` — `string`  e.g. `WISE`, `VITAL`, `POOJA INTERNATIONAL ACADEMY`
- `contactemail` — `string`  e.g. `[REDACTED]`
- `contactmobile` — `string`  e.g. `[REDACTED]`
- `defaultcountrycode` — `string`  e.g. `GB`
- `faqurl` — `string`  e.g. `https://eclassapp.live/faq/`, `https://www.nwkings.com/#faq`, `https://topachievers.in/faqs`
- `footerstring` — `string`  e.g. `&copy; Wise Leap Technologies Pvt Ltd`, `&copy; Wise Leap Technologies Pvt Ltd`, `&copy; Wise Leap Technologies Pvt Ltd`
- `homeurl` — `string`  e.g. `/lens/home`, `/waiting-home`, `/waiting-home`
- `iosappurl` — `string`  e.g. `https://apps.apple.com/app/id1525875644`, `https://apps.apple.com/in/app/lens-learner-app/id1641075491`, `https://apps.apple.com/us/app/adrplexus-online-live/id675641`
- `lensinmeetingicon` — `string`  e.g. `https://cdn.wiseapp.live/whitelabel/jhmi/in_meeting_icon.png`, `https://cdn.wiseapp.live/whitelabel/yellowmonkey/yellowmonke`
- `loginbackgroundimage` — `string`  e.g. `https://cdn.wiseapp.live/whitelabel/edunique/edunique_backgr`, `https://cdn.wiseapp.live/whitelabel/bmc/bmc_logo_2.webp`
- `macappurl` — `string`  e.g. `https://cdn.wiseapp.live/files/lens/madmonkey/Mad%20Monkey.d`, `https://cdn.wiseapp.live/files/lens/vmc/VMC%20Live.dmg`, `https://cdn.wiseapp.live/files/lens/wise_lens/Lens.dmg`
- `namevariables` — `object`
  - `admin` — `string`  e.g. `manager`, `admin`, `admin`
  - `assessment` — `string`  e.g. `assignment`, `assessment`, `assessment`
  - `classroom` — `string`  e.g. `batch`, `course`, `course`
  - `classroomname` — `string`  e.g. `batch name`, `name`, `name`
  - `classroomsubject` — `string`  e.g. `batch stream`, `subject`, `subject`
  - `content` — `string`  e.g. `material`, `content`, `content`
  - `criteria` — `string`  e.g. `criteria`, `criteria`, `criteria`
  - `discussion` — `string`  e.g. `post`, `discussion`, `discussion`
  - `group` — `string`  e.g. `batch folder`, `bundle`, `bundle`
  - `institute` — `string`  e.g. `organization`, `institute`, `institute`
  - `invoice` — `string`  e.g. `invoice`
  - `liveclassroom` — `string`  e.g. `batch`, `group course`, `group course`
  - `onetooneclassroom` — `string`  e.g. `individual batch`, `1:1 course`, `1:1 course`
  - `parent` — `string`  e.g. `parent`, `parent`, `parent`
  - `recordedclassroom` — `string`  e.g. `self paced`, `recorded course`, `recorded course`
  - `resource` — `string`  e.g. `file`, `resource`, `resource`
  - `session` — `string`  e.g. `class`, `session`, `session`
  - `store` — `string`  e.g. `store`
  - `student` — `string`  e.g. `student`, `learner`, `learner`
  - `teacher` — `string`  e.g. `teacher`, `instructor`, `instructor`
  - `test` — `string`  e.g. `test`, `test`, `test`
- `portalurl` — `string`  e.g. `https://oll.co/teacher/upcoming`, `https://learn-giap.talentsprint.com/`, `https://bambinos.live/dashboard-redirect`
- `privacypolicyurl` — `string`  e.g. `https://eclassapp.live/privacy-policy/`, `https://www.nwkings.com/privacy-policy`, `https://www.zugzwang.in/terms-privacy`
- `siteurl` — `string`  e.g. `https://www.wise.live/`, `https://vitaledu.in/`, `http://pioneerschool.in/`
- `sociallinks` — `array<object>|array<unknown>`
  - `sociallinks[]` — `object`
    - `link` — `string`  e.g. `https://www.youtube.com/c/risewithrise`, `https://twitter.com/risewithrise`, `https://www.facebook.com/RiseWithRiSE/`
    - `type` — `string`  e.g. `youtube`, `twitter`, `facebook`
- `superadminhomeurl` — `string`  e.g. `/lens/home`, `/lens/home`, `/lens/home`
- `tollfreenumber` — `string`  e.g. `1800 120 1334`, `[REDACTED-PHONE]`, `[REDACTED-PHONE]`
- `trialclassid` — `string`  e.g. `520952101`, `520952101`, `816260781`
- `windowsappurl` — `string`  e.g. `https://cdn.wiseapp.live/files/lens/madmonkey/Mad%20Monkey.e`, `https://cdn.wiseapp.live/files/lens/vmc/VMC%20Live.exe`, `https://cdn.wiseapp.live/files/lens/wise_lens/Lens.exe`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1648100621497`, `1648100621499`, `1648100621500`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1691055872427`, `1750307389437`, `1750307389437`

### `versionconfig`

- `android` — `object`
  - `latestbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `376`, `1`, `1`
    - `$numberlong` — `string`  e.g. `117`
  - `latestversionname` — `string`  e.g. `8.8.0`, `0.2.1`, `1.8.0`
  - `minbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `338`, `1`, `1`
    - `$numberlong` — `string`  e.g. `117`
- `ios` — `object`
  - `latestbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `259`, `109`, `109`
  - `latestversionname` — `string`  e.g. `4.0.0`, `1.8.0`
  - `minbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `255`, `1`, `1`
- `mac` — `object`
  - `latestbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `9`, `5`, `1`
    - `$numberlong` — `string`  e.g. `36`
  - `minbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `6`, `33`, `1`
- `windows` — `object`
  - `latestbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `10`, `3`, `1`
    - `$numberlong` — `string`  e.g. `36`
  - `latestversionname` — `string`  e.g. `1.2.0`
  - `minbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `6`, `33`, `1`

### `systemconfig`

- `apphash` — `string`  e.g. `+PR6bqfkvts`, `2+oeKDEePuB`, `eZeqQhxeqWZ`
- `customauthconfig` — `object`
  - `jwttokensecret` — `string`  e.g. `[REDACTED]`
- `defaultprofilepicture` — `string`  e.g. `https://cdn.wiseapp.live/whitelabel/topmate/topmate_logo_2.p`, `https://cdn.wiseapp.live/whitelabel/functionup/default.png`
- `maxlogins` — `object`
  - `$numberint` — `string`  e.g. `1`, `5`, `1`
- `securevideorestrictions` — `object`
  - `enforcesecureapp` — `bool`  e.g. `false`, `false`, `false`

### `customauthconfig`

- `jwttokensecret` — `string`  e.g. `[REDACTED]`

### `defaultinstituteid`

- `$oid` — `string`  e.g. `62824921b93ee30009caa8bf`, `62824ae549eb5400074cd75a`, `61fc06b54b31f9e992f780b5`

### `maxlogins`

- `$numberint` — `string`  e.g. `3`, `5`, `1`

### `additionalconfig`

- `ytplayer` — `bool`  e.g. `true`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__whitelabel`(
  `_id` string, 
  `featureconfig` string, 
  `hostnames` string, 
  `adminuserids` string, 
  `displayconfig` string, 
  `namespace` string, 
  `apphash` string, 
  `__v` string, 
  `createdat` string, 
  `updatedat` string, 
  `versionconfig` string, 
  `systemconfig` string, 
  `disabled` string, 
  `contactmobile` string, 
  `trialclassid` string, 
  `faqurl` string, 
  `privacypolicyurl` string, 
  `customauthconfig` string, 
  `defaultinstituteid` string, 
  `maxlogins` string, 
  `additionalconfig` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/Whitelabel/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_013318_00007_yckch', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
