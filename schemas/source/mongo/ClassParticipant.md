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

## Usage (from backend-api)

_77 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.find` × 27
- `.findOne` × 19
- `.updateOne` × 10
- `.aggregate` × 7
- `.exists` × 6
- `.deleteMany` × 3
- `.countDocuments` × 2
- `.deleteOne` × 1
- `.updateMany` × 1
- `.bulkWrite` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `userId` × 17
- `classId` × 2

### Top call sites

- `src/services/feeService.js` × 11
- `src/controllers/InstituteController.js` × 7
- `src/services/classroomService.js` × 7
- `src/controllers/FeeCollectionV2Controller.js` × 5
- `src/services/classroomAdmissionService.js` × 5
- `src/controllers/UserController.js` × 4
- `src/workers/dataTransferWorker.js` × 4
- `src/controllers/TeacherController.js` × 3

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
