# -*- coding: utf-8 -*-
"""
Created on  2021/7/1 21:11
    
@author: shengrihui
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from tqdm import tqdm

bro=webdriver.Chrome(executable_path='chromedriver.exe')
#bro.get('https://www.baidu.com')

bro.get('https://changjiang.yuketang.cn/v2/web/index')
sleep(1)
#登录
changeimg=bro.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/img')
changeimg.click()
sleep(1)
phonenumber=bro.find_element_by_name("loginname")
phonenumber.send_keys('15958653143')
password=bro.find_element_by_name('password')
password.send_keys('Srhykt0018')
password.send_keys(Keys.ENTER)
sleep(3)
#切换到我听的课
subjech=bro.find_element_by_xpath('//*[@id="tab-student"]')
subjech.click()
sleep(2)
#数学
math=bro.find_element_by_xpath('//*[@id="pane-student"]/div/div/div[4]/div/div[1]/div/div[1]')
math.click()
sleep(3)
#成绩单
score=bro.find_element_by_xpath('//*[@id="tab-student_school_report"]/span')
score.click()
sleep(3)

lessons=bro.find_elements_by_xpath('//*[@id="pane-student_school_report"]/div/div[2]/section[2]/div[6]/ul/li')
while lessons==[]:
    sleep(3)
    lessons = bro.find_elements_by_xpath('//*[@id="pane-student_school_report"]/div/div[2]/section[2]/div[6]/ul/li')

tbar=tqdm(lessons)
for lesson in tbar:
    lesson.click()
    sleep(2)
    #进入课件
    windows=bro.window_handles
    bro.switch_to.window(windows[-1])
    openppt=bro.find_element_by_xpath('//*[@id="app"]/div[2]/div/section/main/div[1]/div[1]/div/div[2]/div[2]')
    openppt.click()
    sleep(2)

    ppts=bro.find_elements_by_class_name("thumbImg-container")
    for ppt in ppts:
        ppt.click()
        sleep(6)
    bro.close()
    windows=bro.window_handles
    bro.switch_to.window(windows[-1])

bro.quit()




