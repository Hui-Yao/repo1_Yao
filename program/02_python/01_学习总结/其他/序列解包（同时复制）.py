#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

a = 1
b = 2
# a,b = b,a+b
a,b = c = b,a+b

print(c)
print(a,b)

'''在第三句：
a,b = b,a+b   与    a,b = c = b,a+b  是等价的，
输出c，可知c为元组。可推知同时复制的过程为先将等号右边的b，a+b组成一个元组，
等号左边的a，b再分别取对应的元素。

这是同时赋值的！！！


'''
