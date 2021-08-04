# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 22:40:25 2021

@author: shengrihui
"""

#pickle

import pickle

a1="aaa"
a2=100
a3=[1,2,3,(1,3)]
with open("e.dat","wb") as f:
    pickle.dump(a1,f)
    pickle.dump(a3,f)
    pickle.dump(a2,f)

with open("e.dat","rb") as f:
    b1=pickle.load(f)
    b2=pickle.load(f)
    b3=pickle.load(f)
    
print(b1);print(b2);print(b3)