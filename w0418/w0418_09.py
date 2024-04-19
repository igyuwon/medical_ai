import requests
from bs4 import BeautifulSoup
url="https://comic.naver.com/bestChallenge"
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"}
res=requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

with open("webtoon.html","w",encoding="utf8") as f:
    f.write(soup.prettify())