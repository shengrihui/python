# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 20:22:53 2021

@author: shengrihui
"""

a=100

def outer():
    b=200
    
    def middle():
        c=300
        
        def inner():
            
            nonlocal b
            print(b)
            b=499
            
        inner()
    
    middle()
    print("b:",b)

outer()
    