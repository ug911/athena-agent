---
database: processed
table: liveclassinsight_details
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:11:32+00:00'
sampled_rows: 0
---

# `processed.liveclassinsight_details`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `sessionid` | `string` |  |
| `userid` | `string` |  |
| `createdat` | `timestamp` |  |
| `starttime` | `timestamp` |  |
| `endtime` | `timestamp` |  |
| `meetingid` | `string` |  |
| `num_participants` | `bigint` |  |
| `duration_in_seconds` | `bigint` |  |
| `participant_name` | `string` |  |
| `type` | `string` |  |
| `attendanceduration` | `int` |  |
| `attentiveduration` | `int` |  |
| `speakingduration` | `int` |  |
| `rating` | `int` |  |
| `comment` | `string` |  |
| `participant_userid` | `string` |  |
| `participant_zoomuserid` | `string` |  |
| `participant_platform` | `string` |  |
| `participant_firstentrytime` | `string` |  |
| `participant_lastexittime` | `string` |  |

## DDL

```sql
CREATE VIEW processed.liveclassinsight_details AS
SELECT
  m._id
, m.sessionid
, m.userid
, m.createdat
, m.starttime
, m.endtime
, m.meetingid
, m.num_participants
, DATE_DIFF('second', m.starttime, m.endtime) duration_in_seconds
, p.name participant_name
, p.type
, p.attendanceduration
, p.attentiveduration
, p.speakingduration
, p.rating
, p.comment
, p.participant_userid
, p.participant_zoomuserid
, p.participant_platform
, p.participant_firstEntryTime
, p.participant_lastExitTime
FROM
  ((
   SELECT
     _id
   , sessionid
   , userid
   , createdat
   , starttime
   , endtime
   , meetingid
   , CARDINALITY(TRY_CAST(JSON_PARSE(participants) AS ARRAY(JSON))) num_participants
   FROM
     liveclassinsight
)  m
LEFT JOIN (
   SELECT
     p.*
   , r.rating
   , r.comment
   FROM
     ((
      SELECT
        _id
      , CAST(JSON_EXTRACT(r, '$["name"]') AS VARCHAR) name
      , CAST(JSON_EXTRACT(r, '$["type"]') AS VARCHAR) type
      , CAST(JSON_EXTRACT(r, '$["attendanceduration"]["$numberint"]') AS INTEGER) attendanceduration
      , CAST(JSON_EXTRACT(r, '$["attentiveduration"]["$numberint"]') AS INTEGER) attentiveduration
      , CAST(JSON_EXTRACT(r, '$["speakingduration"]["$numberint"]') AS INTEGER) speakingduration
      , CAST(JSON_EXTRACT(r, '$.userid') AS VARCHAR) participant_userid
      , CAST(JSON_EXTRACT(r, '$.zoomuserid') AS VARCHAR) participant_zoomuserid
      , CAST(JSON_EXTRACT(r, '$.platform') AS VARCHAR) participant_platform
      , CAST(JSON_EXTRACT(r, '$.firstEntryTime') AS VARCHAR) participant_firstEntryTime
      , CAST(JSON_EXTRACT(r, '$.lastExitTime') AS VARCHAR) participant_lastExitTime
      FROM
        ((
         SELECT
           _id
         , TRY_CAST(JSON_PARSE(participants) AS ARRAY(JSON)) participants
         FROM
           liveclassinsight
      ) 
      CROSS JOIN UNNEST(participants) t (r))
   )  p
   LEFT JOIN (
      SELECT
        _id
      , CAST(JSON_EXTRACT(r, '$["rating"]["$numberint"]') AS INTEGER) rating
      , CAST(JSON_EXTRACT(r, '$["comment"]') AS VARCHAR) comment
      , CAST(JSON_EXTRACT(r, '$.userid') AS VARCHAR) participant_userid
      FROM
        ((
         SELECT
           _id
         , TRY_CAST(JSON_PARSE(userratings) AS ARRAY(JSON)) userratings
         FROM
           liveclassinsight
         WHERE (userratings <> '[]')
      ) 
      CROSS JOIN UNNEST(userratings) t (r))
   )  r ON ((r._id = p._id) AND (r.participant_userid = p.participant_userid)))
)  p ON (m._id = p._id))
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
