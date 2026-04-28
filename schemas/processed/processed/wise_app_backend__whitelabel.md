---
database: processed
table: wise_app_backend__whitelabel
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/Whitelabel/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:18:01+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__whitelabel`

## Columns

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

_String columns with ≤20 distinct values in 200 sampled rows. Distribution shown as `value (×count)`._

- `disabled`: `true (×194)`, `false (×6)`

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `64defd3e57e7d26f3fcd6121`, `64df0a0e17dd9d5af47568b1`, `64df20f48788724f6192c8ae`

### `featureconfig`

- `adminuserids` — `array<string>`
  - `adminuserids[]` — `string`  e.g. `64defd3e57e7d28217cd6122`, `64df0a0e17dd9d3e637568b2`, `64df20f487887212dc92c8af`
- `cancreateclassrooms` — `bool`  e.g. `true`, `true`, `true`
- `disableemaillogin` — `bool`  e.g. `false`, `false`, `false`
- `disablefees` — `bool`  e.g. `false`, `false`, `false`
- `disablegooglelogin` — `bool`  e.g. `false`, `false`, `false`
- `disablephonelogin` — `bool`  e.g. `false`, `false`, `false`
- `enablejwtbasedlogin` — `bool`  e.g. `false`, `false`, `false`
- `enableparentportal` — `bool`  e.g. `true`, `true`, `true`

### `hostnames`

  - `[]` — `string`  e.g. `hari-classes.wise.live`, `chessbrainz.wise.live`, `phuongg.wise.live`

### `displayconfig`

- `androidappurl` — `string`  e.g. `https://play.google.com/store/apps/details?id=app.rightinsti`
- `appiconlink` — `string`  e.g. `https://firebasestorage.googleapis.com/v0/b/wise-leap-app.ap`, `https://firebasestorage.googleapis.com/v0/b/wise-leap-app.ap`, `https://firebasestorage.googleapis.com/v0/b/wise-leap-app.ap`
- `brandingfavicon` — `string`  e.g. `https://cdn.wiseapp.live/images/institute_thumbnail/10.png`, `https://cdn.wiseapp.live/images/institute_thumbnail/7.png`, `https://cdn.wiseapp.live/images/institute_thumbnail/10.png`
- `brandinglogo` — `string`  e.g. `https://cdn.wiseapp.live/images/institute_thumbnail/10.png`, `https://cdn.wiseapp.live/images/institute_thumbnail/7.png`, `https://cdn.wiseapp.live/images/institute_thumbnail/10.png`
- `brandingname` — `string`  e.g. `Hari classes`, `Chessbrainz`, `phuongg`
- `contactemail` — `string`  e.g. `[REDACTED]`
- `contactmobile` — `string`  e.g. `[REDACTED]`
- `footerstring` — `string`
- `namevariables` — `object`
  - `admin` — `string`  e.g. `admin`
  - `assessment` — `string`  e.g. `assignment`
  - `classroom` — `string`  e.g. `course`
  - `classroomname` — `string`  e.g. `name`
  - `classroomsubject` — `string`  e.g. `subject`
  - `content` — `string`  e.g. `content`
  - `criteria` — `string`  e.g. `criteria`
  - `discussion` — `string`  e.g. `discussion`
  - `group` — `string`  e.g. `bundle`
  - `institute` — `string`  e.g. `institute`
  - `liveclassroom` — `string`  e.g. `live classes`
  - `onetooneclassroom` — `string`  e.g. `1:1 course`
  - `parent` — `string`  e.g. `parent`
  - `recordedclassroom` — `string`  e.g. `recorded course`
  - `resource` — `string`  e.g. `resource`
  - `session` — `string`  e.g. `class`
  - `student` — `string`  e.g. `student`
  - `teacher` — `string`  e.g. `educator`
  - `test` — `string`  e.g. `test`
- `siteurl` — `string`  e.g. `https://www.coimbatorechesscentre.com/`, `http://theiasakademia.com/`
- `sociallinks` — `array<object>|array<unknown>`
  - `sociallinks[]` — `object`
    - `link` — `string`  e.g. `https://www.facebook.com/Coimbatorechesscentre`, `https://www.instagram.com/coimbatorechesscentre/`
    - `type` — `string`  e.g. `facebook`, `instagram`
- `tollfreenumber` — `string`
- `trialclassid` — `string`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1692335422033`, `1692338702123`, `1692344564542`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1753254516082`, `1753254516082`, `1753254516082`

### `versionconfig`

- `android` — `object`
  - `latestbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `1`, `1`, `1`
  - `minbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `1`, `1`, `1`
- `ios` — `object`
  - `latestbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `1`, `1`, `1`
  - `minbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `1`, `1`, `1`
- `mac` — `object`
  - `latestbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `1`, `1`, `1`
  - `minbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `1`, `1`, `1`
- `windows` — `object`
  - `latestbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `1`, `1`, `1`
  - `minbuildnumber` — `object`
    - `$numberint` — `string`  e.g. `1`, `1`, `1`

### `systemconfig`

- `apphash` — `string`  e.g. `TUWNJ1ip5oO`, `IDbq5cpelvl`, `i84GD8wUsXx`

### `defaultinstituteid`

- `$oid` — `string`  e.g. `64e737c16ddd180019a8d269`, `64ed83fe6fb522001816a18f`, `64ed85696fb522001816a190`

## DDL

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
  'trino_query_id'='20260428_012150_00034_meihw', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
