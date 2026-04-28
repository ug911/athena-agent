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

## Usage (from backend-api)

_44 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 18
- `.findOneAndUpdate` × 6
- `.find` × 5
- `.create` × 4
- `.updateOne` × 4
- `.exists` × 3
- `.aggregate` × 2
- `.updateMany` × 1
- `.findById` × 1

### Top call sites

- `src/services/premiumService.js` × 15
- `src/controllers/DevAPIController.js` × 8
- `src/services/communications/commCreditService.js` × 6
- `src/controllers/PremiumController.js` × 4
- `src/services/premiumStreamingService.js` × 4
- `src/services/dataCheckService.js` × 3
- `src/controllers/InternalController.js` × 1
- `src/services/storageService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
