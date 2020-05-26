#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

#题目：对10个数进行降序排序。

num_list = []
for i in range(10):
    num_list.append(int(input('请输入数字：')))

change = []

for i in range(10):
    max1 = max(num_list)
    change.append(max1)
    num_list.remove(max1)
print(change)




