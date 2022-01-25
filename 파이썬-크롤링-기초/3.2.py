import requests
from bs4 import BeautifulSoup
import pyautogui

# keyword = input("검색어 작성>>")
keyword = pyautogui.prompt("검색어 작성>>")

response = requests.get(f"https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select('.news_tit')

# print(links)


for link in links:
    title = link.text
    url = link.attrs['href']
    print(title, url)

