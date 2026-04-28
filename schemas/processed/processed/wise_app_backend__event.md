---
database: processed
table: wise_app_backend__event
type: table
layer: processed
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/event/
format: INPUTFORMAT
partition_keys: []
last_synced: '2026-04-28T07:14:54+00:00'
sampled_rows: 200
---

# `processed.wise_app_backend__event`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `eventid` | `string` |  |
| `eventname` | `string` |  |
| `payload` | `string` |  |
| `eventtimestamp` | `string` |  |
| `__v` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows on 2026-04-28. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `69de570505cc98aef6c688b1`, `69de570641168717a1aebbb1`, `69de570692648a764ca7c52d`

### `payload`

- `assessment` — `object`
  - `feedback` — `string`  e.g. `The audio quality, video presentation, and overall professio`, `Good job!`
  - `getmark` — `object`
    - `$numberint` — `string`  e.g. `10`, `26`
  - `id` — `string`  e.g. `69ca08ee7a00432425901ac3`, `6909d290bfb2407b962c2768`, `698b1082ccf7f7fc13e90ca4`
  - `maxmark` — `object`
    - `$numberint` — `string`  e.g. `10`, `30`
- `class` — `object`
  - `id` — `string`  e.g. `69d6463d265fa49908bead6e`, `699298ab2f5bc25203c2deb4`, `6943ff7b585d27d5cd4ed989`
  - `meetingid` — `object|string`  e.g. `94080722186`, `93864478522`, `96535361987`
    - `$numberdouble` — `string`  e.g. `9.1276407556E+10`, `9.1039138117E+10`, `9.4454534778E+10`
  - `name` — `string`  e.g. `MM1944 Prisha`, `Physics (Mechanics) - Hamad`, `MM1908 Ehsan khan`
  - `namespace` — `string`  e.g. `mentormatch`, `supatutor`, `learn2read`
  - `subject` — `string`  e.g. `11 | MATHS | British Curriculum | CSM009`, `AP - C`, `9 | MATHS | IGCSE | CSM010`
- `data` — `object`
  - `quizzes` — `object`
    - `$numberint` — `string`  e.g. `5`, `5`
  - `revisionnotes` — `object`
    - `$numberint` — `string`  e.g. `10`, `8`
- `discussion` — `object`
  - `comment` — `object`
    - `attachments` — `array<object>`
      - `discussion.comment.attachments[]` — `object`
        - `filename` — `string`  e.g. `276.mp4`
        - `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/69c6068e59c459d1a1bd`
        - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`
        - `s3key` — `string`  e.g. `upload_files/69c6068e59c459d1a1bda189/upload_ffb70a2c-b336-4`
        - `size` — `object`
          - `$numberint` — `string`  e.g. `6010121`
        - `type` — `string`  e.g. `video`
    - `comment` — `string`  e.g. `Thank you sir `, `📰Read ✨👍👍`
    - `createdat` — `string`  e.g. `2026-04-14T15:02:48.100Z`, `2026-04-14T15:05:05.118Z`, `2026-04-14T15:03:59.836Z`
    - `editedat` — `string`  e.g. `2026-04-14T15:02:48.100Z`, `2026-04-14T15:05:05.118Z`, `2026-04-14T15:03:59.836Z`
    - `userid` — `string`  e.g. `660fa2d000520d32d10e20c9`, `69b4150724bc164822d19374`, `69c6068e59c459d1a1bda189`
  - `id` — `string`  e.g. `69de080fec4072f774839a93`, `69db570cfa8079e9441f6b6c`, `69dd9445a66dda7b2bd2623c`
- `institute` — `object`
  - `id` — `string`  e.g. `655b3d6ac327ce0025351d4b`, `65cc63108cd15a6d8841c166`, `64dcc496132b0b00199c19e3`
  - `namespace` — `string`  e.g. `britishacademiadeingles`
- `participant` — `object`
  - `id` — `string`  e.g. `69de560898ee51775fe34169`, `69de560998ee51775fe34249`, `69de560998ee51775fe34249`
  - `profile` — `string`  e.g. `student`
- `resource` — `object`
  - `id` — `string`  e.g. `69de5774bc1b5bc4aa68e093`, `69de578994bdedbf18a8e447`, `69de5797b3edf0435d286fac`
  - `name` — `string`  e.g. `Maths Homework 14-4-26.pdf`, `rotational dynamic.pdf`, `Corrected HW of 9-4-26.pdf`
  - `type` — `string`  e.g. `file`, `file`, `file`
- `sectionid` — `string`  e.g. `699d8f386a4854235e46fe0e`, `6994820b56b20aaa5e7fe726`, `699d8f386a4854235e46fe0e`
- `session` — `object`
  - `autosubmitted` — `bool`  e.g. `true`, `true`, `true`
  - `classid` — `string`  e.g. `6812123f091671657f7d1f1e`, `69ae9d5c8c9260f262bb9078`, `698e73212ed315b64775c488`
  - `createdat` — `string`  e.g. `2026-04-14T15:02:56.610Z`, `2026-01-25T08:59:48.049Z`, `2026-01-27T13:21:24.497Z`
  - `id` — `string`  e.g. `69d6476a56c894f81b9d87df`, `699298d8d7d3bab567d9f160`, `69bab2d290b5e072f1811901`
  - `meetingid` — `object|string`  e.g. `94080722186`, `93864478522`, `96535361987`
    - `$numberdouble` — `string`  e.g. `9.1276407556E+10`, `9.1039138117E+10`, `9.4454534778E+10`
  - `meetingstatus` — `string`  e.g. `IN_PROGRESS`, `IN_PROGRESS`, `IN_PROGRESS`
  - `meetinguuid` — `string`  e.g. `C8HDOj2nRnOESCoHOm/vAg==`, `fVym2go+TRu6nfv/XpjNNw==`, `70+yN7b9S7W+UHYdCWeRVg==`
  - `scheduled` — `bool`  e.g. `false`, `true`, `true`
  - `scheduledendtime` — `string`  e.g. `2026-04-14T16:07:34.000Z`, `2026-04-18T08:00:00.000Z`
  - `scheduledstarttime` — `string`  e.g. `2026-04-14T15:07:34.000Z`, `2026-04-18T07:00:00.000Z`
  - `starttime` — `string`  e.g. `2026-04-14T15:02:56.609Z`, `2026-04-14T15:02:56.782Z`, `2026-04-14T15:02:57.616Z`
  - `type` — `string`  e.g. `AD_HOC`, `SCHEDULED`, `SCHEDULED`
- `student` — `object`
  - `id` — `string`  e.g. `69d3879798ee51775fd64fd1`, `691597d2d1e46605c63ea465`
- `submission` — `object`
  - `endtime` — `string`  e.g. `2026-04-14T14:02:51+00:00`, `2026-04-14T15:03:12+00:00`, `2026-04-14T13:12:33+00:00`
  - `id` — `string`  e.g. `69de48ebee0b010001711f7b`, `69de562a2759af00018f9fcb`, `69de3af04c58980001aa10de`
  - `marksobtained` — `object`
    - `$numberint` — `string`  e.g. `5`, `0`, `328`
  - `passed` — `bool`  e.g. `true`, `false`, `true`
  - `starttime` — `string`  e.g. `2026-04-14T14:02:19+00:00`, `2026-04-14T14:58:50+00:00`, `2026-04-14T13:02:40+00:00`
  - `status` — `string`  e.g. `GRADED`, `SUBMITTED`, `GRADED`
- `test` — `object`
  - `id` — `string`  e.g. `69de3f2aee0b010001711f1a`, `69b448c4aaacca0001f0f0f5`, `69de18674c58980001aa0d91`
- `transaction` — `object`
  - `amount` — `object`
    - `currency` — `string`  e.g. `INR`, `INR`, `THB`
    - `value` — `object`
      - `$numberint` — `string`  e.g. `25000`, `57700`, `50000`
  - `createdat` — `string`  e.g. `2026-04-14T15:02:51.663Z`, `2026-04-14T15:03:08.038Z`, `2026-04-14T15:04:22.846Z`
  - `id` — `string`  e.g. `69de571b98ee51775fe5c077`, `69de572c98ee51775fe5e3d7`, `69de577698ee51775fe65abc`
  - `metadata` — `object`
    - `classid` — `string`  e.g. `6812123f091671657f7d1f1e`, `69ae9d5c8c9260f262bb9078`, `698e73212ed315b64775c488`
    - `invoicetype` — `string`  e.g. `TUTOR_PAYOUT`, `TUTOR_PAYOUT`, `TUTOR_PAYOUT`
    - `paid` — `bool`  e.g. `false`, `false`, `false`
    - `sessioncredits` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `sessionid` — `string`  e.g. `69de4aefb3edf0435d2569df`, `69ae9da4b6c72a9a0d81a787`, `69c351762280b9a3811cbd3a`
    - `sessionstarttime` — `string`  e.g. `2026-04-14T14:11:02.957Z`, `2026-04-14T13:57:59.754Z`, `2026-04-12T05:58:32.041Z`
  - `note` — `string`  e.g. `Session conducted on 14th Apr`, `Session conducted on 14th Apr`, `Session conducted on 12th Apr`
  - `receiverid` — `string`  e.g. `671c98c4ed43711b17868449`, `67f8f068cdd211ec1592dbf9`, `69366668c05630afe5d8a2a4`
  - `senderid` — `string`  e.g. `67ca9f10ed8b9119b8dc81f9`, `68063a6ecdd211ec157d7fe6`, `696e2c4343579bbada233f6b`
  - `status` — `string`  e.g. `CREATED`, `CREATED`, `CREATED`
  - `transactiontype` — `string`  e.g. `TUTOR_PAYOUT`, `TUTOR_PAYOUT`, `TUTOR_PAYOUT`
  - `type` — `string`  e.g. `INVOICE`, `INVOICE`, `INVOICE`
  - `updatedat` — `string`  e.g. `2026-04-14T15:02:51.663Z`, `2026-04-14T15:03:08.038Z`, `2026-04-14T15:04:22.846Z`
- `user` — `object`
  - `email` — `string`  e.g. `[REDACTED]`
  - `id` — `string`  e.g. `67386548fbd3304585d4be09`, `663f68c6cd91265d34f1f097`, `64dcc3f2cacfaa35815f90c8`
  - `name` — `string`  e.g. `[REDACTED]`
  - `namespace` — `string`  e.g. `toprankers`, `mentormatch`, `uhprep`
  - `phonenumber` — `string`  e.g. `[REDACTED]`
- `verification` — `object`
  - `code` — `string`  e.g. `1149`, `3906`, `9943`
  - `data` — `object`
    - `attempts` — `object`
      - `$numberint` — `string`  e.g. `0`, `0`, `0`
    - `code` — `string`  e.g. `1149`, `3906`, `9943`
    - `createdat` — `string`  e.g. `2026-04-14T15:02:53.702Z`, `2026-04-14T15:04:05.127Z`, `2026-04-14T15:04:17.977Z`
    - `expirytime` — `string`  e.g. `2026-04-14T15:05:53.701Z`, `2026-04-14T15:07:05.127Z`, `2026-04-14T15:07:17.977Z`
    - `id` — `string`  e.g. `69de571d41168717a1aec1ae`, `69de5765e3aba9e596353b97`, `69de577192648a764ca7de76`
    - `identifier` — `string`  e.g. `[REDACTED-PHONE]`, `[REDACTED-EMAIL]`, `[REDACTED-PHONE]`
    - `idtype` — `string`  e.g. `PHONE_NUMBER`, `EMAIL`, `PHONE_NUMBER`
    - `ip` — `string`  e.g. `106.216.200.155`, `86.41.73.55`, `223.233.83.0`
    - `resendcount` — `object`
      - `$numberint` — `string`  e.g. `0`, `0`, `0`
    - `resendwindow` — `string`  e.g. `2026-04-14T15:04:53.701Z`, `2026-04-14T15:06:05.127Z`, `2026-04-14T15:06:17.977Z`
    - `updatedat` — `string`  e.g. `2026-04-14T15:02:53.702Z`, `2026-04-14T15:04:05.127Z`, `2026-04-14T15:04:17.977Z`
    - `verified` — `bool`  e.g. `false`, `false`, `false`
- `version` — `object`
  - `$numberint` — `string`  e.g. `2`, `2`, `2`

### `eventtimestamp`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1776178949531`, `1776178950145`, `1776178950384`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__event`(
  `_id` string, 
  `eventid` string, 
  `eventname` string, 
  `payload` string, 
  `eventtimestamp` string, 
  `__v` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/event/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260428_004725_00088_g6yam', 
  'trino_version'='0.215-24582-g0575ac4')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
