---
collection: "verification"
athena_table: "wise_app_backend__verification"
mongo_field_count: 9
athena_field_count: 20
matched: 6
coverage_pct: 66.7
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `verification` ↔ `processed.wise_app_backend__verification`

- **Mongo source**: [`src/models/Verification.js`](../source/mongo/verification.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__verification.md`](../processed/processed/wise_app_backend__verification.md)
- **Coverage**: 6/9 Mongo fields are present in Athena (**66.7%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `identifier` | `String` |  | required |
| `idType` | `String` |  |  |
| `ip` | `String` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `phonenumber` | `string` | column |
| `_id.$oid` | `string` | JSON path |
| `attempts.$numberint` | `string` | JSON path |
| `resendcount.$numberint` | `string` | JSON path |
| `resendwindow.$date` | `object` | JSON path |
| `resendwindow.$date.$numberlong` | `string` | JSON path |
| `expirytime.$date` | `object` | JSON path |
| `expirytime.$date.$numberlong` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
