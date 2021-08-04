# -*- coding: utf-8 -*-
"""
Created on Thu May  6 20:56:07 2021

@author: 11200
"""

import requests
from lxml import etree
from bs4 import BeautifulSoup
import os
path1='1'
path2='《高等数学》同济版 全程教学视频（宋浩老师）'
#path=r'E:/CS/PYTHON/小练习/99其他/04B站下载视频改名/《高等数学》同济版 全程教学视频（宋浩老师)/'
file_list=os.listdir(path1)
#print(file_list)

num_list=[]
title_list=[]
#print(title_list)
with open('ul.txt','r',encoding='utf-8') as f:
    while True:
        t=f.readline()
        if not t:
            break
        num_list.append(t.strip())
        title_list.append(f.readline().strip())
        f.readline()


sz=len(title_list)
for i in range(sz):
    title=title_list[i]
    num=num_list[i]
    for old in file_list:
        if title in old:
            #print(title)
            #rint(old)
            old_name=os.path.join(path1,old)
            new_name=os.path.join(path2,"{}-{}".format(num,old))
            try:
                os.renames(old_name, new_name)
                print("{}finsh".format(num))
            except:
                continue



"""
tree=etree.parse('ul.html')
print(tree)

url='https://www.bilibili.com/video/BV1Eb411u7Fw?from=search&seid=1342765075775195967'

header={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
    }

page_text=requests.get(url=url,headers=header).text
page_soup=BeautifulSoup(page_text,'lxml')

print(page_soup)
span_list=page_soup.find('span',class_='part')
print(span_list)

tree=etree.HTML(page_text)

'''
<div class="link-content"><img src="//s1.hdslb.com/bfs/static/jinkela/video/asserts/playing.gif" style="display: none;"><span class="page-num">P33</span><span class="part">洛必达法则</span></div>
'''
li_list=tree.xpath('//*[@id="multi_page"]/div[2]/ul/li')
print(li_list)
for li in li_list:
    
    title=li.xpath('./a')
    print(title)
"""