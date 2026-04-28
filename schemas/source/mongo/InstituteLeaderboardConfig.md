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

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
