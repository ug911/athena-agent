---
collection: "VendorConfiguration"
model: "VendorConfiguration"
source_file: "src/models/VendorConfiguration.js"
field_count: 19
last_synced: "2026-04-28T10:58:23+00:00"
---

# `VendorConfiguration` (Mongo collection)

- **Model**: `VendorConfiguration`
- **Source**: [`src/models/VendorConfiguration.js`](../../../src/models/VendorConfiguration.js)
- **Athena counterpart**: try `processed.wise_app_backend__vendor_configuration` or `processed.wise_app_backend__vendorconfiguration` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ userId: 1 }, {unique: 1}]`

## Local sub-schemas referenced

`apiAccessSchema`, `s3ConfigurationSchema`, `vendorConfigurationSchema`, `webhookSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `webhooks[]` | `<webhookSchema>` |  |  |  | [] |  |
| `webhooks[].enabled` | `Boolean` |  |  |  | true |  |
| `webhooks[].name` | `String` |  |  |  | 'Webhook Subscription' |  |
| `webhooks[].method` | `String` |  | POST | required | 'POST' |  |
| `webhooks[].auth` | `String` |  |  |  |  |  |
| `webhooks[].url` | `String` |  |  | required |  |  |
| `webhooks[].events` | `Array<String>` |  |  | required |  |  |
| `apiAccess` | `<apiAccessSchema>` |  |  |  |  |  |
| `apiAccess.enabled` | `Boolean` |  |  |  | false |  |
| `apiAccess.apiKeys` | `Array<String>` |  |  |  |  |  |
| `s3Configuration` | `<s3ConfigurationSchema>` |  |  |  |  |  |
| `s3Configuration.enabled` | `Boolean` |  |  |  | false |  |
| `s3Configuration.accessKeyId` | `String` |  |  | required |  |  |
| `s3Configuration.secretAccessKey` | `String` |  |  | required |  |  |
| `s3Configuration.region` | `String` |  |  |  |  |  |
| `s3Configuration.bucketName` | `String` |  |  | required |  |  |
| `s3Configuration.pathPrefix` | `String` |  |  | required |  |  |
| `s3Configuration.aclConfig` | `Object` |  |  |  | {} |  |

## Usage (from backend-api)

_15 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 7
- `.updateOne` × 6
- `.findOneAndUpdate` × 1
- `.create` × 1

### Top call sites

- `src/controllers/InstituteController.js` × 8
- `src/controllers/UserController.js` × 4
- `src/services/VendorWebhookService.js` × 1
- `src/services/developerActions.js` × 1
- `src/services/userAuthService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
