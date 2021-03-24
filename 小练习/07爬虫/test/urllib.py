# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 20:58:16 2021

@author: shengrihui
"""

import urllib.request

response=urllib.request.urlopen("http://www.baidu.com")

print(response)
#print(response.read())
#print(response.read().decode('utf-8'))
a=response.read().decode('utf-8')

with open("baidu.html","w",encoding="utf-8") as f:
    f.write(a)

import os
os.startfile("baidu.html")
