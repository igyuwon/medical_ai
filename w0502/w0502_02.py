import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
# browser = webdriver.Chrome()
# browser.maximize_window()
# 파일불러오기
with open("melon.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,"lxml")
trs = soup.find_all("tr",{"id":"lst50"})
print("개수 : ",len(trs))
# db저장
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()
for tr in trs:
    rank = tr.find("span",{"class":"rank"})
    rank = int(rank.text.strip())
    print("순위 : ",rank)
    s_rank = tr.find("span",{"class":"rank_wrap"})
    v_rank = tr.find("span",{"class":"rank_wrap"})['title']
    print(v_rank)
    if v_rank =="순위 동일":
        v_rank = 0
    elif v_rank.find('단계 하락') != -1:
        v_rank = s_rank.find("span",{"class":"down"}).text
        v_rank = int(v_rank)*-1
    else:
        v_rank = s_rank.find("span",{"class":"up"}).text
        v_rank = int(v_rank)        
    print("순위변동 : ",v_rank)
    img = tr.find("img")['src']
    print("이미지 : ",img)
    r_title = tr.find("div",{"class":"ellipsis rank01"})
    title = r_title.find("a").text.strip()
    print("제목 : ",title)
    r_singer = tr.find("div",{"class":"ellipsis rank02"})
    singer = r_singer.find("a").text.strip()
    print("가수 : ",singer)
    r_likeNum = tr.find("button",{"class":"button_etc like"})
    likeNum = int(r_likeNum.find("span",{"class":"none"}).nextSibling.strip().replace(",",""))
    print("좋아요수 : ",likeNum)
    print("-"*30)
    # sql = f"insert into melon values ( melon_seq.nextval,{rank},{v_rank},'{img}','{title}','{singer}',{likeNum})"
    sql =f"insert into melon values (\
melon_seq.nextval,{rank},{v_rank},'{img}',\
'{title}','{singer}',{likeNum})"
    cursor.execute(sql)
    cursor.execute('commit')
cursor.close()
conn.close()    
# 21 ---------------
# rank = trs[21].find("span",{"class":"rank"})
# print("순위 : ",rank.text.strip())
# s_rank = trs[21].find("span",{"class":"rank_wrap"})
# v_rank = trs[21].find("span",{"class":"rank_wrap"})['title']
# print(v_rank)
# if v_rank =="순위 동일":
#     v_rank = 0
# elif v_rank.find('단계 하락') != -1:
#     v_rank = s_rank.find("span",{"class":"down"}).text
#     v_rank = int(v_rank)*-1
# else:
#     v_rank = s_rank.find("span",{"class":"up"}).text
#     v_rank = int(v_rank)        
# print("순위변동 : {:+d}".format(v_rank))  # +부호 넣기
# img = trs[21].find("img")['src']
# print("이미지 : ",img)
# r_title = trs[21].find("div",{"class":"ellipsis rank01"})
# title = r_title.find("a")
# print("제목 : ",title.text.strip())
# r_singer = trs[21].find("div",{"class":"ellipsis rank02"})
# singer = r_singer.find("a")
# print("가수 : ",singer.text.strip())
# r_likeNum = trs[21].find("button",{"class":"button_etc like"})
# likeNum = r_likeNum.find("span",{"class":"none"}).nextSibling.strip()
# print("좋아요수 : ",likeNum)
##-----------------


# rank = browser.find_element(By.XPATH,'//*[@id="lst50"]/td[2]/div/span[1]').text
# print("랭킹 : ",rank)
# img = browser.find_element(By.XPATH,'//*[@id="lst50"]/td[4]/div/a/img').get_attribute("src")
# print("이미지 링크 : ",img)
# title = browser.find_element(By.XPATH,'//*[@id="lst50"]/td[6]/div/div/div[1]/span/a').text
# print("노래제목 : ",title)
# singer = browser.find_element(By.XPATH,'//*[@id="lst50"]/td[6]/div/div/div[2]/a').text
# print("가수 : ",singer)
# likeNum = browser.find_element(By.XPATH,'//*[@id="lst50"]/td[8]/div/button/span[2]').text
# likeNum = browser.replace(",","").strip()
# print("좋아요 수 : ",likeNum)


