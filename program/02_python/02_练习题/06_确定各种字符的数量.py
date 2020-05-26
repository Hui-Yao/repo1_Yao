#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

#输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

str_list = list(input('请输入字符串：'))
alpha = []
num = []
space = []
other = []

for i in str_list:
    if i.isalpha():
        alpha.append(i)
    elif i.isdigit():
        num.append(i)
    elif i.isspace():
        space.append(i)
    else:
        other.append(i)

print('there are {} alpha in the str,it`s {}'.format(len(alpha),alpha))
print('there are {} digit in the str,it`s {}'.format(len(num),num))
print('there are {} space in the str,it`s {}'.format(len(space),space))
print('there are {} other characters in the str,it`s {}'.format(len(other),other))







