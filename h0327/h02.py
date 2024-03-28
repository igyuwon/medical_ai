# 파일을 읽어와서 출력

# 파일열기
with open('/Users/igyuwon/Medical_ai/medical_ai/h0327/aaa/member2.csv','r',encoding='utf8') as f:

    while True:
        txt = f.readline()
        if txt == "": break
        mem = txt.split(",")
        print(mem[0],mem[1])
