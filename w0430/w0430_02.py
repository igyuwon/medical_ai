import oracledb

# sql
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() # db와 연결되어 지시자 생성

# stu_score avg 90점 이상 A, 80이상 B, C, D, 60점 미만 F
# 학번, 이름, 합계, 평균, 학점 출력
# sql = "select no,name,total,avg,\
#     case\
#     when avg >= 90 then 'A'\
#     when avg >= 80 then 'B'\
#     when avg >= 70 then 'C'\
#     when avg >= 60 then 'D'\
#     else 'F'\
#     end as grade\
#     from stu_score\
#     order by grade"

# board 정보에서 id, name 포함해서 데이터를 가져와 출력하시오.
# board 테이블 id, member 테이블 name
# board 테이블 id, member 테이블 name

# sql = "select bno, a.id,name,btitle,bcontent,bdate,bgroup,bstep,bindent,bhit,bfile\
#     from board a,member b\
#     where a.id = b.id"


# print("[ 모든 데이터 출력 ]")
# # print(data)
# for d in data:
#     print("-"*20)
#     print(d)
# print("-")

sql = "select * from stu_score"

cursor.execute(sql) # cursor에 select한 결과값을 저장(결과값 : list)
data = cursor.fetchall() # fetchall():모든 데이터 가져옴. fetchone() : 1개의 데이터 가져옴.
# 평균을 가지고 파이썬을 프로그램하여 학점을 출력하시오.
# 학번, 이름, 합계, 평균, 학점
# for d in data:
#     no, name, total, avg = d[0], d[1], d[5], d[6]
#     if avg >= 90:
#         grade = 'A'
#     elif avg >= 80:
#         grade = 'B'
#     elif avg >= 70:
#         grade = 'C'
#     elif avg >= 60:
#         grade = 'D'
#     else:
#         garde = 'F'
#     print("학번 : ",no)
#     print("이름 : ",name)
#     print("총점 : ",total)
#     print("평균 : ",avg)
#     print("학점 : ",grade)
#     print("-"*40)

# print("타입 : ",type(data))

# salary 평균을 출력하시오.
sql = "select round(avg(salary),2) as salary from employees"
cursor.execute(sql)
data = cursor.fetchone()
print(data[0])

conn.close()