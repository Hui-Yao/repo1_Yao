#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

def calc(n):
    if n == 0:
        return 1
    else:
        return n*calc(n-1)

print(calc(5))









