---
collection: "user"
model: "user"
source_file: "src/models/User.js"
field_count: 60
last_synced: "2026-04-28T10:58:23+00:00"
---

# `user` (Mongo collection)

- **Model**: `user`
- **Source**: [`src/models/User.js`](../../../src/models/User.js)
- **Athena counterpart**: try `processed.wise_app_backend__user` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ phoneNumber: 1 }, {}]`
- `[{ email: 1 }, {}]`
- `[{ createdAt: 1 }, {}]`
- `[{ uuid: 1 }, { unique: true, partialFilterExpression: { uuid: { $type: "string" } } }]`
- `[{ referralCode: 1 }, { unique: true, partialFilterExpression: { referralCode: { $type: "string" } } }]`
- `[{ referrer: 1 }, {}]`
- `[{ "identities.identifier": 1, namespace: 1 }, { unique: true }]`
- `[{ "parentIds": 1 }, { sparse: 1 }]`

## Local sub-schemas referenced

`IdentitySchema`, `notificationTokenSchema`, `publicProfileSchema`, `sessionSchema`, `sessionSettingsSchema`, `userSchema`, `youtubeUploaderSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `name` | `String` |  |  |  | '' |  |
| `phoneNumber` | `String` |  |  |  |  |  |
| `email` | `String` |  |  |  |  |  |
| `identities[]` | `<IdentitySchema>` |  |  |  |  |  |
| `identities[].identifier` | `String` |  |  | required |  |  |
| `identities[].provider` | `String` |  | PHONE_NUMBER, FIREBASE_ID, VENDOR_USER_ID | required |  |  |
| `identities[].providerMetadata` | `Object` |  |  |  | {} |  |
| `namespace` | `String` |  |  |  | 'wise' |  |
| `uuid` | `String` |  |  |  | uuidv4 |  |
| `activated` | `Boolean` |  |  |  | true |  |
| `referrer` | `ObjectId` | `user` |  |  |  |  |
| `referralCode` | `String` |  |  |  |  |  |
| `referralLink` | `String` |  |  |  |  |  |
| `acquiredBy` | `ObjectId` | `user` |  |  |  |  |
| `integrations` | `?` |  |  |  |  |  |
| `profile` | `String` |  | teacher, student, parent | required | 'student' |  |
| `parentIds` | `Array<ObjectId>` | `user` |  |  | undefined |  |
| `permissions` | `Array` |  |  |  |  |  |
| `sessions[]` | `<sessionSchema>` |  |  |  | [] |  |
| `sessions[].token` | `String` |  |  |  |  |  |
| `sessions[].ip` | `String` |  |  |  |  |  |
| `sessions[].identity` | `String` |  |  |  |  |  |
| `sessions[].platform` | `String` |  |  |  |  |  |
| `sessions[].deviceName` | `String` |  |  |  |  |  |
| `sessions[].deviceId` | `String` |  |  |  |  |  |
| `settings` | `<inline-schema>` |  |  |  | {} |  |
| `block` | `Boolean` |  |  |  | false |  |
| `deleted` | `Boolean` |  |  |  | false |  |
| `profilePicture` | `String` |  |  |  | '' |  |
| `lastLoggedInOn` | `Date` |  |  |  |  |  |
| `publicProfile` | `<publicProfileSchema>` |  |  |  | {} |  |
| `publicProfile.isPublic` | `Boolean` |  |  |  | false |  |
| `publicProfile.subdomain` | `String` |  |  |  |  |  |
| `publicProfile.publishedAt` | `Date` |  |  |  |  |  |
| `publicProfile.subdomainsCreated` | `Number` |  |  |  | 0 |  |
| `publicProfile.marketingTemplates` | `Array` |  |  |  |  |  |
| `publicProfile.bio` | `String` |  |  |  |  |  |
| `publicProfile.title` | `String` |  |  |  |  |  |
| `publicProfile.logoURL` | `String` |  |  |  |  |  |
| `publicProfile.introVideo` | `String` |  |  |  |  |  |
| `publicProfile.experience` | `Number` |  |  |  |  |  |
| `publicProfile.gradesTeaching` | `Array` |  |  |  |  |  |
| `publicProfile.subjects` | `Array` |  |  |  |  |  |
| `publicProfile.teachingLanguages` | `Array` |  |  |  |  |  |
| `publicProfile.currentLocation` | `String` |  |  |  |  |  |
| `publicProfile.education` | `String` |  |  |  |  |  |
| `publicProfile.socialProfile` | `socialProfileSchema` |  |  |  |  |  |
| `publicProfile.teachingPreference` | `<inline-schema>` |  |  |  | {} |  |
| `publicProfile.testimonials` | `Array<<inline-schema>>` |  |  |  |  |  |
| `notificationTokens[]` | `<notificationTokenSchema>` |  |  |  |  |  |
| `notificationTokens[].token` | `String` |  |  | required |  |  |
| `notificationTokens[].type` | `String` |  | push, web |  |  |  |
| `notificationTokens[].projectId` | `String` |  |  |  |  |  |
| `notificationTokens[].platform` | `String` |  |  |  |  |  |
| `notificationTokens[].sessionId` | `ObjectId` |  |  |  |  |  |
| `magicLiveTokenConfig` | `Object` |  |  |  |  |  |
| `loginPin` | `String` |  |  |  |  |  |
| `whitelabelNamespace` | `String` |  |  |  |  |  |
| `metadata` | `Object` |  |  |  |  |  |
| `instituteZoomPoolName` | `String` |  |  |  |  |  |

## Usage (from backend-api)

_213 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 109
- `.updateOne` × 42
- `.find` × 37
- `.findOneAndUpdate` × 10
- `.aggregate` × 4
- `.create` × 4
- `.exists` × 2
- `.updateMany` × 2
- `.deleteMany` × 1
- `.populate` × 1
- `.findById` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `parentIds` × 1

### Top call sites

- `src/services/loginService.js` × 21
- `src/controllers/InstituteController.js` × 17
- `src/controllers/TeacherController.js` × 16
- `src/controllers/UserController.js` × 14
- `src/services/instituteService.js` × 11
- `src/services/feeService.js` × 11
- `src/controllers/DevAPIController.js` × 10
- `src/services/instituteAdmissionService.js` × 8

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
