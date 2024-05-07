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

# 마우스 이동
pyautogui.moveTo(500,500)

# 스크롤 이동
pyautogui.scroll(-500)

# 마우스 클릭
pyautogui.click()

# 마우스 더블클릭
pyautogui.doubleClick()

# sleep
pyautogui.sleep(3)