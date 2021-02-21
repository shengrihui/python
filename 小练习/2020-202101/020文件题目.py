# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 09:44:07 2021

@author: 86159
"""


f=open('txtpython.txt','r+')
ff=open('new.txt','w')
for i in f:
    s=f.readline()
    ss=s[:s.rfind('。')+1]+'\n'
    ff.writelines(ss)

f.close()
ff.close()
