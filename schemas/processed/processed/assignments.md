---
database: processed
table: assignments
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:10:14+00:00'
sampled_rows: 0
---

# `processed.assignments`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `classid` | `string` |  |
| `assignment_id` | `string` |  |
| `topic` | `string` |  |
| `description` | `string` |  |
| `submissiondate` | `string` |  |
| `maxmarks` | `string` |  |
| `starttime` | `string` |  |
| `createdat` | `date` |  |
| `submitby` | `date` |  |
| `num_attachments` | `bigint` |  |
| `attachments` | `array<string>` |  |
| `num_submissions` | `bigint` |  |
| `submissions` | `array<string>` |  |

## DDL

```sql
CREATE VIEW processed.assignments AS
SELECT
  CAST("json_extract"(userid, '$["$oid"]') AS varchar) userid
, CAST("json_extract"(classid, '$["$oid"]') AS varchar) classid
, CAST("json_extract"(_id, '$["$oid"]') AS varchar) assignment_id
, topic
, description
, submissiondate
, TRY_CAST("json_extract"(maxmarks, '$["$numberint"]') AS varchar) maxmarks
, starttime
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) createdat
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(submitby, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) submitby
, "cardinality"("transform"(CAST("json_parse"(attachments) AS array(json)), (x) -> "json_extract"(x, '$._id["$oid"]'))) num_attachments
, "transform"(CAST("json_parse"(attachments) AS array(json)), (x) -> CAST("json_extract"(x, '$.type') AS varchar)) attachments
, "cardinality"("transform"(CAST("json_parse"(submission) AS array(json)), (x) -> "json_extract"(x, '$.studentid["$oid"]'))) num_submissions
, "transform"(CAST("json_parse"(submission) AS array(json)), (x) -> CAST("json_extract"(x, '$.studentid["$oid"]') AS varchar)) submissions
FROM
  wise_app_backend__assignments
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
