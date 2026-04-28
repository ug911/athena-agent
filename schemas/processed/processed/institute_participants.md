---
database: processed
table: institute_participants
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:11:25+00:00'
sampled_rows: 0
---

# `processed.institute_participants`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `institute_participant_id` | `string` |  |
| `userid` | `string` |  |
| `instituteid` | `string` |  |
| `status` | `string` |  |
| `createdat` | `date` |  |
| `updatedat` | `date` |  |
| `joinedon` | `date` |  |
| `relation` | `string` |  |
| `additionalnote` | `string` |  |
| `tags` | `array<string>` |  |

## DDL

```sql
CREATE VIEW processed.institute_participants AS
SELECT
  CAST("json_extract"("_id", '$["$oid"]') AS varchar) institute_participant_id
, CAST("json_extract"("userid", '$["$oid"]') AS varchar) userid
, CAST("json_extract"("instituteid", '$["$oid"]') AS varchar) instituteid
, status
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) createdat
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(updatedat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) updatedat
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(joinedon, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) joinedon
, "relation"
, CAST("json_extract"("metadata", '$["additionalnote"]') AS VARCHAR) additionalnote
, CAST("json_extract"("metadata", '$["tags"]') AS ARRAY(VARCHAR)) tags
FROM
  "processed"."wise_app_backend__institute_participants"
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->

## Notes

- **Membership table.** One row per `(userid, instituteid, relation)`. A user enrolled in N institutes within the same tenant has N rows.
- **`relation` values**: `STUDENT`, `TEACHER`, `ADMIN`. For "students of a tenant" filter `relation = 'STUDENT'`.
- **`status` values**: `ACCEPTED` (active member), `REMOVED` (left / kicked), `REQUESTED` (pending join request). For active rosters use `status = 'ACCEPTED'`. For historical analysis include `REMOVED`.
- **Tenant scoping**: no `namespace` column. Join `instituteid → processed.institute.instituteid` to get `namespace` and the human-readable institute name.
- **Cross-institute users**: a student can join multiple institutes under the same namespace (common at large tenants like `leadiasacademy`). Aggregate carefully — `COUNT(DISTINCT userid)` per namespace ≠ `SUM(COUNT(DISTINCT userid))` per institute.
