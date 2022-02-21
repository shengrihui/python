# -*- coding: utf-8 -*-
"""
Created on  2021/7/1 21:11
    
@author: shengrihui
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from tqdm import tqdm

#登录
def login(phonenumber='15958653143',password='Srhykt0018'):
    changeimg=bro.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/img')
    changeimg.click()
    sleep(1)
    phonenumber_input=bro.find_element_by_name("loginname")
    phonenumber_input.send_keys(phonenumber)
    password_input=bro.find_element_by_name('password')
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    sleep(3)
    
    #切换到我听的课
    subjech=bro.find_element_by_xpath('//*[@id="tab-student"]')
    subjech.click()
    sleep(2)

def each_ppt():
    ppts = bro.find_elements_by_class_name("container")
    for ppt in ppts:
        ppt.click()
        if '未读'  in ppt.text:
            sleep(6)
    bro.close()
    windows=bro.window_handles
    bro.switch_to.window(windows[-1])

def enter_ppts():
    # 成绩单
    score = bro.find_element_by_xpath('//*[@id="tab-student_school_report"]/span')
    score.click()
    sleep(3)
    
    lessons = bro.find_elements_by_xpath('//*[@id="pane-student_school_report"]/div/div[2]/section[2]/div[6]/ul/li')
    while lessons == []:
        sleep(3)
        lessons = bro.find_elements_by_xpath('//*[@id="pane-student_school_report"]/div/div[2]/section[2]/div[6]/ul/li')

    for lesson in lessons:
        if lesson.text=='老师没有在该模块发布教学活动':
            break
        if '已完成' in lesson.text:
            continue
        lesson.click()
        
        sleep(4)
        # 进入课件
        windows = bro.window_handles
        bro.switch_to.window(windows[-1])
        
        openppt = None
        while openppt == None:
            openppt = bro.find_element_by_xpath('//*[@id="app"]/div[2]/div/section/main/div[1]/div[1]/div/div[2]/div[2]')
            openppt.click()
            sleep(3)
        each_ppt()

def choose_subject(subject_list=[]):
    lessons=bro.find_elements_by_xpath('//*[@id="pane-student"]/div/div/div[*]')
    for lesson in lessons:
        name=lesson.find_element_by_xpath('./div/div[1]/div/div[1]/div[1]/h1')
        if name.text in subject_list or subject_list==[]:
            name.click()
            sleep(5)
            enter_ppts()
            bro.back()



# import os
# os.system('shutdown /s /t 60')

if __name__=='__main__':
    bro = webdriver.Chrome(executable_path='chromedriver.exe')
    bro.get("https://changjiang.yuketang.cn/v2/web/index")
    sleep(1)
    #login('15518860964',"Zz302048") #drink
    login('15958653143','Srhykt0018')
    #login('16639159358','Yuketang2003') #zhangxuanyuan
    choose_subject([])
    #choose_subject()

    bro.quit()


