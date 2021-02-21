# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 11:56:40 2021

@author: 86159
"""

#27、有n个乒乓球运动员打淘汰赛，编写函数计算至少需要多少场比赛才能决出冠军，不允许直接使用n-1。
def demo(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    m, c = divmod(n, 2)
    return m + demo(c+m)

print(demo(int(input('输入人数：'))))