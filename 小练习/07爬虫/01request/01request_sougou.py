# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 17:15:41 2021

@author: shengrihui
"""

import requests

#1.指定URL
url='https://www.sogou.com/'

#2.发起请求
#get返回一个响应对象
respond=requests.get(url=url)

#3.获取响应数据
#text返回字符串的响应数据
page_text=respond.text
print(page_text)

#4.持久化存储
with open('sougou.html','w',encoding='utf-8') as f:
    f.write(page_text)
