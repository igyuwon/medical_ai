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

select department_id,round(avg(salary),2),min(salary),max(salary) from employees
where department_id is not null
group by department_id
order by department_id;

-- 홍 이라고 검색하면 홍에 관련된 학생 모두 검색
select * from stu_score
where name like '%홍%'
order by no asc;

select name, avg from stu_score
where avg >= 60
order by no;

-- 사원번호, 사원명, 부서번호, 부서명을 출력하시오.
select employee_id, emp_name, a.department_id, department_name
from employees a, departments b
where a.department_id = b.department_id and emp_name like '_a%'
and salary >= (select avg(salary) from employees);

-- 그리고, 두번째 자리에 a가 들어가는 사원을 검색하시오.
select emp_name from employees
where emp_name like '_a%';

-- 월급이 평균이상인 사람만 검색하시오.
select salary from employees
where salary >= (select avg(salary) from employees);

select * from employees;
select * from departments;
select * from jobs;

-- 사원번호 e, 사원명 e, 부서번호 e, 부서명 d, 직급번호 e, 직급명 출력하시오
select e.employee_id, e.emp_name, e.department_id, d.department_name, j.job_id, j.job_title
from employees e, departments d, jobs j
where j.job_id =  e.job_id and e.department_id= d.department_id;

-- 사원번호, 사원명, 월급, 최소월급분,직급, 직급타이틀
-- 최소월급 몇 % 이상을 받고 있는 출력(최소월급 / 현재월급 * 100)
select employee_id, emp_name, salary, to_char(round(((salary - min_salary)/salary)*100,2))||'%', e.job_id, job_title
from employees e, jobs j
where e.job_id = j.job_id;

select job_id, job_title from jobs;


