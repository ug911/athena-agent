---
collection: "user"
athena_table: "wise_app_backend__user"
mongo_field_count: 60
athena_field_count: 95
matched: 41
coverage_pct: 68.3
last_diffed: "2026-04-28T11:07:30+00:00"
---

# Schema gap: `user` ↔ `processed.wise_app_backend__user`

- **Mongo source**: [`src/models/User.js`](../source/mongo/user.md)
- **Athena counterpart**: [`schemas/processed/processed/wise_app_backend__user.md`](../processed/processed/wise_app_backend__user.md)
- **Coverage**: 41/60 Mongo fields are present in Athena (**68.3%**).

## In Mongo, missing from Athena

These fields are declared in the Mongoose schema but the Athena lake pipeline doesn't expose them. Either widen the extractor or note the field as JSON-only inside an existing varchar column.

| Path | Type | Ref | Required |
| --- | --- | --- | --- |
| `activated` | `Boolean` |  |  |
| `integrations` | `?` |  |  |
| `parentIds` | `Array<ObjectId>` | `user` |  |
| `permissions` | `Array` |  |  |
| `deleted` | `Boolean` |  |  |
| `publicProfile.subdomain` | `String` |  |  |
| `publicProfile.publishedAt` | `Date` |  |  |
| `publicProfile.bio` | `String` |  |  |
| `publicProfile.title` | `String` |  |  |
| `publicProfile.logoURL` | `String` |  |  |
| `publicProfile.introVideo` | `String` |  |  |
| `publicProfile.experience` | `Number` |  |  |
| `publicProfile.currentLocation` | `String` |  |  |
| `publicProfile.education` | `String` |  |  |
| `publicProfile.socialProfile` | `socialProfileSchema` |  |  |
| `magicLiveTokenConfig` | `Object` |  |  |
| `whitelabelNamespace` | `String` |  |  |
| `metadata` | `Object` |  |  |
| `instituteZoomPoolName` | `String` |  |  |

## In Athena, missing from Mongo

These fields exist in the Athena table but aren't declared in the current Mongoose schema. Likely renamed / deprecated, or added by the lake pipeline (timestamps, flattened helpers).

| Path | Type | Source |
| --- | --- | --- |
| `isadmin` | `string` | column |
| `activesessions` | `string` | column |
| `pendingrequest` | `string` | column |
| `joinedrequest` | `string` | column |
| `adminpendingrequest` | `string` | column |
| `adminrequest` | `string` | column |
| `premiumconfig` | `string` | column |
| `config` | `string` | column |
| `zoomaccountid` | `string` | column |
| `zoomprefix` | `string` | column |
| `zoomuserid` | `string` | column |
| `lastmeetingstartedon` | `string` | column |
| `parentid` | `string` | column |
| `_id.$oid` | `string` | JSON path |
| `publicprofile.subdomainscreated.$numberint` | `string` | JSON path |
| `publicprofile.teachingpreference.offline` | `bool` | JSON path |
| `publicprofile.teachingpreference.online` | `bool` | JSON path |
| `createdat.$date` | `object` | JSON path |
| `createdat.$date.$numberlong` | `string` | JSON path |
| `notificationtokens.[]` | `object` | JSON path |
| `notificationtokens.[].createdat` | `object` | JSON path |
| `notificationtokens.[].createdat.$date` | `object` | JSON path |
| `notificationtokens.[].createdat.$date.$numberlong` | `string` | JSON path |
| `notificationtokens.[].sessionid.$oid` | `string` | JSON path |
| `__v.$numberint` | `string` | JSON path |
| `lastloggedinon.$date` | `object` | JSON path |
| `lastloggedinon.$date.$numberlong` | `string` | JSON path |
| `acquiredby.$oid` | `string` | JSON path |
| `updatedat.$date` | `object` | JSON path |
| `updatedat.$date.$numberlong` | `string` | JSON path |
| `identities.[]` | `object` | JSON path |
| `identities.[].providermetadata.displayname` | `string` | JSON path |
| `identities.[].providermetadata.photourl` | `string` | JSON path |
| `identities.[].providermetadata.providerid` | `string` | JSON path |
| `identities.[].providermetadata.uid` | `string` | JSON path |
| `referrer.$oid` | `string` | JSON path |
| `sessions.[]` | `object` | JSON path |
| `sessions.[]._id` | `object` | JSON path |
| `sessions.[]._id.$oid` | `string` | JSON path |
| `sessions.[].createdat` | `object` | JSON path |
| `sessions.[].createdat.$date` | `object` | JSON path |
| `sessions.[].createdat.$date.$numberlong` | `string` | JSON path |
| `settings.sessionsettings` | `object` | JSON path |
| `settings.sessionsettings.advanceslotbookingbuffer` | `object` | JSON path |
| `settings.sessionsettings.advanceslotbookingbuffer.$numberint` | `string` | JSON path |
| `settings.sessionsettings.allowonlyconsecutiveslotbooking` | `bool` | JSON path |
| `settings.sessionsettings.blockedadjacentslotbuffer` | `object` | JSON path |
| `settings.sessionsettings.blockedadjacentslotbuffer.$numberint` | `string` | JSON path |
| `settings.timezone` | `string` | JSON path |
