# -*- coding: utf-8 -*-
"""
Created on  2021/10/28 17:21
    
@author: shengrihui
"""
import base64
import json
import requests
def base64_api(uname, pwd, img,typeid):
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd,"typeid":typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
    return ""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from tqdm import tqdm

bro=webdriver.Chrome(executable_path='chromedriver.exe')
#bro.get('https://www.baidu.com')

#bro.get('http://i.mooc.chaoxing.com/space/index?t=1631526459928')
bro.get('https://mooc1.chaoxing.com/course/200024563.html?_from_=219851663_44738115_170191601_a7e08ff28f312ace578b906eb8e5eac6&rtag=')
sleep(1)
login=bro.find_element_by_xpath('//*[@id="outerBody"]/div[1]/div[2]/div/div[2]')
login.click()

#登录
phonenumber=bro.find_element_by_name("uname")
phonenumber.send_keys('15958653143')
password=bro.find_element_by_name('password')
password.send_keys('srhxxt0018')
#img=bro.find_element_by_xpath('//*[@id="numVerCode"]/src')
#print(img.text)
#result = base64_api(uname='shengrihui', pwd='srhtj0018', img=img_path,typeid='1003')
sleep(20)  #输验证码
password.send_keys(Keys.ENTER)

course_list=bro.find_elements_by_xpath('//*[@id="courseList"]/li[*]/div[0]')
for course in course_list:
    course.click()