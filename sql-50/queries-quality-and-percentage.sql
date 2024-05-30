select query_name,
       round(avg(1.0 * rating / position), 2)                 as quality,
       round(100.0 * count(rating < 3 or null) / count(*), 2) as poor_query_percentage
from Queries
where query_name is not null
group by query_name
