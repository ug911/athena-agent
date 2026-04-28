---
collection: "zoom"
athena_table: "wise_app_backend__zoom"
mongo_field_count: 86
athena_field_count: 127
matched: 71
coverage_pct: 82.6
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `zoom` ↔ `processed.wise_app_backend__zoom`

- **Mongo source**: [`src/models/Session.js`](../source/mongo/zoom.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__zoom.md`](../processed/processed/wise_app_backend__zoom.md)
- **Coverage**: 71/86 Mongo fields are present in Athena (**82.6%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `provider` | `String` |  |  |
| `participants[].offline` | `Boolean` |  |  |
| `attendees` | `Array<ObjectId>` | `user` |  |
| `lastCommentedAt` | `Date` |  |  |
| `public` | `Boolean` |  |  |
| `recordingsCaptured` | `Boolean` |  |  |
| `recordingUnsharedAt` | `Date` |  |  |
| `thumbnail` | `String` |  |  |
| `offline` | `Boolean` |  |  |
| `description` | `String` |  |  |
| `privateNote` | `String` |  |  |
| `streamingData` | `<streamingDataSchema>` |  |  |
| `streamingData.streamingKey` | `String` |  | required |
| `streamingData.streamingURL` | `String` |  | required |
| `streamingData.pageURL` | `String` |  | required |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `webhookreceived` | `string` | column |
| `_id.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `start_time.$date` | `object` | JSON path |
| `start_time.$date.$numberlong` | `string` | JSON path |
| `participants.[]` | `object` | JSON path |
| `participants.[].absolutepercentattendance.$numberint` | `string` | JSON path |
| `participants.[].duration.$numberint` | `string` | JSON path |
| `participants.[].firstentrytime.$date` | `object` | JSON path |
| `participants.[].firstentrytime.$date.$numberlong` | `string` | JSON path |
| `participants.[].inmeetingduration.$numberint` | `string` | JSON path |
| `participants.[].lastexittime.$date` | `object` | JSON path |
| `participants.[].lastexittime.$date.$numberlong` | `string` | JSON path |
| `participants.[].relativepercentattendance.$numberint` | `string` | JSON path |
| `participants.[].wiseuserid.$oid` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `duration.$numberint` | `string` | JSON path |
| `end_time.$date` | `object` | JSON path |
| `end_time.$date.$numberlong` | `string` | JSON path |
| `scheduledstarttime.$date` | `object` | JSON path |
| `scheduledstarttime.$date.$numberlong` | `string` | JSON path |
| `scheduledendtime.$date` | `object` | JSON path |
| `scheduledendtime.$date.$numberlong` | `string` | JSON path |
| `participant.$numberint` | `string` | JSON path |
| `maxparticipantduration.$numberint` | `string` | JSON path |
| `metadata.autorecord` | `bool` | JSON path |
| `metadata.cancellationmetadata` | `object` | JSON path |
| `metadata.cancellationmetadata.approved` | `bool` | JSON path |
| `metadata.cancellationmetadata.requestedby` | `string` | JSON path |
| `metadata.cancellationmetadata.requestedon` | `object` | JSON path |
| `metadata.cancellationmetadata.requestedon.$date` | `object` | JSON path |
| `metadata.cancellationmetadata.requestedon.$date.$numberlong` | `string` | JSON path |
| `metadata.cancellationmetadata.requestnote` | `string` | JSON path |
| `metadata.endedby` | `string` | JSON path |
| `metadata.endreason` | `string` | JSON path |
| `metadata.isownerzoom` | `bool` | JSON path |
| `metadata.lensenabled` | `bool` | JSON path |
| `metadata.ownerid` | `object` | JSON path |
| `metadata.ownerid.$oid` | `string` | JSON path |
| `metadata.paiduser` | `bool` | JSON path |
| `metadata.poolname` | `string` | JSON path |
| `metadata.recurrenceid` | `string` | JSON path |
| `metadata.registrationenabled` | `bool` | JSON path |
| `metadata.restartedsessions` | `array<object>|array<unknown>` | JSON path |
| `metadata.restartedsessions.restartedsessions[]` | `object` | JSON path |
| `metadata.restartedsessions.restartedsessions[].sessionid` | `object` | JSON path |
| `metadata.restartedsessions.restartedsessions[].sessionid.$oid` | `string` | JSON path |
| `metadata.waitingmeeting` | `bool` | JSON path |
| `metadata.webinar` | `bool` | JSON path |
| `metadata.zoomadminaccountid` | `string` | JSON path |
| `metadata.zoomuseraccountid` | `string` | JSON path |
| `metadata.zoomuserid` | `string` | JSON path |
| `recordings.[]` | `object` | JSON path |
| `recordings.[]._id` | `object` | JSON path |
| `recordings.[]._id.$oid` | `string` | JSON path |
| `recordings.[].duration.$numberint` | `string` | JSON path |
| `recordings.[].file._id` | `object` | JSON path |
| `recordings.[].file._id.$oid` | `string` | JSON path |
| `recordings.[].file.size.$numberint` | `string` | JSON path |
| `recordings.[].partindex.$numberint` | `string` | JSON path |
| `recordings.[].sessionindex.$numberint` | `string` | JSON path |
