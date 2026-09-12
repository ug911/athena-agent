---
canonical: processed
table: wise_app_backend__event
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/event/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:23:20+00:00'
sampled_rows: 200
sampled_region: in
---

# `processed.wise_app_backend__event`

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
| `eventid` | `string` |  |
| `eventname` | `string` |  |
| `payload` | `string` |  |
| `eventtimestamp` | `string` |  |
| `__v` | `string` |  |

## Inferred JSON structure

_Inferred from 200 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `6a4e3c5c2393beb3d1820396`, `6a4e3c5cc9f70b16c72e6f58`, `6a4e3c5c10bb889b1b9f41bf`

### `payload`

- `assessment` — `object`
  - `feedback` — `string`  e.g. `bagus`, `BAGUS`, `BAGUS`
  - `getmark` — `object`
    - `$numberint` — `string`  e.g. `22`
  - `id` — `string`  e.g. `6a450e7bef13a14f02233eba`, `6a450e7bef13a14f02233eba`, `6a4e3c7f241940a7d2fac245`
  - `maxmark` — `object`
    - `$numberint` — `string`  e.g. `40`
  - `name` — `string`  e.g. `8 July 2026 HW `
- `class` — `object`
  - `classnumber` — `object`
    - `$numberint` — `string`  e.g. `288728138`, `315755252`, `628305328`
  - `id` — `string`  e.g. `6a044a46f2c6cf97b631bde1`, `6a4e0bc12393beb3d1771290`, `69e8ac33e9a370102a7a75d2`
  - `meetingid` — `object|string`  e.g. `96200042150`, `99146990903`, `94508894282`
    - `$numberdouble` — `string`  e.g. `9.9102189055E+10`, `9.2084429109E+10`, `9.8457023686E+10`
  - `name` — `string`  e.g. `DANISH-Junior - Advanced Level`, `CLAT | English Language | By Shazli Ul Hussaini Maam`, `Grammar Level 2_Group_25`
  - `namespace` — `string`  e.g. `furtadosschoolofmusic`, `musicpandit`, `iwish-academy`
  - `subject` — `string`  e.g. `Junior - Advanced Level`, `Toprankers`, `Grammar Level 2`
- `discussion` — `object`
  - `comment` — `object`
    - `attachments` — `array<object>`
      - `discussion.comment.attachments[]` — `object`
        - `_id` — `string`  e.g. `6a4e3c97241940a7d2faca79`
        - `filename` — `string`  e.g. `recording-1783512211199.mp3`, `recording-1783512211199.mp3`
        - `path` — `string`  e.g. `https://files.wiseapp.live/upload_files/67cbf035ed8b9119b873`, `https://files.wiseapp.live/upload_files/67cbf035ed8b9119b873`
        - `s3filepath` — `string`  e.g. `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`, `https://wise-app-s3-bucket.s3-ap-south-1.amazonaws.com/uploa`
        - `s3key` — `string`  e.g. `upload_files/67cbf035ed8b9119b8738cc9/upload_2b449276-8be8-4`, `upload_files/67cbf035ed8b9119b8738cc9/upload_2b449276-8be8-4`
        - `size` — `object`
          - `$numberint` — `string`  e.g. `41834`, `41834`
        - `type` — `string`  e.g. `audio`, `audio`
    - `comment` — `string`  e.g. `  Y`, `O`, `M`
    - `createdat` — `string`  e.g. `2026-07-08T12:02:40.441Z`, `2026-07-08T12:02:51.184Z`, `2026-07-08T12:03:00.547Z`
    - `deleted` — `bool`  e.g. `false`
    - `editedat` — `string`  e.g. `2026-07-08T12:02:40.441Z`, `2026-07-08T12:02:51.184Z`, `2026-07-08T12:03:00.547Z`
    - `id` — `string`  e.g. `6a4e3c97241940a7d2faca78`
    - `userid` — `string`  e.g. `67cbf035ed8b9119b8738cc9`, `67cbf035ed8b9119b8738cc9`, `67cbf035ed8b9119b8738cc9`
  - `id` — `string`  e.g. `6a4e267e241940a7d2f52d2a`, `6a4e267e241940a7d2f52d2a`, `6a4e267e241940a7d2f52d2a`
  - `poll` — `bool`  e.g. `false`, `false`
  - `title` — `string`  e.g. `hw`, `Homework -8th july 2026 `
- `institute` — `object`
  - `id` — `string`  e.g. `64fecc62a287120018c81ef4`, `6917288e1fa497299740969e`, `692067aa94ccfa630318fef5`
  - `namespace` — `string`  e.g. `thoughtflows`, `topmate`, `topmate`
- `newvalue` — `object`
  - `settings` — `object`
    - `autoaccept` — `bool`  e.g. `false`, `true`, `false`
- `oldvalue` — `object`
  - `settings` — `object`
    - `autoaccept` — `bool`  e.g. `true`, `false`, `true`
- `participant` — `object`
  - `id` — `string`  e.g. `6a4e3c5f8962898b87650f35`, `6630c4c82d914479b375efe0`, `6630c4c82d914479b375efe0`
  - `profile` — `string`  e.g. `student`, `teacher`, `teacher`
- `payment_order` — `object`
  - `amount` — `object`
    - `$numberint` — `string`  e.g. `500000`
  - `currency` — `string`  e.g. `INR`
  - `gateway_order_id` — `string`  e.g. `order_TB09C7pwnpzHvo`
  - `id` — `string`  e.g. `6a4e3c6de2183300010cabc3`
  - `payee_user_id` — `string`  e.g. `65d868629981243ddd1f5626`
  - `payer_user_id` — `string`  e.g. `69b834b624bc1648222f5b7c`
  - `payment_gateway` — `string`  e.g. `RAZORPAY`
  - `payment_transaction_id` — `string`  e.g. `6a4e3c6da85399d51250e1cc`
  - `payment_type` — `string`  e.g. `CREATED`
  - `status` — `string`  e.g. `CREATED`
- `resource` — `object`
  - `id` — `string`  e.g. `6a4e3c6cca57d9452040c9df`
  - `name` — `string`  e.g. `IMG_20260708_173220_835.webp`
  - `type` — `string`  e.g. `file`
- `sectionid` — `string`  e.g. `6a4506db48ee93335a7d9209`, `698c68a658253d55006b7abb`
- `session` — `object`
  - `autosubmitted` — `bool`  e.g. `true`, `true`, `true`
  - `classid` — `string`  e.g. `6a3fb7f2a04bf99f53da96b1`, `69c817bbca20919f2cf1dc34`, `69d4e5e49ee511e7269f4069`
  - `createdat` — `string`  e.g. `2026-07-08T12:02:36.641Z`, `2026-07-08T08:35:13.644Z`, `2026-07-08T12:02:37.845Z`
  - `id` — `string`  e.g. `6a4e3c5c2393beb3d182038c`, `6a4e0bc1c9f70b16c723b4b7`, `6a4e3a962393beb3d1816937`
  - `meetingid` — `object|string`  e.g. `96200042150`, `99146990903`, `94508894282`
    - `$numberdouble` — `string`  e.g. `9.9102189055E+10`, `9.2084429109E+10`, `9.8457023686E+10`
  - `meetingstatus` — `string`  e.g. `IN_PROGRESS`, `IN_PROGRESS`, `IN_PROGRESS`
  - `meetinguuid` — `string`  e.g. `9sio2v7DQiGyZvZH4lMvog==`, `WFhx1MLiSoW89cX4leE0mg==`, `ZJkIqy17RVOyUD60ZYGy8g==`
  - `scheduled` — `bool`  e.g. `false`, `true`, `false`
  - `scheduledendtime` — `string`  e.g. `2026-07-08T13:35:00.000Z`, `2026-07-08T13:15:00.000Z`, `2026-07-08T13:10:00.000Z`
  - `scheduledstarttime` — `string`  e.g. `2026-07-08T12:50:00.000Z`, `2026-07-08T13:00:00.000Z`, `2026-07-08T12:50:00.000Z`
  - `starttime` — `string`  e.g. `2026-07-08T12:02:36.640Z`, `2026-07-08T12:02:36.615Z`, `2026-07-08T12:02:37.844Z`
  - `type` — `string`  e.g. `AD_HOC`, `SCHEDULED`, `AD_HOC`
  - `updates` — `object`
    - `scheduledendtime` — `string`  e.g. `2026-07-09T16:00:00.000Z`
    - `scheduledstarttime` — `string`  e.g. `2026-07-09T15:00:00.000Z`
    - `start_time` — `string`  e.g. `2026-07-09T15:00:00.000Z`
  - `updatetype` — `string`  e.g. `SINGLE`
- `student` — `object`
  - `id` — `string`  e.g. `674d31543b7c522b9abe9c8f`, `683bcaacb213e9ac4996daa8`, `69b834b624bc1648222f5b7c`
  - `namespace` — `string`  e.g. `leadiasacademy`
- `submission` — `object`
  - `endtime` — `string`  e.g. `2026-07-08T11:48:30+00:00`, `2026-07-08T12:04:11+00:00`, `2026-07-08T12:04:11+00:00`
  - `id` — `string`  e.g. `6a4e37d17c2dde0001bc9084`, `6a4e380b1c5071000175671b`, `6a4e380b1c5071000175671b`
  - `marksobtained` — `object`
    - `$numberint` — `string`  e.g. `12`, `0`, `10`
  - `passed` — `bool`  e.g. `true`, `false`, `true`
  - `starttime` — `string`  e.g. `2026-07-08T11:43:13+00:00`, `2026-07-08T11:44:11+00:00`, `2026-07-08T11:44:11+00:00`
  - `status` — `string`  e.g. `GRADED`, `SUBMITTED`, `GRADED`
- `test` — `object`
  - `id` — `string`  e.g. `6a44c128a33cbd00014593f9`, `6a44c128a33cbd00014593f9`, `6a44c128a33cbd00014593f9`
- `transaction` — `object`
  - `amount` — `object`
    - `currency` — `string`  e.g. `INR`, `INR`, `INR`
    - `value` — `object`
      - `$numberint` — `string`  e.g. `500000`, `12500`, `45000`
  - `createdat` — `string`  e.g. `2026-07-08T12:02:53.150Z`, `2026-07-08T12:03:26.865Z`, `2026-07-08T12:03:54.103Z`
  - `id` — `string`  e.g. `6a4e3c6da85399d51250e1cc`, `6a4e3c8e8962898b87656006`, `6a4e3caa8962898b87657f72`
  - `metadata` — `object`
    - `classid` — `string`  e.g. `690f25e2c328a7b5e0be81f4`, `6a3fb7f2a04bf99f53da96b1`, `69c817bbca20919f2cf1dc34`
    - `invoicetype` — `string`  e.g. `TUTOR_PAYOUT`, `TUTOR_PAYOUT`, `TUTOR_PAYOUT`
    - `paid` — `bool`  e.g. `false`, `false`, `false`
    - `sessioncredits` — `object`
      - `$numberint` — `string`  e.g. `1`, `1`, `1`
    - `sessionid` — `string`  e.g. `6a3fb8cca04bf99f53dab562`, `6a4e1916a85399d512486a99`, `6a2fc32a456e14e28ce3a6f8`
    - `sessionstarttime` — `string`  e.g. `2026-07-08T11:29:23.475Z`, `2026-07-08T11:00:16.894Z`, `2026-07-08T11:02:17.424Z`
  - `note` — `string`  e.g. `Session conducted on 8th Jul`, `Session conducted on 8th Jul`, `Session conducted on 8th Jul`
  - `receiverid` — `string`  e.g. `65d868629981243ddd1f5626`, `6a310d85904c8925d4f1319f`, `69aa5ea213cc1073afb7bb24`
  - `senderid` — `string`  e.g. `69b834b624bc1648222f5b7c`, `6a3390f7edb08f0348239186`, `69ac543013cc1073af39f8cd`
  - `status` — `string`  e.g. `CREATED`, `CREATED`, `CREATED`
  - `transactiontype` — `string`  e.g. `FEE_COLLECTION`, `TUTOR_PAYOUT`, `TUTOR_PAYOUT`
  - `type` — `string`  e.g. `PAYMENT`, `INVOICE`, `INVOICE`
  - `updatedat` — `string`  e.g. `2026-07-08T12:02:53.150Z`, `2026-07-08T12:03:26.865Z`, `2026-07-08T12:03:54.103Z`
- `user` — `object`
  - `email` — `string`  e.g. `[REDACTED]`
  - `id` — `string`  e.g. `673d7b9653322ccd5b5e0fe6`, `648dade5d20ce0f14728e242`, `64fecbcec47b39bb3f976657`
  - `name` — `string`  e.g. `[REDACTED]`
  - `namespace` — `string`  e.g. `teaminterval`, `toprankers`, `learn2read`
  - `phonenumber` — `string`  e.g. `[REDACTED]`
- `verification` — `object`
  - `code` — `string`  e.g. `9316`, `9807`, `6975`
  - `data` — `object`
    - `attempts` — `object`
      - `$numberint` — `string`  e.g. `0`, `0`, `0`
    - `code` — `string`  e.g. `9316`, `9807`, `6975`
    - `createdat` — `string`  e.g. `2026-07-08T12:02:31.147Z`, `2026-07-08T12:02:40.879Z`, `2026-07-08T12:02:46.528Z`
    - `expirytime` — `string`  e.g. `2026-07-08T12:05:31.147Z`, `2026-07-08T12:05:40.878Z`, `2026-07-08T12:05:46.528Z`
    - `id` — `string`  e.g. `6a4e3c57241940a7d2fab29c`, `6a4e3c60ab0052bf61ea2316`, `6a4e3c66321882d97ab3323e`
    - `identifier` — `string`  e.g. `[REDACTED-PHONE]`, `[REDACTED-EMAIL]`, `[REDACTED-PHONE]`
    - `idtype` — `string`  e.g. `PHONE_NUMBER`, `EMAIL`, `PHONE_NUMBER`
    - `ip` — `string`  e.g. `152.57.129.201`, `194.213.108.1`, `104.28.164.49`
    - `namespace` — `string`  e.g. `corizo`, `iteskul`, `corizo`
    - `resendcount` — `object`
      - `$numberint` — `string`  e.g. `0`, `0`, `0`
    - `resendwindow` — `string`  e.g. `2026-07-08T12:04:31.147Z`, `2026-07-08T12:04:40.878Z`, `2026-07-08T12:04:46.528Z`
    - `updatedat` — `string`  e.g. `2026-07-08T12:02:31.147Z`, `2026-07-08T12:02:40.879Z`, `2026-07-08T12:02:46.528Z`
    - `verified` — `bool`  e.g. `false`, `false`, `false`
- `version` — `object`
  - `$numberint` — `string`  e.g. `2`, `2`, `2`

### `eventtimestamp`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1783512156658`, `1783512156633`, `1783512156928`

### `__v`

- `$numberint` — `string`  e.g. `0`, `0`, `0`

## DDL

_From `IN` (processed)._

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
  'trino_query_id'='20260811_005216_00043_rgfsw', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
