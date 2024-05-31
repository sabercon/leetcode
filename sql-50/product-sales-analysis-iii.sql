with product_id_min_year as (select product_id, min(year) min_year
                             from Sales
                             group by product_id)

select s.product_id, s.year first_year, s.quantity, s.price
from Sales s
         join product_id_min_year m on s.product_id = m.product_id and s.year = m.min_year
