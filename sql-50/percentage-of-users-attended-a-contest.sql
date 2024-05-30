select contest_id, round(100.0 * count(distinct user_id) / (select count(*) from Users), 2) as percentage
from Register
group by contest_id
order by percentage desc, contest_id asc
