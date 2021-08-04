                                                                    # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

for i in range(1,6):
    j=6-i
    s=""
    while j>0:
        s+=" "
        j-=1
    j=2*i-1
    while j>0:
        j-=1
        s+="*"
    print(s)