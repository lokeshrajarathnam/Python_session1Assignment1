# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
alist =[]

for val in range(2000,3200):
    if(val % 7) ==0 and (val % 5) != 0:
        alist.append(val)
        acount +=1
print(alist)



