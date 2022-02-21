# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 08:54:08 2021

@author: shengrihui
"""

#csv

import csv

with open("f.csv","r",encoding="utf-8") as f:
    print(list(csv.reader(f)))
    
with open("f2.csv","w") as f:
         s_csv=csv.writer(f)
         s_csv.writerow(["姓名","年龄",123])
         
         c=[["盛日辉",12,"dd"],["python",100]]
         s_csv.writerows(c)
print("finish")