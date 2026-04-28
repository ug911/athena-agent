---
collection: "LiveClassInsight"
athena_table: "wise_app_backend__liveclassinsight"
mongo_field_count: 66
athena_field_count: 47
matched: 24
coverage_pct: 36.4
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `LiveClassInsight` ↔ `processed.wise_app_backend__liveclassinsight`

- **Mongo source**: [`src/models/LiveClassInsight.js`](../source/mongo/LiveClassInsight.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__liveclassinsight.md`](../processed/processed/wise_app_backend__liveclassinsight.md)
- **Coverage**: 24/66 Mongo fields are present in Athena (**36.4%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `meetingStartedWebhookReceivedAt` | `Date` |  |  |
| `hostLensRegisteredAt` | `Date` |  |  |
| `classId` | `ObjectId` | `class` |  |
| `participants[].firstEntryTime` | `Date` |  |  |
| `participants[].lastExitTime` | `Date` |  |  |
| `agendas[]` | `<PostMeetingAgendaSchema>` |  |  |
| `agendas[].title` | `String` |  |  |
| `agendas[].description` | `String` |  |  |
| `agendas[].tags` | `Array` |  |  |
| `agendas[].visibleTags` | `Array` |  |  |
| `agendas[].agendaItems` | `Array<<inline-schema>>` |  |  |
| `tempData` | `<TempDataSchema>` |  |  |
| `tempData.participants[].left` | `Boolean` |  |  |
| `tempData.participants[].socketIds` | `Array` |  |  |
| `tempData.participants[].lastConnectedAt` | `Date` |  |  |
| `tempData.participants[].lastDisconnectedAt` | `Date` |  |  |
| `tempData.participants[].wiseUUID` | `String` |  |  |
| `tempData.participants[].firstEntryTime` | `Date` |  |  |
| `tempData.participants[].lastExitTime` | `Date` |  |  |
| `tempData.leaderboardConfig` | `LeaderboardConfigSchema` |  |  |
| `tempData.discussionConfig` | `DiscussionConfigSchema` |  |  |
| `tempData.allowStudentTalkTime` | `Boolean` |  |  |
| `tempData.agendas[]` | `<InMeetingAgendaSchema>` |  |  |
| `tempData.agendas[].title` | `String` |  |  |
| `tempData.agendas[].description` | `String` |  |  |
| `tempData.agendas[].tags` | `Array` |  |  |
| `tempData.agendas[].visibleTags` | `Array` |  |  |
| `tempData.agendas[].lastLaunchedAt` | `Date` |  |  |
| `tempData.agendas[].agendaItems` | `Array<<inline-schema>>` |  |  |
| `metadata` | `<MetadataSchema>` |  |  |
| `metadata.loginRequired` | `Boolean` |  |  |
| `metadata.registrationRequired` | `Boolean` |  |  |
| `metadata.parentMeetingUUID` | `String` |  |  |
| `metadata.ownerId` | `String` |  |  |
| `metadata.pollsMigrated` | `Boolean` |  |  |
| `metadata.ratingsMigrated` | `Boolean` |  |  |
| `trend[]` | `<trendSchema>` |  |  |
| `trend[].windowStartTime` | `Date` |  |  |
| `trend[].attentiveCount` | `Number` |  |  |
| `trend[].totalParticipantCount` | `Number` |  |  |
| `plugins[]` | `<PluginSchema>` |  |  |
| `plugins[].data` | `Object` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `userratings` | `string` | column |
| `_id.$oid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `starttime.$date` | `object` | JSON path |
| `starttime.$date.$numberlong` | `string` | JSON path |
| `endtime.$date` | `object` | JSON path |
| `endtime.$date.$numberlong` | `string` | JSON path |
| `sessionid.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `userratings.[]` | `object` | JSON path |
| `userratings.[].comment` | `string` | JSON path |
| `userratings.[].rating` | `object` | JSON path |
| `userratings.[].rating.$numberint` | `string` | JSON path |
| `participants.[]` | `object` | JSON path |
| `participants.[].attendanceduration.$numberint` | `string` | JSON path |
| `participants.[].attentiveduration.$numberint` | `string` | JSON path |
| `participants.[].customerkey` | `string` | JSON path |
| `participants.[].iszoomuser` | `bool` | JSON path |
| `participants.[].speakingduration.$numberint` | `string` | JSON path |
| `participants.[].videoonduration.$numberint` | `string` | JSON path |
| `participants.[].zoomuserid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
