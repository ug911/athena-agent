---
collection: "Leaderboard"
model: "Leaderboard"
source_file: "src/models/Leaderboard.js"
field_count: 18
last_synced: "2026-04-28T10:58:23+00:00"
---

# `Leaderboard` (Mongo collection)

- **Model**: `Leaderboard`
- **Source**: [`src/models/Leaderboard.js`](../../../src/models/Leaderboard.js)
- **Athena counterpart**: try `processed.wise_app_backend__leaderboard` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ classId: 1 }]`
- `[{ instituteId: 1, type: 1 }]`

## Local sub-schemas referenced

`LeaderboardSchema`, `PointsDistributionSchema`, `UserPointsSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `Institute` |  |  |  |  |
| `classId` | `ObjectId` | `class` |  |  |  |  |
| `type` | `String` |  | INSTITUTE, CLASSROOM |  |  |  |
| `weeklyPointsTable[]` | `<UserPointsSchema>` |  |  |  |  |  |
| `weeklyPointsTable[].userId` | `String` |  |  | required |  |  |
| `weeklyPointsTable[].pointsDistribution` | `<PointsDistributionSchema>` |  |  |  |  |  |
| `weeklyPointsTable[].totalPoints` | `Number` |  |  | required |  |  |
| `weeklyPointsTable[].rank` | `Number` |  |  |  |  |  |
| `monthlyPointsTable[]` | `<UserPointsSchema>` |  |  |  |  |  |
| `monthlyPointsTable[].userId` | `String` |  |  | required |  |  |
| `monthlyPointsTable[].pointsDistribution` | `<PointsDistributionSchema>` |  |  |  |  |  |
| `monthlyPointsTable[].totalPoints` | `Number` |  |  | required |  |  |
| `monthlyPointsTable[].rank` | `Number` |  |  |  |  |  |
| `allTimePointsTable[]` | `<UserPointsSchema>` |  |  |  |  |  |
| `allTimePointsTable[].userId` | `String` |  |  | required |  |  |
| `allTimePointsTable[].pointsDistribution` | `<PointsDistributionSchema>` |  |  |  |  |  |
| `allTimePointsTable[].totalPoints` | `Number` |  |  | required |  |  |
| `allTimePointsTable[].rank` | `Number` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
