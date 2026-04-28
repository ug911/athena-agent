---
collection: "PremiumOrder"
model: "PremiumOrder"
source_file: "src/models/PremiumOrder.js"
field_count: 21
last_synced: "2026-04-28T10:58:23+00:00"
---

# `PremiumOrder` (Mongo collection)

- **Model**: `PremiumOrder`
- **Source**: [`src/models/PremiumOrder.js`](../../../src/models/PremiumOrder.js)
- **Athena counterpart**: try `processed.wise_app_backend__premium_order` or `processed.wise_app_backend__premiumorder` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ userId: 1 }, {}]`
- `[{ type: 1 }, {}]`
- `[{ startsFrom: 1 }, {}]`
- `[{ renewsOn: 1 }, {}]`

## Local sub-schemas referenced

`PremiumOrderSchema`, `planMetadataSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `planDisplayName` | `String` |  |  |  |  |  |
| `planDescription` | `String` |  |  |  |  |  |
| `startsFrom` | `Date` |  |  | required |  |  |
| `renewsOn` | `Date` |  |  | required |  |  |
| `amount` | `amountSchema` |  |  |  |  |  |
| `metadata` | `Object` |  |  |  |  |  |
| `status` | `String` |  | STATUS_CREATED, STATUS_ACTIVE, STATUS_CANCELLED |  | STATUS_CREATED |  |
| `type` | `String` |  | <ALL_PREMIUM_TYPES> |  | TYPE_LICENSE |  |
| `billingPeriod` | `String` |  | PLAN_TYPE_MONTHLY, PLAN_TYPE_ANNUAL |  | PLAN_TYPE_MONTHLY |  |
| `streamingGBs` | `Number` |  |  |  |  |  |
| `storageGBs` | `Number` |  |  |  |  |  |
| `commsCredits` | `Number` |  |  |  |  |  |
| `premiumPlanType` | `String` |  | <ALL_PREMIUM_PLAN_TYPES> |  |  |  |
| `planMetadata` | `<planMetadataSchema>` |  |  |  | {} |  |
| `planMetadata.baseAmount` | `amountSchema` |  |  |  |  |  |
| `planMetadata.domesticTransactionFee` | `Number` |  |  |  |  |  |
| `planMetadata.internationalTransactionFee` | `Number` |  |  |  |  |  |
| `planMetadata.storageGBs` | `Number` |  |  |  |  |  |
| `planMetadata.unitCount` | `Number` |  |  |  |  |  |
| `planMetadata.unitAmount` | `amountSchema` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
