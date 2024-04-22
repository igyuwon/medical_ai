import requests
from bs4 import BeautifulSoup

url="https://www.gmarket.co.kr/n/best"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

# print(soup)
# with open('gmarket.html','w',encoding='utf8') as f:
#     f.write(soup.prettify())

goods_number = soup.find("p",{"class":"no1"})
print("상품번호 : "+goods_number.text)
goods_title = soup.find("a",{"class":"itemname"})
print("상품이름 : "+goods_title.text)
goods_price = soup.find("div",{"class":"s-price"})
discount_price = goods_price.strong.get_text()
print("상품가격 : "+discount_price)

print('-'*60)

best_div = soup.find("div",{"class":"best-list"})
print('div 베스트상품 : ' + best_div.text)

# 1개 best상품 출력
# li01 = best_div.find("li")
# print("li01 순위 : ",li01.p.text)
# print("제목 : ", li01.find("a",{"class":"itemname"}).text)
# print("가격 : ", li01.find("div",{"class":"s-price"}).strong.span.text)

# 여러개 상품 출력
lis = best_div.find_all("li")
print("베스트 상품 개수 : ",len(lis))

for li in lis[0:4]:
    print("순위 : ",li.p.text)
    print("제목 : ", li.find("a",{"class":"itemname"}).text)
    print("가격 : ", li.find("div",{"class":"s-price"}).strong.span.text)
    print("-"*100)

