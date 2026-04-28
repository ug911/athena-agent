---
database: processed
table: registration_form
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:11:53+00:00'
sampled_rows: 0
---

# `processed.registration_form`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `instituteid` | `string` |  |
| `createdat` | `timestamp` |  |
| `updatedat` | `timestamp` |  |
| `disableupdatingsubmission` | `string` |  |
| `requiredforstudents` | `string` |  |
| `question_id` | `string` |  |
| `question_type` | `string` |  |
| `question_required` | `string` |  |
| `question_text` | `string` |  |

## DDL

```sql
CREATE VIEW processed.registration_form AS
SELECT
  _id
, instituteid
, createdat
, updatedat
, disableupdatingsubmission
, requiredforstudents
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
     "processed".wise_app_backend__registration_form
) 
CROSS JOIN UNNEST(question_fields) t (q))
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
