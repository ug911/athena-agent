---
collection: "UserStreamingInfo"
model: "UserStreamingInfo"
source_file: "src/models/UserUsageInfo.js"
field_count: 19
last_synced: "2026-04-28T10:58:23+00:00"
---

# `UserStreamingInfo` (Mongo collection)

- **Model**: `UserStreamingInfo`
- **Source**: [`src/models/UserUsageInfo.js`](../../../src/models/UserUsageInfo.js)
- **Athena counterpart**: try `processed.wise_app_backend__user_streaming_info` or `processed.wise_app_backend__userstreaminginfo` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ userId: 1 }, {unique: 1}]`
- `[{ userId: 1, "streamingUsage.date": 1 }, { unique: true }]`

## Local sub-schemas referenced

`UserUsageInfoSchema`, `communicationEntry`, `storageInfoSchema`, `streamingInfoSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `streamingUsage[]` | `<streamingInfoSchema>` |  |  |  | [] |  |
| `streamingUsage[].date` | `Date` |  |  | required |  |  |
| `streamingUsage[].remainingGBs` | `Number` |  |  | required |  |  |
| `streamingUsage[].consumedMBs` | `Number` |  |  | required |  |  |
| `streamingUsage[].uniqueStreamedVideos` | `Number` |  |  | required |  |  |
| `streamingUsage[].uniqueRequestIPs` | `Number` |  |  | required |  |  |
| `storageUsage[]` | `<storageInfoSchema>` |  |  |  | [] |  |
| `storageUsage[].date` | `Date` |  |  | required |  |  |
| `storageUsage[].remainingGBs` | `Number` |  |  | required |  |  |
| `storageUsage[].consumedGBs` | `Number` |  |  | required |  |  |
| `totalStreamedGBs` | `Number` |  |  | required | 0 |  |
| `communicationUsage[]` | `<communicationEntry>` |  |  |  | [] |  |
| `communicationUsage[].date` | `Date` |  |  | required |  |  |
| `communicationUsage[].whatsapp` | `Number` |  |  | required |  |  |
| `communicationUsage[].email` | `Number` |  |  | required |  |  |
| `communicationUsage[].creditsUsed` | `Number` |  |  | required |  |  |
| `communicationUsage[].creditsRemaining` | `Number` |  |  | required |  |  |
| `totalCreditsUsed` | `Number` |  |  | required | 0 |  |

## Usage (from backend-api)

_18 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 6
- `.findOneAndUpdate` × 6
- `.find` × 3
- `.updateOne` × 3

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `userId` × 1

### Top call sites

- `src/services/communications/commCreditService.js` × 4
- `src/services/premiumReminderService.js` × 3
- `src/services/premiumService.js` × 3
- `src/services/premiumStreamingService.js` × 3
- `src/services/premiumAnalyticsService.js` × 2
- `src/services/storageService.js` × 2
- `src/controllers/PremiumController.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
