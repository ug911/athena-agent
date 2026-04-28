---
database: processed
table: saved_communications
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:12:13+00:00'
sampled_rows: 0
---

# `processed.saved_communications`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `userid` | `string` |  |
| `ownerid` | `string` |  |
| `creditsused` | `string` |  |
| `type` | `string` |  |
| `category` | `string` |  |
| `createdat` | `date` |  |

## DDL

```sql
CREATE VIEW processed.saved_communications AS
SELECT
  CAST(JSON_EXTRACT(_id, '$["$oid"]') AS VARCHAR) _id
, CAST(JSON_EXTRACT(userid, '$["$oid"]') AS VARCHAR) userid
, CAST(JSON_EXTRACT(ownerid, '$["$oid"]') AS VARCHAR) ownerid
, CAST(JSON_EXTRACT(creditsused, '$["$numberint"]') AS VARCHAR) creditsused
, type
, category
, DATE(FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(createdat, '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE))) createdat
FROM
  wise_app_backend__saved_communication
LIMIT 10
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
