# Hand-curated joins

Verified during query authoring. Prefer these over the auto-extracted hints below.

| Left | Right | Notes |
| --- | --- | --- |
| `wise_app_backend__zoom.classid` (`$oid`) | `class.class_id` | One class → many sessions. |
| `wise_app_backend__zoom.userid` (`$oid`) | `user.userid` | Session **host** — may differ from class owner. |
| `wise_app_backend__zoom.metadata.ownerid` (`$oid`) | `user.userid` | Class owner snapshot at session creation. |
| `class.instituteid` | `institute.instituteid` | A class → one institute. |
| `class.namespace` | `institute.namespace` / `user.namespace` | Tenant identifier; one namespace → many institutes. |
| `liveclassinsight.sessionid` | `wise_app_backend__zoom._id` (`$oid`) | Session-insight reference (not yet validated by query — verify before relying on). |
| `wise_app_backend__raw_zoom_attendance.sessionid` (`$oid`) | `wise_app_backend__zoom._id` (`$oid`) | Per-segment join/leave events for a session. Many segments per session. |
| `wise_app_backend__raw_zoom_attendance.classid` (`$oid`) | `class.class_id` | |
| `wise_app_backend__raw_zoom_attendance.participants[]._id` | `user.userid` | Wise user id of the attendee (the segment's `user_id` field is Zoom-internal, not Wise). |
| `zoom_attendance.zoom_id` | `wise_app_backend__zoom._id` (`$oid`) | Already-extracted oid; one zoom_id → many rows (one per participant). |
| `zoom_attendance.class_id` | `class.class_id` | |
| `zoom_missed_attendance.class_id` | `class.class_id` | Missed sessions only. |

# Auto-extracted join clauses

_Mined from view DDLs. Each entry is a `LEFT = RIGHT` equality observed inside an `ON` clause, with the views in which it appears. Use as **hints**, not a contract — verify against the table's schema file before relying on them._

| Left | Right | Seen in |
| --- | --- | --- |
| `a.userid` | `u.userid` | `processed.features_user_teacher`, `processed.ft_teacher_announcements`, `processed.ft_teacher_assignments`, `processed.ft_teacher_class`, `processed.ft_teacher_study_materials` (+2 more) |
| `a.userid` | `b.userid` | `processed.upsc_live_classrooms`, `processed.upsc_live_teacher_private_class_stats`, `processed.upsc_live_teacher_public_class_stats`, `processed.user_features` |
| `a.class_id` | `ann.classid` | `processed.upsc_live_teacher_private_class_stats`, `processed.upsc_live_teacher_public_class_stats` |
| `a.class_id` | `ass.classid` | `processed.upsc_live_teacher_private_class_stats`, `processed.upsc_live_teacher_public_class_stats` |
| `a.class_id` | `tst.classid` | `processed.upsc_live_teacher_private_class_stats`, `processed.upsc_live_teacher_public_class_stats` |
| `a.class_id` | `zoom.classid` | `processed.upsc_live_teacher_private_class_stats`, `processed.upsc_live_teacher_public_class_stats` |
| `a.userid` | `c.userid` | `processed.user_features` |
| `a.userid` | `d.userid` | `processed.user_features` |
| `a.userid` | `e.userid` | `processed.user_features` |
| `a.userid` | `f.userid` | `processed.user_features` |
| `a.userid` | `h.userid` | `processed.user_features` |
| `a.userid` | `i.userid` | `processed.user_features` |
| `a.userid` | `j.userid` | `processed.user_features` |
| `a.userid` | `k.userid` | `processed.user_features` |
| `a.userid` | `l.userid` | `processed.user_features` |
| `a.userid` | `m.userid` | `processed.user_features` |
| `c.userid` | `u.userid` | `processed.features_user_teacher` |
| `d.userid` | `u.userid` | `processed.features_user_teacher` |
| `m._id` | `p._id` | `processed.liveclassinsight_details` |
| `s.userid` | `u.userid` | `processed.features_user_teacher` |
| `t.userid` | `u.userid` | `processed.features_user_teacher` |
| `u.userid` | `z.userid` | `processed.features_user_teacher` |
| `x.class_id` | `y.class_id` | `processed.ft_student_class` |
| `x.testid` | `y.testid` | `processed.tests` |