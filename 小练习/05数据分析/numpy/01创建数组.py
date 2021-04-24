# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 11:12:33 2021

@author: shengrihui
"""

import numpy as np
import random
#import math

#arange创建数组
def arangeTest():
    print("{:-^40}".format(("arange函数创建数组")))
    a=np.arange(10)
    print(type(a))
    print(a)
    
    #np.sqrt开平方运算
    print(np.sqrt(a))
    #print(list(map(math.sqrt,a)))
    
    #与range相似
    #只能是一维数组
    a2=np.arange(100,1,-3)
    print(a2)
    
    a3=np.arange(1,27,4,dtype=float)
    print(a3)


#array函数创建数组
def arrayTest():
    print("\n{:-^40}".format(("array()函数创建数组")))
    numlist=[ i for i in range(1,6) ]
    b=np.array(numlist)
    print(b)
    print(type(b))
    
    #二维数组每个数量要相等
    b2=np.array([[1,2,3],[4,5,6],[7,8,9]])
    print(b2)
    
    b3=np.array([ [ [random.randint(0,10)  for k in range(5) ] for j in range(4) ]  for i in range(3) ])
    print(b3)
    
    #dtype数据类型，ndmin多少维度
    b4=np.array(numlist, dtype=float, ndmin=4)
    print(b4)


#随机创建数组
def randomTest():
    print("\n{:-^40}".format(("随机创建数组，正态分布")))
    
    #size维度，生成的是[0,1)的小数
    c=np.random.random(size=5)
    print(c)
    print(type(c))
    c2=np.random.random(size=(2,3,4,5))
    print(c2)
    
    #随机整数
    c3=np.random.randint(3,18,size=(3,4),dtype='int64')
    print(c3)
    print("随机整型的dtupe:",c3.dtype)
    
    #标准正态分布，期望为0，方差为1
    c4=np.random.randn(3,4)
    print(c4)
    
    #指定期望和方差
    c5=np.random.normal(loc=2,scale=50,size=(3,4))
    print(c5)


arangeTest()
arrayTest()
randomTest()


























