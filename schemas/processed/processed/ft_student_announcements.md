---
database: processed
table: ft_student_announcements
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:10:53+00:00'
sampled_rows: 0
---

# `processed.ft_student_announcements`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `comments` | `bigint` |  |
| `commented_announcements` | `bigint` |  |
| `commented_announcements_classes` | `bigint` |  |
| `commented_announcements_teachers` | `bigint` |  |
| `commented_announcements_low` | `bigint` |  |
| `commented_announcements_med` | `bigint` |  |
| `commented_announcements_high` | `bigint` |  |
| `commented_announcements_14` | `bigint` |  |
| `commented_announcements_29` | `bigint` |  |

## DDL

```sql
CREATE VIEW processed.ft_student_announcements AS
SELECT
  CAST(ann AS varchar) userid
, "count"(*) comments
, "count"(DISTINCT announcement_id) commented_announcements
, "count"(DISTINCT classid) commented_announcements_classes
, "count"(DISTINCT userid) commented_announcements_teachers
, "sum"((CASE WHEN (comments < 5) THEN 1 ELSE 0 END)) commented_announcements_low
, "sum"((CASE WHEN (comments BETWEEN 5 AND 9) THEN 1 ELSE 0 END)) commented_announcements_med
, "sum"((CASE WHEN (comments > 9) THEN 1 ELSE 0 END)) commented_announcements_high
, "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '14' DAY)) THEN 1 ELSE 0 END)) commented_announcements_14
, "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '29' DAY)) THEN 1 ELSE 0 END)) commented_announcements_29
FROM
  (announcements
CROSS JOIN UNNEST(comment_users) t (ann))
WHERE (comments > 0)
GROUP BY 1
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
