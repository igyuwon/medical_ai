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
url = "https://finance.naver.com/"
# 브라우저 페이지 열기
browser.get(url)

time.sleep(3)
# elem = browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[6]/a')
# elem.click()
# time.sleep(3)
elem = browser.find_element(By.XPATH,'//*[@id="container"]/div[2]/div/div[3]/a')
elem.click()
time.sleep(3)
soup = BeautifulSoup(browser.page_source,'lxml')
print(soup.prettify())
with open('stock.html','w',encoding='utf8') as f:
    f.write(soup.prettify())
time.sleep(100)
