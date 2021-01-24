# -*- coding: utf-8 -*-
"""
Created on Sun Dec 20 15:41:33 2020

@author: 86159
"""

def printName(isC,last,family):
    
    def pN(a,b):
        print(a,b)
    
    if isC:
        pN(family,last)
    else:
        pN(last,family)
    

printName(1,'rihui','sheng')
printName(0,'John','Trump')
