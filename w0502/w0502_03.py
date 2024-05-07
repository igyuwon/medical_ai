# 1. 야놀자 홈페이지 이동
# 2. 검색창에 호텔 입력
# 3. 날짜선택
# 4. 6월5일 ~ 6일 클릭
# 5. 확인버튼 클릭
# 6. 검색창 클릭 > enter 입력
# 7. 검색 진행
# 8. 스크롤 이동 반복
# ------------------------------------------
# 9. 정보창이 띄워지면, 이미지, 제목, 평점, 평가수, 금액 저장하시오.
# yanolja 테이블
# yno,img,title,grade,grade_num,price

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

conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()

url= "https://www.yanolja.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()

browser.get(url)
time.sleep(2)

# 검색버튼
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/section/header/section/a[2]/div/div')
elem.click()
time.sleep(1)
# 검색창에 호텔 입력
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div[1]/form/div/div[1]/div/input')
elem.click()
time.sleep(1)
elem.send_keys('호텔')
time.sleep(3)

# 날짜버튼 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div[1]/form/div/div[2]/div[1]/button')
elem.click()
time.sleep(5)

# 6월 5일 클릭
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[4]')
elem.click()
time.sleep(2)

# 6월 6일 클릭
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[5]')
elem.click()
time.sleep(2)

# 확인버튼 클릭
elem = browser.find_element(By.XPATH,'/html/body/div[4]/div/div/section/section[4]/button')
elem.click()
time.sleep(2)

# 검색창 클릭
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div[1]/form/div/div[1]/div/input')
elem.click()
time.sleep(2)
elem.send_keys(Keys.ENTER)
time.sleep(5)

soup = BeautifulSoup(browser.page_source,"lxml")

prev_height = browser.execute_script("return document.body.scrollHeight")
print("최초 높이:",prev_height)
cnt = 0
while True:
    if cnt == 5: break
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break
    prev_height = curr_height
    # print('현재 높이 :',curr_height)
    cnt += 1

hotel_list = soup.find_all("div",{"class":"PlaceListItemText_container__fUIgA text-unit"})
print("-"*80)
for hotel in hotel_list:
    img = hotel.find("div",{"class","PlaceListImage_imageText__2XEMn"})["style"]
    img = img[23:]
    print("이미지 : ",img)
    title = hotel.find("strong",{"class":"PlaceListTitle_text__2511B"}).text
    print("제목 : ",title)
    grade = hotel.find("span",{"class":"Icon_icon__2BP_o PlaceListScore_star__2IZFX"}).nextSibling.text
    print("평점 : ",grade)
    grade_num = hotel.find("span",{"class":"PlaceListScore_reviewInfo__3QSCU"}).text.strip()
    grade_num = int(grade_num[1:-1].replace(",",""))
    print("평가수 : ",grade_num)

    try:
        price = hotel.find("span",{"class":"PlacePriceInfoV2_discountPrice__1PuwK"})
        price = int(price.text.replace(",",""))
        print("금액 : ",price)
    except:
        price = 0
        print(f"금액 : {price}")

    print("-"*80)
    sql = f'''
    insert into yeogi values (
    yeogi_seq.nextval,'{img}','{title}','{grade}',{grade_num},{price}
    '''
    cursor.execute(sql)
    cursor.execute('commit')


time.sleep(10)


cursor.close()
conn.close()  


