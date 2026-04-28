---
collection: "ClassroomCertificateConfig"
athena_table: "wise_app_backend__classroom_certificate_config"
mongo_field_count: 7
athena_field_count: 20
matched: 7
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `ClassroomCertificateConfig` ↔ `processed.wise_app_backend__classroom_certificate_config`

- **Mongo source**: [`src/models/ClassroomCertificateConfig.js`](../source/mongo/ClassroomCertificateConfig.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__classroom_certificate_config.md`](../processed/processed/wise_app_backend__classroom_certificate_config.md)
- **Coverage**: 7/7 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `templateid.$oid` | `string` | JSON path |
| `variables.[]` | `object` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
