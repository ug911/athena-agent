---
database: processed
table: ft_teacher_announcements
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:11:04+00:00'
sampled_rows: 0
---

# `processed.ft_teacher_announcements`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `userid` | `string` |  |
| `days_since_user` | `bigint` |  |
| `announcements` | `bigint` |  |
| `announcement_comments` | `bigint` |  |
| `announcement_comments_per_announcement` | `double` |  |
| `announcement_classes` | `bigint` |  |
| `announcement_low_comments` | `bigint` |  |
| `announcement_med_comments` | `bigint` |  |
| `announcement_high_comments` | `bigint` |  |
| `announcement_days_since_last_announcement` | `bigint` |  |
| `announcement_days_since_first_announcement` | `bigint` |  |
| `announcements_first_7` | `bigint` |  |
| `announcements_next_7` | `bigint` |  |
| `announcements_first_14` | `bigint` |  |
| `announcements_next_14` | `bigint` |  |
| `announcements_first_30` | `bigint` |  |
| `announcements_next_30` | `bigint` |  |
| `announcements_first_60` | `bigint` |  |
| `announcement_comments_first_7` | `bigint` |  |
| `announcement_comments_next_7` | `bigint` |  |
| `announcement_comments_first_14` | `bigint` |  |
| `announcement_comments_next_14` | `bigint` |  |
| `announcement_comments_first_30` | `bigint` |  |
| `announcement_comments_next_30` | `bigint` |  |
| `announcement_comments_first_60` | `bigint` |  |
| `announcements_last_7` | `bigint` |  |
| `announcements_last2last_7` | `bigint` |  |
| `announcements_last_14` | `bigint` |  |
| `announcements_last2last_14` | `bigint` |  |
| `announcements_last_30` | `bigint` |  |
| `announcements_last2last_30` | `bigint` |  |
| `announcements_last_60` | `bigint` |  |
| `announcement_comments_last_7` | `bigint` |  |
| `announcement_comments_last2last_7` | `bigint` |  |
| `announcement_comments_last_14` | `bigint` |  |
| `announcement_comments_last2last_14` | `bigint` |  |
| `announcement_comments_last_30` | `bigint` |  |
| `announcement_comments_last2last_30` | `bigint` |  |
| `announcement_comments_last_60` | `bigint` |  |

## DDL

```sql
CREATE VIEW processed.ft_teacher_announcements AS
SELECT
  userid
, days_since_user
, announcements
, announcement_comments
, announcement_comments_per_announcement
, announcement_classes
, announcement_low_comments
, announcement_med_comments
, announcement_high_comments
, announcement_days_since_last_announcement
, announcement_days_since_first_announcement
, announcements_first_7
, (announcements_first_14 - announcements_first_7) announcements_next_7
, announcements_first_14
, (announcements_first_30 - announcements_first_14) announcements_next_14
, announcements_first_30
, (announcements_first_60 - announcements_first_30) announcements_next_30
, announcements_first_60
, announcement_comments_first_7
, (announcement_comments_first_14 - announcement_comments_first_7) announcement_comments_next_7
, announcement_comments_first_14
, (announcement_comments_first_30 - announcement_comments_first_14) announcement_comments_next_14
, announcement_comments_first_30
, (announcement_comments_first_60 - announcement_comments_first_30) announcement_comments_next_30
, announcement_comments_first_60
, announcements_last_7
, (announcements_last_14 - announcements_last_7) announcements_last2last_7
, announcements_last_14
, (announcements_last_30 - announcements_last_14) announcements_last2last_14
, announcements_last_30
, (announcements_last_60 - announcements_last_30) announcements_last2last_30
, announcements_last_60
, announcement_comments_last_7
, (announcement_comments_last_14 - announcement_comments_last_7) announcement_comments_last2last_7
, announcement_comments_last_14
, (announcement_comments_last_30 - announcement_comments_last_14) announcement_comments_last2last_14
, announcement_comments_last_30
, (announcement_comments_last_60 - announcement_comments_last_30) announcement_comments_last2last_30
, announcement_comments_last_60
FROM
  (
   SELECT
     a.userid
   , days_since_user
   , "count"(*) announcements
   , "sum"(comments) announcement_comments
   , "round"(((1E0 * "sum"(comments)) / "count"(*))) announcement_comments_per_announcement
   , "count"(DISTINCT classid) announcement_classes
   , "sum"((CASE WHEN (comments < 5) THEN 1 ELSE 0 END)) announcement_low_comments
   , "sum"((CASE WHEN (comments BETWEEN 5 AND 9) THEN 1 ELSE 0 END)) announcement_med_comments
   , "sum"((CASE WHEN (comments > 9) THEN 1 ELSE 0 END)) announcement_high_comments
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) announcements_last_7
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '15' DAY)) THEN 1 ELSE 0 END)) announcements_last_14
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) announcements_last_30
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '61' DAY)) THEN 1 ELSE 0 END)) announcements_last_60
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '8' DAY)) THEN comments ELSE 0 END)) announcement_comments_last_7
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '15' DAY)) THEN comments ELSE 0 END)) announcement_comments_last_14
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '31' DAY)) THEN comments ELSE 0 END)) announcement_comments_last_30
   , "sum"((CASE WHEN ("date"(a.createdat) > (current_date - INTERVAL  '61' DAY)) THEN comments ELSE 0 END)) announcement_comments_last_60
   , "date_diff"('day', "min"("date"(a.createdat)), current_date) announcement_days_since_first_announcement
   , "date_diff"('day', "max"("date"(a.createdat)), current_date) announcement_days_since_last_announcement
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '8' DAY)) THEN 1 ELSE 0 END)) announcements_first_7
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '15' DAY)) THEN 1 ELSE 0 END)) announcements_first_14
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '31' DAY)) THEN 1 ELSE 0 END)) announcements_first_30
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '61' DAY)) THEN 1 ELSE 0 END)) announcements_first_60
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '8' DAY)) THEN comments ELSE 0 END)) announcement_comments_first_7
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '15' DAY)) THEN comments ELSE 0 END)) announcement_comments_first_14
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '31' DAY)) THEN comments ELSE 0 END)) announcement_comments_first_30
   , "sum"((CASE WHEN (a.createdat < (u.createdat + INTERVAL  '61' DAY)) THEN comments ELSE 0 END)) announcement_comments_first_60
   FROM
     ((
      SELECT
        userid
      , classid
      , "date"(createdat) createdat
      , announcement_id
      , comments
      FROM
        announcements
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
