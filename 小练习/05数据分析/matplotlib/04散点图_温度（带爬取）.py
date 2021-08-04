# -*- coding: utf-8 -*-
"""
Created on Tue May  4 10:58:16 2021

@author: 11200
"""

import requests
from lxml import etree
from matplotlib import pyplot as plt

#爬取温度和对应日期的函数
def get_temp_date(month):
    temp_max_list=[]
    date=[]
    url='http://lishi.tianqi.com/beijing/{}.html'.format(month)
    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'
        }
    
    page_text=requests.get(url=url,headers=header).text
    #print(page_text)
    
    tree=etree.HTML(page_text)
    #rint(tree)
    
    li_list=tree.xpath('/html/body/div[7]/div[1]/div[4]/ul/li')
    
    for li in li_list:
        t=li.xpath('./div[2]/text()')[0]
        d=li.xpath('./div[1]/text()')[0]
        
        t=t.strip('℃')
        d=d[5:7]+"月"+d[8:10]+"日"
        #print(d)
        temp_max_list.append(int(t))
        date.append(d)
    return temp_max_list,date

#中文字体和设置图片
plt.rcParams['font.sans-serif'] = ['SimHei'] #解决中文显示
plt.rcParams['axes.unicode_minus'] = False #解决符号无法显示
plt.figure(figsize=(16,9),dpi=80)

#获取数据
temp_03max,date03=get_temp_date(202003)
temp_10max,date10=get_temp_date(2020 10)

#x刻度
x03=list(range(len(date03)))
x10=[ i+30 for i in list(range(len(date10)))]
x=x03+x10
x_labels=date03+date10
plt.xticks(x[::3],x_labels[::3],rotation=45)

#绘图
plt.scatter(x03,temp_03max,label='03月')
plt.scatter(x10,temp_10max,label='10月')

#图例等信息
plt.grid(alpha=0.6) #网格
plt.xlabel('日期')
plt.ylabel('温度')
plt.legend(loc='upper left')
plt.title("北京2020年03月和10月最高温散点图")

plt.savefig('04散点图_温度.png')
plt.show()


