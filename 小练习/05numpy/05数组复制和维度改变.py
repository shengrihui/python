# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 22:33:50 2021

@author: shengrihui
"""

import numpy as np

def np_copy():
    a=np.arange(1,25)
    print('a:\n',a)
    aa=a.reshape(4,6)
    print('aa:\n',aa)
    
    sub_aa1=aa[:2,:3]
    print('sub_aa1:\n',sub_aa1)
    sub_aa1[0,0]=666
    print('sub_aa1:\n',sub_aa1)
    print('aa:\n',aa)
    
    sub_aa2=np.copy(aa[:2,:2])
    print('sub_aa2:\n',sub_aa2)
    sub_aa2[0][0]=88
    print('sub_aa2:\n',sub_aa2)
    print('aa:\n',aa)


def change_nd():
    a=np.arange(1,25)
    print(a)
    print()
    #reshape
    b=a.reshape(3,8)
    print(b)
    b2=a.reshape((3,4,2))
    print(b2)
    
    print('np.reshape')
    c=np.reshape(a,(3,4,2))
    print(c)
    
    print('多维转一维数组')
    d=np.reshape(c,24)
    print(d)
    d2=c.reshape(-1)
    print(d2)
    print(c.ravel())
    print(c.flatten())

    
    
np_copy()
#change_nd()