---
database: processed
table: session_feedback_submission_student
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:12:16+00:00'
sampled_rows: 0
---

# `processed.session_feedback_submission_student`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `classid` | `string` |  |
| `sessionid` | `string` |  |
| `userid` | `string` |  |
| `comment` | `string` |  |
| `commenttext` | `string` |  |
| `rating` | `int` |  |
| `createdat` | `timestamp` |  |
| `updatedat` | `timestamp` |  |

## DDL

```sql
CREATE VIEW processed.session_feedback_submission_student AS
SELECT
  CAST(JSON_EXTRACT(_id, '$["$oid"]') AS VARCHAR) _id
, CAST(JSON_EXTRACT(classid, '$["$oid"]') AS VARCHAR) classid
, CAST(JSON_EXTRACT(sessionid, '$["$oid"]') AS VARCHAR) sessionid
, CAST(JSON_EXTRACT(userid, '$["$oid"]') AS VARCHAR) userid
, comment
, commenttext
, CAST(JSON_EXTRACT(rating, '$["$numberint"]') AS INTEGER) rating
, FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(createdat, '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE)) createdat
, FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(updatedat, '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE)) updatedat
FROM
  wise_app_backend__session_feedback_submission
WHERE (profile = 'student')
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
