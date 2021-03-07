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

        
        
#使用pandas读取数据文件，创建DataFrame对象，并删除其中所有缺失值；
#使用matplotlib生成每天营业额折线图，保存图形为first.jpg
#使用matplotlib绘制每个月营业额柱状图，保存为second.jpg
#找出相邻两个月最大涨幅，并写入maxMonth.txt
#使用matplotlib显示2018年4个季度的营业额分布饼状图，保存为third.jpg
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.sans-serif']=['SimHei'] #pyplot中文显示
df=pd.read_csv('data.csv',encoding='cp936')
df=df.dropna()#读取数据，丢弃缺失值
#生成天营业额折线图
#plt.figure()  
df.plot(x='日期',kind='line')   
plt.savefig('D:/刘帅工作/2020/教学/Python应用开发/第7周/源码/数据分析源码/first.jpg')
#生成月营业额柱状图
plt.figure()  
df1=df[:]  #str1.rindex(str2)返回子串 str2 在串str1中最后出现位置，如果没有匹配的字符串会报异常
df1['month']=df1['日期'].map(lambda x:x[:x.rindex('-')])#提取出月份,新建了一个month列出来？？
df1=df1.groupby(by='month',as_index=False).sum() #as_inside=False不把month作为新的index
df1.plot(x='month',kind='bar')
plt.savefig('D:/刘帅工作/2020/教学/Python应用开发/第7周/源码/数据分析源码/second.jpg')

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
df3=df1[:]
df3['季度']=df1['month'].map(lambda x:x[x.rindex('-')+1:])
df3['季度']=df3['季度'].map(getQuarter)

df3=df3.groupby(by='季度',as_index=False).sum() #as_inside=False不把month作为新的index
df3.plot(x='季度',kind='bar')
#查找涨幅最大月份，写入文件
plt.figure()
df2=df1.drop('month',axis=1).diff()#在销量列中每月跟上月相减的差集
m=df2['销量'].nlargest(1).keys()[0]#查找销量列中差集最大的一个数所对应的索引
with open('D:/刘帅工作/2020/教学/Python应用开发/第7周/源码/数据分析源码/maxMonth.txt','w')as fp:
   fp.write(df1.loc[m,'month'])#索引m对应的month
#生成季度营业额饼状图
plt.figure()
one=df1[:3]['销量'].sum()
two=df1[3:6]['销量'].sum()
three=df1[6:9]['销量'].sum()
four=df1[9:12]['销量'].sum()

plt.pie([one,two,three,four],labels=['one','two','three','four'])
plt.savefig('D:/刘帅工作/2020/教学/Python应用开发/第7周/源码/数据分析源码/third.fig')