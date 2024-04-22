import requests
from bs4 import BeautifulSoup

url="https://www.google.com/search?q=%ED%99%98%EC%9C%A8+1%EB%8B%AC%EB%9F%AC"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

# print(soup)

# with open('google1.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())

print("title : ",soup.title.soup)

# attrs : 해당 태그의 속성값 모두 출력
exchange_rate_class = soup.find("input",{"class":"lWzCpb ZEB7Fb"})
print(exchange_rate_class.attrs)
usa_value = exchange_rate_class["value"]
print("미국달러 : "+usa_value)
exchange_rate_class = soup.find("input",{"class":"lWzCpb a61j6"})
kor_value = exchange_rate_class["value"]
print("원화 : "+kor_value)

