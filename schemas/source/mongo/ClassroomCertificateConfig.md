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

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
