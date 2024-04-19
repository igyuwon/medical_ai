import requests
from bs4 import BeautifulSoup

url="https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

s_all = soup.find('div',{'class':'box_type_l'})
tr_list = s_all.find_all('tr')

# print(tr_list)

for i in range(2,15,1):
    s = tr_list[i]
    td_list = s.find_all('td')
    if len(td_list) == 1:
        continue
    print("-"*40)
    for j in td_list:
        print(j.text.strip())
