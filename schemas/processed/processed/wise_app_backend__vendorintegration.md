---
canonical: processed
table: wise_app_backend__vendorintegration
type: table
layer: processed
regions:
  in: processed
  na: processed_na
location: s3://[REDACTED-BUCKET]/processed/wise-app-backend/VendorIntegration/
format: INPUTFORMAT
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:29:44+00:00'
sampled_rows: 95
sampled_region: in
---

# `processed.wise_app_backend__vendorintegration`

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
| `createdat` | `string` |  |
| `updatedat` | `string` |  |
| `userid` | `string` |  |
| `settings` | `string` |  |
| `enabled` | `string` |  |
| `integrationtype` | `string` |  |

## Enum-like columns

_String columns with ≤20 distinct values in 95 sampled rows from `IN`. Distribution shown as `value (×count)`._

- `enabled`: `true (×93)`, `false (×2)`
- `integrationtype`: `YOUTUBE (×57)`, `INTERAKT (×21)`, `GOOGLE_DRIVE (×9)`, `PORTAL_LOGIN (×3)`, `LESSON_SPACE (×2)`, `PENCIL_SPACES (×2)`, `VIMEO (×1)`

## Inferred JSON structure

_Inferred from 95 sampled rows from `IN` on 2026-08-11. Not authoritative — values may be missing or have additional keys._

### `_id`

- `$oid` — `string`  e.g. `659be7c78b3b180018c10db8`, `674725b563ea6d00182dbe5f`, `675a9106207538001c8e47a5`

### `createdat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1704716231194`, `1732715957488`, `1733988614625`

### `updatedat`

- `$date` — `object`
  - `$numberlong` — `string`  e.g. `1704716231194`, `1732715957488`, `1733988614625`

### `userid`

- `$oid` — `string`  e.g. `658e7dd3a6c3e519b0b3ad3e`, `670e01ff956430de65e15300`, `674ed04b720034526b51142d`

### `settings`

- `accesstoken` — `string`  e.g. `[REDACTED]`
- `apikey` — `string`  e.g. `[REDACTED]`
- `apiurl` — `string`  e.g. `https://partner-api.flexge.com/external/students/auth`
- `displayicon` — `string`  e.g. `https://cdn.wiseapp.live/images/calendar-plus-bold.svg`, `https://cdn.wiseapp.live/images/calendar-plus-bold.svg`
- `displayname` — `string`  e.g. `[REDACTED]`
- `email` — `string`  e.g. `[REDACTED]`
- `iframe` — `bool`  e.g. `true`
- `logintype` — `string`  e.g. `HTTP_API`, `WISE_TOKEN`, `WISE_TOKEN`
- `method` — `string`  e.g. `POST`
- `portalfallbackurl` — `string`  e.g. `https://student.britishacademiadeingles.com`, `/not-found`, `/not-found`
- `portalloginurl` — `string`  e.g. `https://student.britishacademiadeingles.com/auth-callback?to`, `https://excelr-jumbo-pass-871360913814.asia-south1.run.app/a`, `https://group-sessions-admin-lzatke3riq-el.a.run.app/api/aut`
- `refreshtoken` — `string`  e.g. `[REDACTED]`
- `responsekey` — `string`  e.g. `token`
- `subdomain` — `string`  e.g. `aws`
- `targetrole` — `string`  e.g. `student`, `student`
- `targetroles` — `array<string>`
  - `targetroles[]` — `string`  e.g. `STUDENT`, `STUDENT`, `ADMIN`
- `templatemapping` — `object`
  - `certificatecreation` — `string`  e.g. `wise_backend_certificate_issue_new1`, `backend_certificate_issue`, `backend_certificate_issue`
  - `dailysessionreminder` — `string`  e.g. `session_reminder`
  - `discussioncreated` — `string`  e.g. `backend_new_discussion`, `backend_new_discussion`, `backend_new_discussion`
  - `feeadded` — `string`  e.g. `backend_invoice_reminder`, `backend_invoice_reminder`, `backend_invoice_reminder`
  - `feeaddedautocharge` — `string`  e.g. `backend_invoice_autocharge_reminder`, `backend_invoice_autocharge_reminder`, `backend_invoice_autocharge_reminder`
  - `feedue` — `string`  e.g. `backend_fees_due`, `backend_fees_due`, `backend_fees_due`
  - `feeoverdue` — `string`  e.g. `backend_fees_overdue`, `backend_fees_overdue`, `backend_fees_overdue`
  - `feepaid` — `string`  e.g. `backend_fees_paid`, `backend_fees_paid`, `backend_fees_paid`
  - `instructoraddedtoclassroom` — `string`  e.g. `backend_course_invite_instructor`, `backend_course_invite_instructor`, `backend_course_invite_instructor`
  - `learneraddedtoclassroom` — `string`  e.g. `backend_course_invite_learner`, `backend_course_invite_learner`, `backend_course_invite_learner`
  - `phoneotp` — `string`  e.g. `backend_otp_authentication`, `backend_otp_authentication`, `backend_otp_authentication`
  - `sessioncreditupdates` — `string`  e.g. `backend__session_credits_updated`, `backend__session_credits_updated`, `backend_session_credits_updated`
  - `sessionfeedback` — `string`  e.g. `backend_session_completed`, `backend_session_completed`, `backend_session_completed`
  - `sessionnotstartedadminreminder` — `string`  e.g. `wise_backend_session_reminder_delayed_admin_new1`, `backend_session_reminder_delayed_admin`, `backend_session_reminder_delayed_admin`
  - `sessionnotstartedteacherreminder` — `string`  e.g. `wise_backend_session_reminder_delayed_teacher_new1`, `backend_session_reminder_delayed_teacher`, `backend_session_reminder_delayed_teacher`
  - `sessionreminder_10` — `string`  e.g. `wise_session_reminder_new`, `backend_session_reminder_1q`, `backend_session_reminder`
  - `sessionreminder_1440` — `string`  e.g. `wise_session_reminder_new`, `backend_session_reminder_1q`, `backend_session_reminder`
  - `sessionreminder_2160` — `string`  e.g. `backend_session_reminder`
  - `sessionreminder_60` — `string`  e.g. `wise_session_reminder_new`, `backend_session_reminder_1q`, `backend_session_reminder`
  - `sessionstarted` — `string`  e.g. `backend_session_live_reminder_learner`, `backend_session_reminder_learner_started`, `backend_session_reminder_learner_started`
  - `sessionupdated` — `string`  e.g. `backend_session_update_notification`, `backend_session_update_notification`, `backend_session_update_notification`
  - `wisestudentinvite` — `string`  e.g. `wise_backend_institute_invite_student_new1`, `wise_institute_invite_student`
  - `wiseteacherinvite` — `string`  e.g. `wise_backend_institute_invite_teacher_new`, `backend_institute_invite_instructor`, `backend_institute_invite_instructor`

## DDL

_From `IN` (processed)._

```sql
CREATE EXTERNAL TABLE `processed.wise_app_backend__vendorintegration`(
  `_id` string, 
  `createdat` string, 
  `updatedat` string, 
  `userid` string, 
  `settings` string, 
  `enabled` string, 
  `integrationtype` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe' 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat'
LOCATION
  's3://[REDACTED-BUCKET]/processed/wise-app-backend/VendorIntegration/'
TBLPROPERTIES (
  'auto.purge'='false', 
  'has_encrypted_data'='false', 
  'numFiles'='-1', 
  'parquet.compression'='GZIP', 
  'totalSize'='-1', 
  'transactional'='false', 
  'trino_query_id'='20260811_013254_00097_std7g', 
  'trino_version'='0.215-24619-g93e00a8')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
