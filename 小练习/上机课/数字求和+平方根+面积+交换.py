# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:24:03 2020

@author: 86159
"""
a=float(input("输入第一边的长："))
b=float(input("输入第二边的长："))
c=float(input("输入第三边的长："))
s=(a+b+c)*0.5
ss=(s*(s-a)*(s-b)*(s-c))**0.5
print('三角形的面积是%.3f' %(ss))







x=input("输入x的值：")
y=input("输入y的值：")
t=x
x=y
y=t
print("交换后x的值是{}".format(x))
print("交换后y的值是{}".format(y))


print("他的学号是{1}，名字叫{2}，是{0}".format(200611,"abc","sss"))
print("{0:+^20}".format("python"))

num1=float(input("输入第一个数字："))
num2=float(input("输入第二个数字："))
s=num1+num2
print("{0}与{1}的和是{2}".format(num1,num2,s))

print('两数之和为%.1f' %(float(input('输入第一个数字：'))+float(input("输入第二个数："))))

num3=float(input('输入一个数字:'))
print('%0.3f的平方根是%0.3f' %(num3,num3**0.5))




