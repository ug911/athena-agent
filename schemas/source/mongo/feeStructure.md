---
collection: "feeStructure"
model: "feeStructure"
source_file: "src/models/FeeStructure.js"
field_count: 7
last_synced: "2026-04-28T10:58:23+00:00"
---

# `feeStructure` (Mongo collection)

- **Model**: `feeStructure`
- **Source**: [`src/models/FeeStructure.js`](../../../src/models/FeeStructure.js)
- **Athena counterpart**: try `processed.wise_app_backend__fee_structure` or `processed.wise_app_backend__feestructure` — verify in `schemas/INDEX.md`.

## Local sub-schemas referenced

`feeStructureSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `classId` | `ObjectId` | `class` |  | required |  |  |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `type` | `String` |  | TYPE_ONE_TIME, TYPE_RECURRING |  |  |  |
| `amount` | `amountSchema` |  |  |  |  |  |
| `startDate` | `Date` |  |  |  |  |  |
| `endDate` | `Date` |  |  |  |  |  |
| `active` | `Boolean` |  |  |  | true |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
