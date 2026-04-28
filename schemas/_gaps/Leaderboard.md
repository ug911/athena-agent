---
collection: "Leaderboard"
athena_table: "wise_app_backend__leaderboard"
mongo_field_count: 18
athena_field_count: 100
matched: 18
coverage_pct: 100.0
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `Leaderboard` ↔ `processed.wise_app_backend__leaderboard`

- **Mongo source**: [`src/models/Leaderboard.js`](../source/mongo/Leaderboard.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__leaderboard.md`](../processed/processed/wise_app_backend__leaderboard.md)
- **Coverage**: 18/18 Mongo fields are present in Athena (**100.0%**).

## In Mongo, missing from Athena

_None — every Mongo field has a counterpart in Athena._

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `_id.$oid` | `string` | JSON path |
| `classid.$oid` | `string` | JSON path |
| `instituteid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `alltimepointstable.[]` | `object` | JSON path |
| `alltimepointstable.[].pointsdistribution.assessmentmarks` | `object` | JSON path |
| `alltimepointstable.[].pointsdistribution.assessmentmarks.$numberint` | `string` | JSON path |
| `alltimepointstable.[].pointsdistribution.assessmentsubmission` | `object` | JSON path |
| `alltimepointstable.[].pointsdistribution.assessmentsubmission.$numberint` | `string` | JSON path |
| `alltimepointstable.[].pointsdistribution.discussioncomment` | `object` | JSON path |
| `alltimepointstable.[].pointsdistribution.discussioncomment.$numberint` | `string` | JSON path |
| `alltimepointstable.[].pointsdistribution.lenspoints` | `object` | JSON path |
| `alltimepointstable.[].pointsdistribution.lenspoints.$numberint` | `string` | JSON path |
| `alltimepointstable.[].pointsdistribution.pollvoting` | `object` | JSON path |
| `alltimepointstable.[].pointsdistribution.pollvoting.$numberint` | `string` | JSON path |
| `alltimepointstable.[].pointsdistribution.resourcecompletion` | `object` | JSON path |
| `alltimepointstable.[].pointsdistribution.resourcecompletion.$numberint` | `string` | JSON path |
| `alltimepointstable.[].pointsdistribution.sessionduration` | `object` | JSON path |
| `alltimepointstable.[].pointsdistribution.sessionduration.$numberint` | `string` | JSON path |
| `alltimepointstable.[].pointsdistribution.sessionparticipation` | `object` | JSON path |
| `alltimepointstable.[].pointsdistribution.sessionparticipation.$numberint` | `string` | JSON path |
| `alltimepointstable.[].pointsdistribution.testmarks` | `object` | JSON path |
| `alltimepointstable.[].pointsdistribution.testmarks.$numberint` | `string` | JSON path |
| `alltimepointstable.[].pointsdistribution.testsubmission` | `object` | JSON path |
| `alltimepointstable.[].pointsdistribution.testsubmission.$numberint` | `string` | JSON path |
| `alltimepointstable.[].rank.$numberint` | `string` | JSON path |
| `alltimepointstable.[].totalpoints.$numberint` | `string` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `monthlypointstable.[]` | `object` | JSON path |
| `monthlypointstable.[].pointsdistribution.assessmentmarks` | `object` | JSON path |
| `monthlypointstable.[].pointsdistribution.assessmentmarks.$numberint` | `string` | JSON path |
| `monthlypointstable.[].pointsdistribution.assessmentsubmission` | `object` | JSON path |
| `monthlypointstable.[].pointsdistribution.assessmentsubmission.$numberint` | `string` | JSON path |
| `monthlypointstable.[].pointsdistribution.discussioncomment` | `object` | JSON path |
| `monthlypointstable.[].pointsdistribution.discussioncomment.$numberint` | `string` | JSON path |
| `monthlypointstable.[].pointsdistribution.lenspoints` | `object` | JSON path |
| `monthlypointstable.[].pointsdistribution.lenspoints.$numberint` | `string` | JSON path |
| `monthlypointstable.[].pointsdistribution.pollvoting` | `object` | JSON path |
| `monthlypointstable.[].pointsdistribution.pollvoting.$numberint` | `string` | JSON path |
| `monthlypointstable.[].pointsdistribution.resourcecompletion` | `object` | JSON path |
| `monthlypointstable.[].pointsdistribution.resourcecompletion.$numberint` | `string` | JSON path |
| `monthlypointstable.[].pointsdistribution.sessionduration` | `object` | JSON path |
| `monthlypointstable.[].pointsdistribution.sessionduration.$numberint` | `string` | JSON path |
| `monthlypointstable.[].pointsdistribution.sessionparticipation` | `object` | JSON path |
| `monthlypointstable.[].pointsdistribution.sessionparticipation.$numberint` | `string` | JSON path |
| `monthlypointstable.[].pointsdistribution.testmarks` | `object` | JSON path |
| `monthlypointstable.[].pointsdistribution.testmarks.$numberdouble` | `string` | JSON path |
| `monthlypointstable.[].pointsdistribution.testmarks.$numberint` | `string` | JSON path |
| `monthlypointstable.[].pointsdistribution.testsubmission` | `object` | JSON path |
| `monthlypointstable.[].pointsdistribution.testsubmission.$numberint` | `string` | JSON path |
| `monthlypointstable.[].rank.$numberint` | `string` | JSON path |
| `monthlypointstable.[].totalpoints.$numberint` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `weeklypointstable.[]` | `object` | JSON path |
| `weeklypointstable.[].pointsdistribution.assessmentmarks` | `object` | JSON path |
| `weeklypointstable.[].pointsdistribution.assessmentmarks.$numberint` | `string` | JSON path |
| `weeklypointstable.[].pointsdistribution.assessmentsubmission` | `object` | JSON path |
| `weeklypointstable.[].pointsdistribution.assessmentsubmission.$numberint` | `string` | JSON path |
| `weeklypointstable.[].pointsdistribution.discussioncomment` | `object` | JSON path |
| `weeklypointstable.[].pointsdistribution.discussioncomment.$numberint` | `string` | JSON path |
| `weeklypointstable.[].pointsdistribution.lenspoints` | `object` | JSON path |
| `weeklypointstable.[].pointsdistribution.lenspoints.$numberint` | `string` | JSON path |
| `weeklypointstable.[].pointsdistribution.pollvoting` | `object` | JSON path |
| `weeklypointstable.[].pointsdistribution.pollvoting.$numberint` | `string` | JSON path |
| `weeklypointstable.[].pointsdistribution.resourcecompletion` | `object` | JSON path |
| `weeklypointstable.[].pointsdistribution.resourcecompletion.$numberint` | `string` | JSON path |
| `weeklypointstable.[].pointsdistribution.sessionduration` | `object` | JSON path |
| `weeklypointstable.[].pointsdistribution.sessionduration.$numberint` | `string` | JSON path |
| `weeklypointstable.[].pointsdistribution.sessionparticipation` | `object` | JSON path |
| `weeklypointstable.[].pointsdistribution.sessionparticipation.$numberint` | `string` | JSON path |
| `weeklypointstable.[].pointsdistribution.testmarks` | `object` | JSON path |
| `weeklypointstable.[].pointsdistribution.testmarks.$numberint` | `string` | JSON path |
| `weeklypointstable.[].pointsdistribution.testsubmission` | `object` | JSON path |
| `weeklypointstable.[].pointsdistribution.testsubmission.$numberint` | `string` | JSON path |
| `weeklypointstable.[].rank.$numberint` | `string` | JSON path |
| `weeklypointstable.[].totalpoints.$numberint` | `string` | JSON path |
