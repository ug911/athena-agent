---
collection: "ClassroomFee"
model: "ClassroomFee"
source_file: "src/models/ClassroomFee.js"
field_count: 10
last_synced: "2026-04-28T10:58:23+00:00"
---

# `ClassroomFee` (Mongo collection)

- **Model**: `ClassroomFee`
- **Source**: [`src/models/ClassroomFee.js`](../../../src/models/ClassroomFee.js)
- **Athena counterpart**: try `processed.wise_app_backend__classroom_fee` or `processed.wise_app_backend__classroomfee` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ classId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`ClassroomFeeSchema`, `paymentOptionsSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `classId` | `ObjectId` | `class` |  | required |  |  |
| `timezone` | `String` |  |  |  |  |  |
| `currency` | `String` |  | <ALLOWED_CURRENCIES> | required |  |  |
| `paymentOptions[]` | `<paymentOptionsSchema>` |  |  |  |  |  |
| `paymentOptions[].title` | `String` |  |  |  |  |  |
| `paymentOptions[].type` | `String` |  | <VALID_PAYMENT_OPTION_TYPES> | required |  |  |
| `paymentOptions[].installments` | `Array<<inline-schema>>` |  |  |  |  |  |
| `paymentOptions[].totalAmount` | `amountSchema` |  |  |  |  |  |
| `paymentOptions[].metadata` | `<inline-schema>` |  |  |  |  |  |
| `metadata` | `Object` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
