import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")
s_all = soup.find('div',{'class':'box_type_l'})
tr_list = s_all.find_all('tr')
# 타입 - 리스트 타입
# print(len(tr_list))
# print(type(tr_list))
# with open('stock.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())
samsung = tr_list[2]
# print(samsung)
td_list = samsung.find_all('td')
print(td_list)
print('순위 : ',td_list[0].text)
print('종목명 : ',td_list[1].find('a').text)
print('검색비율 : ',td_list[2].text)
print('현재가 : ',td_list[3].text)
# print(tr_list[2])

# print(samsung)

