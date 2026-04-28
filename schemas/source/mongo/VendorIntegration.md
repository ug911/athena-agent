---
collection: "VendorIntegration"
model: "VendorIntegration"
source_file: "src/models/ClientIntegration.js"
field_count: 5
last_synced: "2026-04-28T10:58:23+00:00"
---

# `VendorIntegration` (Mongo collection)

- **Model**: `VendorIntegration`
- **Source**: [`src/models/ClientIntegration.js`](../../../src/models/ClientIntegration.js)
- **Athena counterpart**: try `processed.wise_app_backend__vendor_integration` or `processed.wise_app_backend__vendorintegration` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ userId: 1, integrationType: 1 }]`
- `[{ whitelabelNamespace: 1, integrationType: 1 }]`

## Local sub-schemas referenced

`clientIntegrationSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `userId` | `ObjectId` | `user` |  |  |  |  |
| `whitelabelNamespace` | `String` |  |  |  |  |  |
| `integrationType` | `String` |  | <ALL_INTEGRATION_TYPES> | required |  |  |
| `settings` | `Object` |  |  | required |  |  |
| `enabled` | `Boolean` |  |  |  | true |  |

## Usage (from backend-api)

_15 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 5
- `.deleteOne` × 2
- `.updateOne` × 2
- `.find` × 2
- `.findOneAndUpdate` × 2
- `.deleteMany` × 1
- `.create` × 1

### Top call sites

- `src/controllers/InstituteController.js` × 3
- `src/services/PencilSpacesIntegrationService.js` × 2
- `src/services/GoogleDriveIntegrationService.js` × 2
- `src/services/LessonSpaceIntegrationService.js` × 2
- `src/services/clientIntegrations/portalLoginService.js` × 2
- `src/controllers/UserController.js` × 1
- `src/services/loginService.js` × 1
- `src/services/youtubeAuthService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
