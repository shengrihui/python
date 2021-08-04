# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 19:02:42 2021

@author: shengrihui
"""

import csv
import datetime
import random

with open("收入数据.csv","w",newline='') as f:
    f_csv=csv.writer(f)
    f_csv.writerow(["日期","收入金额"])
    
    date=datetime.date(2020, 1, 1)
    li=[]
    for i in range(366):
        li.append([str(date),random.randrange(1000)])
        date=date+datetime.timedelta(days=1)
        
    f_csv.writerows(li)
        
        