import requests
from bs4 import BeautifulSoup
import pyautogui

# keyword = input("검색어 작성>>")
keyword = pyautogui.prompt("검색어 작성>>")
lastPage = pyautogui.prompt("몇 페이지까지 궁금하늬?")
lastPageNum = int(lastPage) + 1
index: int = 1

for page in range(1, lastPageNum, 1):
    response = requests.get("https://www.fmkorea.com/index.php?mid=humor&search_keyword=%E3%85%87%E3%85%8E&search_target=title_content&page=1")

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        links = soup.select('.hx')

        for link in links:
            title = link.text
            url = link.attrs['href']
            print(page, index, title, url)
            # print(link)
            index += 1
    else:
        print(response.status_code)