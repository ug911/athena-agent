---
database: processed
table: liveclassinsight
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:11:28+00:00'
sampled_rows: 0
---

# `processed.liveclassinsight`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `sessionid` | `string` |  |
| `userid` | `string` |  |
| `meetingid` | `string` |  |
| `meetingpassword` | `string` |  |
| `meetinguuid` | `string` |  |
| `userratings` | `string` |  |
| `participants` | `string` |  |
| `createdat` | `timestamp` |  |
| `updatedat` | `timestamp` |  |
| `starttime` | `timestamp` |  |
| `endtime` | `timestamp` |  |
| `__v` | `string` |  |

## DDL

```sql
CREATE VIEW processed.liveclassinsight AS
SELECT
  TRY_CAST(JSON_EXTRACT(_id, '$["$oid"]') AS VARCHAR) _id
, TRY_CAST(JSON_EXTRACT(sessionid, '$["$oid"]') AS VARCHAR) sessionid
, TRY_CAST(JSON_EXTRACT(userid, '$["$oid"]') AS VARCHAR) userid
, meetingid
, meetingpassword
, meetinguuid
, userratings
, participants
, COALESCE(DATE_PARSE(SUBSTR(TRY_CAST("json_extract"(createdat, '$["$date"]') AS varchar), 1, 19), '%Y-%m-%dT%T'), "from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) createdat
, COALESCE(DATE_PARSE(SUBSTR(TRY_CAST("json_extract"(updatedat, '$["$date"]') AS varchar), 1, 19), '%Y-%m-%dT%T'), "from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(updatedat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) updatedat
, COALESCE(DATE_PARSE(SUBSTR(TRY_CAST("json_extract"(starttime, '$["$date"]') AS varchar), 1, 19), '%Y-%m-%dT%T'), "from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(starttime, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) starttime
, COALESCE(DATE_PARSE(SUBSTR(TRY_CAST("json_extract"(endtime, '$["$date"]') AS varchar), 1, 19), '%Y-%m-%dT%T'), "from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(endtime, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) endtime
, TRY_CAST("json_extract"(__v, '$["$numberlong"]') AS varchar) __v
FROM
  processed.wise_app_backend__liveclassinsight
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
