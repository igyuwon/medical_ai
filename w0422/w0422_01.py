'''
import requests
from bs4 import BeautifulSoup

url=""
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
           "Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()
'''
import requests
from bs4 import BeautifulSoup

url="https://browse.auction.co.kr/list?category=22160000"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
           "Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# 데이터 불러오기
soup = BeautifulSoup(res.text,"lxml")

# with open("auction.html","w",encoding='utf8') as f:
#     f.write(soup.prettify())
# print(soup.prettify())

div_find = soup.find_all("div",{"class":"section--itemcard"})
# print(div_find)
for lst in div_find[0:3]:
    print("-"*100)
    img = lst.find("img",attrs = {"class":"image--itemcard"})
    img_values = img['src']
    print("이미지 : ", img_values)
    brand = lst.find("span",{"class":"text--brand"})
    goods = lst.find("span",{"class":"text--title"})
    print("제품명 : ",brand.text+""+goods.text)

    price = lst.find("strong",{"class":"text__price-seller"})
    print("가격 : ",price.text+"원")

    award = lst.find("li",{"class":"item awards"})
    if award is not None:
        print("평점 : ", award.find("span", {"class": "for-a11y"}).text)
    else:
        print("평점을 찾을 수 없습니다.")
    

