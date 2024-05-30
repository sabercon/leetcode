select round(100.0 * count(o = c or null) / count(*), 2) as immediate_percentage
from (select customer_id, min(order_date) as o, min(customer_pref_delivery_date) as c
      from Delivery
      group by customer_id)
