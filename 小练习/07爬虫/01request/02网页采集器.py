# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 18:55:46 2021

@author: shengrihui
"""

import requests

url='https://www.sogou.com/web'

#UA  User-Agent
#UA检测  反扒机制
#UA伪装  反反爬策略
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

#url中的参数，封装到字典中
#kw获取动态关键字，param参数
kw=input('enter a word:')
param={
       "query":kw

       }
#get传入url和param，自动拼接处理,UA伪装
response=requests.get(url=url,params=param,headers=header)
page_text=response.text


filename='02.'+kw+'.html'
with open(filename,'w',encoding='utf-8') as fp:
    fp.write(page_text)
    
print(page_text)
