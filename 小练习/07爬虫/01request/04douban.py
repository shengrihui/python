# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 21:06:20 2021

@author: shengrihui
"""

import requests
import json

url = 'https://movie.douban.com/j/chart/top_list'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}

param = {
    'type': 24,
    'interval_id': '100:90',
    'action': ' ',
    'start': 0,
    'limit': 20
}

response = requests.get(url=url, params=param, headers=header)

list_data = response.json()

filename = '04douban.json'
fp = open(filename, 'w', encoding='utf-8')
json.dump(list_data, fp=fp, ensure_ascii=False)

fp.close()
print('over!!!')
