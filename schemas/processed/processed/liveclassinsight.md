---
canonical: processed
table: liveclassinsight
type: view
layer: processed
regions:
  in: processed
  na: processed_na
location: null
format: null
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:17:10+00:00'
sampled_rows: 0
sampled_region: null
---

# `processed.liveclassinsight`

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

_From `IN` (processed)._

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
