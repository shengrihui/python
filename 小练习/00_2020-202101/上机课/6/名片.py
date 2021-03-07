# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 16:41:23 2020

@author: 86159
"""

company=input("请输入公司：")
name=input("请输入名字：")
Class=input("请输入班级：")
no=input("请输入学号：")
title=input("请输入职位：")
phone=input("请输入电话号码：")
mail=input("请输入邮箱地址：")
print("*"*50)
print(company.center(50))
print("姓名：%s"% name)
print("班级：%s"% Class)
print("学号：%s"% no)
print("职位：%s"% title)
print("电话：%s"% phone)
print("邮箱：%s"% mail)
print("*"*50)
#print("我是来自%s的%s，学号是%s，电话号码是%s，邮箱地址是%s，请多关照！"%(Class,name,no,phone,mail))