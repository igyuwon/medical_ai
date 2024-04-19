import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&q=%EC%98%81%ED%99%94"
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')

movie_list = soup.find("ol", {"class": "movie_list"})

m_list = movie_list.find_all("li")
for i, m in enumerate(m_list):
    if i == 5:
        break
    print(f'[ 번호 {i+1}]')
    print('-'*50)
    img_screen = m.find("img")["data-original-src"]
    print(img_screen)

    # 이미지 다운로드 및 파일에 쓰기
    img_res = requests.get(img_screen)
    #img_res.raise_for_status()
    with open(f'movie_{i}.jpg', 'wb') as f:
        f.write(img_res.content)
    
print("개수 : ", len(m_list))
print('종료')