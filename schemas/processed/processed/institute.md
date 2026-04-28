---
database: processed
table: institute
type: view
layer: processed
location: null
format: null
partition_keys: []
last_synced: '2026-04-28T07:11:21+00:00'
sampled_rows: 0
---

# `processed.institute`

## Columns

| Column | Type | Notes |
| --- | --- | --- |
| `instituteid` | `string` |  |
| `ownerid` | `string` |  |
| `name` | `string` |  |
| `namespace` | `string` |  |
| `createdat` | `date` |  |
| `updatedat` | `date` |  |
| `settings` | `string` |  |
| `metadata` | `string` |  |

## DDL

```sql
CREATE VIEW processed.institute AS
SELECT
  CAST("json_extract"("_id", '$["$oid"]') AS varchar) instituteid
, CAST("json_extract"("ownerid", '$["$oid"]') AS varchar) ownerid
, name
, namespace
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(createdat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) createdat
, "date"("from_unixtime"(TRY_CAST("substr"(TRY_CAST("json_extract"(updatedat, '$["$date"]["$numberlong"]') AS varchar), 1, 10) AS double))) updatedat
, "settings"
, "metadata"
FROM
  "processed"."wise_app_backend__institute"
```

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas, example filters) below this line. -->

## Notes

- **Multiple institutes per namespace.** `namespace` is the tenant key (shared with `class.namespace`, `user.namespace`); `instituteid` is the specific institute id within that tenant. e.g. `namespace = 'leadiasacademy'` resolves to **six** institutes: Lead Junior, Lead IAS, Lead Junior Telugu, Lead IAS Junior Int'l, Training and Development, Junior Delhi. Don't assume the institute list is small or static — always derive it from `processed.institute` for the namespace at query time.
- **Join to sessions.** `class.instituteid = institute.instituteid` — institute is reached via `class`, not directly from zoom.
