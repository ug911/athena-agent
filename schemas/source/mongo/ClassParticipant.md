---
collection: "ClassParticipant"
model: "ClassParticipant"
source_file: "src/models/ClassParticipant.js"
field_count: 10
last_synced: "2026-04-28T10:58:23+00:00"
---

# `ClassParticipant` (Mongo collection)

- **Model**: `ClassParticipant`
- **Source**: [`src/models/ClassParticipant.js`](../../../src/models/ClassParticipant.js)
- **Athena counterpart**: try `processed.wise_app_backend__class_participant` or `processed.wise_app_backend__classparticipant` — verify in `schemas/INDEX.md`.

## Local sub-schemas referenced

`ClassParticipantSchema`, `metadataSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `classId` | `ObjectId` | `class` |  | required |  |  |
| `relation` | `String` |  | RELATION_STUDENT, RELATION_ADMIN, RELATION_COTEACHER | required |  |  |
| `status` | `String` |  | STATUS_REQUESTED, STATUS_INVITED, STATUS_ACCEPTED, STATUS… | required |  |  |
| `joinedOn` | `Date` |  |  |  | (doc) => doc?.status == STATUS_ACCEPT… |  |
| `metadata` | `<metadataSchema>` |  |  |  | {} |  |
| `metadata.paymentOptionId` | `String` |  |  |  |  |  |
| `metadata.settleDues` | `Boolean` |  |  |  |  |  |
| `metadata.feesWaived` | `Boolean` |  |  |  |  |  |
| `metadata.payoutSettings` | `String` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
