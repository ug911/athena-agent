---
database: processed
table: student_registration_form
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:12:26+00:00'
sampled_rows: 0
---

# `processed.student_registration_form`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `instituteid` | `string` |  |
| `enabled` | `string` |  |
| `disableupdatingsubmission` | `string` |  |
| `requiredforstudents` | `string` |  |
| `questionid` | `string` |  |
| `questiontype` | `string` |  |
| `questionrequired` | `string` |  |
| `questiontext` | `string` |  |
| `userid` | `string` |  |
| `answer` | `string` |  |
| `status` | `string` |  |
| `createdat` | `date` |  |
| `updatedat` | `date` |  |

## DDL

```sql
CREATE VIEW processed.student_registration_form AS
SELECT
  a.instituteid
, a.enabled
, a.disableupdatingsubmission
, a.requiredforstudents
, a.questionid
, a.type questiontype
, a.required questionrequired
, a.questiontext
, b.userid
, b.answer
, b.status
, b.createdat
, b.updatedat
FROM
  ((
   SELECT
     instituteid
   , createdat
   , updatedat
   , enabled
   , disableupdatingsubmission
   , requiredforstudents
   , CAST(JSON_EXTRACT(f, '$.questionid') AS VARCHAR) questionid
   , CAST(JSON_EXTRACT(f, '$.type') AS VARCHAR) type
   , CAST(JSON_EXTRACT(f, '$.required') AS VARCHAR) required
   , CAST(JSON_EXTRACT(f, '$.questiontext') AS VARCHAR) questiontext
   FROM
     ((
      SELECT
        CAST(JSON_EXTRACT("instituteid", '$["$oid"]') AS VARCHAR) instituteid
      , CAST(JSON_PARSE("fields") AS ARRAY(JSON)) ff
      , CAST(JSON_EXTRACT(settings, '$.disableupdatingsubmission') AS VARCHAR) disableupdatingsubmission
      , CAST(JSON_EXTRACT(settings, '$.requiredforstudents') AS VARCHAR) requiredforstudents
      , enabled
      , DATE(FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT("createdat", '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS INTEGER))) createdat
      , DATE(FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT("updatedat", '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS INTEGER))) updatedat
      FROM
        wise_app_backend__registration_form
   ) 
   CROSS JOIN UNNEST(ff) t (f))
)  a
LEFT JOIN (
   SELECT
     instituteid
   , userid
   , CAST(JSON_EXTRACT(field, '$.questionid') AS VARCHAR) questionid
   , CAST(JSON_EXTRACT(field, '$.answer') AS VARCHAR) answer
   , status
   , createdat
   , updatedat
   FROM
     ((
      SELECT
        CAST(JSON_EXTRACT("_id", '$["$oid"]') AS VARCHAR) _id
      , CAST(JSON_EXTRACT("instituteid", '$["$oid"]') AS VARCHAR) instituteid
      , CAST(JSON_EXTRACT("userid", '$["$oid"]') AS VARCHAR) userid
      , CAST(JSON_PARSE(answers) AS ARRAY(JSON)) answers
      , status
      , DATE(FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT("createdat", '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS INTEGER))) createdat
      , DATE(FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT("updatedat", '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS INTEGER))) updatedat
      FROM
        wise_app_backend__registration_form_submission
   ) 
   CROSS JOIN UNNEST(answers) t (field))
)  b ON ((a.instituteid = b.instituteid) AND (a.questionid = b.questionid)))
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->

## Notes

- **Long format.** One row per `(instituteid, userid, questionid)` — i.e. one row per answered question. To get a wide row per student, pivot with `MAX(IF(questiontext = 'X', answer))` per `questionid` or `questiontext`.
- **Joins to existing form**: `instituteid` (already extracted as varchar) is the form owner — same as `class.instituteid`. There is one form per institute. A student enrolled in multiple institutes has separate submissions per institute.
- **Question identifiers**:
  - `questionid` is **stable** across question text edits — prefer this when pivoting for long-lived reports.
  - `questiontext` is the human label and can drift (e.g. one institute uses `Pincode`, another uses `Pin Code`; same semantic field). Collapse with `IN ('Pincode','Pin Code')` when unifying across institutes in the same namespace.
- **Standard `questionid`s** (built-in fields): `user_name`, `user_email`, `user_phone_number`, `user_profile_picture`. Custom questions use random short ids like `wola5fuu`.
- **`questiontype` values seen**: `TEXT`, `EMAIL`, `PHONE`, `NUMBER`, `DATE`, `IMAGE`, `POLL`. **POLL answers store the option id**, not the option label — to resolve labels, look at `wise_app_backend__registration_form.fields[].options[]`. e.g. `reg_graduation_stream` returns `A`/`B`/`C` rather than the human-readable stream name.
- **Date answers** come back as ISO strings (e.g. `1997-02-28T00:00:00.000Z`) — wrap with `from_iso8601_timestamp` when filtering.
- **Not every institute has a form configured.** Empty / unconfigured institutes return zero rows here, so use a `LEFT JOIN` from the student roster if you want all students regardless of form completion.
- **Output column redaction**: when pivoting answers into columns, do NOT name the output columns `email` / `phone_number` / etc. — the Athena MCP guard redacts by output-name pattern. Use `reg_email_addr`, `reg_contact_number` style.
