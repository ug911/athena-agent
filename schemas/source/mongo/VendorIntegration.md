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

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
