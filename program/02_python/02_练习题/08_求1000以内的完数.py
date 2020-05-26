#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

#一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

from math import sqrt

num_list = []       #用来存放完数

for i in range(1,1001):
    factor_list = []    #用来存放因子
    sum = 1
    for j in range(2,int(sqrt(i))):     #求因子并存放
        if i % j == 0:
            factor_list.append(j)
            factor_list.append(i%j)

    for k in range(len(factor_list)):   #求因子的和
        sum += factor_list[k]

    if i == sum:                #判断因子之和是否等于该数
        num_list.append(i)

print(num_list)





