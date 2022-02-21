import pyautogui
import pyperclip
import time

def mouseClick(img, c=1):
    location = pyautogui.locateCenterOnScreen(img, confidence=0.9)
    if location is not None:
        print(location)
        pyautogui.click(location.x, location.y, clicks=c, interval=0.3, duration=0.3, button='left')
        return True
    else:
        return False

def temperature():
    import random
    return random.randint(362,371)/10

def doTask(task):
    if task['type'] == '双击图片':
        if mouseClick(task['content'], 2):
            return True
        else:
            return False
    elif task['type'] == '单击图片':
        return mouseClick(task['content'], 1)
    elif task['type'] == '输入':
        print(task['content'])
        pyperclip.copy(task['content'])
        #pyautogui.typewrite(message=task['content'], interval=0.25)
        pyautogui.hotkey('ctrl', 'v')
        return True
    elif task['type'] == '滚轮':
        pyautogui.scroll(task['content'])
        return True
    elif task['type'] == '单击':
        x,y=pyautogui.position()
        pyautogui.click(x,y)
        return True
    return False


if __name__ == '__main__':
    tasklist = [
        {"type": "双击图片", "content": "dingding.png"}, #打开钉钉
        {"type": "单击图片", "content": "gzt.png"},   #打开工作台
        {"type": "单击图片", "content": "mrjkdk.png"},    #打开每日健康打卡
        {"type": "单击图片", "content": "dtx.png"},   #打开待打卡
        {"type": "滚轮", "content": -300},
        #{"type": "单击图片", "content": "number.png"},
        #{"type": "输入", "content": str(temperature())},
        {"type": "单击图片", "content": "place.png"},
        {"type": "单击", "content": ""},
        {"type": "输入", "content": "浙江省台州市玉环市玉城街道中段村泽坎路51号"},
        {"type": "单击图片", "content": "tj.png"},
    ]

    i = 0
    while i < len(tasklist):
        if doTask(tasklist[i]):
            i += 1
            time.sleep(3)
        else:
            print(tasklist[i]['type'] + ".....")
