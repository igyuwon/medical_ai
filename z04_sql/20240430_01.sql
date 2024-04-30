select * from stu_score;

select * from stu_score
where name like '_a%'
order by no asc;


select a.*, name from board a,member b
where a.id = b.id;

select bno, a.id,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile
from board a,member b
where a.id = b.id;

select * from stu_score;
select no,name,total,avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score
order by grade
;

select round(avg(salary),2) as salary from employees;

select * from employees;

-- employees 테이블에서 사원번호, 이름, 월급, 실제월급(월급+(월급*커미션)), 월급 *1410(원)원화로 환산해서
-- 원화표시, 천단위 표시해서 출력
select employee_id, emp_name,salary,salary+(salary*nvl(commission_pct,0)) real_salary, 
to_char(salary*1410,'L99,999,999') kor_salary 
from employees
order by employee_id;

