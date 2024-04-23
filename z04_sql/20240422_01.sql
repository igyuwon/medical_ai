select * from employees;

select employee_id,emp_name from employees;

-- type = number �� ��� ��Ģ���� ����
select salary,salary*1400 k_sal,salary*1400*12 as y_sal from employees;

-- as ��Ī : �÷����� ��Ī�� �ο� as ���� ����
select * from stu_score;

-- ���̽����� �����ϸ� �÷� �̸��� ���������� �Ѿ�´�
select department_id from employees;

-- null : 0 �ϼ��� �ְ� ������ �� �� ���� ���� -> value�� �� �� ����!!
-- Nvl() : null value -> ���� null �� ��� value ���� �ο�����
select nvl(department_id,0) from employees;
select salary,salary + (salary*nvl(commission_pct,0)) as "Real_sal" from employees;

-- oracle�� ��ҹ����� ������ ����! ��Ī(������)�� ��ҹ��� ������ �ϰ� ������ ""�� �ٿ�����(Ư������ ��� ����)
select salary as ���� from employees;

-- as �ѱ� �����ϳ� ������ ��Ī�� �ѱ��� ������ (������ �� �� ����)
select * from departments;

select department_id, department_name from departments;

-- concat (||) : �����͸� �ϳ��� ��ĥ �� ���
-- split() : �����͸� �и���Ŵ
select kor||','||eng||','||math stu from stu_score;
select kor+eng+math as total,(kor+eng+math)/3 from stu_score;

-- �ߺ����� distnct
-- ������ where
select distinct department_id from employees where department_id is not null;
select distinct manager_id from employees where manager_id is not null;

select * from employees;

select employee_id, salary from employees
where employee_id=200 or employee_id=201 or employee_id=202;

select * from employees
where employee_id  >= 200 and employee_id <= 203;

select * from employees
where employee_id <= 150 or employee_id >= 200;

-- department_id 10,30,50�� �ش�Ǵ� ����� ����Ͻÿ�.
select employee_id, department_id from employees
where department_id = 10 or department_id = 30 or department_id=50;

-- ���� 6000 ~ 9000 ������ ����� ����Ͻÿ�.
-- ���� order by �÷� asc : ��������, desc : ��������
select employee_id, salary from employees
where salary >= 6000 and salary <=9000
order by salary asc;

-- ���� 6000,7000,8000�� ����� ����Ͻÿ�.
select employee_id, salary from employees
where salary = 6000 or salary = 7000 or  salary = 8000;

-- �μ���ȣ�� 50�̸鼭, ������ 8000�̻��� ����� ����Ͻÿ�.
select * from employees
where department_id = 50 and salary >= 8000;

-- stu_score ȫ�浿 ����Ͻÿ�.
select * from stu_score
where name = 'ȫ�浿';

-- ��������
select hire_date from employees
order by hire_date asc;

-- ��������
select hire_date from employees
order by hire_date desc;

select emp_name,hire_date from employees
where hire_date >= '02/01/01'
order by hire_date asc;

select hire_date,hire_date+100 from employees;
-- �ݿø� round
select round(sysdate-hire_date,2) from employees;
select * from employees;

-- ������ġ��� +������ �Ұ���, ||��ɾ� ���
select emp_name||email from employees;

-- �Ի��� 05�� �̻� 06�� ���� �̸鼭 ������ 6000�޷� �̻��� ����� �Ի��� �������ķ� ���
select emp_name,hire_date,salary from employees
where hire_date >= '05/01/01' and hire_date <= '06/12/31' and salary >= 6000
order by hire_date desc;

-- !=, <>, not 
select department_id from employees
where department_id != 10 and not department_id = 50
order by department_id;

-- salary 5000 �̻� 9000 ����
select emp_name, salary from employees
where salary >= 5000 and salary <= 9000
order by salary;

-- ����� 99�� �̻��� �л��� �˻��Ͻÿ�.
select * from stu_score
where avg >= 99;

select * from students;

update students set name='������'
where no = 10;
commit;

select * from students;

-- students
-- ��� 70, ��� 75�� �̻��� �л��� ����Ͻÿ�.
select * from students
where kor >= 70 and avg >= 75;

-- �������� 80, �������� 70, �������� 90 �� �л��� ����Ͻÿ�.
select * from students
where kor = 80 or kor = 70 or kor = 90;

-- in���� ������ �ʵ尡 �������� �� �߿� �ϳ��� �˻��� ���
select name, kor from students
where kor not in (80,70,90);

update students set kor=100
where no=1;

rollback;

select * from students
where no=1;

-- ����
update students set kor=100, total=100+eng+math, avg = (100+eng+math)/3
where no=1;

-- �������� 80~90 �̻��� �л��� ����Ͻÿ�.
select * from students
where 80<=kor and 90>=kor
order by kor;

-- between a and b : a���� ũ�ų� ���� b���� �۰ų� ���� �� �˻�
select kor from students
where kor between 70 and 90;

-- not between a and b : a���� ũ�ų�, b���� ���� �� �˻�
select kor from students
where kor not between 70 and 90;

-- ��¥�� between a and b
select hire_date from employees
order by hire_date;

-- �Ի��� 99�⺸�� ũ�ų� ����, 01�⺸�� �۰ų� ���� ��� �˻�
select hire_date from employees
where hire_date >= '99/01/01' and hire_date <= '01/12/31'
order by hire_date;

-- �̸��˻�
select * from students
where name = 'ȫ�浿';

-- like �˻� : Ư��
-- ȫ���� �����ϴ� �ܾ �˻�
select * from students
where name like 'ȫ%';

-- %�� : ������ ������ �ܾ� �˻�
select * from students
where name like '%��';

-- %��% : ���� ���ԵǾ� �ִ� �ܾ� �˻�
select * from students
where name like '%��%';

-- _ :  �� ĭ ������ ���, �� �տ� �Ѱ��� �ܾ �����鼭 ���� ���ԵǾ� �ִ� �ܾ� �˻�
select * from students
where name like '_��%';

-- 3��°�� t�� ���ִ� �̸� �˻�
select * from students
where name like '__t%';

-- �̸��� 4�ڸ���, 3��° r�� �� �ִ� �̸� �˻�
select * from students
where name like '__r_';
-- where name like '__r%' and length(name)=4;

-- �̸��� A�� ���۵Ǵ� �� �˻�
select no,name from students
where name like 'A%';

-- �̸��� a�� �� �ִ� �л� �˻�
select no,name from students
where name like '%a%';

-- ��ҹ��� ���� ���� a�� �� �ִ� �л� �˻�
-- �ҹ��� ġȯ (lower), �빮�� ġȯ (upper), ù���� �빮�� (initcap)
select no, name from students
where lower(name) like '%a%';

-- a�� ���Ե��� ���� �̸��� �˻�
select no, name from students
where lower(name) not like '%a%';

-- manager_id 100�� ��� �˻�
select employee_id,emp_name,manager_id from employees
where manager_id=100;

-- null�� ��񱳰� �ȵ�.
select employee_id,emp_name,manager_id from employees
where manager_id=null;

-- null ���� is null ��ɾ� ���
select employee_id,emp_name,manager_id from employees
where manager_id is null;

select employee_id,emp_name,manager_id from employees
where manager_id is not null;

-- �ѱ����� ����
select * from stu_score
order by name asc;

select * from students;

-- 1�� ���������� �������� �� ����, ���� ������ ���, ���������� �������� ����
select * from students
order by kor desc, eng asc;

select * from students
order by total desc;

alter table students add rank number(3);

-- �÷�Ÿ��
desc students;

select * from students;

update students set rank=0;
commit;

-- ���
select no, rank() over(order by total desc) as rank from students;

update students s1 set rank = (select ranks
from (select no,rank() over(order by total desc ) as ranks from students) s2
where s1.no = s2.no );

-- ����
update students set rank=13
where no=1;
rollback;
select * from students;

select * from (select * from students where avg >= 70)
where kor >=70;







