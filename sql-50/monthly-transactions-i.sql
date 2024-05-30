select to_char(trans_date, 'YYYY-MM')                           as month,
       country,
       count(*)                                                 as trans_count,
       count(state = 'approved' or null)                        as approved_count,
       sum(amount)                                              as trans_total_amount,
       sum(case when state = 'approved' then amount else 0 end) as approved_total_amount
from Transactions
group by month, country
