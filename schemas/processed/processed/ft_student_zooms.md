---
database: processed
table: ft_student_zooms
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:11:01+00:00'
sampled_rows: 0
---

# `processed.ft_student_zooms`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `first_zoom_on_student` | `date` |  |
| `days_since_first_zoom_student` | `bigint` |  |
| `last_zoom_on_student` | `date` |  |
| `days_since_last_zoom_student` | `bigint` |  |
| `total_class_duration` | `bigint` |  |
| `avg_attending_duration` | `double` |  |
| `avg_attending_participants` | `double` |  |
| `attended_zooms` | `bigint` |  |
| `attended_zooms_classes` | `bigint` |  |
| `attended_zooms_teachers` | `bigint` |  |
| `attended_zooms_low` | `bigint` |  |
| `attended_zooms_med` | `bigint` |  |
| `attended_zooms_high` | `bigint` |  |
| `attended_zooms_14` | `bigint` |  |
| `attended_zooms_29` | `bigint` |  |

## DDL

```sql
CREATE VIEW processed.ft_student_zooms AS
SELECT
  CAST(zp AS varchar) userid
, "min"("date"(createdat)) first_zoom_on_student
, "date_diff"('day', "min"("date"(createdat)), current_date) days_since_first_zoom_student
, "max"("date"(createdat)) last_zoom_on_student
, "date_diff"('day', "max"("date"(createdat)), current_date) days_since_last_zoom_student
, "sum"(duration) total_class_duration
, "round"(((1E0 * "sum"(duration)) / "count"(*))) avg_attending_duration
, "round"(((1E0 * "sum"(participants)) / "count"(*))) avg_attending_participants
, "count"(*) attended_zooms
, "count"(DISTINCT classid) attended_zooms_classes
, "count"(DISTINCT userid) attended_zooms_teachers
, "sum"((CASE WHEN ((participants > 1) AND (participants < 5)) THEN 1 ELSE 0 END)) attended_zooms_low
, "sum"((CASE WHEN (participants BETWEEN 5 AND 9) THEN 1 ELSE 0 END)) attended_zooms_med
, "sum"((CASE WHEN (participants > 9) THEN 1 ELSE 0 END)) attended_zooms_high
, "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '15' DAY)) THEN 1 ELSE 0 END)) attended_zooms_14
, "sum"((CASE WHEN ("date"(createdat) > (current_date - INTERVAL  '29' DAY)) THEN 1 ELSE 0 END)) attended_zooms_29
FROM
  (zoomers
CROSS JOIN UNNEST(zoom_participants) t (zp))
WHERE (participants > 1)
GROUP BY 1
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
