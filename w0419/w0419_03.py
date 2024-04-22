import requests
from bs4 import BeautifulSoup

url="https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
           "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')

# with open("coupang.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
# print("완료")

# 1000건 이상, 4.9 이상 출력

# # 일단 4개 출력
ul_search = soup.find("ul",{"class":"search-product-list"})

# 모든 상품 검색
lis = ul_search.find_all("li")
# print("상품이름 : ",lis[1].find("div",{"class":"name"}).text)
# print("상품이름 : ",lis[1].find("strong",{"class":"price-value"}).text)
# print("평점 : ",lis[1].find("em",{"class":"rating"}).text)
# print("리뷰수 : ",lis[1].find("span",{"class":"rating-total-count"}).text)

count = 0
for idx,li in enumerate(lis[0:20]):
    # 광고상품 제외
    if "search-product__ad-badge" in li['class']:
        continue
    
    # 평점 5.0 이상 - 문자와 숫자 비교(실수형으로 변경)
    if float(li.find("em",{"class":"rating"}).text) < 5.0:
        continue
    # 평가인원수가 200명 이상 - 정수형으로 변경
    if int(li.find("span",{"class":"rating-total-count"}).text[1:-1]) < 200:
        continue
    
    print("-"*100)
    print("[ ", idx+1, "번째 상품 ]")
    print("li class : ",li['class'])
    print("상품이름 : ",li.find("div",{"class":"name"}).text.strip())
    print("상품가격 : ",li.find("strong",{"class":"price-value"}).text)
    print("평점 : ",li.find("em",{"class":"rating"}).text)
    print("리뷰수 : ",li.find("span",{"class":"rating-total-count"}).text[1:-1])


