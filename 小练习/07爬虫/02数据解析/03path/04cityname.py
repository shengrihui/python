# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 14:03:41 2021

@author: shengrihui
"""

import requests
from lxml import etree

url = 'https://www.aqistudy.cn/historydata'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

page_text = requests.get(url=url, headers=header).text

tree = etree.HTML(page_text)


def test01():
    all_cities = []
    hot_li_list = tree.xpath('//div[@class="hot"]//li')
    for li in hot_li_list:
        city_name = li.xpath('./a/text()')[0]
        all_cities.append(city_name)

    all_li_list = tree.xpath('//div[@class="all"]//li')
    for li in all_li_list:
        city_name = li.xpath('./a/text()')[0]
        all_cities.append(city_name)

    # print(all_cities)
    print(len(all_cities))


def test02():
    all_cities = []
    D

    all_li_list = tree.xpath('//div[@class="hot"]//li | //div[@class="all"]//li')
    for li in all_li_list:
        city_name = li.xpath('./a/text()')[0]
        all_cities.append(city_name)

    # print(all_cities)
    print(len(all_cities))


test01()
test02()
