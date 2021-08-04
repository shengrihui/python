# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:39:55 2021

@author: 86159
"""

#29、编写函数，给定任意字符串，找出其中只出现一次的字符，如果有多个这样的字符，就全部找出。


s=input('输入：')

ss=set(s)
for i in ss:
    if s.count(i)==1:
        print(i)



