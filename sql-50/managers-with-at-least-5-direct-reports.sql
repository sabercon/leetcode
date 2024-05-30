select any_value(manager.name) as name
from Employee manager
         inner join Employee report on manager.id = report.managerId
group by manager.id
having count(*) >= 5
