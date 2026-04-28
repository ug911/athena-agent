---
database: processed
table: announcements
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:10:11+00:00'
sampled_rows: 0
---

# `processed.announcements`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `classid` | `string` |  |
| `announcement_id` | `string` |  |
| `title` | `string` |  |
| `description` | `string` |  |
| `date` | `string` |  |
| `createdat` | `date` |  |
| `lastcommentedat` | `date` |  |
| `comments` | `bigint` |  |
| `comment_users` | `array<string>` |  |

## DDL

```sql
CREATE VIEW processed.announcements AS
SELECT
  CAST("json_extract"(userid, '$["$oid"]') AS varchar) userid
, CAST("json_extract"(classid, '$["$oid"]') AS varchar) classid
, CAST("json_extract"(_id, '$["$oid"]') AS varchar) announcement_id
, title
, description
, date
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) createdat
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(lastcommentedat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) lastcommentedat
, "cardinality"("transform"(CAST("json_parse"(comments) AS array(json)), (x) -> "json_extract"(x, '$._id["$oid"]'))) comments
, "transform"(CAST("json_parse"(comments) AS array(json)), (x) -> CAST("json_extract"(x, '$.userid["$oid"]') AS varchar)) comment_users
FROM
  wise_app_backend__announcements
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
