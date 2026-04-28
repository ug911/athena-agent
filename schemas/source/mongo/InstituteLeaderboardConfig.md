---
collection: "InstituteLeaderboardConfig"
model: "InstituteLeaderboardConfig"
source_file: "src/models/InstituteLeaderboardConfig.js"
field_count: 9
last_synced: "2026-04-28T10:58:23+00:00"
---

# `InstituteLeaderboardConfig` (Mongo collection)

- **Model**: `InstituteLeaderboardConfig`
- **Source**: [`src/models/InstituteLeaderboardConfig.js`](../../../src/models/InstituteLeaderboardConfig.js)
- **Athena counterpart**: try `processed.wise_app_backend__institute_leaderboard_config` or `processed.wise_app_backend__instituteleaderboardconfig` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ instituteId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`InstituteLeaderboardConfigSchema`, `LeaderboardRuleSchema`, `LevelSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `Institute` |  | required |  |  |
| `enabled` | `Boolean` |  |  | required |  |  |
| `pointConfigurations[]` | `<LeaderboardRuleSchema>` |  |  |  |  |  |
| `pointConfigurations[].category` | `String` |  | <ALL_LEADERBOARD_CATEGORIES> | required |  |  |
| `pointConfigurations[].points` | `Number` |  |  | required |  |  |
| `levels[]` | `<LevelSchema>` |  |  |  |  |  |
| `levels[].index` | `Number` |  |  | required |  |  |
| `levels[].title` | `String` |  |  | required |  |  |
| `levels[].thresholdPoints` | `Number` |  |  | required |  |  |

## Usage (from backend-api)

_7 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 3
- `.findOneAndUpdate` × 1
- `.find` × 1
- `.create` × 1
- `.deleteOne` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `instituteId` × 1

### Top call sites

- `src/services/leaderboardService.js` × 3
- `src/controllers/InstituteController.js` × 1
- `src/services/DemoAccountService.js` × 1
- `src/services/instituteService.js` × 1
- `src/services/studentReportsServiceV2.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
