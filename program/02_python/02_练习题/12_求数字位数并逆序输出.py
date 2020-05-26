#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

#给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

num = int(input('输入数字：'))
num_list = list(str(num))
length = len(num_list)
print(length)
for i in num_list[::-1]:
    print(i,end = '')


# for i in range(length):
#     change.append(num_list[long-1])
#     long-=1
# print(change,length)


