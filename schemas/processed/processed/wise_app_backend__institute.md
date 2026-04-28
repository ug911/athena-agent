---
database: processed
table: wise_app_backend__institute
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/Institute/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:15:12+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__institute`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `name` | `string` |  |
| `namespace` | `string` |  |
| `ownerid` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `settings` | `string` |  |
| `metadata` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `namespace`: `wise (×165)`, `zugzwang (×12)`, `wise_upsc (×10)`, `eclass (×4)`, `dailylearn (×3)`, `nios_class (×2)`, `lifeskilllearnings (×1)`, `image_classes (×1)`, `credence (×1)`, `zeal (×1)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `61eab31dc50cdf61457cf939`, `61eed44d6e5163e0dc11a841`, `61f00dee480a4768fca9ab48`

### `ownerid`

- `$oid` — `string`  e.g. `5f114ad25a61c636f00bc1d8`, `61e4f91f5ed4ada0eafd33a4`, `608435a470bd4b021da76348`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1642771229947`, `1643041869412`, `1643122158716`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1775552879556`, `1775552879556`, `1775030334437`

### `settings`

- `allowpublicregistrations` — `bool`  e.g. `true`, `true`, `true`
- `autorecord` — `bool`  e.g. `true`, `false`, `false`
- `autounsharerecording` — `bool`  e.g. `true`, `true`, `true`
- `calendarsettings` — `object`
  - `inviteattendees` — `bool`  e.g. `false`, `false`, `false`
- `chatsettings` — `object`
  - `enabled` — `bool`  e.g. `true`, `true`, `true`
- `classroomdefaultsettings` — `object`
  - `autoaccept` — `bool`  e.g. `true`, `true`, `true`
- `contractsettings` — `object`
  - `enabled` — `bool`  e.g. `false`, `false`, `false`
  - `showcontractstoparentonly` — `bool`  e.g. `false`, `false`, `false`
- `defaultcurrency` — `string`  e.g. `USD`, `INR`, `INR`
- `defaultsessioncancellationpolicynote` — `string`  e.g. `If you cancel, 
• 0 to 24 hours before the session, you will`, `If you cancel, 
• 0 to 24 hours before the session, you will`, `If you cancel,
• 0 to 12 hours before the session, you will `
- `devicebindingsettings` — `object`
  - `devicelimit` — `object`
    - `$numberint` — `string`  e.g. `5`, `5`, `5`
  - `enabled` — `bool`  e.g. `true`, `true`, `true`
- `disablerecordingresources` — `bool`  e.g. `false`, `false`, `false`
- `disablescreenrecording` — `bool`  e.g. `true`, `false`, `false`
- `disablestoprecording` — `bool`  e.g. `false`, `false`, `false`
- `disablewaitingroom` — `bool`  e.g. `false`, `true`, `true`
- `disablewebsdk` — `bool`  e.g. `false`, `true`, `true`
- `enableadhocsession` — `bool`  e.g. `true`, `true`, `true`
- `enablegoogledriveinassessments` — `bool`  e.g. `true`
- `enablemeetingannotation` — `bool`  e.g. `true`, `true`, `true`
- `enableresourcedownload` — `bool`  e.g. `false`, `true`, `false`
- `feesettings` — `object`
  - `allowaccessforpendingconfirmation` — `bool`  e.g. `true`, `true`, `true`
  - `autoapprovetutorpayouts` — `bool`  e.g. `false`, `false`, `false`
  - `autocharge` — `bool`  e.g. `true`, `false`, `false`
  - `autochargedaysafter` — `object`
    - `$numberint` — `string`  e.g. `1`, `1`, `1`
  - `enablecoupons` — `bool`  e.g. `false`, `false`, `false`
  - `enablefees` — `bool`  e.g. `true`, `true`, `true`
  - `enabletutorpayout` — `bool`  e.g. `false`, `false`, `false`
  - `invoiceadditionalnote` — `string`  e.g. `Terms and Conditions

1. You can see attendance of students `, `Payment Methods:
1. Stripe Payment.  Please register your de`
  - `invoicebillinginformation` — `string`  e.g. `36/5 Hustle Hub, 27th Main Road
Sector 2, HSR Layout
Bangalo`
  - `showfeestoparentonly` — `bool`  e.g. `false`, `false`, `false`
- `hidemeetingparticipants` — `bool`  e.g. `true`, `false`, `false`
- `joinlenssecondarycta` — `string`  e.g. `BROWSER`, `BROWSER`, `BROWSER`
- `localesettings` — `object`
  - `timeformat` — `string`  e.g. `12h`, `12h`, `12h`
- `meetingchatsetting` — `string`  e.g. `ENABLE_HOSTS`
- `notificationsettings` — `object`
  - `categoryconfig` — `object`
    - `sessionreminder_1440` — `object`
      - `disableemail` — `bool`  e.g. `false`
    - `sessionreminder_60` — `object`
      - `disableemail` — `bool`  e.g. `true`
      - `disablewhatsapp` — `bool`  e.g. `true`
    - `wisestudentinvite` — `object`
      - `disableemail` — `bool`  e.g. `false`
  - `disablewhatsapp` — `bool`  e.g. `true`
  - `enableemail` — `bool`  e.g. `true`, `true`
  - `enablewhatsapp` — `bool`  e.g. `true`, `true`
- `participantadditionalnotevisibility` — `string`  e.g. `ADMIN`, `ADMIN`
- `participantregistrationformvisibility` — `string`  e.g. `ADMIN`, `ADMIN`
- `recordingdeletionpolicy` — `object`
  - `classroomstoskip` — `array<object>|array<unknown>`
    - `recordingdeletionpolicy.classroomstoskip[]` — `object`
      - `$oid` — `string`  e.g. `6373ca920f8d8b5f2eadacb7`, `68dabcc3995c18132a1bd67b`, `68dabd81941dbba06af086e9`
  - `deleteafterdays` — `object`
    - `$numberint` — `string`  e.g. `-1`, `-1`, `-1`
- `sessionallowstartbeforeminutes` — `object`
  - `$numberint` — `string`  e.g. `30`, `10`, `30`
- `sessionnotstartedreminderdelay` — `object`
  - `$numberint` — `string`  e.g. `5`, `5`, `5`
- `sessionrecordingview` — `string`  e.g. `SPEAKER`, `GALLERY`, `GALLERY`
- `sessionsettings` — `object`
  - `advanceslotbookingbuffer` — `object`
    - `$numberint` — `string`  e.g. `60`, `720`, `60`
  - `allowonlyconsecutiveslotbooking` — `bool`  e.g. `false`, `false`, `false`
  - `allowstudenttocancelsession` — `bool`  e.g. `true`, `false`, `false`
  - `allowteacherfeedbackupdate` — `bool`  e.g. `true`, `true`, `true`
  - `allowteachertomanagecredits` — `bool`  e.g. `false`, `false`
  - `autosubmitsessionfeedback` — `bool`  e.g. `false`, `false`
  - `blockedadjacentslotbuffer` — `object`
    - `$numberint` — `string`  e.g. `0`, `0`, `0`
  - `bookingtimeslotgranularity` — `object`
    - `$numberint` — `string`  e.g. `15`, `15`, `15`
  - `creditsettings` — `object`
    - `autodeduct` — `bool`  e.g. `false`, `false`, `true`
    - `autodeductformissedsessions` — `bool`  e.g. `false`, `false`, `false`
    - `deductionstrategy` — `string`  e.g. `MANUAL`, `MANUAL`, `AT_SESSION_TIME`
    - `deductiontype` — `string`  e.g. `FIXED`, `FIXED`, `FIXED`
  - `disableaititle` — `bool`  e.g. `true`, `true`, `true`
  - `disableofflinesessions` — `bool`  e.g. `false`, `false`, `false`
  - `disallowconflict` — `bool`  e.g. `false`, `false`, `false`
  - `donotoverridehost` — `bool`  e.g. `false`, `false`
  - `enableinstitutelevelcredits` — `bool`  e.g. `true`, `true`
  - `enableliveclasscredits` — `bool`  e.g. `true`, `false`, `false`
  - `livemeetingprovider` — `string`  e.g. `ZOOM`, `ZOOM`, `ZOOM`
  - `maxadvanceslotbookingdays` — `object`
    - `$numberint` — `string`  e.g. `180`, `180`, `180`
  - `meetingsummaryvisibility` — `string`  e.g. `ALL`, `ALL`, `ALL`
  - `restrictteachersessionvisibility` — `bool`  e.g. `false`, `false`
  - `sessionaiconfig` — `object`
    - `enabled` — `bool`  e.g. `true`, `true`, `true`
  - `showscheduledtimeforpastsessionstostudents` — `bool`  e.g. `false`, `false`, `false`
  - `studentfeedbackvisibility` — `string`  e.g. `ADMIN`, `ADMIN_TEACHER`, `ADMIN`
  - `studentslotcancellationbuffer` — `object`
    - `$numberint` — `string`  e.g. `60`, `720`, `60`
  - `updatecreditaccess` — `string`  e.g. `ADMIN_TEACHER`, `ADMIN`, `ADMIN_TEACHER`
- `showwebinaroption` — `bool`  e.g. `false`, `false`, `false`
- `storeredirectionurl` — `string`  e.g. `https://lifeskilllearnings.com`, `https://www.youtube.com/@imageclasses`
- `taxsettings` — `object`
  - `defaulttaxrulegroupid` — `object`
    - `$oid` — `string`  e.g. `690af4b678722beb3bfa225b`
  - `enabled` — `bool`  e.g. `true`
- `teacheravailabilitysettings` — `object`
  - `disableupdatingleaves` — `bool`  e.g. `false`, `false`, `false`
  - `disableupdatingworkinghours` — `bool`  e.g. `false`, `false`, `false`
  - `enabled` — `bool`  e.g. `true`, `true`, `true`
- `teacherpermissions` — `object`
  - `disablecontentmanagement` — `bool`  e.g. `false`, `false`, `false`
  - `disablesessionmanagement` — `bool`  e.g. `false`, `false`, `false`
- `uploadresourcestoyoutube` — `bool`  e.g. `false`, `false`, `false`
- `welcomeemailnote` — `string`  e.g. `You now have easy, online access to view all of your tutorin`
- `zoomsettings` — `object`
  - `disablebreakoutroom` — `bool`  e.g. `false`, `false`, `false`
  - `enableparticipantscreensharing` — `bool`  e.g. `false`, `false`, `false`
  - `entryexitchime` — `string`  e.g. `NONE`, `NONE`, `NONE`
  - `hostvideoon` — `bool`  e.g. `false`, `false`, `false`

### `metadata`

- `institutesize` — `string`  e.g. `1_10`, `1_10`, `50_plus`
- `institutetype` — `string` (nullable)  e.g. `ONLINE`, `COACHING`, `ONLINE`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__institute`(
  `_id` string, 
  `name` string, 
  `namespace` string, 
  `ownerid` string, 
  `createdat` string, 
  `updatedat` string, 
  `settings` string, 
  `metadata` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/Institute/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_003518_00007_v8j8j', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
