-- intent: week-on-week count of tutors who ran >=4 live sessions that have an AI summary or transcript,
--         restricted to human-named tutors in tenants with >=10 active teachers. Swap `processed` ->
--         `processed_na` for NA. Verified against IN + NA on 2026-08-11.
--
-- Notes / gotchas baked in below:
--   * zoomers_v3 needs `row = 1` (latest revision per zoom_id) and `meetingstatus = 'ENDED'`
--     (scheduled rows carry far-future start_time values, into the 2040s).
--   * The AI artifact tables can hold a row with an EMPTY array, so presence of a row is not enough.
--   * Tutor name classification is heuristic: strip honorifics / role words / grade tokens / subject tags /
--     roster ids / the tenant's own brand token, then require >=3 residual letters. A second, orthogonal
--     signal flags names shared by >=3 distinct accounts in one tenant (demo seeds, shared logins).
--     Expect ~1% of org accounts to leak through as "human"; tightening further starts misclassifying
--     real names like `Teacher Amy` or `Ms Ema`.
--   * Bound the week window to whole ISO weeks; the warehouse is a once-a-day full dump, so the
--     in-progress week is always partial.

WITH s AS (
  SELECT zoom_id, userid, date_trunc('week', start_time) AS wk
  FROM processed.zoomers_v3
  WHERE row = 1
    AND meetingstatus = 'ENDED'
    AND start_time >= timestamp '2026-06-15 00:00:00'
    AND start_time <  timestamp '2026-08-10 00:00:00'
),
host_ns AS (
  SELECT DISTINCT s.userid, u.namespace,
         lower(trim(coalesce(u.name,''))) AS nm_norm,
         ' ' || regexp_replace(lower(trim(coalesce(u.name,''))), '[^\p{L} ]', ' ') || ' ' AS toks
  FROM (SELECT DISTINCT userid FROM s) s
  JOIN processed.user u ON u.userid = s.userid
),
-- tenant size = distinct hosts of an ENDED session anywhere in the window (applied once, not per week,
-- so tenants don't drop in and out of the series)
ns_size AS (SELECT namespace, count(DISTINCT userid) AS active_teachers FROM host_ns GROUP BY 1),
summ AS (
  SELECT DISTINCT json_extract_scalar(sessionid,'$["$oid"]') AS sid
  FROM processed.wise_app_backend__rawzoomsummary
  WHERE summaries IS NOT NULL AND summaries <> '[]'
),
tr AS (
  SELECT DISTINCT json_extract_scalar(sessionid,'$["$oid"]') AS sid
  FROM processed.wise_app_backend__rawsessiontranscript
  WHERE files IS NOT NULL AND files <> '[]'
),
per_tutor AS (
  SELECT s.wk, s.userid, count_if(summ.sid IS NOT NULL OR tr.sid IS NOT NULL) AS ai_sessions
  FROM s
  LEFT JOIN summ ON summ.sid = s.zoom_id
  LEFT JOIN tr   ON tr.sid   = s.zoom_id
  GROUP BY 1,2
),
qual AS (SELECT wk, userid FROM per_tutor WHERE ai_sessions >= 4),
stripped AS (
  SELECT h.*,
    regexp_replace(regexp_replace(toks,
      ' (mr|mrs|ms|miss|sir|madam|maam|mam|dr|prof|teacher|teachers|tutor|instructor|faculty|coach|trainer|mentor|pengajar|sensei|office|hr|admin|administrator|owner|department|dept|operations|ops|sales|marketing|agency|institute|academy|academic|school|classes|class|education|educational|learning|community|softwares|software|team|staff|reception|principal|coordinator|consultant|expert|demo|webinar|uat|staging|test|live|online|centre|center|group|pvt|ltd|limited|private|llc|solutions|services|edu|tech|it|no|the|and|of|kg|lkg|ukg|nursery|pre|grade|std|standard|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|personalized|personalised|section|batch|math|maths|mathematics|science|english|ela|hindi|physics|chemistry|biology|coding|chess|music|accounting|social|sst|gk|prep) ', ' '),
      ' (mr|mrs|ms|miss|sir|madam|maam|mam|dr|prof|teacher|teachers|tutor|instructor|faculty|coach|trainer|mentor|pengajar|sensei|office|hr|admin|administrator|owner|department|dept|operations|ops|sales|marketing|agency|institute|academy|academic|school|classes|class|education|educational|learning|community|softwares|software|team|staff|reception|principal|coordinator|consultant|expert|demo|webinar|uat|staging|test|live|online|centre|center|group|pvt|ltd|limited|private|llc|solutions|services|edu|tech|it|no|the|and|of|kg|lkg|ukg|nursery|pre|grade|std|standard|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|personalized|personalised|section|batch|math|maths|mathematics|science|english|ela|hindi|physics|chemistry|biology|coding|chess|music|accounting|social|sst|gk|prep) ', ' ') AS resid_raw,
    array_join(filter(split(lower(namespace),'-'), x -> length(x) >= 4), '|') AS ns_pat
  FROM host_ns h
),
final AS (
  -- \p{L} (not [a-z]) so Arabic / Korean / accented names are not wrongly classed as degenerate
  SELECT userid, namespace, nm_norm,
    CASE WHEN ns_pat = '' THEN regexp_replace(resid_raw,'[^\p{L}]','')
         ELSE regexp_replace(regexp_replace(resid_raw,'[^\p{L}]',''), ns_pat, '') END AS resid
  FROM stripped
),
dupes AS (SELECT namespace, nm_norm, count(DISTINCT userid) AS n_accounts FROM final GROUP BY 1,2),
classified AS (
  SELECT f.userid, f.namespace,
         CASE WHEN length(f.resid) < 3      THEN 'non_human'       -- org / system / class-slot naming
              WHEN d.n_accounts >= 3        THEN 'shared_generic'  -- demo seed or shared login
              ELSE 'human' END AS bucket
  FROM final f
  JOIN dupes d ON d.namespace = f.namespace AND d.nm_norm = f.nm_norm
)
SELECT q.wk AS week_start,
       count_if(c.bucket = 'human')  AS human_named_tutors,
       count_if(c.bucket <> 'human') AS non_human_accounts,
       count(*)                      AS total_in_scope
FROM qual q
JOIN classified c ON c.userid = q.userid
JOIN ns_size   n ON n.namespace = c.namespace AND n.active_teachers >= 10
GROUP BY q.wk
ORDER BY q.wk;
