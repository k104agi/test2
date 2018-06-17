import requests
from bs4 import BeautifulSoup


class Notice:
    def __init__(self, title, date, view):
        self.title = title
        self.date = date
        self.view = view


url_list = 'http://www.leagueoflegends.co.kr/?m=news&cate=notice'
response = requests.get(url_list)
html = response.text

soup = BeautifulSoup(html, 'lxml')
all_info = soup.select('tbody > tr')

# print(all_info)

notice_list = list()

for get_info in all_info:
    title = get_info.select_one('td.tleft > a').text
    date = get_info.select_one('td:nth-of-type(2)').text
    view = get_info.select_one('td:nth-of-type(3)').text
    #     print(title)
    #     print(date)
    #     print(view)
    notice_list.append(Notice(title, date, view))

for result in notice_list:
    print(result.title)
    print(result.date)
    print(result.view)
    print()
