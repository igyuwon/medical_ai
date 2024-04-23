import requests
from bs4 import BeautifulSoup

url="https://browse.auction.co.kr/list?category=22160000&k=31&p=1"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
           "Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
res = requests.get(url,headers=headers)
res.raise_for_status()

# 데이터 불러오기
soup = BeautifulSoup(res.text,"lxml")

# with open("auction.html","w",encoding='utf8') as f:
#     f.write(soup.prettify())
# print(soup.prettify())

# print(soup.find("div",{"id":"section--inner_content_body_container"}))
section = soup.find("div",{"id":"section--inner_content_body_container"})
print("-"*100)
# print(section.find("div",{"class":"section--itemcard"}))

itemcards = section.find_all("div",{"class":"section--itemcard_info"})

print("개수 : ",len(itemcards))

for i,itemcard in enumerate(itemcards[0:10]):
    print("[ ",i+1,"번째 ]")
    print("제목 : ",itemcard.find("span",{"class":"text--title"}).text)
    # replace 함수 : ,를 제거, int 타입 변경 / '{0:,}'.format(num)
    price = int((itemcard.find("strong",{"class":"text__price-seller"}).text).replace(",",""))
    print("금액 : ",'{0:,}'.format(price))
    if itemcard.find("ul",{"class":"list--score"}).text == "":
        print("후기평점 : 없음")
    else:
        list_score = itemcard.find("ul",{"class":"list--score"})
        # 후기 평점 4.9점 이상 출력
        if list_score.find("span",{"class":"for-a11y"}).text[5:-1] != "":
            for_a11y = float(list_score.find("span",{"class":"for-a11y"}).text[5:-1])
            if for_a11y > 4.5:
                print("후기평점 : ",for_a11y)
            else:
                print("후기평점 : 미달")
        else:
            print("후기평점 : 없음")
                
        # 구매 건수 비교
        buycnt = int(list_score.find("span",{"class":"text--buycnt"}).text[3:])
        if buycnt>2:
            print("구매건수 : ",buycnt)
        else:
            print("구매건수 : 구매건수가 적어 생략")
    
    print('-'*100)
