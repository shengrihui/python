# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 14:38:24 2020

@author: 86159
"""

#*事元组，**事字典

def f1(a,b,*c,d):
    print(a,b,c,d)
    
f1(1,2,3,4,5,6,'ss',d=3)

def f2(a,b,*c5,**d):
    print(a,b,c5,d)
    
f2(1,2,3,4,5,6,'ss',name='3',eaage=5)