---
canonical: processed
table: wise_app_backend__institute
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/Institute/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:23:54+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__institute`

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
| `name` | `string` |  |
| `namespace` | `string` |  |
| `ownerid` | `string` |  |
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `settings` | `string` |  |
| `metadata` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `61eab31dc50cdf61457cf939`, `61eed44d6e5163e0dc11a841`, `61f1111376d8fd11d34dc4d0`

### `ownerid`

- `$oid` — `string`  e.g. `5f114ad25a61c636f00bc1d8`, `61e4f91f5ed4ada0eafd33a4`, `5f365e25f02b25bb4f7764ee`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1642771229947`, `1643041869412`, `1643188499438`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1778063297523`, `1778063297523`, `1778063297523`

### `settings`

- `accesscontrol` — `object`
  - `classroomlevel` — `object`
    - `delete_class` — `object`
      - `admin` — `bool`  e.g. `true`
- `aireportsettings` — `object`
  - `enabled` — `bool`  e.g. `true`, `true`, `true`
  - `preview` — `bool`  e.g. `true`, `true`, `true`
- `allowpublicregistrations` — `bool`  e.g. `true`, `true`, `true`
- `autorecord` — `bool`  e.g. `true`, `false`, `false`
- `autounsharerecording` — `bool`  e.g. `true`, `true`, `true`
- `blockedplatforms` — `array<string>`
  - `blockedplatforms[]` — `string`  e.g. `ios`, `web`
- `calendarsettings` — `object`
  - `inviteattendeeparents` — `bool`  e.g. `false`, `false`, `false`
  - `inviteattendees` — `bool`  e.g. `false`, `false`, `false`
  - `invitedemoattendees` — `bool`  e.g. `true`, `true`, `true`
  - `sendupdates` — `bool`  e.g. `true`, `true`, `true`
- `chatsettings` — `object`
  - `chatpermissions` — `object`
    - `parent` — `object`
      - `classadmin` — `bool`  e.g. `true`, `true`, `true`
      - `enabled` — `bool`  e.g. `true`, `true`, `true`
      - `teacher` — `bool`  e.g. `true`, `true`, `true`
    - `student` — `object`
      - `classadmin` — `bool`  e.g. `true`, `true`, `true`
      - `enabled` — `bool`  e.g. `true`, `true`, `true`
      - `teacher` — `bool`  e.g. `true`, `true`, `true`
    - `teacher` — `object`
      - `classadmin` — `bool`  e.g. `true`, `true`, `true`
      - `enabled` — `bool`  e.g. `true`, `true`, `true`
      - `parent` — `bool`  e.g. `true`, `true`, `true`
      - `student` — `bool`  e.g. `true`, `true`, `true`
      - `teacher` — `bool`  e.g. `true`, `true`, `true`
  - `enabled` — `bool`  e.g. `true`, `true`, `true`
  - `reactionsenabled` — `bool`  e.g. `true`, `true`, `true`
- `classroomdefaultsettings` — `object`
  - `autoaccept` — `bool`  e.g. `true`, `true`, `true`
  - `magicjointokenconfig` — `object`
    - `loginrequired` — `bool`  e.g. `false`, `false`, `false`
    - `registrationrequired` — `bool`  e.g. `false`, `false`, `false`
- `contractsettings` — `object`
  - `enabled` — `bool`  e.g. `false`, `false`, `false`
  - `showcontractstoparentonly` — `bool`  e.g. `false`, `false`, `false`
- `defaultcurrency` — `string`  e.g. `USD`, `INR`, `USD`
- `defaultsessioncancellationpolicynote` — `string`  e.g. `If you cancel, 
• 0 to 24 hours before the session, you will`, `If you cancel, 
• 0 to 24 hours before the session, you will`, `If you cancel,
• 0 to 12 hours before the session, you will `
- `devicebindingsettings` — `object`
  - `devicelimit` — `object`
    - `$numberint` — `string`  e.g. `5`, `5`, `5`
  - `enabled` — `bool`  e.g. `true`, `true`, `true`
- `disableautoadmit` — `bool`  e.g. `true`, `true`
- `disablerecordingresources` — `bool`  e.g. `false`, `false`, `false`
- `disablescreenrecording` — `bool`  e.g. `true`, `false`, `false`
- `disablesessionlivestreaming` — `bool`  e.g. `true`, `false`, `true`
- `disablestoprecording` — `bool`  e.g. `false`, `false`, `true`
- `disablewaitingroom` — `bool`  e.g. `false`, `true`, `false`
- `disablewebsdk` — `bool`  e.g. `false`, `true`, `true`
- `enableadhocsession` — `bool`  e.g. `true`, `true`, `true`
- `enablegoogledriveinassessments` — `bool`  e.g. `true`, `true`, `true`
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
1. Stripe Payment.  Please register your de`, `additional notes`
  - `invoicebillinginformation` — `string`  e.g. `36/5 Hustle Hub, 27th Main Road
Sector 2, HSR Layout
Bangalo`, `institute`, `Address: 13, Uttam Towers, Opp Aga Khan Palace, Nagar Road, `
  - `showfeestoparentonly` — `bool`  e.g. `false`, `false`, `false`
- `hidemeetingparticipants` — `bool`  e.g. `true`, `false`, `false`
- `hidespeakerviewparticipants` — `bool`  e.g. `true`, `true`, `true`
- `joinlensprimarycta` — `string`  e.g. `HIDE`, `HIDE`, `SHOW`
- `joinlenssecondarycta` — `string`  e.g. `BROWSER`, `BROWSER`, `BROWSER`
- `keeprawrecordings` — `bool`  e.g. `true`
- `localesettings` — `object`
  - `timeformat` — `string`  e.g. `12h`, `12h`, `12h`
- `meetingchatsetting` — `string`  e.g. `ENABLE_HOSTS`, `ENABLE_HOSTS`, `ENABLE_HOSTS`
- `notificationsettings` — `object`
  - `categoryconfig` — `object`
    - `certificatecreation` — `object`
      - `disableemail` — `bool`  e.g. `true`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `true`, `false`, `false`
    - `contractcreated` — `object`
      - `disableemail` — `bool`  e.g. `true`, `true`, `true`
      - `disablewhatsapp` — `bool`  e.g. `true`, `false`
    - `contractsigned` — `object`
      - `disableemail` — `bool`  e.g. `true`, `true`, `true`
      - `disablewhatsapp` — `bool`  e.g. `false`
    - `dailysessionreminder` — `object`
      - `disableemail` — `bool`  e.g. `true`, `true`, `true`
      - `disablewhatsapp` — `bool`  e.g. `true`, `true`, `true`
    - `demosessionreminder_2160` — `object`
      - `disableemail` — `bool`  e.g. `true`, `true`, `true`
      - `disablewhatsapp` — `bool`  e.g. `true`, `true`, `true`
    - `demosessionupdated` — `object`
      - `disableemail` — `bool`  e.g. `false`
      - `disablewhatsapp` — `bool`  e.g. `false`
    - `discussioncreated` — `object`
      - `disableemail` — `bool`  e.g. `true`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `true`, `true`, `false`
    - `feeadded` — `object`
      - `disableemail` — `bool`  e.g. `false`, `true`, `false`
      - `disablewhatsapp` — `bool`  e.g. `false`, `true`, `true`
    - `feeaddedautocharge` — `object`
      - `disableemail` — `bool`  e.g. `false`, `true`, `false`
      - `disablewhatsapp` — `bool`  e.g. `false`, `true`, `true`
    - `feedue` — `object`
      - `disableemail` — `bool`  e.g. `false`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `false`, `false`, `false`
    - `feeoverdue` — `object`
      - `disableemail` — `bool`  e.g. `false`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `false`, `false`, `false`
    - `feepaid` — `object`
      - `disableemail` — `bool`  e.g. `false`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `false`, `false`, `false`
    - `instructoraddedtoclassroom` — `object`
      - `disableemail` — `bool`  e.g. `false`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `false`, `false`, `false`
    - `learneraddedtoclassroom` — `object`
      - `disableemail` — `bool`  e.g. `false`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `false`, `false`, `false`
    - `paymentfailed` — `object`
      - `disableemail` — `bool`  e.g. `true`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `true`, `true`, `true`
    - `phoneotp` — `object`
      - `disableemail` — `bool`  e.g. `false`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `false`, `false`, `false`
    - `sessioncreditupdates` — `object`
      - `disableemail` — `bool`  e.g. `false`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `false`, `false`, `false`
    - `sessionfeedback` — `object`
      - `disableemail` — `bool`  e.g. `false`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `true`, `true`, `false`
    - `sessionfeedbackwithquiz` — `object`
      - `disableemail` — `bool`  e.g. `true`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `true`, `true`, `true`
    - `sessionnotstartedadminreminder` — `object`
      - `disableemail` — `bool`  e.g. `false`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `false`, `false`, `false`
    - `sessionnotstartedteacherreminder` — `object`
      - `disableemail` — `bool`  e.g. `false`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `false`, `false`, `false`
    - `sessionreminder_10` — `object`
      - `disableemail` — `bool`  e.g. `false`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `false`, `false`, `false`
    - `sessionreminder_1440` — `object`
      - `disableemail` — `bool`  e.g. `true`, `false`, `true`
      - `disablewhatsapp` — `bool`  e.g. `true`, `true`, `true`
    - `sessionreminder_2160` — `object`
      - `disableemail` — `bool`  e.g. `true`, `true`, `true`
      - `disablewhatsapp` — `bool`  e.g. `true`, `true`, `true`
    - `sessionreminder_60` — `object`
      - `disableemail` — `bool`  e.g. `true`, `true`, `false`
      - `disablewhatsapp` — `bool`  e.g. `true`, `true`, `true`
    - `sessionstarted` — `object`
      - `disableemail` — `bool`  e.g. `true`, `true`, `true`
      - `disablewhatsapp` — `bool`  e.g. `true`, `true`, `true`
    - `sessionupdated` — `object`
      - `disableemail` — `bool`  e.g. `false`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `true`, `true`, `false`
    - `unreadchatreminder` — `object`
      - `disableemail` — `bool`  e.g. `true`, `true`, `true`
      - `disablewhatsapp` — `bool`  e.g. `true`, `false`
    - `wisestudentinvite` — `object`
      - `disableemail` — `bool`  e.g. `false`, `true`, `true`
      - `disablewhatsapp` — `bool`  e.g. `false`, `true`, `true`
    - `wiseteacherinvite` — `object`
      - `disableemail` — `bool`  e.g. `false`, `false`, `false`
      - `disablewhatsapp` — `bool`  e.g. `false`, `false`, `false`
  - `disableemail` — `bool`  e.g. `true`, `false`, `false`
  - `disablewhatsapp` — `bool`  e.g. `true`, `false`, `true`
  - `emailbannerimageurl` — `string`  e.g. `https://files.wiseapp.live/upload_files/6341338ac5d2498cfb48`
  - `enableemail` — `bool`  e.g. `true`
  - `enablewhatsapp` — `bool`  e.g. `true`
  - `fromemail` — `string`  e.g. `[REDACTED-EMAIL]`, `[REDACTED-EMAIL]`, `[REDACTED-EMAIL]`
  - `imagesinemailsenabled` — `bool`  e.g. `false`, `false`, `false`
  - `registrationformreminderenabled` — `bool`  e.g. `false`, `false`, `false`
  - `replytoemail` — `string`  e.g. `[REDACTED-EMAIL]`, `[REDACTED-EMAIL]`, `[REDACTED-EMAIL]`
- `onboardinginstructions` — `object`
  - `admin` — `bool`  e.g. `false`, `false`, `false`
  - `parent` — `bool`  e.g. `false`, `false`, `false`
  - `student` — `bool`  e.g. `false`, `false`, `false`
  - `teacher` — `bool`  e.g. `false`, `false`, `false`
- `participantadditionalnotevisibility` — `string`  e.g. `ADMIN`, `ADMIN`, `ADMIN`
- `participantregistrationformvisibility` — `string`  e.g. `ADMIN`, `ADMIN`, `ADMIN`
- `privacypolicylink` — `string`  e.g. `https://jrfpsychology.com/terms-%26-conditions`, `https://chessgaja.com/privacy-policy-2/`, `https://iteskul.com/privacy`
- `recordingdeletionpolicy` — `object`
  - `classroomstoskip` — `array<object>|array<unknown>`
    - `recordingdeletionpolicy.classroomstoskip[]` — `object`
      - `$oid` — `string`  e.g. `6373ca920f8d8b5f2eadacb7`, `69c9cb1028a7a05379b68841`, `6a2ec99349c63a9c570ca428`
  - `deleteafterdays` — `object`
    - `$numberint` — `string`  e.g. `-1`, `-1`, `-1`
- `recordsessiongalleryview` — `bool`  e.g. `false`, `false`, `true`
- `sessionallowstartbeforeminutes` — `object`
  - `$numberint` — `string`  e.g. `30`, `10`, `30`
- `sessionnotstartedreminderdelay` — `object`
  - `$numberint` — `string`  e.g. `5`, `5`, `5`
- `sessionrecordingview` — `string`  e.g. `SPEAKER`, `GALLERY`, `GALLERY`
- `sessionsettings` — `object`
  - `advanceslotbookingbuffer` — `object`
    - `$numberint` — `string`  e.g. `360`, `720`, `60`
  - `allowonlyconsecutiveslotbooking` — `bool`  e.g. `false`, `false`, `false`
  - `allowstudenttocancelsession` — `bool`  e.g. `true`, `false`, `false`
  - `allowteacherfeedbackupdate` — `bool`  e.g. `true`, `true`, `true`
  - `allowteachertomanagecredits` — `bool`  e.g. `false`, `true`, `false`
  - `allowunpaidcreditsforbooking` — `bool`  e.g. `true`, `true`
  - `autosubmitsessionfeedback` — `bool`  e.g. `false`, `false`, `false`
  - `blockedadjacentslotbuffer` — `object`
    - `$numberint` — `string`  e.g. `0`, `0`, `0`
  - `bookingtimeslotgranularity` — `object`
    - `$numberint` — `string`  e.g. `15`, `15`, `15`
  - `creditsettings` — `object`
    - `allowteachercreditupdateonautosubmit` — `bool`  e.g. `false`, `true`, `false`
    - `autodeduct` — `bool`  e.g. `false`, `false`, `true`
    - `autodeductformissedsessions` — `bool`  e.g. `false`, `false`, `false`
    - `creditsperhour` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `deductionstrategy` — `string`  e.g. `MANUAL`, `MANUAL`, `AT_SESSION_TIME`
    - `deductiontype` — `string`  e.g. `FIXED`, `FIXED`, `FIXED`
    - `lowcreditthreshold` — `object`
      - `$numberint` — `string`  e.g. `0`, `0`, `0`
  - `defaultsessiondurationselection` — `object`
    - `$numberint` — `string`  e.g. `60`, `60`, `60`
  - `disableaititle` — `bool`  e.g. `true`, `true`, `true`
  - `disableofflinesessions` — `bool`  e.g. `false`, `false`, `false`
  - `disallowconflict` — `bool`  e.g. `false`, `false`, `false`
  - `donotoverridehost` — `bool`  e.g. `true`, `false`, `false`
  - `enablegooglemeet` — `bool`  e.g. `true`, `true`, `true`
  - `enableinstitutelevelcredits` — `bool`  e.g. `true`, `true`, `true`
  - `enableliveclasscredits` — `bool`  e.g. `false`, `false`, `false`
  - `enablerecurringsessionbooking` — `bool`  e.g. `true`, `true`
  - `livemeetingprovider` — `string`  e.g. `ZOOM`, `ZOOM`, `ZOOM`
  - `maxadvanceslotbookingdays` — `object`
    - `$numberint` — `string`  e.g. `180`, `180`, `180`
  - `meetingsummaryvisibility` — `string`  e.g. `ALL`, `ALL`, `ALL`
  - `restrictteachersessionvisibility` — `bool`  e.g. `false`, `true`, `false`
  - `sessionaiconfig` — `object`
    - `aidataenabled` — `bool`  e.g. `false`, `false`, `false`
    - `aisummaryenabled` — `bool`  e.g. `false`, `false`, `false`
    - `enabled` — `bool`  e.g. `false`, `false`, `false`
    - `summaryprompt` — `string`  e.g. `Based on the {transcript|summary}, create a clear summary un`, `Based on the {transcript|summary}, create a clear and detail`, `Based on the {transcript|summary}, create a clear summary in`
  - `showscheduledtimeforpastsessionstostudents` — `bool`  e.g. `false`, `false`, `false`
  - `studentfeedbackvisibility` — `string`  e.g. `ADMIN`, `ADMIN_TEACHER`, `ADMIN`
  - `studentslotcancellationbuffer` — `object`
    - `$numberint` — `string`  e.g. `60`, `720`, `60`
  - `updatecreditaccess` — `string`  e.g. `ADMIN_TEACHER`, `ADMIN`, `ADMIN_TEACHER`
- `showhiddenclassroomdata` — `bool`  e.g. `true`, `true`
- `showtagstoparticipants` — `bool`  e.g. `false`, `false`, `false`
- `showwebinaroption` — `bool`  e.g. `false`, `false`, `false`
- `storeredirectionurl` — `string`  e.g. `https://lifeskilllearnings.com`, `https://www.youtube.com/@imageclasses`, `https://linko.page/triceacademy`
- `taxsettings` — `object`
  - `defaulttaxrulegroupid` — `object`
    - `$oid` — `string`  e.g. `690af4b678722beb3bfa225b`, `692ee8670aeedbf3bc24c87d`
  - `enabled` — `bool`  e.g. `true`, `true`
- `teacheravailabilitysettings` — `object`
  - `disableupdatingleaves` — `bool`  e.g. `false`, `false`, `false`
  - `disableupdatingworkinghours` — `bool`  e.g. `false`, `false`, `false`
  - `enabled` — `bool`  e.g. `true`, `true`, `true`
- `teacherpermissions` — `object`
  - `disablecontentmanagement` — `bool`  e.g. `false`, `false`, `false`
  - `disablesessionmanagement` — `bool`  e.g. `false`, `false`, `false`
- `termsofservicelink` — `string`  e.g. `https://jrfpsychology.com/terms-%26-conditions`, `https://chessgaja.com/terms-and-conditions/`, `https://iteskul.com/terms`
- `uploadresourcestoyoutube` — `bool`  e.g. `false`, `true`, `false`
- `welcomeemailnote` — `string`  e.g. `Click here to die google.com/aaaa`, `You now have easy, online access to view all of your tutorin`, `This is a test message`
- `zoomsettings` — `object`
  - `disablebreakoutroom` — `bool`  e.g. `false`, `false`, `false`
  - `enablefocusmode` — `bool`  e.g. `true`, `true`, `true`
  - `enableparticipantscreensharing` — `bool`  e.g. `false`, `false`, `false`
  - `entryexitchime` — `string`  e.g. `NONE`, `NONE`, `NONE`
  - `hostvideoon` — `bool`  e.g. `false`, `false`, `false`

### `metadata`

- `institutesize` — `string`  e.g. `1_10`, `1_10`, `1_10`
- `institutetype` — `string` (nullable)  e.g. `SCHOOL`, `ONLINE`, `COACHING`
- `systemgenerated` — `bool`  e.g. `true`, `true`, `true`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_003807_00016_zrnrf', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
