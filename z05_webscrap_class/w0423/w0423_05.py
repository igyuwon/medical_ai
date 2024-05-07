import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
           "Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

# selenium은 자동화프로그램

browser = webdriver.Chrome()
url = "https://news.naver.com/main/ranking/popularDay.naver"
# 브라우저 페이지 열기
browser.get(url)
time.sleep(5)
soup = BeautifulSoup(browser.page_source,"lxml")

company_list = soup.find("div",{"class":"_officeCard _officeCard0"})
rank_box_list = company_list.find_all("div",{"class":"rankingnews_box"})
for divs in rank_box_list[0:12]:
    ul_list = divs.find("ul",{"class":"rankingnews_list"})
    lis = ul_list.find_all("li")
    print("-"*100)
    print("신문사 이름 : ",divs.find("strong",{"class":"rankingnews_name"}).text)
    for li in lis[0:5]:
        print("등수 : ",li.find("em",{"class":"list_ranking_num"}).text)
        content = li.find("div",{"class":"list_content"})
        print("내용 : ",content.find("a",{"class":"list_title nclicks('RBP.rnknws')"}).text)
        img_a = li.find("a",{"class":"list_img nclicks('RBP.rnknws')"})
        img = img_a.find("img")["src"]
        print("이미지링크 : ",img)
        print('\n')
        #print("이미지 링크 : ",img.find("img")["src"])
    print("-"*100)

