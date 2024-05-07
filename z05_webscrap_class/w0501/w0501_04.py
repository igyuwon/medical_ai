import oracledb

while True:
    # hhh,1111,홍길자,여자,sysdate
    id = input("아이디를 입력하세요(-1. 종료) : ")
    if id == '-1':
        break

    # id로 검색을 먼저 한 후 데이터를 입력하도록 해야 함.
    # id가 존재하면 id 를 다시 입력, id가 존재하지 않으면 패스워드 입력받음.
    #####
    sql = f'''
    select * from member
    where id = '{id}'
    '''
    conn = oracledb.connect(user="ora_user", password="1111",dsn = "localhost:1521/xe")
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    # print('id 개수 : ',len(data))

    # ID가 존재하는지 확인
    if len(data)==1:
        print('ID가 존재합니다. 다른 아이디를 입력해주세요')
        continue

    pw = input("패스워드를 입력하세요 : ")
    name = input("이름을 입력하세요 : ")
    gender = input("성별을 입력하세요 : ")

    # db연결, 해제
    sql = f'''
    insert into member values(member_seq.nextval,'{id}','{pw}','{name}','{gender}',sysdate)
    '''
    conn = oracledb.connect(user="ora_user", password="1111",dsn = "localhost:1521/xe")
    cursor= conn.cursor()
    cursor.execute(sql)
    cursor.execute('commit')

    print("입력이 완료되었습니다.")


    cursor.close()
    conn.close()