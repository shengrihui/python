# -*- coding: utf-8 -*-
"""
Created on Sun May 10 20:51:53 2020

@author: Eternal
"""


import csv
import random
import datetime
ff="D:/刘帅工作/2020/教学/Python应用开发/第7周/源码/数据分析源码/data.csv"

with open(ff,'w',newline="")as fp:
    fcsv=csv.writer(fp)#写一行数据
    fcsv.writerow(["日期","收入金额"])
    start_date=datetime.date(2019,1,1)
    for i in range(365):
        fcsv.writerow([str(start_date),random.randrange(1000)])
        start_date=start_date+datetime.timedelta(days=1)

        
        
#使用pandas读取数据文件，创建DataFrame对象，并删除其中所有缺失值

import pandas as pd
import matplotlib
matplotlib.rcParams['font.sans-serif']=['SimHei'] #pyplot中文显示


df=pd.read_csv('data.csv',encoding='cp936')
df=df.dropna()#读取数据，丢弃缺失值
#生成天营业额折线图
#plt.figure()  
df.plot(x='日期',kind='line')   

#生成月营业额柱状图

df1=df[:]  #str1.rindex(str2)返回子串 str2 在串str1中最后出现位置，如果没有匹配的字符串会报异常
df1['month']=df1['日期'].map(lambda x:x[:x.rindex('-')])#提取出月份,新建了一个month列出来？？
df1=df1.groupby(by='month',as_index=False).sum() #as_inside=False不把month作为新的index
df1.plot(x='month',kind='bar')


#生成季度营业额柱状图
def getQuarter(x) :
    x=int(x)
    y=1
    if x<4:
        y=1
        return y
    if x<7:
        y=2
        return y
    if x<10:
        y=3
        return y
    if x<13:
        y=4
        return y
    return y
df2=df1[:]
df2['季度']=df1['month'].map(lambda x:x[x.rindex('-')+1:])
df2['季度']=df2['季度'].map(getQuarter)
df2=df2.groupby(by='季度',as_index=False).sum() #as_inside=False不把month作为新的index
df2.plot(x='季度',kind='bar')
