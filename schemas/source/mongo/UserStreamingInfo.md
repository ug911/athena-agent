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

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
