-- intent: max concurrent zoom sessions (= max licenses in use) per namespace over the last 7 days. Sweep-line pattern: +1 at start_time, -1 at end_time, running cumulative sum, take MAX. ORDER BY ts, delta DESC counts simultaneous starts before ends (worst-case license usage).
WITH zoom AS (
  SELECT
    CAST(json_extract(z.classid, '$["$oid"]') AS varchar) AS class_id,
    from_unixtime(CAST(json_extract_scalar(z.start_time, '$["$date"]["$numberlong"]') AS bigint)/1000) AS start_time,
    from_unixtime(CAST(json_extract_scalar(z.end_time,   '$["$date"]["$numberlong"]') AS bigint)/1000) AS end_time
  FROM processed.wise_app_backend__zoom z
),
sessions AS (
  SELECT c.namespace, z.start_time, z.end_time
  FROM zoom z
  JOIN processed.class c ON c.class_id = z.class_id
  WHERE z.start_time IS NOT NULL AND z.end_time IS NOT NULL
    AND z.end_time > z.start_time
    AND z.start_time <  current_timestamp
    AND z.end_time   >= current_timestamp - interval '7' day
),
events AS (
  SELECT namespace, start_time AS ts,  1 AS delta FROM sessions
  UNION ALL
  SELECT namespace, end_time   AS ts, -1 AS delta FROM sessions
),
running AS (
  SELECT namespace, ts,
         SUM(delta) OVER (
           PARTITION BY namespace
           ORDER BY ts, delta DESC
           ROWS UNBOUNDED PRECEDING
         ) AS concurrent
  FROM events
)
SELECT namespace, MAX(concurrent) AS max_concurrent_zoom_licenses
FROM running
GROUP BY namespace
ORDER BY max_concurrent_zoom_licenses DESC;
