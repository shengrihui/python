# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 14:52:41 2021

@author: shengrihui
"""

#csv dictreader
import csv

with open("f.csv","r",encoding='utf-8') as f:
    reader=csv.DictReader(f)
    print(reader)
    
    li=[row for row in reader]
    print(li)