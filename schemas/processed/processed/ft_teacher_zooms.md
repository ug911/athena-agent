---
database: processed
table: ft_teacher_zooms
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:11:18+00:00'
sampled_rows: 0
---

# `processed.ft_teacher_zooms`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `days_since_user` | `bigint` |  |
| `zooms` | `bigint` |  |
| `zoom_avg_duration` | `double` |  |
| `zoom_avg_participants` | `double` |  |
| `zoom_participants` | `bigint` |  |
| `zoom_participants_per_zoom` | `double` |  |
| `zoom_classes` | `bigint` |  |
| `zoom_low_participants` | `bigint` |  |
| `zoom_med_participants` | `bigint` |  |
| `zoom_high_participants` | `bigint` |  |
| `zoom_days_since_last_zoom` | `bigint` |  |
| `zoom_days_since_first_zoom` | `bigint` |  |
| `zooms_first_7` | `bigint` |  |
| `zooms_next_7` | `bigint` |  |
| `zooms_first_14` | `bigint` |  |
| `zooms_next_14` | `bigint` |  |
| `zooms_first_30` | `bigint` |  |
| `zooms_next_30` | `bigint` |  |
| `zooms_first_60` | `bigint` |  |
| `zoom_participant_first_7` | `bigint` |  |
| `zoom_participant_next_7` | `bigint` |  |
| `zoom_participant_first_14` | `bigint` |  |
| `zoom_participant_next_14` | `bigint` |  |
| `zoom_participant_first_30` | `bigint` |  |
| `zoom_participant_next_30` | `bigint` |  |
| `zoom_participant_first_60` | `bigint` |  |
| `zooms_last_7` | `bigint` |  |
| `zooms_last2last_7` | `bigint` |  |
| `zooms_last_14` | `bigint` |  |
| `zooms_last2last_14` | `bigint` |  |
| `zooms_last_30` | `bigint` |  |
| `zooms_last2last_30` | `bigint` |  |
| `zooms_last_60` | `bigint` |  |
| `zoom_participant_last_7` | `bigint` |  |
| `zoom_participant_last2last_7` | `bigint` |  |
| `zoom_participant_last_14` | `bigint` |  |
| `zoom_participant_last2last_14` | `bigint` |  |
| `zoom_participant_last_30` | `bigint` |  |
| `zoom_participant_last2last_30` | `bigint` |  |
| `zoom_participant_last_60` | `bigint` |  |

## DDL

```sql
CREATE VIEW processed.ft_teacher_zooms AS
SELECT
  userid
, days_since_user
, zooms
, zoom_avg_duration
, zoom_avg_participants
, zoom_participants
, zoom_participants_per_zoom
, zoom_classes
, zoom_low_participants
, zoom_med_participants
, zoom_high_participants
, zoom_days_since_last_zoom
, zoom_days_since_first_zoom
, zooms_first_7
, (zooms_first_14 - zooms_first_7) zooms_next_7
, zooms_first_14
, (zooms_first_30 - zooms_first_14) zooms_next_14
, zooms_first_30
, (zooms_first_60 - zooms_first_30) zooms_next_30
, zooms_first_60
, zoom_participant_first_7
, (zoom_participant_first_14 - zoom_participant_first_7) zoom_participant_next_7
, zoom_participant_first_14
, (zoom_participant_first_30 - zoom_participant_first_14) zoom_participant_next_14
, zoom_participant_first_30
, (zoom_participant_first_60 - zoom_participant_first_30) zoom_participant_next_30
, zoom_participant_first_60
, zooms_last_7
, (zooms_last_14 - zooms_last_7) zooms_last2last_7
, zooms_last_14
, (zooms_last_30 - zooms_last_14) zooms_last2last_14
, zooms_last_30
, (zooms_last_60 - zooms_last_30) zooms_last2last_30
, zooms_last_60
, zoom_participant_last_7
, (zoom_participant_last_14 - zoom_participant_last_7) zoom_participant_last2last_7
, zoom_participant_last_14
, (zoom_participant_last_30 - zoom_participant_last_14) zoom_participant_last2last_14
, zoom_participant_last_30
, (zoom_participant_last_60 - zoom_participant_last_30) zoom_participant_last2last_30
, zoom_participant_last_60
FROM
  (
   SELECT
     a.userid
   , days_since_user
   , "count"(*) zooms
   , "sum"(participant) zoom_participants
   , "round"(((1E0 * "sum"(participant)) / "count"(*))) zoom_participants_per_zoom
   , "count"(DISTINCT classid) zoom_classes
   , "sum"((CASE WHEN (participant < 5) THEN 1 ELSE 0 END)) zoom_low_participants
   , "sum"((CASE WHEN (participant BETWEEN 5 AND 9) THEN 1 ELSE 0 END)) zoom_med_participants
   , "sum"((CASE WHEN (participant > 9) THEN 1 ELSE 0 END)) zoom_high_participants
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) zooms_last_7
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '15' DAY)) THEN 1 ELSE 0 END)) zooms_last_14
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) zooms_last_30
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '61' DAY)) THEN 1 ELSE 0 END)) zooms_last_60
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '8' DAY)) THEN participant ELSE 0 END)) zoom_participant_last_7
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '15' DAY)) THEN participant ELSE 0 END)) zoom_participant_last_14
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '31' DAY)) THEN participant ELSE 0 END)) zoom_participant_last_30
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '61' DAY)) THEN participant ELSE 0 END)) zoom_participant_last_60
   , "date_diff"('day', "min"("date"(a.createdat)), current_date) zoom_days_since_first_zoom
   , "date_diff"('day', "max"("date"(a.createdat)), current_date) zoom_days_since_last_zoom
   , "round"(((1E0 * "sum"(duration)) / "count"(*))) zoom_avg_duration
   , "round"(((1E0 * "sum"(participant)) / "count"(*))) zoom_avg_participants
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) zooms_first_7
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '15' DAY)) THEN 1 ELSE 0 END)) zooms_first_14
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) zooms_first_30
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '61' DAY)) THEN 1 ELSE 0 END)) zooms_first_60
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '8' DAY)) THEN participant ELSE 0 END)) zoom_participant_first_7
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '15' DAY)) THEN participant ELSE 0 END)) zoom_participant_first_14
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '31' DAY)) THEN participant ELSE 0 END)) zoom_participant_first_30
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '61' DAY)) THEN participant ELSE 0 END)) zoom_participant_first_60
   FROM
     ((
      SELECT
        userid
      , classid
      , "date"(createdat) createdat
      , zoom_id
      , duration
      , participant
      FROM
        zoomers
      WHERE (participant > 1)
   )  a
   INNER JOIN (
      SELECT
        userid
      , createdat
      , "date_diff"('day', createdat, current_date) days_since_user
      FROM
        user
   )  u ON (a.userid = u.userid))
   GROUP BY 1, 2
)
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->
