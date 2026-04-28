---
database: processed
table: tests
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:12:37+00:00'
sampled_rows: 0
---

# `processed.tests`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `classid` | `string` |  |
| `testid` | `string` |  |
| `status` | `string` |  |
| `_type` | `string` |  |
| `createdat` | `date` |  |
| `num_submissions` | `bigint` |  |
| `submissions` | `array<string>` |  |

## DDL

```sql
CREATE VIEW processed.tests AS
SELECT
  userid
, classid
, x.testid
, status
, _type
, createdat
, num_submissions
, submissions
FROM
  ((
   SELECT
     CAST("json_extract"(_id, '$["$oid"]') AS varchar) testid
   , CAST("json_extract"(class_id, '$["$oid"]') AS varchar) classid
   , CAST("json_extract"(user_id, '$["$oid"]') AS varchar) userid
   , COALESCE("date"("substr"(TRY_CAST("json_extract"(created_at, '$["$date"]') AS varchar), 1, 10)), "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(created_at, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double)))) createdat
   , status
   , _type
   FROM
     exam_service__tests
   WHERE ((active = 'true') AND (NOT (status IN ('DRAFT'))))
)  x
LEFT JOIN (
   SELECT
     CAST("json_extract"(test_id, '$["$oid"]') AS varchar) testid
   , "count"(*) num_submissions
   , "array_agg"(CAST("json_extract"(user_id, '$["$oid"]') AS varchar)) submissions
   FROM
     processed.exam_service__submissions
   GROUP BY 1
)  y ON (x.testid = y.testid))
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
