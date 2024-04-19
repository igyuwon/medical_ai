import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res = requests.get(url, headers = headers)
res.raise_for_status()
# print(type(res.text))

# with open("stock.html","w",encoding="utf-8") as f:
#     f.write(res.text)

soup = BeautifulSoup(res.text,"lxml") # text를 html 파싱
# print(type(soup))

# with open("stock2.html","w",encoding="utf8") as f:
#     f.write(soup.prettify()) # html 소스를 정렬해서 출력해줌

# print("<title> : ",soup.title) # 태그를 입력
# print("<title> 텍스트 : ",soup.title.get_text()) # 태그의 글자를 가져옴
# print("<title> 텍스트 : ",soup.title.text) # 태그의 글자를 가져옴
print("<a> 태그 : ",soup.a)
print("<a> 태그글자 : ",soup.a.text)
print("<a> 속성전체 : ",soup.a.attrs) # 태그의 속성값 모두 가져옴

print("<a>[1게속성] : ",soup.a["href"]) # 태그의 1개 속성 가져옴