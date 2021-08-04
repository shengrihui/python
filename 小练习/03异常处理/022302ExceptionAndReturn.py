# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 22:17:33 2021

@author: shengrihui
"""

def test():
    print("step0")
    try:
        print("step try")
        #return "try"  #正常到finally，
        #x=3/0
        #return "try"  #最终返回的是None
    except:
        print("step except")
        return "except"   #z正常返回
    else:
        print("step else")
        return "else"
    finally:
        print("step finally")
        return "finally"
        
print("step print")
print(test())
print("end")

