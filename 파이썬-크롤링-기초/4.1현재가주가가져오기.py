import requests
from bs4 import BeautifulSoup
import pyautogui

# keyword = input("검색어 작성>>")
# keyword = pyautogui.prompt("검색어 작성>>")
# code = '005930'
codes = [
    '005930'
    , '000660'
    , '035720'
]
index: int = 1

for code in codes:
    response = requests.get(f"https://finance.naver.com/item/sise.naver?code={code}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.select_one('#_nowVal')

    print(code, price.text.replace(',',''))



