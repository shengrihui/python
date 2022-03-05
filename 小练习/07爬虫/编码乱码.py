# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 14:00:33 2021

@author: shengrihui
"""

import requests
from bs4 import BeautifulSoup

url = 'http://www.purepen.com/sgyy/index.htm'

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
}
res = requests.get(url=url, headers=header)

print(res.encoding)
print(res.apparent_encoding)

# text=res.text.encode('ISO-8859-1').decode('GB2312')

# res.encoding='gb2312'

res.encoding = res.apparent_encoding

text = res.text

print(text)
