# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 16:38:27 2020

@author: 86159
"""

import time
import math


def test01():
    start=time.time()
    for i in range(100000000):
        b=math.sqrt(60)
    end = time.time()
    print('用时{}'.format(end-start))


def test02():
    a=math.sqrt
    start=time.time()
    for i in range(100000000):
        b=a(60)
    end = time.time()
    print('用时{}'.format(end-start))


test01()
test02()
