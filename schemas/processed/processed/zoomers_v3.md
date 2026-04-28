---
database: processed
table: zoomers_v3
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:18:44+00:00'
sampled_rows: 0
---

# `processed.zoomers_v3`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `zoom_id` | `string` |  |
| `classid` | `string` |  |
| `title` | `string` |  |
| `attendancerecorded` | `string` |  |
| `mettingended` | `string` |  |
| `licensed` | `string` |  |
| `paiduser` | `string` |  |
| `duration` | `int` |  |
| `createdat` | `date` |  |
| `updatedat` | `date` |  |
| `start_time` | `timestamp` |  |
| `end_time` | `timestamp` |  |
| `updated_at_full_date_str` | `string` |  |
| `maxparticipantduration` | `string` |  |
| `participant` | `int` |  |
| `participant_list` | `string` |  |
| `archived` | `string` |  |
| `type` | `string` |  |
| `meetingstatus` | `string` |  |
| `recordingshared` | `string` |  |
| `isownerzoom` | `string` |  |
| `ownerid` | `string` |  |
| `mettingid` | `string` |  |
| `start_url` | `string` |  |
| `join_url` | `string` |  |
| `meetinguuid` | `string` |  |
| `location` | `string` |  |
| `row` | `bigint` |  |

## DDL

```sql
CREATE VIEW processed.zoomers_v3 AS
SELECT *
FROM
  (
   SELECT
     *
   , "row_number"() OVER (PARTITION BY zoom_id ORDER BY updated_at_full_date_str DESC) row
   FROM
     (
      SELECT
        CAST("json_extract"(userid, '$["$oid"]') AS varchar) userid
      , CAST("json_extract"(_id, '$["$oid"]') AS varchar) zoom_id
      , CAST("json_extract"(classid, '$["$oid"]') AS varchar) classid
      , title
      , attendancerecorded
      , mettingended
      , licensed
      , CAST(JSON_EXTRACT(metadata, '$.paiduser') AS VARCHAR) paiduser
      , "round"(((CASE WHEN (TRY_CAST("json_extract"(duration, '$["$numberint"]') AS integer) IS NULL) THEN TRY_CAST(duration AS INTEGER) ELSE TRY_CAST("json_extract"(duration, '$["$numberint"]') AS integer) END) / 60000)) duration
      , COALESCE("date"("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]') AS varchar), 1, 10)), "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double)))) createdat
      , COALESCE("date"("substr"(TRY_CAST("json_extract"(updatedat, '$["$date"]') AS varchar), 1, 10)), "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(updatedat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double)))) updatedat
      , COALESCE(DATE_PARSE(SUBSTR(TRY_CAST("json_extract"(start_time, '$["$date"]') AS varchar), 1, 19), '%Y-%m-%dT%T'), "from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(start_time, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) start_time
      , COALESCE(DATE_PARSE(SUBSTR(TRY_CAST("json_extract"(end_time, '$["$date"]') AS varchar), 1, 19), '%Y-%m-%dT%T'), "from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(end_time, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) end_time
      , COALESCE(TRY_CAST("json_extract"(updatedat, '$["$date"]') AS varchar), TRY_CAST("json_extract"(updatedat, '$["$date"]["$numberlong"]') AS varchar)) updated_at_full_date_str
      , maxparticipantduration
      , (CASE WHEN (TRY_CAST("json_extract"(participant, '$["$numberint"]') AS integer) IS NULL) THEN TRY_CAST(participant AS INTEGER) ELSE TRY_CAST("json_extract"(participant, '$["$numberint"]') AS integer) END) participant
      , participants participant_list
      , archived
      , type
      , meetingstatus
      , recordingshared
      , CAST(JSON_EXTRACT(metadata, '$["isownerzoom"]') AS VARCHAR) isownerzoom
      , CAST(JSON_EXTRACT(metadata, '$["ownerid"]["$oid"]') AS VARCHAR) ownerid
      , mettingid
      , start_url
      , join_url
      , meetinguuid
      , location
      FROM
        wise_app_backend__zoom
   ) 
) 
WHERE (row = 1)
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
