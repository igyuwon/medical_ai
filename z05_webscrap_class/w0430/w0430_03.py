import oracledb

# DB connent 연결
conn = oracledb.connect(user="ora_user", password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

# # sql 실행
# sql = '''
# select employee_id, emp_name,salary,salary+(salary*nvl(commission_pct,0)) real_salary, 
# to_char(salary*1410,'99,999,999') kor_salary 
# from employees
# order by employee_id
# '''
# sql = '''

# select * employees;
# '''
# employee_id

# 부서별 평균월급, 최대월급, 최소월급을 출력하시오.
sql = '''select department_id,round(avg(salary),2),min(salary),max(salary) from employees
where department_id is not null
group by department_id
order by department_id'''
cursor.execute(sql)
data = cursor.fetchall()

# sql 실행
# employees 테이블에서 사원번호, 이름, 월급, 실제월급(월급+(월급*커미션)), 월급 *1410(원)원화로 환산해서
# 천단위 표시해서 출력

print("[데이터 출력]")
print('-'*80)
# print('사원번호\t사원명\t월급\t실제월급\t원화환산')
# print('-'*80)
for d in data:
    print(d[0],end='\t')
    print(d[1],end='\t')
    print(d[2],end='\t')
    print(d[3])
    # print("￦"+d[4].strip())

conn.close()
