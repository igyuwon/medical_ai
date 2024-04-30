import oracledb

# sql
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor() # db와 연결되어 지시자 생성

sql = "select * from stu_score"
cursor.execute(sql) # cursor에 select한 결과값을 저장(결과값 : list)
data = cursor.fetchall() # fetchall():모든 데이터 가져옴. fetchone() : 1개의 데이터 가져옴.

print("[ 모든 데이터 출력 ]")
# print(data)
for d in data:
    print(d)
print("-"*40)
print("타입 : ",type(data))