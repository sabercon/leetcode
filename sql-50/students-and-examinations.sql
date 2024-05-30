select stu.student_id, stu.student_name, sub.subject_name, count(e) as attended_exams
from Students stu
         cross join Subjects sub
         left join Examinations e on stu.student_id = e.student_id and sub.subject_name = e.subject_name
group by stu.student_id, stu.student_name, sub.subject_name
order by student_id
