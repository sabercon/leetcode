select round(1.0 * count(a2.player_id) / count(a1.player_id), 2) as fraction
from (select player_id, min(event_date) as first_login from activity group by player_id) a1
         left join activity a2 on a1.player_id = a2.player_id and a1.first_login = a2.event_date - 1
