# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:40:01 2020

@author: 86159
"""

'''
li=[[1,2],2]
print('id(li)',id(li))
print('id(li[0]})',id(li[0]))
print('id(li[1])',id(li[1]))
print('id(li[0][0])',id(li[0][0]))
a=2
print(id(li[1])==id(li[0][1]))
print(a is li[1])
s='123'
print(id(s[1]))
print(id(s))
'''


import copy

a=[10,20,[5,6]]
b=copy.copy(a)
print('a:',a)
print('b:',b)
print('{:*^20}'.format('浅拷贝'))
b.append(30)
b[2].append(7)
print('a:',a)
print('b:',b)
print('b[2][0] is a[2][0]',b[2][0] is a[2][0])

'''
c=a
print('c is a',c is a)
print('b is a',b is a)
c.append(50)
print(c,a)

'''

a=[10,20,[5,6]]
b=copy.deepcopy(a)
print('a:',a)
print('b:',b)
print('{:*^20}'.format('深拷贝'))
b.append(30)
b[2].append(7)
print('a:',a)
print('b:',b)

print('b[2][0] is a[2][0]',b[2][0] is a[2][0])
print('a[0] is b[0]',a[0] is b[0])
