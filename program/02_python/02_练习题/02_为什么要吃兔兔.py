#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

# 古典问题：有一对兔子，从 出生后第3个月起 每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，
# 假如兔子都不死，问每个月的兔子总数为多少？

'''
兔子的对数：月份：1 2 3 4 5 6 7   8
          数量：1 1 2 3 5 8 13 21     斐波那契数列


'''

sum1,sum2,sum3 = 1,1,2

month = int(input('请输入当前月份数：'))
for i in range(4,month+1):
    sum1 = sum2
    sum2 = sum3
    sum3 = sum1+sum2



print('%s月的兔子数为%s。。。'%(month,sum3))


