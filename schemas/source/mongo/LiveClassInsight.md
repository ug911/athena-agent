---
collection: "LiveClassInsight"
model: "LiveClassInsight"
source_file: "src/models/LiveClassInsight.js"
field_count: 66
last_synced: "2026-04-28T10:58:23+00:00"
---

# `LiveClassInsight` (Mongo collection)

- **Model**: `LiveClassInsight`
- **Source**: [`src/models/LiveClassInsight.js`](../../../src/models/LiveClassInsight.js)
- **Athena counterpart**: try `processed.wise_app_backend__live_class_insight` or `processed.wise_app_backend__liveclassinsight` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ classId: 1 }]`
- `[{ meetingUUID: 1 }, { unique: true }]`
- `[{ meetingId: 1 }, {}]`
- `[{ endTime: 1 }, {}]`
- `[{ sessionId: 1 }, {}]`
- `[{ "metadata.parentMeetingUUID": 1 }, { sparse: true }]`

## Local sub-schemas referenced

`InMeetingAgendaSchema`, `LiveClassInsightSchema`, `MetadataSchema`, `ParticipantSchema`, `PluginSchema`, `PostMeetingAgendaSchema`, `TempDataSchema`, `TempUserSchema`, `trendSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `meetingUUID` | `String` |  |  | required |  |  |
| `meetingId` | `String` |  |  | required |  |  |
| `meetingStartedWebhookReceivedAt` | `Date` |  |  |  |  |  |
| `hostLensRegisteredAt` | `Date` |  |  |  |  |  |
| `sessionId` | `ObjectId` | `zoom` |  | required |  |  |
| `meetingPassword` | `String` |  |  | required |  |  |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `classId` | `ObjectId` | `class` |  |  |  |  |
| `startTime` | `Date` |  |  | required |  |  |
| `endTime` | `Date` |  |  |  |  |  |
| `participants[]` | `<ParticipantSchema>` |  |  |  |  |  |
| `participants[].userId` | `String` |  |  |  |  |  |
| `participants[].type` | `String` |  | <ALLOWED_PARTICIPANT_TYPES> |  | PARTICIPANT_TYPE_GUEST |  |
| `participants[].clientUserId` | `String` |  |  |  |  |  |
| `participants[].name` | `String` |  |  | required |  |  |
| `participants[].speakingDuration` | `Number` |  |  | required |  |  |
| `participants[].attentiveDuration` | `Number` |  |  | required |  |  |
| `participants[].attendanceDuration` | `Number` |  |  | required |  |  |
| `participants[].videoOnDuration` | `Number` |  |  | required |  |  |
| `participants[].platform` | `String` |  | WINDOWS, MAC, WEB, ANDROID, IOS, CHROMEBOOK, UNKNOWN |  |  |  |
| `participants[].firstEntryTime` | `Date` |  |  |  |  |  |
| `participants[].lastExitTime` | `Date` |  |  |  |  |  |
| `agendas[]` | `<PostMeetingAgendaSchema>` |  |  |  |  |  |
| `agendas[].title` | `String` |  |  |  |  |  |
| `agendas[].description` | `String` |  |  |  |  |  |
| `agendas[].tags` | `Array` |  |  |  |  |  |
| `agendas[].visibleTags` | `Array` |  |  |  |  |  |
| `agendas[].agendaItems` | `Array<<inline-schema>>` |  |  |  |  |  |
| `tempData` | `<TempDataSchema>` |  |  |  |  |  |
| `tempData.participants[]` | `<TempUserSchema>` |  |  |  |  |  |
| `tempData.participants[].userId` | `String` |  |  | required |  |  |
| `tempData.participants[].type` | `String` |  | <ALLOWED_PARTICIPANT_TYPES> | required |  |  |
| `tempData.participants[].clientUserId` | `String` |  |  |  |  |  |
| `tempData.participants[].platform` | `String` |  | WINDOWS, MAC, WEB, ANDROID, IOS, CHROMEBOOK, UNKNOWN |  |  |  |
| `tempData.participants[].name` | `String` |  |  |  |  |  |
| `tempData.participants[].left` | `Boolean` |  |  |  | false |  |
| `tempData.participants[].socketIds` | `Array` |  |  |  |  |  |
| `tempData.participants[].lastConnectedAt` | `Date` |  |  |  |  |  |
| `tempData.participants[].lastDisconnectedAt` | `Date` |  |  |  |  |  |
| `tempData.participants[].wiseUUID` | `String` |  |  |  |  |  |
| `tempData.participants[].firstEntryTime` | `Date` |  |  |  |  |  |
| `tempData.participants[].lastExitTime` | `Date` |  |  |  |  |  |
| `tempData.leaderboardConfig` | `LeaderboardConfigSchema` |  |  |  |  |  |
| `tempData.discussionConfig` | `DiscussionConfigSchema` |  |  |  |  |  |
| `tempData.allowStudentTalkTime` | `Boolean` |  |  |  | false |  |
| `tempData.agendas[]` | `<InMeetingAgendaSchema>` |  |  |  |  |  |
| `tempData.agendas[].title` | `String` |  |  |  |  |  |
| `tempData.agendas[].description` | `String` |  |  |  |  |  |
| `tempData.agendas[].tags` | `Array` |  |  |  |  |  |
| `tempData.agendas[].visibleTags` | `Array` |  |  |  |  |  |
| `tempData.agendas[].lastLaunchedAt` | `Date` |  |  |  |  |  |
| `tempData.agendas[].agendaItems` | `Array<<inline-schema>>` |  |  |  |  |  |
| `metadata` | `<MetadataSchema>` |  |  |  |  |  |
| `metadata.loginRequired` | `Boolean` |  |  |  |  |  |
| `metadata.registrationRequired` | `Boolean` |  |  |  |  |  |
| `metadata.parentMeetingUUID` | `String` |  |  |  |  |  |
| `metadata.ownerId` | `String` |  |  |  |  |  |
| `metadata.pollsMigrated` | `Boolean` |  |  |  |  |  |
| `metadata.ratingsMigrated` | `Boolean` |  |  |  |  |  |
| `trend[]` | `<trendSchema>` |  |  |  |  |  |
| `trend[].windowStartTime` | `Date` |  |  |  |  |  |
| `trend[].attentiveCount` | `Number` |  |  |  |  |  |
| `trend[].totalParticipantCount` | `Number` |  |  |  |  |  |
| `plugins[]` | `<PluginSchema>` |  |  |  |  |  |
| `plugins[].type` | `String` |  | LIVE_CLASS_PLUGIN_TYPE_CHESS_GAME |  |  |  |
| `plugins[].data` | `Object` |  |  |  |  |  |

## Usage (from backend-api)

_41 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 19
- `.updateOne` × 11
- `.findOneAndUpdate` × 5
- `.aggregate` × 4
- `.find` × 2

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `sessionId` × 1

### Top call sites

- `src/services/lensAnalyticsService.js` × 28
- `src/controllers/LensController.js` × 4
- `src/services/meetingService.js` × 3
- `src/controllers/LensInMeetingController.js` × 1
- `src/services/liveClassDiscussionService.js` × 1
- `src/services/leaderboardService.js` × 1
- `src/services/instituteService.js` × 1
- `src/services/studentReportsServiceV2.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
