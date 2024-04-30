import requests
import random
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
           "Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
# url = 'https://naver.com'
url = 'https://flight.naver.com/'
browser =  webdriver.Chrome()
browser.maximize_window()
browser.get(url)
# time.sleep(random.randint(2,5))

# 원본창[0]
# elem = browser.find_element(By.NAME,"query") # 엔터창 선택
# elem.send_keys('네이버 항공권')
# elem.send_keys(Keys.ENTER) # 엔터
# time.sleep(2)
# elem = browser.find_element(By.CLASS_NAME,'link_name') # 항공권 홈페이지 클릭
# elem.click()
# # 새 창 이동
# browser.switch_to.window(browser.window_handles[1])
# time.sleep(2)
elem = browser.find_element(By.XPATH,'/html/body/div/div/main/div[4]/div/div/div[2]/div[1]/button[1]') # 출발지 버튼 클릭
elem.click()
time.sleep(2)
elem = browser.find_element(By.CLASS_NAME,'autocomplete_Collapse__tP3pM') # 국내 선택
elem.click()
time.sleep(2)
elem = browser.find_elements(By.CLASS_NAME,'autocomplete_Airport__3_dRP')[2] # 김포 선택
elem.click()
time.sleep(2)
'''------------------------------------------------------------------------------------------------------------------------------------------'''
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[1]/button[2]') # 도착지 버튼 클릭
elem.click()
time.sleep(2)
elem = browser.find_element(By.CLASS_NAME,'autocomplete_Collapse__tP3pM') # 국내 선택
elem.click()
time.sleep(2)
elem = browser.find_elements(By.CLASS_NAME,'autocomplete_Airport__3_dRP')[1] # 제주 선택
elem.click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[2]/button[1]') # 출발일정 클릭
elem.click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[1]/button/b') # 출발일자 선택
elem.click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[2]/button/b') # 도착일자 선택
elem.click()
time.sleep(2)

for i in range(2):
    elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/div[3]/button') # 인원 선택
    elem.click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div/div[2]/button') # 항공권 검색
elem.click()
time.sleep(2)

