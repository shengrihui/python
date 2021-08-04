# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 16:31:48 2020

@author: 86159
"""
#试编程从键盘输入用户的性别（用字符型变量sex存储，输入字符F代表女性，输入字符M表示男性）、父母身高（用实型变量存储，faHeight为父亲身高，moHeight为母亲身高）、是否喜爱体育锻炼（用字符型变量sports存储，输入字符Y表示喜爱，输入字符N表示不喜爱）、是否有良好的饮食习惯（用字符变量diet存储，输入字符Y表示良好，输入字符N表示不好）等条件，利用给定公式和身高预测方法对身高进行预测。

sex=input('请输入性别（输入字符F代表女性，输入字符M表示男性）：')

sports=input("是否喜爱运动（输入Y表示喜爱，输入N表示不喜爱）：")
diet=input("饮食是否习惯（输入Y表示良好，输入N表示不好）：")


faheight=float(input("请输入父亲的身高（cm）："))
maheight=float(input("请输入母亲身高（cm）："))
if sex=="M":
    height=(faheight+maheight)*0.54
else:
    height=(faheight*0.923+maheight)/2
    
if diet=="Y":
    height*=1.02

if sports=="Y":
    height*=1.015
    
print("预测身高为%.2fCM" %(height))