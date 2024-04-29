
-- ���Ἲ �������� : �������� �ڷᰡ �Էµ��� �ʵ��� �ϱ� ���� ��Ģ
-- not null, unique, primary key, foreign key, check
create table member(
memNo number(4) not null,
id varchar2(30) primary key,
pw varchar2(30) not null,
name varchar2(30),
gender varchar2(6) check(gender in('����','����')),
mdate date default sysdate
);

-- ������ �Է�, ���, ����, ���� �κ�
insert into member (memNo, id,pw,name,gender,mdate) values (
member_seq.nextval,'aaa','1111','ȫ�浿','����',sysdate
);
insert into member (memNo, id,pw,name,gender) values (
member_seq.nextval,'bbb','1111','������','����'
);

insert into member values(
member_seq.nextval,'ccc','1111','�̼���','����',sysdate
);

-- ���̺� ����
create table board(
bno number(4) primary key,
id varchar2(30), -- �ܷ�Ű ���
btitle varchar2(1000),
bcontent varchar2(4000),
bdate date default sysdate,
bgroup number(4),
bstep number default 0,
bindent number default 0,
bhit number default 1,
bfile varchar2(100) default '',
constraint fk_id foreign key(id) -- �ܷ�Ű(foreign key)�� ��Ī : fk_id
references member(id) -- member ���̺��� primary key id
);

-- primary key�� �����Ϸ��� foreign key ��ϵǾ��ִ� �����͸� �켱 ������ ��� �ؾ���.
-- primary key �����Ǹ� ��� �����ϴ� ��� - on delete cascade, ��� �����ϴ� ��� on update cascade
insert into board(bno, id, btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile) values(
board_seq.nextval,'aaa','�����Դϴ�.','�����Դϴ�.', sysdate,board_seq.currval,0,0,1,''
);

insert into board values(
board_seq.nextval,'bbb','�����Դϴ�.2','�����Դϴ�.2', sysdate,board_seq.currval,0,0,1,''
);

insert into board(bno, id, btitle,bcontent,bgroup) values(
board_seq.nextval,'aaa','�����Դϴ�.3','�����Դϴ�.3', board_seq.currval
);

select * from board;

-- ����
delete board where bno=3;

commit;

delete member where id='aaa';

-- DECODE ���ǹ�
select emp_name,department_id,
decode(department_id,
10,'�ѹ���ȹ��',
20,'������',
30,'����/�����',
40, '�λ��'
)
from employees
order by department_id asc;

select department_id, department_name from departments;

select name,avg,
decode(avg,
90,'A',
80,'B',
70,'C'
) as grade
from stu_score order by avg desc;
-- 90��-A, 80��-B, 70��-C

-- sh_clerk salary * 15%, ad_asst * 10 % MK_rep * 5% �λ�;
select job_id, salary,
decode(job_id,
'SH_CLERK', salary*1.15,
'AD_ASST', salary*1.1,
'MK_REP', salary*1.05
) as salary_up
from employees;

-- job_id, clerk�� �� �ִ� job_id�� �˻��Ͻÿ�
select job_id from employees;

-- LIKE _ �ڸ���, % ����
select job_id from employees
where job_id like '%CLERK%';

select name, avg from stu_score;

select name, avg,
case 
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
else 'F'
end as grade
from stu_score;

select department_id, department_name from departments;

-- case����, department_id �̸��� ���
select department_id from employees
order by department_id asc;

select department_id ,
case
when department_id=10 then '�ѹ���ȹ��'
when department_id=20 then '������'
when department_id=30 then '����/�����'
when department_id=40 then '�λ��'
when department_id=50 then '��ۺ�'
when department_id=60 then 'IT'
when department_id=70 then 'ȫ����'
when department_id=80 then '������'
when department_id=90 then '��ȹ��'
when department_id=100 then '�ڱݺ�'
when department_id=110 then '�渮��'
when department_id=120 then '�繫��'
when department_id=130 then '������'
when department_id=140 then '�ſ������'
when department_id=150 then '�ֽİ�����'
when department_id=160 then '���Ͱ�����'
when department_id=170 then '������'
when department_id=180 then '�Ǽ���'
when department_id=190 then '�����'
when department_id=200 then '���'
else '�ʹ� ����'
end as department_name
from departments;

-- ������ ����Ͻÿ�.
-- job_id
-- CLERK ���� : salary*15%, ad_asst*10%, rep*5%,man*2%

select job_id, salary,
case
when job_id like '%CLERK%' then salary+(salary*0.15)
when job_id like '%ASST%' then salary+(salary*0.1)
when job_id like '%REP%' then salary+(salary*0.05)
when job_id like '%MAN%' then salary+(salary*0.02)
end as salary_up
from employees
order by salary_up asc;

-- ���� ��� ���� 0.15 ����̻� 0.05 �λ��ؼ� ����Ͻÿ�.
-- �� ���̺� �����ؼ� ���

-- employees ���̺��� �˻� - salary_updown�� ����
select emp_name,salary,
case
when (select avg(salary) from employees) >= salary then salary+(salary*0.15)
when (select avg(salary) from employees) < salary then salary+(salary*0.05)
end as salary_up
from employees
order by salary_up asc;

-- employees ���̺��� �˻� - salary_updown�� ����
select emp_name,salary,salary_updown,
case
when (select avg(salary) from employees) >= salary then salary+(salary*0.15)
when (select avg(salary) from employees) < salary then salary+(salary*0.05)
end as salary_up
from (
select a.*,
case
when (select avg(salary) from employees) >= salary then 'down'
when (select avg(salary) from employees) < salary then 'up'
end as salary_updown
from employees a
order by salary asc
)
order by salary_up asc;

-- case 2�� ���
select emp_name,salary,
case
when (select avg(salary) from employees) >= salary then 'up'
when (select avg(salary) from employees) < salary then 'down'
end as salary_updown
,
case
when (select avg(salary) from employees) >= salary then salary+(salary*0.15)
when (select avg(salary) from employees) < salary then salary+(salary*0.05)
end as salary_up

from employees
order by salary_up asc;

select * from stu_score;
select no, name, total, rank from stu_score
order by total desc
;

-- rank() �Լ�
select total,rank, rank() over(order by total desc) as ranks from stu_score;
select no,rank() over (order by total desc) as ranks from stu_score;

select total,rank from stu_score
order by total desc;

update stu_score set rank = 1
where total=291;

-- 1000���� ������ ���� �Է�
update stu_score a
set rank = (
select ranks from(
select no,rank() over (order by total desc) as ranks from stu_score
) b
where a.no = b.no
);

-- commit;

select  * from stu_score
order by rank asc;

select emp_name,department_id from employees;
select department_id, department_name from departments;


select emp_name, employees.department_id, department_name from employees, departments
where employees.department_id = departments.department_id;

-- �׷��Լ� sum,avg.count,max,min stddev ǥ������, variance �л�
-- ������ ����
select sum(salary) from employees;

-- �������� ���� stu_score
select sum(kor) from stu_score;

select count(*) from employees;

select count(*) from employees
where department_id = 50;

-- Ŀ�̼��� �޴� ����� ���� ���Ͻÿ�.
select count(*) from employees
where commission_pct is not null;
select count(commission_pct) from employees;

-- Ŀ�̼��� �ִ� ����� �˻��Ͻÿ�.
select emp_name,commission_pct from employees
where commission_pct is not null;

select emp.employee_id from employees emp;

-- ��ü�����
select count(*) from employees;

-- �μ� ��ȣ�� 50���� �����
select count(*) from employees
where department_id = 50;

select department_id,count(department_id) from employees
group by department_id
order by department_id asc;

select * from stu_score;

-- avg grade
-- stu_score 90�� �̻� A, 80���̻� B, 70���̻� C, 60���̻� D, 60�� �̸� F
select grade,count(grade) from(
select name,avg,
case
when avg >= 90 then 'A'
when avg >= 80 then 'B'
when avg >= 70 then 'C'
when avg >= 60 then 'D'
else 'F'
end as grade
from stu_score
)
group by grade
order by grade asc
;
select kor, trunc(kor,-1) from stu_score;

-- kor ������ 91,92,93,....,99->90 / 81,...,89 -> 80 count
select trunc(kor,-1),count(*) from stu_score
where trunc(kor,-1)=90
group by trunc(kor,-1)
;
select k_kor,count(k_kor) as k_count from(
select trunc(kor,-1) as k_kor from stu_score)
group by k_kor
;

-- �׷��Լ� group by ���
select department_id, count(*) from employees
group by department_id
order by department_id;

select emp_name,count(emp_name) from employees
group by emp_name;

-- �μ��� ��� ������ ���Ͻÿ�.
select department_id, round(avg(salary),2) from employees
group by department_id
order by department_id;

select job_id, count(job_id) from employees
where job_id like '%CLERK%'
group by job_id;

-- CLERK, REP, MAN �� ���� ���
select job_id, avg(salary) from employees
where job_id like '%CLERK%' or job_id like '%REP%' or job_id like '%MAN%'
group by job_id;
;

-- CLERK�� ��µǵ��� �Ͻÿ�
select job_id,length(job_id) from employees;
select job_id, substr(job_id,4,length(job_id)-3) from employees;

select substr(job_id,4,7) as job_id, count(substr(job_id,4,7)) as c_job_id from employees
group by substr(job_id,4,7)
order by c_job_id;

-- �μ��� �ִ� ����, �ּ� ����, ��� ���� ���
select department_id,max(salary) max_sal,min(salary) min_sal,round(avg(salary),2) avg_sal 
from employees
where department_id is not null
group by department_id
order by department_id;

select a.department_id,department_name,count(salary),sum(salary),round(avg(salary),2),max(salary),min(salary)
from employees a,departments b
where a.department_id = b.department_id
group by a.department_id,department_name
order by a.department_id
;

-- �μ��� ��� ��
select department_id,count(department_id) from employees
group by department_id;

-- null�� �ƴ� �� : 35��
select commission_pct from employees
where commission_pct is not null;

-- Ŀ�̼��� �޴� ��� ��
select department_id,count(*),count(commission_pct) from employees
group by department_id;


-- emp_name �ι�° ���ڰ� a�� �����ϴ� ���� ����
select emp_name from employees
where emp_name not like '_a%';

-- having group by ������, where �Ϲ� �÷��� ������
select department_id, round(avg(salary),2) from employees
group by department_id
order by avg(salary);

select department_id, round(avg(salary),2) 
from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= 6000
order by avg(salary);


select department_id, round(avg(salary),2) 
from employees
where emp_name not like '_a%'
group by department_id
having avg(salary) >= (select avg(salary) from employees)
order by avg(salary);

-- �μ��� �ִ������ 8000�̻��� �μ�, �ִ� ������ ����Ͻÿ�
select department_id, max(salary) from employees
group by department_id
having max(salary) >= 8000
order by max(salary) desc;

-- ����
select emp_name, department_id, salary from employees;
select department_id, department_name from departments;

select * from employees, departments;

select count(*) from employees;
select count(*) from departments;

-- ���̺� 2�� ������ ���� �����̶�� ��.
-- 107*27 = 2889
select count(*) from employees, departments;

-- equi join
-- �� ���̺� ���� �÷��� ������ ���ؼ� �ش�Ǵ� �����͸� ���
-- equi join - 106��, null 1�� �˻���������.
select employee_id, emp_name, employees.department_id, department_name, salary 
from employees,departments
where employees.department_id = departments.department_id;

select department_id,department_name from departments;

select id, name from member;
select id,btitle,bcontent from board;

select * from member;

update member set name = 'ȫ����'
where id = 'aaa';

select bno,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile from board,member
where member.id = board.id;








