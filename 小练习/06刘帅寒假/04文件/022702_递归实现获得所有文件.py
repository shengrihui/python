# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:31:01 2021

@author: shengrihui
"""

import os


def getAllfiles(path ,level):
    dirs_list=os.listdir(path)
    for dirs in dirs_list:
        
        print('\t'*level,os.path.join(path,dirs))
        if os.path.isdir(dirs):
            getAllfiles(os.path.join(path,dirs),level+1)
        

getAllfiles("../04文件",0)




