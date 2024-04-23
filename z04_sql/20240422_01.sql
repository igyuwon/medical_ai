select * from employees;

select employee_id,emp_name from employees;

-- type = number 인 경우 사칙연산 가능
select salary,salary*1400 k_sal,salary*1400*12 as y_sal from employees;

-- as 별칭 : 컬럼명을 별칭을 부여 as 생략 가능
select * from stu_score;

-- 파이썬으로 연결하면 컬럼 이름이 변수명으로 넘어온다
select department_id from employees;

-- null : 0 일수도 있고 무한의 값 일 수도 있음 -> value를 알 수 없음!!
-- Nvl() : null value -> 값이 null 인 경우 value 값을 부여해줌
select nvl(department_id,0) from employees;
select salary,salary + (salary*nvl(commission_pct,0)) as "Real_sal" from employees;

-- oracle은 대소문자의 구별이 없음! 별칭(변수명)에 대소문자 구별을 하고 싶으면 ""를 붙여야함(특수문자 사용 가능)
select salary as 월급 from employees;

-- as 한글 가능하나 가급적 별칭에 한글은 지양함 (에러가 날 수 있음)
select * from departments;

select department_id, department_name from departments;

-- concat (||) : 데이터를 하나로 합칠 때 사용
-- split() : 데이터를 분리시킴
select kor||','||eng||','||math stu from stu_score;
select kor+eng+math as total,(kor+eng+math)/3 from stu_score;

-- 중복제거 distnct
-- 조건절 where
select distinct department_id from employees where department_id is not null;
select distinct manager_id from employees where manager_id is not null;

select * from employees;

select employee_id, salary from employees
where employee_id=200 or employee_id=201 or employee_id=202;

select * from employees
where employee_id  >= 200 and employee_id <= 203;

select * from employees
where employee_id <= 150 or employee_id >= 200;

-- department_id 10,30,50에 해당되는 사원을 출력하시오.
select employee_id, department_id from employees
where department_id = 10 or department_id = 30 or department_id=50;

-- 월급 6000 ~ 9000 이하인 사원을 출력하시오.
-- 정렬 order by 컬럼 asc : 순차정렬, desc : 역순정렬
select employee_id, salary from employees
where salary >= 6000 and salary <=9000
order by salary asc;

-- 월급 6000,7000,8000인 사원을 출력하시오.
select employee_id, salary from employees
where salary = 6000 or salary = 7000 or  salary = 8000;

-- 부서번호가 50이면서, 월급이 8000이상인 사원을 출력하시오.
select * from employees
where department_id = 50 and salary >= 8000;

-- stu_score 홍길동 출력하시오.
select * from stu_score
where name = '홍길동';

-- 순차정렬
select hire_date from employees
order by hire_date asc;

-- 역순정렬
select hire_date from employees
order by hire_date desc;

select emp_name,hire_date from employees
where hire_date >= '02/01/01'
order by hire_date asc;

select hire_date,hire_date+100 from employees;
-- 반올림 round
select round(sysdate-hire_date,2) from employees;
select * from employees;

-- 문자합치기는 +연산자 불가능, ||명령어 사용
select emp_name||email from employees;

-- 입사일 05년 이상 06년 이하 이면서 월급이 6000달러 이상인 사원을 입사일 역순정렬로 출력
select emp_name,hire_date,salary from employees
where hire_date >= '05/01/01' and hire_date <= '06/12/31' and salary >= 6000
order by hire_date desc;

-- !=, <>, not 
select department_id from employees
where department_id != 10 and not department_id = 50
order by department_id;

-- salary 5000 이상 9000 이하
select emp_name, salary from employees
where salary >= 5000 and salary <= 9000
order by salary;

-- 평균이 99점 이상인 학생을 검색하시오.
select * from stu_score
where avg >= 99;

select * from students;

update students set name='관순스'
where no = 10;
commit;

select * from students;

-- students
-- 국어가 70, 평균 75점 이상인 학생을 출력하시오.
select * from students
where kor >= 70 and avg >= 75;

-- 국어점수 80, 국어점수 70, 국어점수 90 인 학생을 출력하시오.
select * from students
where kor = 80 or kor = 70 or kor = 90;

-- in연산 동일한 필드가 여러개의 값 중에 하나를 검색할 경우
select name, kor from students
where kor not in (80,70,90);

update students set kor=100
where no=1;

rollback;

select * from students
where no=1;

-- 수정
update students set kor=100, total=100+eng+math, avg = (100+eng+math)/3
where no=1;

-- 국어점수 80~90 이상인 학생을 출력하시오.
select * from students
where 80<=kor and 90>=kor
order by kor;

-- between a and b : a보다 크거나 같고 b보다 작거나 같은 것 검색
select kor from students
where kor between 70 and 90;

-- not between a and b : a보다 크거나, b보다 작은 것 검색
select kor from students
where kor not between 70 and 90;

-- 날짜도 between a and b
select hire_date from employees
order by hire_date;

-- 입사일 99년보다 크거나 같고, 01년보다 작거나 같은 사원 검색
select hire_date from employees
where hire_date >= '99/01/01' and hire_date <= '01/12/31'
order by hire_date;

-- 이름검색
select * from students
where name = '홍길동';

-- like 검색 : 특정
-- 홍으로 시작하는 단어를 검색
select * from students
where name like '홍%';

-- %순 : 순으로 끝나는 단어 검색
select * from students
where name like '%순';

-- %길% : 길이 포함되어 있는 단어 검색
select * from students
where name like '%길%';

-- _ :  한 칸 공간을 사용, 길 앞에 한개의 단어가 있으면서 길이 포함되어 있는 단어 검색
select * from students
where name like '_길%';

-- 3번째에 t가 들어가있는 이름 검색
select * from students
where name like '__t%';

-- 이름이 4자리인, 3번째 r이 들어가 있는 이름 검색
select * from students
where name like '__r_';
-- where name like '__r%' and length(name)=4;

-- 이름이 A로 시작되는 것 검색
select no,name from students
where name like 'A%';

-- 이름에 a가 들어가 있는 학생 검색
select no,name from students
where name like '%a%';

-- 대소문자 구분 없이 a가 들어가 있는 학생 검색
-- 소문자 치환 (lower), 대문자 치환 (upper), 첫글자 대문자 (initcap)
select no, name from students
where lower(name) like '%a%';

-- a가 포함되지 않은 이름을 검색
select no, name from students
where lower(name) not like '%a%';

-- manager_id 100인 사원 검색
select employee_id,emp_name,manager_id from employees
where manager_id=100;

-- null은 등가비교가 안됨.
select employee_id,emp_name,manager_id from employees
where manager_id=null;

-- null 값은 is null 명령어 사용
select employee_id,emp_name,manager_id from employees
where manager_id is null;

select employee_id,emp_name,manager_id from employees
where manager_id is not null;

-- 한글정렬 가능
select * from stu_score
order by name asc;

select * from students;

-- 1차 국어점수로 역순정렬 한 다음, 같은 점수인 경우, 영어점수로 순차정렬 진행
select * from students
order by kor desc, eng asc;

select * from students
order by total desc;

alter table students add rank number(3);

-- 컬럼타입
desc students;

select * from students;

update students set rank=0;
commit;

-- 등수
select no, rank() over(order by total desc) as rank from students;

update students s1 set rank = (select ranks
from (select no,rank() over(order by total desc ) as ranks from students) s2
where s1.no = s2.no );

-- 수정
update students set rank=13
where no=1;
rollback;
select * from students;

select * from (select * from students where avg >= 70)
where kor >=70;







