# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 19:53:38 2020

@author: 86159
"""

#编程计算： s=1-1/2+1/3-1/4+……+1/99-1/100
s=0
for i in range(1,101):
    s += (-1)**(i-1)*(1/i)
print(s)


#判断素数
#异常处理，强制输入大于2的数字
while 1:
    try:
        n=eval(input("请输入一个大于2的整数："))
        if n>2:
            break
    except:
        print("请重新输入！")
        continue
for i  in range(2,n//2):
    if n/i == n//i:
        print("{}不是一个素数".format(n))
        break
else:
    print("{}是一个素数".format(n))



#水仙花数
m=int(input('请输入一个三位数：'))
a,b,c= m//100,m//10%10,m%10
if a**3+b**3+c**3==m:
    print(m,'是水仙花数')
else:
    print(m,'不是水仙花数')





