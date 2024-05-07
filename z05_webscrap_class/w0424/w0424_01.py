import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
           "Accept-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
url = "http://www.google.com"
res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')

print("타이틀 : ",soup.find("title"))

with open("google.html",'r',encoding='utf8') as f:
    soup = BeautifulSoup(f,'lxml')
print("타이틀 : ",soup.find("title"))