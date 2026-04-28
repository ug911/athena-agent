---
collection: "InstituteParticipant"
model: "InstituteParticipant"
source_file: "src/models/InstituteParticipant.js"
field_count: 16
last_synced: "2026-04-28T10:58:23+00:00"
---

# `InstituteParticipant` (Mongo collection)

- **Model**: `InstituteParticipant`
- **Source**: [`src/models/InstituteParticipant.js`](../../../src/models/InstituteParticipant.js)
- **Athena counterpart**: try `processed.wise_app_backend__institute_participant` or `processed.wise_app_backend__instituteparticipant` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ instituteId: 1, userId: 1 }, { unique: true }]`
- `[{ instituteId: 1, joinedOn: -1 }]`

## Local sub-schemas referenced

`instituteParticipantSchema`, `linkedDevicesSchema`, `metadataSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `instituteId` | `ObjectId` | `Institute` |  | required |  |  |
| `relation` | `String` |  | RELATION_STUDENT, RELATION_TEACHER, RELATION_ADMIN | required |  |  |
| `status` | `String` |  | STATUS_REQUESTED, STATUS_ACCEPTED, STATUS_INVITED, STATUS… | required |  |  |
| `joinedOn` | `Date` |  |  |  |  |  |
| `linkedDevices[]` | `<linkedDevicesSchema>` |  |  |  |  |  |
| `linkedDevices[].deviceId` | `String` |  |  | required |  |  |
| `linkedDevices[].deviceName` | `String` |  |  |  |  |  |
| `metadata` | `<metadataSchema>` |  |  |  |  |  |
| `metadata.tags` | `Array<String>` |  |  |  | undefined |  |
| `metadata.instituteManager` | `Boolean` |  |  |  |  |  |
| `metadata.additionalNote` | `String` |  |  |  |  |  |
| `metadata.autoCharge` | `Boolean` |  |  |  |  |  |
| `metadata.taxDisabled` | `Boolean` |  |  |  |  |  |
| `metadata.invoiceBillingInformation` | `String` |  |  |  |  |  |
| `metadata.payoutSettings` | `String` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
