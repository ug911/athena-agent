---
database: processed
table: zoom_summaries
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:18:36+00:00'
sampled_rows: 0
---

# `processed.zoom_summaries`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `_id` | `string` |  |
| `sessionid` | `string` |  |
| `createdat` | `timestamp` |  |
| `updatedat` | `timestamp` |  |
| `num_summaries` | `bigint` |  |
| `summarytitle` | `string` |  |
| `summaryoverview` | `string` |  |
| `summarydetails` | `array<map<string,string>>` |  |
| `num_summarydetails` | `bigint` |  |
| `meetinguuid` | `string` |  |

## DDL

```sql
CREATE VIEW processed.zoom_summaries AS
SELECT
  _id
, sessionId
, createdAt
, updatedAt
, num_summaries
, CAST(JSON_EXTRACT(summary, '$.summarytitle') AS VARCHAR) summarytitle
, CAST(JSON_EXTRACT(summary, '$.summaryoverview') AS VARCHAR) summaryoverview
, CAST(JSON_EXTRACT(summary, '$.summarydetails') AS ARRAY(MAP(VARCHAR, VARCHAR))) summarydetails
, CARDINALITY(CAST(JSON_EXTRACT(summary, '$.summarydetails') AS ARRAY(MAP(VARCHAR, VARCHAR)))) num_summarydetails
, CAST(JSON_EXTRACT(summary, '$.meetinguuid') AS VARCHAR) meetinguuid
FROM
  ((
   SELECT
     CAST(JSON_EXTRACT(_id, '$["$oid"]') AS VARCHAR) _id
   , CAST(JSON_EXTRACT(sessionId, '$["$oid"]') AS VARCHAR) sessionId
   , FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(createdAt, '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE)) createdAt
   , FROM_UNIXTIME(CAST(SUBSTR(CAST(JSON_EXTRACT(updatedAt, '$["$date"]["$numberlong"]') AS VARCHAR), 1, 10) AS DOUBLE)) updatedAt
   , CARDINALITY(CAST(JSON_PARSE(summaries) AS ARRAY(JSON))) num_summaries
   , CAST(JSON_PARSE(summaries) AS ARRAY(JSON)) summaries
   FROM
     wise_app_backend__rawzoomsummary
) 
CROSS JOIN UNNEST(summaries) t (summary))
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
