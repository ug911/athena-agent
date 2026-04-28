---
collection: "CertificateTemplate"
athena_table: "wise_app_backend__certificate_template"
mongo_field_count: 15
athena_field_count: 29
matched: 15
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `CertificateTemplate` ↔ `processed.wise_app_backend__certificate_template`

- **Mongo source**: [`src/models/CertificateTemplate.js`](../source/mongo/CertificateTemplate.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__certificate_template.md`](../processed/processed/wise_app_backend__certificate_template.md)
- **Coverage**: 15/15 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `variables.[]` | `object` | JSON path |
| `variables.[].charlimit.$numberint` | `string` | JSON path |
| `imagewidth.$numberint` | `string` | JSON path |
| `imageheight.$numberint` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
