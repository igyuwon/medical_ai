import oracledb

# 평균점수를 입력받아 입력한 평균 점수 이상의 학생을 출력하시오.
# 반복해서 진행하고 -1을 입력받으면 프로그램을 종료
while True:
    # DB connent 연결
    conn = oracledb.connect(user="ora_user", password="1111",dsn="localhost:1521/xe")
    cursor = conn.cursor()
    avg = input("학생의 평균을 입력하세요(-1.종료) : ")
    if avg == '-1':
        break
    sign = input("부등호를 입력하세요 : ")


    sql = f'''
    select name, round(avg,2) avg from stu_score
    where avg {sign} {avg}
    '''

    cursor.execute(sql)
    data = cursor.fetchall()
    print('-'*40)
    print("이름\t평균")
    print('-'*40)
    for d in data:
        print(d[0],end='\t')
        print(d[1])
    conn.close()
print('프로그램을 종료합니다.')
conn.close()
