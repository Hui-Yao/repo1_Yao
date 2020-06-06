#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
是否有序：
有序：字符串，列表，元组
无序：字典，集合

是否可变：
不可变（hashable）：数值，字符串，元组，frozenset
可变（unhashable）：列表，字典，集合

'''

import copy
a = [9999999,'str',{1,2,3},[1,2],{'apple':10,'orange':5}]

print('赋值语句'.center(50,'*'))
b = a
print('地址容器：',bool(id(a)==id(b)))
print('不可变对象：',bool(id(a[0])==id(b[0])))
print('不可变对象：',bool(id(a[1])==id(b[1])))
print('可变对象：',bool(id(a[2])==id(b[2])))
print('可变对象：',bool(id(a[3])==id(b[3])))
print('可变对象：',bool(id(a[4])==id(b[4])))

import copy
a = [9999999,'str',{1,2,3},[1,2],{'apple':10,'orange':5}]

print('浅复制'.center(50,'*'))
c = copy.copy(a)
print('地址容器：',bool(id(a)==id(c)))
print('不可变对象：',bool(id(a[0])==id(c[0])))
print('不可变对象：',bool(id(a[1])==id(c[1])))
print('可变对象：',bool(id(a[2])==id(c[2])))
print('可变对象：',bool(id(a[3])==id(c[3])))
print('可变对象：',bool(id(a[4])==id(c[4])))

import copy
a = [9999999,'str',{1,2,3},[1,2],{'apple':10,'orange':5}]

print('深复制'.center(50,'*'))
d = copy.deepcopy(a)
print('地址容器：',bool(id(a)==id(d)))
print('不可变对象：',bool(id(a[0])==id(d[0])))
print('不可变对象：',bool(id(a[1])==id(d[1])))
print('可变对象：',bool(id(a[2])==id(d[2])))
print('可变对象：',bool(id(a[3])==id(d[3])))
print('可变对象：',bool(id(a[4])==id(d[4])))

'''
https://www.cnblogs.com/huiyaoo/p/11727242.html


另外函数不可以修改全局变量中的不可变对象，但是可以修改全局变量中的可变对象的元素，是一个道理。
'''




