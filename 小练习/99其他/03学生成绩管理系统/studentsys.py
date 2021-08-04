# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 19:27:10 2021

@author: shengrihui
"""

import csv

class Student():
    def __init__(self,number,name,cla,py_s,c_s):
        self.number=number
        self.name=name
        self.cla=cla
        self.py_s=py_s
        self.c_s=c_s

class StudentSystem():
    
    def __init__(self):
        self.data_list=[]
        self.read_file()
        self.menu()
    
    def stu_in(self,num):
        '''
        这个函数用来找输入的学号是否存在
        s传入操作名称
        返回flag为-1没有这个学号，其他则是这个学号在data_list中的索引
        '''
        flag=-1
        for  i,j in enumerate(self.data_list):
            if num == j.__dict__.get('number'):
                flag=i
                break
        return flag
    
    
    def Add(self):
        number=input("请输入学号：")
        while self.stu_in(number)!=-1:
            number=input("该学号已经存在，请重新输入：")
        name=input("请输入姓名：")
        cla=input("请输入班级：")
        py_s=input("请输入python成绩：")
        while eval(py_s)<0 or eval(py_s)>100:
            py_s=input("输入的成绩不合法，请重新输入：")
        c_s=input("请输入C语言成绩：")
        while eval(c0_s)<0 or eval(c_s)>100:
            c_s=input("输入的成绩不合法，请重新输入：")
        
        s=Student(number, name, cla, py_s, c_s)
        self.data_list.append((s))
        print("添加信息成功！")
        input("\n按任意键继续...")
    
    def Delete(self):
        index=self.stu_in(num=input("请输入要删除的学生学号："))
        if index==-1:
            print("没有这个学号。")
        else:
            self.print_one(index)
            print()
            while True:
                try:
                    info=eval(input("确认要删除该学生的信息吗？（1.是/2.否）"))
                except:
                    print("输入有误，请重新输入。")
                else:
                    break
            if info==1:
                self.data_list.pop(index)
            
            input("\n按任意键继续...")
    
    
    def Updata(self):
        index=self.stu_in(num=input("请输入要修改的学生学号："))
        if index==-1:
            print("没有这个学号。")
            
        else:
            print("---1.学号 2.姓名 3.班级---")
            print("---2.python成绩 5.C语言成绩---")
            print("---0.退出---")
            info=eval(input("请选需要修改的项目："))
            while info!=0:
                if info==1:
                    upd=input("请输入修改后的学号：")
                    self.data_list[index].number=upd
                elif info==2:
                    upd=input("请输入修改后的姓名：")
                    self.data_list[index].name=upd
                elif info==3:
                    upd=input("请输入修改后的班级：")
                    self.data_list[index].cla=upd
                elif info==4:
                    upd=input("请输入修改后的python成绩：")
                    self.data_list[index].py_s=upd
                elif info==5:
                    upd=input("请输入修改后的C语言成绩：")
                    self.data_list[index].c_s=upd
                info=eval(input("修改成功！\n可以再次选择："))
            input("\n按任意键继续...")
                
    def Find(self):
        index=self.stu_in(num=input("请输入要查询的学生学号："))
        if index==-1:
            print("没有这个学号。")
        else:
            self.print_one(index)
            input("\n按任意键继续...")
    
    def print_all(self):
        print("{:<10}{:<10}{:<10}{:<10}{:<10}".format("学号","姓名","班级","python成绩","C语言成绩"))
        for stu in self.data_list:
            print("{:<10}{:<10}{:<10}{:<10}{:<10}".format(stu.number,stu.name,stu.cla,stu.py_s,stu.c_s))
    
    def print_one(self,index):
        #打印一个学生的信息
        stu=self.data_list[index]
        print("学号\t",stu.number)
        print("姓名\t",stu.name)
        print("班级\t",stu.cla)
        print("python成绩\t",stu.py_s)
        print("C语言成绩\t",stu.c_s)
    
    def read_file(self):
        try:
            with open("scores.csv","r",encoding='utf-8') as f:
                f_csv_list=list(csv.reader(f))
                print(len(f_csv_list))
                for i in f_csv_list[1:]:
                    self.data_list.append(  Student(i[0], i[1], i[2], i[3], i[4])      )
        except:
            print("没有成绩文件")
    
    def write_file(self):
        with open("scores.csv","w",encoding='utf-8',newline='') as f:
            f_csv_writer=csv.writer(f)
            f_csv_writer.writerow(['学号','姓名','班级','python成绩','C语言成绩'])
            new_data=[]
            for i in self.data_list:
                li=[i.number,i.name,i.cla,i.py_s,i.c_s]
                new_data.append(li)
            f_csv_writer.writerows(new_data)
    
    def menu(self):
        print("")
        print("---1.增加学生信息---")
        print("---2.修改学生信息---")
        print("---3.查询学生信息---")
        print("---4.删除学生信息---")
        print("---5.展示所有学生信息---")
        print("---0.保存并退出---")
        while 1:
            info=input("请选择操作：")
            if info not in ['0','1','2','3','4','5']:
                print("输入有误，请重新输入。")
                continue
            info=eval(info)
            if info==1:
                self.Add()
            elif info==2:
                self.Updata()
            elif info==3:
                self.Find()
            elif info==4:
                self.Delete()
            elif info==5:
                self.print_all()
            elif info==0:
                self.write_file()
                print("再见！")
                break

if __name__=='__main__':
    a=StudentSystem()
    
    