import requests
from bs4 import BeautifulSoup
url="https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
type_tr = soup.find('tr',{'class':'type1'})

print("th : ",type_tr.th)
print("find_next_sibling : ",type_tr.th.find_next_sibling("th")) # 현재 th에서 다음 th를 찾아줌.
print("next : ",type_tr.th.next) # th태그 다음단락
print("next : ",type_tr.th.next.next)
print("next : ",type_tr.th.next.next.next)