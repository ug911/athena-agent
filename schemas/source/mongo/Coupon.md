---
collection: "Coupon"
model: "Coupon"
source_file: "src/models/Coupon.js"
field_count: 17
last_synced: "2026-04-28T10:58:23+00:00"
---

# `Coupon` (Mongo collection)

- **Model**: `Coupon`
- **Source**: [`src/models/Coupon.js`](../../../src/models/Coupon.js)
- **Athena counterpart**: try `processed.wise_app_backend__coupon` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ couponCode: 1, 'target.instituteId': 1 }, { unique: true }]`
- `[{ 'target.instituteId': 1, createdAt: 1 }, {}]`

## Local sub-schemas referenced

`couponSchema`, `discountSchema`, `targetSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `active` | `Boolean` |  |  |  | true |  |
| `startsFrom` | `Date` |  |  |  | Date.now |  |
| `expiresAt` | `Date` |  |  |  |  |  |
| `description` | `String` |  |  | required |  |  |
| `couponCode` | `String` |  |  | required | function () { return Math.random().to… |  |
| `discount` | `<discountSchema>` |  |  | required |  |  |
| `discount.type` | `String` |  | <VALID_DISCOUNT_TYPES> | required |  |  |
| `discount.value` | `Number` |  |  | required |  |  |
| `discount.currency` | `String` |  | <ALLOWED_CURRENCIES> |  |  |  |
| `discount.maxValue` | `Number` |  |  |  |  |  |
| `couponType` | `String` |  | <VALID_COUPON_TYPES> | required |  |  |
| `perUserCountLimit` | `Number` |  |  |  |  |  |
| `totalCountLimit` | `Number` |  |  |  |  |  |
| `target` | `<targetSchema>` |  |  |  |  |  |
| `target.type` | `String` |  | <VALID_TARGET_TYPES> | required | TARGET_TYPE_INSTITUTE |  |
| `target.instituteId` | `ObjectId` | `Institute` |  |  |  |  |
| `target.classroomsToSkip` | `Array<ObjectId>` | `class` |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
