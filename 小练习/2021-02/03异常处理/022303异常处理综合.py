# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 23:16:32 2021

@author: shengrihui
"""
import traceback
class AgeError(Exception):
    def __init__(self,ErrorImfo):
        Exception.__init__(self)
        self.ErrorImfo=ErrorImfo
        
    def __str__(self):
        return "{}年龄错误，应在0到150之间！".format(self.ErrorImfo)
    

#异常可能会在别的地方导入
if __name__=="__main__":
    try:
        age=int(input("请输入一个年龄："))
    except :
        print("输入的不是数字哦。")
        with open(".\err.txt","w") as f:
            traceback.print_exc(file=f)
    else:
        if not (0<age<150):
            raise AgeError(age)
        else :
            print("输入年龄正常。")
            