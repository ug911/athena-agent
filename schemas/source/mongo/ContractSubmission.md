---
collection: "ContractSubmission"
model: "ContractSubmission"
source_file: "src/models/ContractSubmission.js"
field_count: 13
last_synced: "2026-04-28T10:58:23+00:00"
---

# `ContractSubmission` (Mongo collection)

- **Model**: `ContractSubmission`
- **Source**: [`src/models/ContractSubmission.js`](../../../src/models/ContractSubmission.js)
- **Athena counterpart**: try `processed.wise_app_backend__contract_submission` or `processed.wise_app_backend__contractsubmission` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ instituteId: 1, contractId: 1, userId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`contractSubmissionSchema`, `signeeDetailsSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `Institute` |  | required |  |  |
| `contractId` | `ObjectId` | `Contract` |  | required |  |  |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `answers` | `Array<answerSchema>` |  |  | required |  |  |
| `active` | `Boolean` |  |  |  | true |  |
| `signedByParent` | `Boolean` |  |  |  |  |  |
| `signedAt` | `Date` |  |  | required |  |  |
| `signedContractFile` | `attachmentSchema` |  |  | required |  |  |
| `signeeDetails` | `<signeeDetailsSchema>` |  |  | required |  |  |
| `signeeDetails.ip` | `String` |  |  |  |  |  |
| `signeeDetails.deviceName` | `String` |  |  |  |  |  |
| `signeeDetails.userId` | `ObjectId` | `user` |  | required |  |  |
| `signeeDetails.wiseUUID` | `String` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
