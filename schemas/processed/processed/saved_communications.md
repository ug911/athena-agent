---
canonical: processed
table: saved_communications
type: view
layer: processed
regions:
  in: processed
  na: processed_na
location: null
format: null
partition_keys: []
schema_parity: identical
last_synced: '2026-08-11T13:18:09+00:00'
sampled_rows: 0
sampled_region: null
---

# `processed.saved_communications`

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
| `userid` | `string` |  |
| `ownerid` | `string` |  |
| `creditsused` | `string` |  |
| `type` | `string` |  |
| `category` | `string` |  |
| `createdat` | `date` |  |

## DDL

_From `IN` (processed)._

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
