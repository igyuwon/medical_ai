select * from employees;
-- ȸ������ ���̺� ����
create table member(
    id varchar2(20),
    pw varchar2(20),
    name varchar2(20),
    phone varchar2(20)
);

-- ������ �Է�
insert into member(id,pw,name,phone) values(
'aaa','1111','ȫ�浿','010-1111-1111'
);

insert into member values(
'bbb','1111','������','010-2222-2222'
);

insert into member (id,name,phone) values(
'ccc','�̼���','010-3333-3333'
);
-- �÷��� ���� ����
/*
insert into member values(
'ddd','������','010-4444-4444'
);
*/

select id,pw,name,phone from member;

commit;

rollback;

select id,name from member;
select * from member;

insert into member values(
'ddd','1111','������','010-4444-4444'
);

select * from member;

rollback;

commit;

update member set pw='2222' where id='ccc';

select * from member;

rollback;

-- ��� ���̺� Ȯ��
select * from tab;

-- ���̺� Ÿ�� Ȯ��
desc member;

-- ����Ŭ Ÿ��
-- number-����, date-��¥, char-��������, varchar2-��������, clob-��뷮����

-- number : ����, �Ǽ�
-- number(4) : -9999~9999

create table mem(
no number, -- ���� �������� ����.
no2 number(4),
no3 number(4,2)
);

insert into mem (no) values(1234567890);
insert into mem (no2) values(9999);
insert into mem (no2) values(1.11);
insert into mem (no2) values(11111); -- ����
insert into mem (no2) values(-9999);

insert into mem (no3) values(11.11);
insert into mem (no3) values(111); -- 111.00

select * from mem;

create table mem2(
no number(4,2),
mdate date,
mdate2 timestamp -- date : ��,��,��,��,��,�ʱ��� ���尡�� / timestamp �и��ʱ��� ���尡����.
);

insert into mem2 (mdate) values ('2024-04-19');
insert into mem2 (mdate) values (sysdate); -- sysdate:����ð�
insert into mem2 (mdate2) values (sysdate);
insert into mem2 (mdate,mdate2) values (sysdate,sysdate+30);

select * from mem2;
select to_char(mdate,'yyyy-mm-dd hh:mi:ss') from mem2;
select to_char(mdate2,'yyyy-mm-dd hh:mi:ss:ff') from mem2;

select mdate,mdate+30 from mem2;

select * from employees;

select sysdate-hire_date from employees;

create table mem3(
no number(4,2),
tel char(8),
name varchar2(9),
mdate date,
mdate2 timestamp
);
-- char, varchar2
-- char : ��������
insert into mem3(tel) values('11112222');
insert into mem3(tel) values('22223333');
insert into mem3(tel) values('111');
insert into mem3(tel) values('123456789');
insert into mem3(tel) values('ȫ');

-- varchar2 : ��������
insert into mem3(name) values('11112222');
insert into mem3(name) values('ȫ�浿'); -- �ѱ� : 3ũ��
insert into mem3(name) values('�Ż��Ӵ�'); -- 12�ڸ� �ʿ�
insert into mem3(name) values('AAA');
insert into mem3(name) values('aaa');
select * from mem3;
commit;
select * from mem3 where name='aaa'; -- sql ������ ��ҹ��� ���о���, �����ʹ� ��ҹ��� ������.
select * from mem3 where name='AAA';
select * from mem3 where lower(name)='aaa';

-- select, from 2���� Ű����� ���� ��.
-- * ��� �÷��� ���
-- ��ҹ��ڸ� �������� ����
select * from mem;

select emp_name,department_id from employees;

-- distinct : ���� ���� 1���� ���
select distinct department_id from employees;

select * from departments;
select department_id, department_name from departments;

select * from departments;
select * from employees;
select * from jobs;
select * from products;

select no,mdate2,tel,name,mdate from mem3;

-- �����ȣ, ����̸�, �޿�, �Ի�����
select employee_id,emp_name,salary,hire_date from employees;

desc employees;

select * from stu_score;
drop table stu_scroe;

create table stu_score(
no number,
name varchar2(30),
kor number(3),
eng number(3),
math number(3),
total number(3),
avg number(5,2),
rank number
);

insert into stu_score values(
1,'ȫ�浿',100,100,100,300,100,1
);
insert into stu_score values(
5,'�豸',100,100,100,300,100,1
);

select * from stu_score;

commit;

-- ��������� numberŸ���� ���
insert into stu_score values(
6,'������',100,95,96,(100+95+96),(100+95+96)/3,1
);
select * from stu_score;

insert into stu_score values(
7,'ȫ����',100,100,99,(100+100+99),(100+100+99)/3,1
);

select * from stu_score;
-- ��ȣ, �̸�, ��������, ��������-20, ���, ��������-20�� �� ���
select no,name,kor,kor-20,avg,(kor-20+eng+math)/3 from stu_score;

select * from employees;

-- �޷�, ��ȭ ȯ�� - 1381.79
select employee_id,emp_name,salary from employees;
select employee_id,emp_name,salary,salary*1381.79 from employees;

-- ���� * 12 = ����
select salary*12,salary*1381.79*12 from employees;
select salary*12 as �޷����ؿ���,salary*1381.79*12 as ��ȭ���ؿ��� from employees;

-- Ŀ�̼��� ���� ���� = ���� + ����*Ŀ�̼�
-- commission_pct
select * from employees;
select salary+(salary*commission_pct) from employees;
select employee_id,emp_name,salary,salary+(salary*commission_pct) from employees;

select employee_id,emp_name,salary,commission_pct,salary+(salary*commission_pct) from employees;
-- nvl(�÷�,0)
select employee_id,emp_name,nvl(commission_pct,0),salary+(salary*nvl(commission_pct,0)) from employees;



