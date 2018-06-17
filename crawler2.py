import os
from io import BytesIO
from urllib import parse
import requests
from bs4 import BeautifulSoup


# file_path = './lol_list.html'
# url_list = 'http://www.leagueoflegends.co.kr/?m=news&cate=notice'
# params = {
#     'm': 'news',
# }
#
# if os.path.exists(file_path):
#     html = open(file_path, 'rt').read()
# else:
#     response = requests.get(url_list, params)
#     html = response.text
#     open(file_path, 'wt').write(html)
#
# soup = BeautifulSoup(html, 'lxml')
# all_title = soup.select('.contents-table .request-list td a')
# for title in all_title:
#     print(title.text)


class Notice:
    def __init__(self, title, date, view):
        self.title = None
        self.date = None
        self.view = None

    def crawl(self):
        file_path = './lol_list.html'
        url_list = 'http://www.leagueoflegends.co.kr/?m=news&cate=notice'

        if os.path.exists(file_path):
            html = open(file_path, 'rt').read()
        else:
            response = requests.get(url_list, params)
            html = response.text
            open(file_path, 'wt').write(html)

        soup = BeautifulSoup(html, 'lxml')
        all_title = soup.select('.request-list > tbody >tr')
        title = all_title.text
        print(title)


if __name__ == '__main__':
    crawl(self)