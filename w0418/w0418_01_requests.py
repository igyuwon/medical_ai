#------------------------기본구문------------------------------
import requests # 웹정보 라이브러리
url = "http://www.google.com"
url = "http://www.melon.com"
# res = requests.get("http//www.google.com")
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status() # 에러코드 발생 시 프로그램을 종료
#------------------------------------------------------------

if res.status_code == requests.codes.OK: # 응답코드 : 200
    print("정상적인 페이지 호출")
else:
    print("접근 할 수 없음[ 에러코드 : ",res.status_code,"]")
    
print(res)

res.raise_for_status() # 에러코드 발생 시 프로그램을 종료