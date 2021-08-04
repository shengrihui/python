# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 20:19:26 2021

@author: shengrihui
"""

import requests
import json
post_url='https://fanyi.baidu.com/sug'
header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

#post请求，同get相似
word=input('input a word:')
data={
      'kw':word
      }

response=requests.post(url=post_url,data=data,headers=header)

#如果确认服务器返回的是json类型的数据，可以用json()方法直接返回json对象
dic_obj=response.json()

filename='03baidu_fanyi.json'
fp=open(filename,'w',encoding='utf-8')
#json模块直接写入json文件
#因为有中文，不能用ASCII码，所以ensure_ascii=False
json.dump(dic_obj, fp=fp, ensure_ascii=False)

fp.close()

