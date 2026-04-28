---
database: processed
table: class_participants
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:10:19+00:00'
sampled_rows: 0
---

# `processed.class_participants`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `class_participant_id` | `string` |  |
| `userid` | `string` |  |
| `classid` | `string` |  |
| `createdat` | `date` |  |
| `updatedat` | `date` |  |
| `joinedon` | `date` |  |
| `__v` | `string` |  |
| `relation` | `string` |  |
| `status` | `string` |  |

## DDL

```sql
CREATE VIEW processed.class_participants AS
SELECT
  CAST("json_extract"("_id", '$["$oid"]') AS varchar) class_participant_id
, CAST("json_extract"("userid", '$["$oid"]') AS varchar) userid
, CAST("json_extract"("classid", '$["$oid"]') AS varchar) classid
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) createdat
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(updatedat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) updatedat
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(joinedon, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) joinedon
, CAST("json_extract"("__v", '$["$numberint"]') AS varchar) __v
, "relation"
, "status"
FROM
  "processed"."wise_app_backend__classparticipant"
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
