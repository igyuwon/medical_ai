import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
           "Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}

url = "https://www.daum.net/"

# 크롬브라우저 열기
browser = webdriver.Chrome()

browser.get(url)
time.sleep(3)

elem = browser.find_element(By.CLASS_NAME,"btn_login")
elem.click()

input_js = 'document.getElementById("loginId--1").value="{id}";\
            document.getElementById("password--2").value="{pw}";\
            '.format(id="aaaa",pw="1111")
time.sleep(random.randint(2,5))
# 자바스크립트 명령어 실행
browser.execute_script(input_js)

time.sleep(random.randint(2,5))
elem = browser.find_element(By.CLASS_NAME,"highlight")
time.sleep(random.randint(2,5))
elem.click()

time.sleep(50)
