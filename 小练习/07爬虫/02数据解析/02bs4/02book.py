# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 11:22:50 2021

@author: shengrihui
"""

import requests
from bs4 import BeautifulSoup

url = 'http://www.purepen.com/sgyy/index.htm'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

res = requests.get(url=url, headers=header)
res.encoding = 'gb2312'
page_text = res.text
page_soup = BeautifulSoup(page_text, 'lxml')

td_list = page_soup.select('table  td')
# print(td_list)

fp = open('02book_sanguo.txt', 'w', encoding='utf-8')

for i in range(1, 241, 2):
    # print(type(td_list[i]))
    number = td_list[i].string.strip()
    # print(number)
    title = td_list[i + 1].text.strip()  # 因为是在a标签里
    # print(title)

    a_href = td_list[i + 1].a['href']  # xx.a['href']
    # print(a_href)
    detail_url = 'http://www.purepen.com/sgyy/' + a_href
    # print(detail_url)

    try:
        detail_res = requests.get(url=detail_url, headers=header)
    except:
        print(number, '失败！')
        fp.write(number + ":" + title + "\n" + "\n")
        continue
    detail_res.encoding = 'gb2312'
    detail_text = detail_res.text
    # print(detail_text)
    detail_soup = BeautifulSoup(detail_text, 'lxml')
    passage = detail_soup.find('p').get_text()
    # print(passage)

    fp.write(number + ":" + title + "\n" + passage + "\n")
    print(number, "完成！")

fp.close()
