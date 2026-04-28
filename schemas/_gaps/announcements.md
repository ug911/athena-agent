---
collection: "announcements"
athena_table: "wise_app_backend__announcements"
mongo_field_count: 26
athena_field_count: 49
matched: 14
coverage_pct: 53.8
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `announcements` ↔ `processed.wise_app_backend__announcements`

- **Mongo source**: [`src/models/Discussion.js`](../source/mongo/announcements.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__announcements.md`](../processed/processed/wise_app_backend__announcements.md)
- **Coverage**: 14/26 Mongo fields are present in Athena (**53.8%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `canEdit` | `Boolean` |  |  |
| `canDelete` | `Boolean` |  |  |
| `pollData.question` | `String` |  |  |
| `pollData.options` | `Object` |  |  |
| `pollData.correctAnswer` | `String` |  |  |
| `pollData.endsAt` | `Date` |  |  |
| `pollData.showResults` | `Boolean` |  |  |
| `pollData.stats` | `Object` |  |  |
| `pollData.voteCount` | `Number` |  |  |
| `public` | `Boolean` |  |  |
| `thumbnail` | `String` |  |  |
| `metadata` | `Object` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `userid.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `attachments.[]` | `object` | JSON path |
| `attachments.[]._id` | `object` | JSON path |
| `attachments.[]._id.$oid` | `string` | JSON path |
| `attachments.[].filename` | `string` | JSON path |
| `attachments.[].path` | `string` | JSON path |
| `attachments.[].s3filepath` | `string` | JSON path |
| `attachments.[].s3key` | `string` | JSON path |
| `attachments.[].size` | `object` | JSON path |
| `attachments.[].size.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `comments.[]` | `object` | JSON path |
| `comments.[]._id` | `object` | JSON path |
| `comments.[]._id.$oid` | `string` | JSON path |
| `comments.[].comment` | `string` | JSON path |
| `comments.[].createdat` | `object` | JSON path |
| `comments.[].createdat.$date` | `object` | JSON path |
| `comments.[].createdat.$date.$numberlong` | `string` | JSON path |
| `comments.[].deleted` | `bool` | JSON path |
| `comments.[].deletedby` | `string` | JSON path |
| `comments.[].edited` | `bool` | JSON path |
| `comments.[].editedat` | `object` | JSON path |
| `comments.[].editedat.$date` | `object` | JSON path |
| `comments.[].editedat.$date.$numberlong` | `string` | JSON path |
| `comments.[].userid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `lastcommentedat.$date` | `object` | JSON path |
| `lastcommentedat.$date.$numberlong` | `string` | JSON path |
