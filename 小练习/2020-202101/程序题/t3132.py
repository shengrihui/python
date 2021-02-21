# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 14:26:10 2021

@author: 86159
"""

#31、编写程序，用户输入带有千分位逗号的数字字符串，然后输出不带千分位逗号的数字字符串。如果输入字符串'0'则退出程序。
def convert(strNumber):
    return ''.join(strNumber.split(','))

while True:
    x = input('输入带有千分位逗号的数字：')
    if x == '0':
        print('bye')
        break
    print(convert(x))


#32、编写程序，用户输入不带千分位逗号的数字字符串，然后输出带千分位逗号的数字字符串。

def convert(strNumber):
    # 考虑小数的情况
    temp = strNumber.split('.', 1)
    # 整数部分
    first = temp[0]
    if not first.isdigit():
        return '不是有效数字'
    # 小数部分
    try:
        second = temp[1]
        if not second.isdigit():
            return '不是有效数字'
    except:
        second = ''

    # 增加千分位逗号
    def nested(s):
        result = []
        length = len(s)
        index = length % 3
        if index != 0:
            result.append(s[:index])
        for i in range(index, length, 3):
            result.append(s[i:i+3])
        return ','.join(result)
    
    first = nested(first)
    # 小数部分和整数部分的千分位不一样
    if second:
        second = ''.join(reversed(second))
        second = nested(second)
        second = ''.join(reversed(second))
        # 删除两侧可能的0和千分位逗号
        return '.'.join([first, second]).strip(',0')
    # 删除整数左侧可能的0和逗号
    return first.lstrip('0,')

# 测试
while True:
    x = input('输入不带千分位逗号的数字：')
    if x == '0':
        print('bye')
        break
    print(convert(x))
