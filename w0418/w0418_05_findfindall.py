import requests
from bs4 import BeautifulSoup
url="https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# print(soup)
# 태그로 찾는 방법 title,get_text(),text,a.attrs,a["href"]
# find : 태그정보 찾기 함수, class로 찾는 방법
# print(soup.find(attrs={"class":"box_type_l"}))
# print(soup.find("tr",{"class":"type1"}))
type_tr = soup.find("tr",{"class":"type1"}) # find, find_all, class
print("th : ",type_tr.th) # 1개만 - 첫번째 만나는 th 태그를 찾아줌
print(type_tr.find_all("th")) # 모든것 - 모든 th 태그 찾아줌.
ths = type_tr.find_all("th")
for th in ths:
    print("제목 : ", th.text)

