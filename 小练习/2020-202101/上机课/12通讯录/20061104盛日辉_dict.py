# -*- coding: utf-8 -*-
"""
Created on Wed Dec  9 16:50:28 2020

@author: 86159
"""

a=["欢迎进入通讯录程序","1、查询联系人资料","2、插入心的联系人","3、删除已有联系人","4、退出通讯录程序"]
for i in a:
    print("{}{:-^15}{}".format('|',i,'|'))


txl={}
n=int(input("请输入指令代码："))

while n:
    if n==1:
        name=input("请输入联系人姓名：")
        if name in txl:
            print("{}的联系方式是：{}".format(name,txl[name]))
        else:
            print("该联系人不存在！")
    elif n==2:
        name=input("请输入联系人姓名：")
        if name in txl:
            print("该联系人已存在--->>{}：{}".format(name,txl[name]))
            w=input("是否修改联系人资料（Y/N）：")
            if w=='Y':
                tel=input("请输入联系人联系方式：")
                txl[name]=tel
                print("联系人资料修改成功！")

        else:
            tel=input("请输入联系人联系方式：")
            txl[name]=tel
            print("添加联系人成功！")
    elif n==3:
        name=input("请输入联系人姓名：")
        if name in txl:
            txl.pop(name)
            print("删除联系人成功！")
        else:
            print("该联系人不存在！")
    else:
        print("{}{:-^15}{}".format('|',"感谢使用联系人程序！",'|'))
        break
    
    n=int(input("请输入指令代码："))


