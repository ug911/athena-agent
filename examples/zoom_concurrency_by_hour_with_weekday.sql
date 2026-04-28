-- intent: per hour-of-day stats (max/min/mean/std) of peak concurrent zoom sessions across all Wise namespaces over the last 28 days, plus the weekday on which each hour's max occurred. Sweep-line concurrency, then per-(date,hour,dow) peak; aggregate across days per hour and pick the dow of each hour's max via ROW_NUMBER. Hours are UTC; switch to AT TIME ZONE 'Asia/Kolkata' for IST.
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
  SELECT date(ts) AS d, hour(ts) AS h, day_of_week(ts) AS dow, MAX(concurrent) AS peak
  FROM running
  WHERE ts >= current_timestamp - interval '28' day
    AND ts <  current_timestamp
  GROUP BY date(ts), hour(ts), day_of_week(ts)
),
ranked AS (
  SELECT h, dow, peak,
         ROW_NUMBER() OVER (PARTITION BY h ORDER BY peak DESC) AS rn
  FROM hourly
),
agg AS (
  SELECT h,
         COUNT(*)            AS n_days_observed,
         MAX(peak)           AS max_peak,
         MIN(peak)           AS min_peak,
         ROUND(AVG(peak), 1) AS mean_peak,
         ROUND(STDDEV(peak), 1) AS std_peak
  FROM hourly
  GROUP BY h
),
max_dow AS (SELECT h, dow AS max_dow FROM ranked WHERE rn = 1)
SELECT a.h AS hour_utc,
       a.n_days_observed,
       a.max_peak,
       CASE m.max_dow WHEN 1 THEN 'Mon' WHEN 2 THEN 'Tue' WHEN 3 THEN 'Wed'
                      WHEN 4 THEN 'Thu' WHEN 5 THEN 'Fri' WHEN 6 THEN 'Sat'
                      WHEN 7 THEN 'Sun' END AS max_peak_weekday,
       a.min_peak,
       a.mean_peak,
       a.std_peak
FROM agg a
JOIN max_dow m ON m.h = a.h
ORDER BY a.h;
