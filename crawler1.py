import os
import requests
from bs4 import BeautifulSoup

file_path = 'lol_list.html'
url_list = 'http://www.leagueoflegends.co.kr/?m=news&cate=notice'

if os.path.exists(file_path):
    html = open(file_path, 'rt').read()
else:
    response = requests.get(url_list)
    html = response.text
    open(file_path, 'wt').write(html)

soup = BeautifulSoup(html, 'lxml')
all_title = soup.select('.contents-table .request-list td a')
for title in all_title:
    print(title.text)
    print()
