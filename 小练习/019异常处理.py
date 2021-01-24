# -*- coding: utf-8 -*-
"""
Created on Fri Dec 25 20:10:30 2020

@author: 86159
"""



try:    #将可能出现异常的语句放在try里面
    a=int(input('请输入一个整数：'))
    b=int(input('请输入一个整数：'))
    result=a/b
    #except 捕获异常的类型，可以不写，
except ValueError:
    print('请输入整数。')
except ZeroDivisionError:
    print('除数不能为0')
except BaseException as e:
    print('出错了',e)
    #如果正常，执行else
else:
    print(result)
    #不管正常还是出错，都执行finally,tryz之后是except或者else，然后是finally
finally:
    print('再见。')
        

