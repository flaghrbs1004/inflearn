import requests
from bs4 import BeautifulSoup
import pyautogui

# keyword = input("검색어 작성>>")
keyword = pyautogui.prompt("검색어 작성>>")
lastPageNum = pyautogui.prompt("몇 페이지까지 궁금하늬?")
index: int = 1

for page in range(0, int(lastPageNum), 1):
    response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={page * 10 + 1}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('.news_tit')

    for link in links:
        title = link.text
        url = link.attrs['href']
        print(page, index, title, url)
        index += 1



