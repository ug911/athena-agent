---
database: processed
table: class
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:10:17+00:00'
sampled_rows: 0
---

# `processed.class`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `class_id` | `string` |  |
| `instituteid` | `string` |  |
| `userid` | `string` |  |
| `settings_lockclassroom` | `string` |  |
| `settings_disablestudentcomments` | `string` |  |
| `settings_openclassroom` | `string` |  |
| `settings_lockafter` | `string` |  |
| `settings_disablestudentdiscussions` | `string` |  |
| `settings_disablewebsdk` | `string` |  |
| `createdat` | `date` |  |
| `namespace` | `string` |  |
| `zoom_join_url` | `string` |  |
| `num_joinedrequest` | `bigint` |  |
| `num_pendingadmins` | `bigint` |  |
| `num_pendingrequest` | `bigint` |  |
| `num_admins` | `bigint` |  |
| `num_coteacherrequests` | `bigint` |  |
| `num_coteachers` | `bigint` |  |
| `timing_selected` | `array<int>` |  |
| `occurrences` | `bigint` |  |
| `occurrence_durations` | `array<int>` |  |
| `classnumber` | `string` |  |
| `just_classnumber` | `string` |  |
| `archived` | `string` |  |
| `disablereminder` | `string` |  |
| `lockclassroom` | `string` |  |
| `subject` | `string` |  |
| `name` | `string` |  |
| `deletedstudents` | `array<string>` |  |
| `suspendedstudents` | `array<string>` |  |
| `joinedrequests` | `array<string>` |  |
| `admins` | `array<string>` |  |
| `pendingrequest` | `array<string>` |  |
| `pendingadmins` | `array<string>` |  |
| `coteacherrequests` | `array<string>` |  |
| `coteachers` | `array<string>` |  |

## DDL

```sql
CREATE VIEW processed.class AS
SELECT
  CAST("json_extract"(_id, '$["$oid"]') AS varchar) class_id
, CAST("json_extract"(instituteid, '$["$oid"]') AS varchar) instituteid
, CAST("json_extract"(userid, '$["$oid"]') AS varchar) userid
, CAST("json_extract"(settings, '$["lockclassroom"]') AS varchar) settings_lockclassroom
, CAST("json_extract"(settings, '$["disablestudentcomments"]') AS varchar) settings_disablestudentcomments
, CAST("json_extract"(settings, '$["openclassroom"]') AS varchar) settings_openclassroom
, CAST("json_extract"(settings, '$["lockafter"]["$numberint"]') AS varchar) settings_lockafter
, CAST("json_extract"(settings, '$["disablestudentdiscussions"]') AS varchar) settings_disablestudentdiscussions
, CAST("json_extract"(settings, '$["disablewebsdk"]') AS varchar) settings_disablewebsdk
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) createdat
, namespace
, CAST("json_extract"(zoomlink, '$["$join_url"]') AS varchar) zoom_join_url
, "cardinality"(CAST("json_parse"(joinedrequest) AS array(json))) num_joinedrequest
, "cardinality"(CAST("json_parse"(pendingadmins) AS array(json))) num_pendingadmins
, "cardinality"(CAST("json_parse"(pendingrequest) AS array(json))) num_pendingrequest
, "cardinality"(CAST("json_parse"(admins) AS array(json))) num_admins
, "cardinality"(CAST("json_parse"(coteacherrequests) AS array(json))) num_coteacherrequests
, "cardinality"(CAST("json_parse"(coteachers) AS array(json))) num_coteachers
, "transform"(CAST("json_parse"(timing) AS array(json)), (x) -> CAST("json_extract"(x, '$.selected') AS integer)) timing_selected
, "cardinality"(CAST("json_extract"("json_parse"(schedule), '$.occurrences') AS array(json))) occurrences
, "transform"(CAST("json_extract"("json_parse"(schedule), '$.occurrences') AS array(json)), (x) -> CAST("json_extract"(x, '$.duration["$numberint"]') AS integer)) occurrence_durations
, CAST("json_extract"(classnumber, '$["$numberint"]') AS varchar) classnumber
, CAST("json_extract"(classnumber, '$["$numberint"]') AS varchar) just_classnumber
, archived
, disablereminder
, lockclassroom
, subject
, name
, "transform"(CAST("json_parse"(deletedstudents) AS array(json)), (x) -> CAST("json_extract"(x, '$.userid["$oid"]') AS varchar)) deletedstudents
, "transform"(CAST("json_parse"(suspendedstudents) AS array(json)), (x) -> CAST("json_extract"(x, '$.userid["$oid"]') AS varchar)) suspendedstudents
, "transform"(CAST("json_parse"(joinedrequest) AS array(json)), (x) -> CAST("json_extract"(x, '$["$oid"]') AS varchar)) joinedrequests
, "transform"(CAST("json_parse"(admins) AS array(json)), (x) -> CAST("json_extract"(x, '$["$oid"]') AS varchar)) admins
, "transform"(CAST("json_parse"(pendingrequest) AS array(json)), (x) -> CAST("json_extract"(x, '$["$oid"]') AS varchar)) pendingrequest
, "transform"(CAST("json_parse"(pendingadmins) AS array(json)), (x) -> CAST("json_extract"(x, '$["$oid"]') AS varchar)) pendingadmins
, "transform"(CAST("json_parse"(coteacherrequests) AS array(json)), (x) -> CAST("json_extract"(x, '$["$oid"]') AS varchar)) coteacherrequests
, "transform"(CAST("json_parse"(coteachers) AS array(json)), (x) -> CAST("json_extract"(x, '$["$oid"]') AS varchar)) coteachers
FROM
  wise_app_backend__class
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->

## Notes

- **Tenant scoping.** `namespace` is the canonical tenant key. A single namespace can span multiple institutes — e.g. `leadiasacademy` covers institutes **Lead IAS**, **Lead Junior**, **Lead Junior Telugu**, **Lead IAS Junior Int'l**. Use `class.namespace` for tenant-level filters; use `class.instituteid` (→ `processed.institute`) when you need the specific institute name within a namespace.
- **`userid` is the class owner / primary teacher.** `admins` and `coteachers` arrays carry additional teachers. For per-session host, use `wise_app_backend__zoom.userid` instead — it can differ from the class owner when a co-teacher runs a particular session.
- **Linking to sessions.** `class.class_id = wise_app_backend__zoom.classid` (after extracting the `$oid` from zoom). One class has many sessions.
- **Vocabulary warning.** "Class" is overloaded internally — it can mean either the **recurring class entity** (this table) or a **single occurrence / live session** (a row in `wise_app_backend__zoom`). Always confirm which sense the user wants before writing SQL. The cue: if the question involves a specific time/instance, attendance, or duration, they almost certainly mean a session; if it's about enrollment, schedule, or ownership, they mean the class entity.
