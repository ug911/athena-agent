---
collection: "transaction"
model: "transaction"
source_file: "src/models/Transaction.js"
field_count: 17
last_synced: "2026-04-28T10:58:23+00:00"
---

# `transaction` (Mongo collection)

- **Model**: `transaction`
- **Source**: [`src/models/Transaction.js`](../../../src/models/Transaction.js)
- **Athena counterpart**: try `processed.wise_app_backend__transaction` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ status: 1 }, {}]`
- `[{ type: 1 }, {}]`
- `[{ senderId: 1 }, {}]`
- `[{ receiverId: 1 }, {}]`
- `[{ createdAt: 1 }, {}]`
- `[{ 'metadata.classId': 1 }, {}]`
- `[{ 'metadata.paymentTransactionId': 1 }, {}]`
- `[{ 'metadata.dueOn': 1 }, {}]`
- `[{ 'metadata.chargeOn': 1 }, {}]`
- `[{ 'metadata.couponId': 1 }, { sparse: true }]`

## Local sub-schemas referenced

`lineItemSchema`, `taxLineItemSchema`, `transactionSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `senderId` | `ObjectId` | `user` |  | required |  |  |
| `receiverId` | `ObjectId` | `user` |  | required |  |  |
| `type` | `String` |  | <VALID_TXN_TYPES> |  |  |  |
| `transactionType` | `String` |  | <VALID_TRANSACTION_TYPES> |  |  |  |
| `status` | `String` |  | <VALID_TXN_STATUSES> |  |  |  |
| `amount` | `amountSchema` |  |  |  |  |  |
| `lineItems[]` | `<lineItemSchema>` |  |  |  | undefined |  |
| `lineItems[].amount` | `amountSchema` |  |  |  |  |  |
| `lineItems[].metadata` | `<inline-schema>` |  |  |  |  |  |
| `lineItems[].note` | `String` |  |  |  |  |  |
| `preTaxAmount` | `amountSchema` |  |  |  |  |  |
| `taxLineItems[]` | `<taxLineItemSchema>` |  |  |  | undefined |  |
| `taxLineItems[].description` | `String` |  |  |  |  |  |
| `taxLineItems[].amount` | `amountSchema` |  |  |  |  |  |
| `note` | `String` |  |  |  |  |  |
| `chargedAt` | `Date` |  |  |  |  |  |
| `metadata` | `Object` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
