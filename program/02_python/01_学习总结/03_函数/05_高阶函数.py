#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''高阶函数
定义：将别的函数作为参数传给a函数，则成a函数为高阶函数

'''

def cal(a,b,f):
    sum = f(a)+f(b)
    print(sum)

cal(3,-6,abs)   #abs是计算绝对值的函数
