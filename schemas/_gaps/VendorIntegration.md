---
collection: "VendorIntegration"
athena_table: "wise_app_backend__vendorintegration"
mongo_field_count: 5
athena_field_count: 49
matched: 4
coverage_pct: 80.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `VendorIntegration` ↔ `processed.wise_app_backend__vendorintegration`

- **Mongo source**: [`src/models/ClientIntegration.js`](../source/mongo/VendorIntegration.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__vendorintegration.md`](../processed/processed/wise_app_backend__vendorintegration.md)
- **Coverage**: 4/5 Mongo fields are present in Athena (**80.0%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `whitelabelNamespace` | `String` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `settings.apikey` | `string` | JSON path |
| `settings.apiurl` | `string` | JSON path |
| `settings.displayname` | `string` | JSON path |
| `settings.email` | `string` | JSON path |
| `settings.logintype` | `string` | JSON path |
| `settings.method` | `string` | JSON path |
| `settings.portalfallbackurl` | `string` | JSON path |
| `settings.portalloginurl` | `string` | JSON path |
| `settings.refreshtoken` | `string` | JSON path |
| `settings.responsekey` | `string` | JSON path |
| `settings.targetrole` | `string` | JSON path |
| `settings.templatemapping` | `object` | JSON path |
| `settings.templatemapping.certificatecreation` | `string` | JSON path |
| `settings.templatemapping.dailysessionreminder` | `string` | JSON path |
| `settings.templatemapping.discussioncreated` | `string` | JSON path |
| `settings.templatemapping.feeadded` | `string` | JSON path |
| `settings.templatemapping.feeaddedautocharge` | `string` | JSON path |
| `settings.templatemapping.feedue` | `string` | JSON path |
| `settings.templatemapping.feeoverdue` | `string` | JSON path |
| `settings.templatemapping.feepaid` | `string` | JSON path |
| `settings.templatemapping.instructoraddedtoclassroom` | `string` | JSON path |
| `settings.templatemapping.learneraddedtoclassroom` | `string` | JSON path |
| `settings.templatemapping.phoneotp` | `string` | JSON path |
| `settings.templatemapping.sessioncreditupdates` | `string` | JSON path |
| `settings.templatemapping.sessionfeedback` | `string` | JSON path |
| `settings.templatemapping.sessionfeedbackwithquiz` | `string` | JSON path |
| `settings.templatemapping.sessionnotstartedadminreminder` | `string` | JSON path |
| `settings.templatemapping.sessionnotstartedteacherreminder` | `string` | JSON path |
| `settings.templatemapping.sessionreminder_10` | `string` | JSON path |
| `settings.templatemapping.sessionreminder_1440` | `string` | JSON path |
| `settings.templatemapping.sessionreminder_2160` | `string` | JSON path |
| `settings.templatemapping.sessionreminder_60` | `string` | JSON path |
| `settings.templatemapping.sessionstarted` | `string` | JSON path |
| `settings.templatemapping.sessionupdated` | `string` | JSON path |
| `settings.templatemapping.wisestudentinvite` | `string` | JSON path |
| `settings.templatemapping.wiseteacherinvite` | `string` | JSON path |
