---
canonical: processed
table: zoomers
type: view
layer: processed
regions:
  in: processed
  na: processed_na
location: null
format: null
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:31:52+00:00'
sampled_rows: 0
sampled_region: null
---

# `processed.zoomers`

## Region availability

| Region | Athena database |
| --- | --- |
| `IN` | `processed` |
| `NA` | `processed_na` |

_Schema parity: **identical** across regions._

## Columns (IN)

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `zoom_id` | `string` |  |
| `classid` | `string` |  |
| `attendancerecorded` | `string` |  |
| `mettingended` | `string` |  |
| `duration` | `int` |  |
| `createdat` | `date` |  |
| `updatedat` | `date` |  |
| `start_time` | `timestamp` |  |
| `end_time` | `timestamp` |  |
| `maxparticipantduration` | `string` |  |
| `participants` | `bigint` |  |
| `participant` | `int` |  |
| `zoom_participants` | `array<string>` |  |

## DDL

_From `IN` (processed)._

```sql
CREATE VIEW processed.zoomers AS
SELECT
  CAST("json_extract"(userid, '$["$oid"]') AS varchar) userid
, CAST("json_extract"(_id, '$["$oid"]') AS varchar) zoom_id
, CAST("json_extract"(classid, '$["$oid"]') AS varchar) classid
, attendancerecorded
, mettingended
, "round"(((CASE WHEN (TRY_CAST("json_extract"(duration, '$["$numberint"]') AS integer) IS NULL) THEN TRY_CAST(duration AS INTEGER) ELSE TRY_CAST("json_extract"(duration, '$["$numberint"]') AS integer) END) / 60000)) duration
, COALESCE("date"("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]') AS varchar), 1, 10)), "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double)))) createdat
, COALESCE("date"("substr"(TRY_CAST("json_extract"(updatedat, '$["$date"]') AS varchar), 1, 10)), "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(updatedat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double)))) updatedat
, COALESCE(DATE_PARSE(SUBSTR(TRY_CAST("json_extract"(start_time, '$["$date"]') AS varchar), 1, 19), '%Y-%m-%dT%T'), "from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(start_time, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) start_time
, COALESCE(DATE_PARSE(SUBSTR(TRY_CAST("json_extract"(end_time, '$["$date"]') AS varchar), 1, 19), '%Y-%m-%dT%T'), "from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(end_time, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) end_time
, maxparticipantduration
, "cardinality"("transform"(CAST("json_parse"(participants) AS array(json)), (x) -> "json_extract"(x, '$._id["$oid"]'))) participants
, (CASE WHEN (TRY_CAST("json_extract"(participant, '$["$numberint"]') AS integer) IS NULL) THEN TRY_CAST(participant AS INTEGER) ELSE TRY_CAST("json_extract"(participant, '$["$numberint"]') AS integer) END) participant
, "transform"(CAST("json_parse"(participants) AS array(json)), (x) -> CAST("json_extract"(x, '$.wiseuserid["$oid"]') AS varchar)) zoom_participants
FROM
  wise_app_backend__zoom
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
