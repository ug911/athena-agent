---
canonical: processed
table: session_feedback_submission_student
type: view
layer: processed
regions:
  in: processed
  na: processed_na
location: null
format: null
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:18:14+00:00'
sampled_rows: 0
sampled_region: null
---

# `processed.session_feedback_submission_student`

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
| `comment` | `string` |  |
| `commenttext` | `string` |  |
| `rating` | `int` |  |
| `createdat` | `timestamp` |  |
| `updatedat` | `timestamp` |  |

## DDL

_From `IN` (processed)._

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
