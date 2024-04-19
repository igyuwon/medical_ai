import requests # 웹정보 라이브러리
# url = "http://www.google.com"
# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/#google_vignette"
url = "http://www.melon.com"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}

# res = requests.get("http//www.google.com")
res = requests.get(url, headers = headers)
res.raise_for_status() # 에러코드 발생 시 프로그램을 종료

print(res.text)

# with open("user_agent.html","w",encoding="utf-8") as f:
#     f.write(res.text)