# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 21:14:52 2021

@author: shengrihui
"""

def Is(s):
    f=True
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            f=False
            break
    return f


lenth=len(s)

for l in range(lenth,0,-1):
    
    i=0
    while i<lenth-l+1:
        st=s[i:i+l]
        if Is(st):
            print(st)
            break
        i+=1