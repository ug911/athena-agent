---
collection: "ClassroomCertificate"
model: "ClassroomCertificate"
source_file: "src/models/ClassroomCertificate.js"
field_count: 5
last_synced: "2026-04-28T10:58:23+00:00"
---

# `ClassroomCertificate` (Mongo collection)

- **Model**: `ClassroomCertificate`
- **Source**: [`src/models/ClassroomCertificate.js`](../../../src/models/ClassroomCertificate.js)
- **Athena counterpart**: try `processed.wise_app_backend__classroom_certificate` or `processed.wise_app_backend__classroomcertificate` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ certificateConfigId: 1 }]`
- `[{ userId: 1, certificateConfigId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`ClassroomCertificateSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `classId` | `ObjectId` | `class` |  | required |  |  |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `certificateConfigId` | `ObjectId` | `ClassroomCertificateConfig` |  | required |  |  |
| `randomToken` | `String` |  |  |  | () => hexadecimal(8) |  |
| `archived` | `Boolean` |  |  |  | false |  |

## Usage (from backend-api)

_9 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.find` × 3
- `.findOne` × 2
- `.updateMany` × 1
- `.exists` × 1
- `.deleteOne` × 1
- `.findOneAndUpdate` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `certificateConfigId` × 1

### Top call sites

- `src/controllers/TeacherController.js` × 3
- `src/services/classroomCertificateService.js` × 2
- `src/controllers/StudentController.js` × 1
- `src/controllers/UserController.js` × 1
- `src/controllers/PublicController.js` × 1
- `src/services/studentReportsServiceV2.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
