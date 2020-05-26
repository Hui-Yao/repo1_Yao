#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author = Hui_Yao

'''元组的增删改查：
创建：在创建一个元祖时，逗号比空格重要
删：只能直接删除整个元组，不能删除内部元素；元组内陆嵌套了可变对象另当别论
查：索引，分片

'''

print(type((123)),type((123,)))     #未加逗号是int，加了逗号是tuple

print('元组方法'.center(50,'*'))

tiger = (123,'tiger','run')

xi1 = tiger.count(123)      #1.count(value)——统计元组中value的个数
print(xi1)

tiger.index('tiger')        #2.index(value[,start[.end]])——从左边开始寻找，返回第一个value项的index；可以指定搜索范围



