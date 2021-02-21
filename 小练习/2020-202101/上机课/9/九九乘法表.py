# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 17:01:57 2020

@author: 86159
"""

i=1
while i<10:
    j=1
    while j<=i:
        s='%dx%d=%d' %(j,i,i*j)
        print(s,end=" ")
        j+=1
    print("")
    i+=1