# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:26:03 2020

@author: 86159
"""


h=float(input("请输入身高（米）："))
w=float(input("请输入体重（千克）："))
t=w/(h**2)
if t<18:
    print('偏瘦')
elif 18<=t<25:
    print("正常")
elif 25<=t<27:
    print("超重")
else:
    print("肥胖")




