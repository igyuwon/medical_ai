# 서울특별시, 인천, 경기도 3개의 인구를 웹스크래핑해서
# 서울특별시 : 인구
# 인천 : 인구
# 경기도 : 인구
# 합계 : 인구를 출력하시오.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup


browser = webdriver.Chrome()
url = "https://jumin.mois.go.kr/ageStatMonth.do"
# 브라우저 페이지 열기
browser.get(url)
time.sleep(5)
soup = BeautifulSoup(browser.page_source,"lxml")

table = soup.find("table",{"id":"contextTable"})
# print(len(city_list))
tbody = table.find("tbody")
# print(len(tbody))
city_list = tbody.find_all("td",{"class":"td_admin th1"})
print(len(city_list))
# 서울
seoul = city_list[1].text
print(city_list)
print("도시 이름 : ",seoul)
tr_list = tbody.find_all("tr")
td_list = tr_list[1].find_all("td")
seoul_population = td_list[2].text.replace(',','')
print(seoul+"의 총 인구수 : "+seoul_population)
print("-"*50)
# 인천
incheon = city_list[4].text
print("도시 이름 : ",incheon)
tr_list = tbody.find_all("tr")
td_list = tr_list[4].find_all("td")
incheon_population = td_list[2].text.replace(',','')
print(incheon+"의 총 인구수 : "+incheon_population)
print("-"*50)
# 경기도
ggd = city_list[9].text
print("도시 이름 : ",ggd)
tr_list = tbody.find_all("tr")
td_list = tr_list[9].find_all("td")
ggd_population = td_list[2].text.replace(',','')
print(ggd+"의 총 인구수 : "+ ggd_population)
print("-"*50)
# 총 인구수
total_population = int(seoul_population)+int(incheon_population)+int(ggd_population)
print("총 인구수 : ",total_population)
print("-"*50)
print("selenium 응용해봄")
s_name = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[2]/td[2]')
s_num = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[2]/td[3]')
i_name = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[5]/td[2]')
i_num = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[5]/td[3]')
k_name = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[10]/td[2]')
k_num = browser.find_element(By.XPATH,'//*[@id="contextTable"]/tbody/tr[10]/td[3]')
print(s_name.text , ':', s_num.text.replace(',',''))
print(i_name.text , ':', i_num.text.replace(',',''))
print(k_name.text , ':', k_num.text.replace(',',''))