# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 16:51:17 2021

@author: shengrihui
"""

import time
print('''
你好！
这是一个有点小愚蠢的斗地主小游戏。
虽然有点小愚蠢，但还是可以玩的哦。
要开始吗？
''')

t=input('输入"Y"表示开始，输入"N"表示离开（不区分大小写）:')

while 1:
    t=t.upper()
    if t!='Y' and t!='N':
        print('你输了个啥？')
        t=input('再来一遍吧：')
    else:
        break
if t.upper()=='Y':
    print("""
那开始吧。
规则什么的就和斗地主一样，我就不说了。
只是我们的出牌方式是需要键盘输入的，但也是不区分大小写的。
其中，大王用'B'来表示，小王用'S'来表示。
对输入没有特殊要求哦。
现在，让我们开始吧！
       
    """)
    import process
elif t.upper()=='N':
    print('啊，这。')
    time.sleep(2)
    print('这。')
    time.sleep(2)
    print('那再见吧。')
    time.sleep(5)