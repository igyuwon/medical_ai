import time
from selenium import webdriver
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
           "Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

# selenium으로 정보 가져오기
browser = webdriver.Chrome()
browser.get("https://comic.naver.com/bestChallenge")
# 페이지 로딩시간을 최대한 보장
time.sleep(3)
soup = BeautifulSoup(browser.page_source,"lxml")
# with open("webtoons2.html","w",encoding="utf8") as f:
#     f.write(soup.prettify())
# print("완료")
li_list = soup.find("ul",{"class":"AsideList__content_list--FXDvm AsideList__challenge--HeKuU"})
# print(li_list)
lis = li_list.find_all("li",{"class" : "AsideList__item--i30ly"})
print(len(lis))

print("-"*100)
for li in lis[0:10]:
    rank = li.find("strong",{"class":"AsideList__ranking--sNPZy"}).text
    title = li.find("span",{"class":"text"}).text
    author = li.find("a",{"class":"ContentAuthor__author--CTAAP"}).text
    img = li.find("img",{"class":"Poster__image--d9XTI"})["src"]
    print("등수 : ",rank)
    print("제목 : ",title)
    print("작가 : ",author)
    print("이미지 : ",img)
    print("-"*100)
    # 이미지 파일 저장 방법
    img_poster = requests.get(img,headers=headers)
    with open("webtoons_{}.jpeg".format(rank),"wb") as f:
        f.write(img_poster.content)