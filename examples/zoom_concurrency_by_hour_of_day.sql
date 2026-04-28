-- intent: per hour-of-day stats (max/min/mean/std) of peak concurrent zoom sessions across the entire Wise ecosystem over the last 28 days. Two-stage: sweep-line concurrency, then bucket events by (date, hour) and take per-bucket peak, then aggregate across days per hour. Hours are UTC; switch to AT TIME ZONE 'Asia/Kolkata' for IST.
WITH zoom AS (
  SELECT
    from_unixtime(CAST(json_extract_scalar(start_time, '$["$date"]["$numberlong"]') AS bigint)/1000) AS start_time,
    from_unixtime(CAST(json_extract_scalar(end_time,   '$["$date"]["$numberlong"]') AS bigint)/1000) AS end_time
  FROM processed.wise_app_backend__zoom
),
sessions AS (
  SELECT start_time, end_time
  FROM zoom
  WHERE start_time IS NOT NULL AND end_time IS NOT NULL
    AND end_time > start_time
    AND start_time <  current_timestamp
    AND end_time   >= current_timestamp - interval '28' day
),
events AS (
  SELECT start_time AS ts,  1 AS delta FROM sessions
  UNION ALL
  SELECT end_time   AS ts, -1 AS delta FROM sessions
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
