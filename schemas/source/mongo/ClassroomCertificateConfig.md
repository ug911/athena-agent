---
collection: "ClassroomCertificateConfig"
model: "ClassroomCertificateConfig"
source_file: "src/models/ClassroomCertificateConfig.js"
field_count: 7
last_synced: "2026-04-28T10:58:23+00:00"
---

# `ClassroomCertificateConfig` (Mongo collection)

- **Model**: `ClassroomCertificateConfig`
- **Source**: [`src/models/ClassroomCertificateConfig.js`](../../../src/models/ClassroomCertificateConfig.js)
- **Athena counterpart**: try `processed.wise_app_backend__classroom_certificate_config` or `processed.wise_app_backend__classroomcertificateconfig` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ classId: 1 }]`

## Local sub-schemas referenced

`ClassroomCertificateConfigSchema`, `certificateVariableSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `classId` | `ObjectId` | `class` |  | required |  |  |
| `templateId` | `ObjectId` | `CertificateTemplate` |  | required |  |  |
| `variables[]` | `<certificateVariableSchema>` |  |  |  |  |  |
| `variables[].name` | `String` |  |  | required |  |  |
| `variables[].value` | `String` |  |  | required |  |  |
| `variables[].style` | `String` |  |  |  |  |  |
| `archived` | `Boolean` |  |  |  | false |  |

## Usage (from backend-api)

_8 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.find` × 2
- `.findOne` × 2
- `.exists` × 1
- `.updateOne` × 1
- `.findOneAndUpdate` × 1
- `.create` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `templateId` × 2

### Top call sites

- `src/controllers/TeacherController.js` × 3
- `src/services/classroomCertificateService.js` × 3
- `src/controllers/UserController.js` × 1
- `src/controllers/PublicController.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
