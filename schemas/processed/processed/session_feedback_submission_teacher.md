---
canonical: processed
table: session_feedback_submission_teacher
type: view
layer: processed
regions:
  in: processed
  na: processed_na
location: null
format: null
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:18:19+00:00'
sampled_rows: 0
sampled_region: null
---

# `processed.session_feedback_submission_teacher`

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
| `classid` | `string` |  |
| `sessionid` | `string` |  |
| `userid` | `string` |  |
| `sessionstatus` | `string` |  |
| `createdat` | `timestamp` |  |
| `updatedat` | `timestamp` |  |
| `questiontext` | `string` |  |
| `answer` | `string` |  |
| `type` | `string` |  |

## DDL

_From `IN` (processed)._

```sql
CREATE VIEW processed.session_feedback_submission_teacher AS
SELECT
  _id
, classid
, sessionid
, userid
, sessionstatus
, createdat
, updatedat
, CAST(JSON_EXTRACT(a, '$["questiontext"]') AS VARCHAR) questiontext
, CAST(JSON_EXTRACT(a, '$["answer"]') AS VARCHAR) answer
, CAST(JSON_EXTRACT(a, '$["type"]') AS VARCHAR) type
FROM
  ((
   SELECT
     CAST(JSON_EXTRACT(_id, '$["$oid"]') AS VARCHAR) _id
   , CAST(JSON_EXTRACT(classid, '$["$oid"]') AS VARCHAR) classid
   , CAST(JSON_EXTRACT(sessionid, '$["$oid"]') AS VARCHAR) sessionid
   , CAST(JSON_EXTRACT(userid, '$["$oid"]') AS VARCHAR) userid
   , sessionstatus
   , CAST(JSON_PARSE(answers) AS ARRAY(JSON)) answers
   , FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(createdat, '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE)) createdat
   , FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(updatedat, '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE)) updatedat
   FROM
     wise_app_backend__session_feedback_submission
   WHERE (profile = 'teacher')
) 
CROSS JOIN UNNEST(answers) t (a))
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
