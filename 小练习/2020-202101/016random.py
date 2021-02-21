# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 17:48:12 2020

@author: 86159
"""

import random



f=lambda x,y:'{}{}'.format(x,y)

a=random.random()   #random用于生成一个0到1的随机浮点数：0<= n < 1.0
print(f('random\t',a))

b=random.uniform(1,3)
print(f('unform(1,3)\t',b))
b=random.uniform(4,3)
print(f('unform(4,3)\t',b))
b=random.uniform(3,3)
print(f('unform(3,3)\t',b))

print('randint(a,b)，a和b都能娶到')
c=random.randint(1,3)
print(f('randint(1,3)\t',c))
c=random.randint(2,3)
print(f('randint(2,3)\t',c))

d=random.randrange(10,30,2)
print('randrange()从指定范围内，按指定基数递增的集合中 获取一个随机数。')
print(f('randrange(10,30,2)\t',d),'\t等效random.choice(range(10,30,2))')

e=random.choice('abcdefg')
print(f("random.choice('abcdefg')\t",e))

f1=list(range(1,20,3))
random.shuffle(f1)
print(f("random.shuffle(f1)\t",f1))

g=list(range(6))
gg=random.sample(g,3)
print('从指定序列中随机获取指定长度的片断并随机排列。注意：sample函数不会修改原有序列')
print(f('random.samplelist(range(6))(,3)\t',gg))




