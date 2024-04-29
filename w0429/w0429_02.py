import requests
import random
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
           "Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://flight.naver.com/"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

time.sleep(1)

# 출발지 선택 // 전체 문서 b
elem = browser.find_element(By.XPATH,'//b[text()="ICN"]')
time.sleep(1)
elem.click()
time.sleep(2)

# 국내 부분 선택
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()
time.sleep(2)

# 김포국제공항 선택
elem = browser.find_element(By.XPATH,'//i[contains(text(),"김포국제공항")]')
time.sleep(1)
elem.click()
time.sleep(2)

# 도착지 선택 // 전체 문서 b
elem = browser.find_element(By.XPATH,'//b[text()="도착"]')
time.sleep(2)
elem.click()
time.sleep(2)

# 국내 부분 선택
elem = browser.find_element(By.XPATH,'//button[text()="국내"]')
time.sleep(1)
elem.click()
time.sleep(2)

# 김포국제공항 선택
elem = browser.find_element(By.XPATH,'//i[contains(text(),"제주국제공항")]')
time.sleep(1)
elem.click()
time.sleep(2)


time.sleep(30)

# 실제 구문 -  여러개 가져오기
# browser.find_elements(By.XPATH,'//b[text()="15"]')

# 문자열과 일치할 때 선택방법
# '//i[text()="김포국제공항"]'

# 문자열이 포함할 때 선택방법
# '//i[contains(text()="김포국제공항")]'

# id로 선택하는 방법
# '//i[@id="_next"]'

# class로 선택하는 방법
# '//i[@class="_next"]'