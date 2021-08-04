# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 12:44:25 2021

@author: 86159
"""

#30、阅读以下冒泡法排序代码，尝试写出优化代码，提高代码运行效率。

from random import randint
import time
co=20000
nu=999

"""
a=time.time()
lst = [randint(1, nu) for i in range(co)]
print('Before sort:\n', lst)
lst.sort()
print('After sort:\n', lst)
b=time.time()
t0=b-a


a=time.time()
lst = [randint(1, nu) for i in range(co)]
print('Before sort:\n', lst)
lst=sorted(lst)
print('After sort:\n', lst)
b=time.time()
t00=b-a
"""


'''-------------------冒泡排序--------'''
def bubbleSort1(lst):
    length = len(lst)
    for i in range(0, length):
        for j in range(0, length-i-1):
            #比较相邻两个元素大小，并根据需要进行交换
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

a=time.time()
lst = [randint(1, nu) for i in range(co)]
#print('Before sort:\n', lst)
bubbleSort1(lst)
#print('After sort:\n', lst)
b=time.time()
t1=b-a



"""
'''--------参考答案：--------'''
def bubbleSort2(lst):
    length = len(lst)
    for i in range(0, length):
        flag = True
        for j in range(0, length-i-1):
            #比较相邻两个元素大小，并根据需要进行交换
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                flag = False
        if flag:
            break
a=time.time()
lst = [randint(1, num) for i in range(co)]
print('Before sort:\n', lst)
bubbleSort2(lst)
print('After sort:\n', lst)
b=time.time()
t2=b-a
"""

"""
'''---------------选择排序----------------'''
def bsort1(lis):
    length=len(lis)
    for i in range(0,length-1):
        k=i
        for j in range(i+1,length):
            if lis[j]>lis[k]:
                k=j
        lis[i],lis[k]=lis[k],lis[i]
        
a=time.time()
lst = [randint(1, nu) for i in range(co)]
print('Before sort:\n', lst)
bsort1(lst)
print('After sort:\n', lst)
b=time.time()
t3=b-a
"""


"""
'''---------------插入排序-----'''
def bsort2(lst):
    length=len(lst)
    for i in range(length-1):
        for j in range(i+1,0 ,-1):
            while lst[j]<lst[j-1]:
                lst[j],lst[j-1]=lst[j-1],lst[j]
a=time.time()
lst = [randint(1, nu) for i in range(co)]
print('Before sort:\n', lst)
bsort2(lst)
print('After sort:\n', lst)
b=time.time()
t4=b-a
"""

'''-----------桶排序----------'''
def tsort1(lst):
    d={}
    for i in lst:
        d[i]=d.get(i,0)+1
    lst.clear()
    lt=list(d.items())
    lt.sort(key=lambda x:x[0])
    for i in lt:
        for j in range(i[1]):
            lst.append(i[0])
            
a=time.time()
lst = [randint(1, nu) for i in range(co)]
#print('Before sort:\n', lst)
tsort1(lst)
#print('After sort:\n', lst)
b=time.time()
t5=b-a





print('共有%d个数' %co)
print('数字范围是',nu)
#print('sort',t0)
#print('sorted',t00)
print('冒泡普通',t1)
#print('参考答案',t2)
#print('选择排序',t3)
#print('插入排序',t4)
print('桶排序 ',t5)










