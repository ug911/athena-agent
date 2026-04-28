---
collection: "InstitutePublicProfile"
athena_table: "wise_app_backend__institute_public_profile"
mongo_field_count: 17
athena_field_count: 50
matched: 17
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `InstitutePublicProfile` ↔ `processed.wise_app_backend__institute_public_profile`

- **Mongo source**: [`src/models/InstitutePublicProfile.js`](../source/mongo/InstitutePublicProfile.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__institute_public_profile.md`](../processed/processed/wise_app_backend__institute_public_profile.md)
- **Coverage**: 17/17 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `instituteid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `institutecovers.[]` | `object` | JSON path |
| `institutecovers.[].link` | `string` | JSON path |
| `institutecovers.[].type` | `string` | JSON path |
| `publishedat.$date` | `object` | JSON path |
| `publishedat.$date.$numberlong` | `string` | JSON path |
| `sections.[]` | `object` | JSON path |
| `sections.[]._id` | `object` | JSON path |
| `sections.[]._id.$oid` | `string` | JSON path |
| `sections.[].classids.[].classids[].$oid` | `string` | JSON path |
| `sections.[].courseids` | `array<object>|array<unknown>` | JSON path |
| `sections.[].courseids.[].courseids[]` | `object` | JSON path |
| `sections.[].courseids.[].courseids[].$oid` | `string` | JSON path |
| `socialprofile.email` | `string` | JSON path |
| `socialprofile.facebook` | `string` | JSON path |
| `socialprofile.instagram` | `string` | JSON path |
| `socialprofile.linkedin` | `string` | JSON path |
| `socialprofile.twitter` | `string` | JSON path |
| `socialprofile.website` | `string` | JSON path |
| `socialprofile.whatsapp` | `string` | JSON path |
| `socialprofile.youtube` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `subdomaincreated.$numberint` | `string` | JSON path |
