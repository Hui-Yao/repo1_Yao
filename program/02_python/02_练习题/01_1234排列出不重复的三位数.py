#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

#有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？


#my method
count = 0
for i in range(1,5):
    for j in range(1,5):
        if i != j:
            for k in range(1,5):
                if i != k and j != k:
                    print(i,j,k)
                    count += 1

print('there is %s number...'%count)

#配套答案
number = 0

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j != k:
                print(i,j,k)
                number += 1

print(number)


