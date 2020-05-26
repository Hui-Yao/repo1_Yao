#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

#将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

import math
n = int(input('请输入数字：'))
print(type(n))
factor = []
judge = 0

while True:
    for m in range(2,n+1):
        if n%m == 0:
            factor.append(m)
            if n/m == 1:
                # factor.append(m)
                judge = 1
            n = n/m
        break
    if judge:
        break

print(factor)

