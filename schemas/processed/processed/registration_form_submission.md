---
database: processed
table: registration_form_submission
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:11:56+00:00'
sampled_rows: 0
---

# `processed.registration_form_submission`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `instituteid` | `string` |  |
| `userid` | `string` |  |
| `status` | `string` |  |
| `createdat` | `timestamp` |  |
| `updatedat` | `timestamp` |  |
| `question_id` | `string` |  |
| `question_text` | `string` |  |
| `question_type` | `string` |  |
| `question_required` | `string` |  |
| `question_answer` | `string` |  |

## DDL

```sql
CREATE VIEW processed.registration_form_submission AS
SELECT
  reg_sub._id
, reg_sub.instituteid
, reg_sub.userid
, reg_sub.status
, reg_sub.createdat
, reg_sub.updatedat
, reg_sub.question_id
, reg_form.question_text
, reg_form.question_type
, reg_form.question_required
, reg_sub.question_answer
FROM
  ((
   SELECT
     _id
   , instituteid
   , userid
   , status
   , createdat
   , updatedat
   , CAST(JSON_EXTRACT(q, '$["questionid"]') AS VARCHAR) question_id
   , CAST(JSON_EXTRACT(q, '$["answer"]') AS VARCHAR) question_answer
   FROM
     ((
      SELECT
        CAST(JSON_EXTRACT(_id, '$["$oid"]') AS VARCHAR) _id
      , CAST(JSON_EXTRACT(instituteid, '$["$oid"]') AS VARCHAR) instituteid
      , CAST(JSON_EXTRACT(userid, '$["$oid"]') AS VARCHAR) userid
      , FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(createdat, '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE)) createdat
      , FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(updatedat, '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE)) updatedat
      , CAST(JSON_PARSE(answers) AS ARRAY(JSON)) question_answers
      , status
      FROM
        wise_app_backend__registration_form_submission
   ) 
   CROSS JOIN UNNEST(question_answers) t (q))
)  reg_sub
LEFT JOIN (
   SELECT
     instituteid
   , CAST(JSON_EXTRACT(q, '$["questionid"]') AS VARCHAR) question_id
   , CAST(JSON_EXTRACT(q, '$["type"]') AS VARCHAR) question_type
   , CAST(JSON_EXTRACT(q, '$["required"]') AS VARCHAR) question_required
   , CAST(JSON_EXTRACT(q, '$["questiontext"]') AS VARCHAR) question_text
   FROM
     ((
      SELECT
        CAST(JSON_EXTRACT(_id, '$["$oid"]') AS VARCHAR) _id
      , CAST(JSON_EXTRACT(instituteid, '$["$oid"]') AS VARCHAR) instituteid
      , FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(createdat, '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE)) createdat
      , FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(updatedat, '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE)) updatedat
      , CAST(JSON_EXTRACT(settings, '$.disableupdatingsubmission') AS VARCHAR) disableupdatingsubmission
      , CAST(JSON_PARSE(fields) AS ARRAY(JSON)) question_fields
      , CAST(JSON_EXTRACT(settings, '$.requiredforstudents') AS VARCHAR) requiredforstudents
      FROM
        wise_app_backend__registration_form
   ) 
   CROSS JOIN UNNEST(question_fields) t (q))
)  reg_form ON ((reg_form.instituteid = reg_sub.instituteid) AND (reg_form.question_id = reg_sub.question_id)))
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
