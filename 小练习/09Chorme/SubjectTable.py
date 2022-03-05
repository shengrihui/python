from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import *
from lxml import etree
import json


# 登录
def login(usernumber='20061104', password='srh0018+'):
    login_img = bro.find_element_by_xpath('//*[@id="ampHasNoLogin"]')
    login_img.click()
    sleep(3)
    username_input = bro.find_element_by_name("username")
    username_input.send_keys(usernumber)
    password_input = bro.find_element_by_id('password')
    password_input.send_keys(password)
    password_input.send_keys(Keys.ENTER)
    sleep(2)

    # 切换到教务系统
    # jiaowu = bro.find_element_by_xpath('//*[@id="ampTabContentItem0"]/div[6]/pc-card-html-5399202351392607-01/amp-w-frame/div/div[2]/div/div/div/div/widget-app-item[1]/div/div/div[1]/img')
    while True:
        try:
            print("进入教务系统...")
            jiaowu = bro.find_element_by_xpath(
                '//*[@id="ampTabContentItem0"]/div[1]/pc-card-html-4764378802414004-01/amp-w-frame/div/div[2]/div[1]/div/div/div/div/div/div/div[2]/div/widget-app-item[4]/div/div/div[2]/div[1]')
            jiaowu.click()
            break
        except:
            sleep(1)
    # # 公共课表查询
    # sleep(2)
    # print(bro)
    # #(windows)
    # #public_subject = bro.find_element_by_xpath('//*[@id="divSubMenuList"]/div[5]/div[1]/a')
    # print("进入公共课表查询...")
    # windows = bro.window_handles
    # bro.switch_to.window(windows[-1])
    #
    # while True:
    #     try:
    #         print("进入公共课表查询...")
    #         public_subject=bro.find_element_by_xpath('//*[@id="divSubMenuList"]/div[5]/div[1]')
    #         public_subject.click()
    #         break
    #     except:
    #         sleep(1)
    sleep(5)


# 读取表格当中的课程信息
def read_table(**kwargs):
    global bro

    def read_divoneclass(*args, **kwargs):
        tree=etree.HTML(divoneinner.get_attribute("outerHTML"))
        span_list=tree.xpath('.//span')
        

    one_classroom = []
    tr_list = bro.find_elements(By.XPATH, '//*[@id="tableMain"]/tbody/tr')
    class_idx_week = [1] * (weekdays := len(tr_list[0].find_elements(By.TAG_NAME, 'th')) - 1)
    class_idx_day = 0
    for tr_idx, tr in enumerate(tr_list):
        if tr_idx == 0 or tr.find_element(By.TAG_NAME, 'th').get_attribute("class") == "thRest":
            continue
        class_idx_day += 1
        td_list = tr.find_elements(By.TAG_NAME, 'td')
        for td_idx, td in enumerate(td_list):
            class_last_time = int(td.get_attribute("rowspan"))
            # weekday循环：找出这个td是星期几
            for weekday in range(weekdays):
                if class_idx_week[weekday] == class_idx_day:
                    try:
                        divoneinner_list = td.find_elements(By.CLASS_NAME, "divOneInner")
                    except:
                        divoneinner_list = []
                    for divoneinner in divoneinner_list:
                        read_divoneclass(divoneinner, **kwargs, weekday=weekday, class_idx=class_idx_day)
                    class_idx_week[weekday] += class_last_time
                    break

    exit(0)


def get_subject_table_from_web():
    global bro, all_class
    bro = webdriver.Chrome(executable_path='chromedriver.exe')
    bro.set_window_rect(500, 0, 1920 * 0.9, 1040 * 0.9)
    # http://ehall.cidp.edu.cn/new/index.html
    # bro.get("http://ehall.cidp.edu.cn/new/index.html")
    # sleep(3)
    # login()
    bro.implicitly_wait(3)
    bro.get('https://jw.cidp.edu.cn/Teacher/TImeTable.aspx?display=11111111111&isPublic=1')
    campus_select = bro.find_element(By.XPATH, '//*[@id="ddlCampus"]')
    building_select = bro.find_element(By.XPATH, '//*[@id="ddlBuilding"]')
    classroom_select = bro.find_element(By.XPATH, '//*[@id="ddlClassRoom"]')
    week_select = bro.find_element(By.XPATH, '//*[@id="ddlWeek"]')
    for campus_idx, campus in enumerate(Select(campus_select).options):
        Select(campus_select).select_by_index(campus_idx)
        for building_idx, building in enumerate(Select(building_select).options):
            if building.text != "天仪楼":
                continue
            Select(building_select).select_by_index(building_idx)
            for classroom_idx, classroom in enumerate(Select(classroom_select).options):
                if classroom_idx == 0:
                    continue
                Select(classroom_select).select_by_index(classroom_idx)
                # for week_idx,week in enumerate(Select(week_select).options):
                #     if 0<week_idx<=16:
                # Select(week_select).select_by_index(week_idx)
                read_table(campus=campus.text, building=building.text, classroom=classroom.text)


if __name__ == '__main__':
    all_class = []
    get_subject_table_from_web()
