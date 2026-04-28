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

## Usage (from backend-api)

_37 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 22
- `.deleteOne` × 4
- `.find` × 3
- `.exists` × 2
- `.create` × 2
- `.aggregate` × 2
- `.findOneAndUpdate` × 1
- `.updateOne` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `classId` × 1

### Top call sites

- `src/services/feeService.js` × 14
- `src/controllers/FeeCollectionV2Controller.js` × 7
- `src/services/instituteService.js` × 3
- `src/controllers/PublicController.js` × 2
- `src/services/instituteAdmissionService.js` × 2
- `src/controllers/StudentController.js` × 1
- `src/controllers/UserController.js` × 1
- `src/controllers/InstituteController.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
