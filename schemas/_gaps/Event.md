---
collection: "Event"
athena_table: "wise_app_backend__event"
mongo_field_count: 5
athena_field_count: 129
matched: 4
coverage_pct: 80.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `Event` ↔ `processed.wise_app_backend__event`

- **Mongo source**: [`src/models/DBEvent.js`](../source/mongo/Event.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__event.md`](../processed/processed/wise_app_backend__event.md)
- **Coverage**: 4/5 Mongo fields are present in Athena (**80.0%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `expiresAt` | `Date` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `payload.assessment` | `object` | JSON path |
| `payload.assessment.feedback` | `string` | JSON path |
| `payload.assessment.getmark` | `object` | JSON path |
| `payload.assessment.getmark.$numberint` | `string` | JSON path |
| `payload.assessment.id` | `string` | JSON path |
| `payload.assessment.maxmark` | `object` | JSON path |
| `payload.assessment.maxmark.$numberint` | `string` | JSON path |
| `payload.class` | `object` | JSON path |
| `payload.class.id` | `string` | JSON path |
| `payload.class.meetingid` | `object|string` | JSON path |
| `payload.class.meetingid.$numberdouble` | `string` | JSON path |
| `payload.class.name` | `string` | JSON path |
| `payload.class.namespace` | `string` | JSON path |
| `payload.class.subject` | `string` | JSON path |
| `payload.data` | `object` | JSON path |
| `payload.data.quizzes` | `object` | JSON path |
| `payload.data.quizzes.$numberint` | `string` | JSON path |
| `payload.data.revisionnotes` | `object` | JSON path |
| `payload.data.revisionnotes.$numberint` | `string` | JSON path |
| `payload.discussion` | `object` | JSON path |
| `payload.discussion.comment` | `object` | JSON path |
| `payload.discussion.comment.attachments` | `array<object>` | JSON path |
| `payload.discussion.comment.attachments.discussion.comment.attachments[]` | `object` | JSON path |
| `payload.discussion.comment.attachments.discussion.comment.attachments[].filename` | `string` | JSON path |
| `payload.discussion.comment.attachments.discussion.comment.attachments[].path` | `string` | JSON path |
| `payload.discussion.comment.attachments.discussion.comment.attachments[].s3filepath` | `string` | JSON path |
| `payload.discussion.comment.attachments.discussion.comment.attachments[].s3key` | `string` | JSON path |
| `payload.discussion.comment.attachments.discussion.comment.attachments[].size` | `object` | JSON path |
| `payload.discussion.comment.attachments.discussion.comment.attachments[].size.$numberint` | `string` | JSON path |
| `payload.discussion.comment.attachments.discussion.comment.attachments[].type` | `string` | JSON path |
| `payload.discussion.comment.comment` | `string` | JSON path |
| `payload.discussion.comment.createdat` | `string` | JSON path |
| `payload.discussion.comment.editedat` | `string` | JSON path |
| `payload.discussion.comment.userid` | `string` | JSON path |
| `payload.discussion.id` | `string` | JSON path |
| `payload.institute` | `object` | JSON path |
| `payload.institute.id` | `string` | JSON path |
| `payload.institute.namespace` | `string` | JSON path |
| `payload.participant` | `object` | JSON path |
| `payload.participant.id` | `string` | JSON path |
| `payload.participant.profile` | `string` | JSON path |
| `payload.resource` | `object` | JSON path |
| `payload.resource.id` | `string` | JSON path |
| `payload.resource.name` | `string` | JSON path |
| `payload.resource.type` | `string` | JSON path |
| `payload.sectionid` | `string` | JSON path |
| `payload.session` | `object` | JSON path |
| `payload.session.autosubmitted` | `bool` | JSON path |
| `payload.session.classid` | `string` | JSON path |
| `payload.session.createdat` | `string` | JSON path |
| `payload.session.id` | `string` | JSON path |
| `payload.session.meetingid` | `object|string` | JSON path |
| `payload.session.meetingid.$numberdouble` | `string` | JSON path |
| `payload.session.meetingstatus` | `string` | JSON path |
| `payload.session.meetinguuid` | `string` | JSON path |
| `payload.session.scheduled` | `bool` | JSON path |
| `payload.session.scheduledendtime` | `string` | JSON path |
| `payload.session.scheduledstarttime` | `string` | JSON path |
| `payload.session.starttime` | `string` | JSON path |
| `payload.session.type` | `string` | JSON path |
| `payload.student` | `object` | JSON path |
| `payload.student.id` | `string` | JSON path |
| `payload.submission` | `object` | JSON path |
| `payload.submission.endtime` | `string` | JSON path |
| `payload.submission.id` | `string` | JSON path |
| `payload.submission.marksobtained` | `object` | JSON path |
| `payload.submission.marksobtained.$numberint` | `string` | JSON path |
| `payload.submission.passed` | `bool` | JSON path |
| `payload.submission.starttime` | `string` | JSON path |
| `payload.submission.status` | `string` | JSON path |
| `payload.test` | `object` | JSON path |
| `payload.test.id` | `string` | JSON path |
| `payload.transaction` | `object` | JSON path |
| `payload.transaction.amount` | `object` | JSON path |
| `payload.transaction.amount.currency` | `string` | JSON path |
| `payload.transaction.amount.value` | `object` | JSON path |
| `payload.transaction.amount.value.$numberint` | `string` | JSON path |
| `payload.transaction.createdat` | `string` | JSON path |
| `payload.transaction.id` | `string` | JSON path |
| `payload.transaction.metadata` | `object` | JSON path |
| `payload.transaction.metadata.classid` | `string` | JSON path |
| `payload.transaction.metadata.invoicetype` | `string` | JSON path |
| `payload.transaction.metadata.paid` | `bool` | JSON path |
| `payload.transaction.metadata.sessioncredits` | `object` | JSON path |
| `payload.transaction.metadata.sessioncredits.$numberint` | `string` | JSON path |
| `payload.transaction.metadata.sessionid` | `string` | JSON path |
| `payload.transaction.metadata.sessionstarttime` | `string` | JSON path |
| `payload.transaction.note` | `string` | JSON path |
| `payload.transaction.receiverid` | `string` | JSON path |
| `payload.transaction.senderid` | `string` | JSON path |
| `payload.transaction.status` | `string` | JSON path |
| `payload.transaction.transactiontype` | `string` | JSON path |
| `payload.transaction.type` | `string` | JSON path |
| `payload.transaction.updatedat` | `string` | JSON path |
| `payload.user` | `object` | JSON path |
| `payload.user.email` | `string` | JSON path |
| `payload.user.id` | `string` | JSON path |
| `payload.user.name` | `string` | JSON path |
| `payload.user.namespace` | `string` | JSON path |
| `payload.user.phonenumber` | `string` | JSON path |
| `payload.verification` | `object` | JSON path |
| `payload.verification.code` | `string` | JSON path |
| `payload.verification.data` | `object` | JSON path |
| `payload.verification.data.attempts` | `object` | JSON path |
| `payload.verification.data.attempts.$numberint` | `string` | JSON path |
| `payload.verification.data.code` | `string` | JSON path |
| `payload.verification.data.createdat` | `string` | JSON path |
| `payload.verification.data.expirytime` | `string` | JSON path |
| `payload.verification.data.id` | `string` | JSON path |
| `payload.verification.data.identifier` | `string` | JSON path |
| `payload.verification.data.idtype` | `string` | JSON path |
| `payload.verification.data.ip` | `string` | JSON path |
| `payload.verification.data.resendcount` | `object` | JSON path |
| `payload.verification.data.resendcount.$numberint` | `string` | JSON path |
| `payload.verification.data.resendwindow` | `string` | JSON path |
| `payload.verification.data.updatedat` | `string` | JSON path |
| `payload.verification.data.verified` | `bool` | JSON path |
| `payload.version` | `object` | JSON path |
| `payload.version.$numberint` | `string` | JSON path |
| `eventtimestamp.$date` | `object` | JSON path |
| `eventtimestamp.$date.$numberlong` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
