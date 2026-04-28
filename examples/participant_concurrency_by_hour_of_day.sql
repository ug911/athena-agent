-- intent: per hour-of-day stats (max/min/mean/std) of peak concurrent LIVE PARTICIPANTS across the Wise ecosystem over the last 28 days. Each participant counts from their firstentrytime to lastexittime inside wise_app_backend__zoom.participants[]. Note: ~3 GB scan because every zoom doc's participants array is unnested — materialize a participant_intervals table if reusing.
WITH parts AS (
  SELECT
    from_unixtime(CAST(json_extract_scalar(r, '$.firstentrytime["$date"]["$numberlong"]') AS bigint)/1000) AS entry_t,
    from_unixtime(CAST(json_extract_scalar(r, '$.lastexittime["$date"]["$numberlong"]')   AS bigint)/1000) AS exit_t
  FROM processed.wise_app_backend__zoom
  CROSS JOIN UNNEST(TRY_CAST(json_parse(participants) AS array(json))) AS t(r)
  WHERE participants IS NOT NULL AND participants <> '[]'
),
ranges AS (
  SELECT entry_t, exit_t
  FROM parts
  WHERE entry_t IS NOT NULL AND exit_t IS NOT NULL
    AND exit_t > entry_t
    AND entry_t <  current_timestamp
    AND exit_t  >= current_timestamp - interval '28' day
),
events AS (
  SELECT entry_t AS ts,  1 AS delta FROM ranges
  UNION ALL
  SELECT exit_t  AS ts, -1 AS delta FROM ranges
),
running AS (
  SELECT ts,
         SUM(delta) OVER (ORDER BY ts, delta DESC ROWS UNBOUNDED PRECEDING) AS concurrent
  FROM events
),
hourly AS (
  SELECT date(ts) AS d, hour(ts) AS h, MAX(concurrent) AS peak
  FROM running
  WHERE ts >= current_timestamp - interval '28' day
    AND ts <  current_timestamp
  GROUP BY date(ts), hour(ts)
)
SELECT h AS hour_utc,
       COUNT(*)               AS n_days_observed,
       MAX(peak)              AS max_peak,
       MIN(peak)              AS min_peak,
       ROUND(AVG(peak), 1)    AS mean_peak,
       ROUND(STDDEV(peak), 1) AS std_peak
FROM hourly
GROUP BY h
ORDER BY h;
