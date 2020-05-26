#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"


#方法一：将数a依次除以所有比a小的数，若能整除则不为素数，全都不能整除则为素数
for i in range(101,201):
    judge = 1
    for j in range(2,i):
        if i%j == 0:
            judge = 0
    if judge == 1:
        print(i)


print('分割线'.center(50,'*'))

#方法二：假设数a的两个因子为c，d，根号a为e，则总有一个数大于或等于e，另一个小于等于e，故将a除以冲2到根号a，，，
from math import  sqrt
for i in range(101,201):
    judge = 1
    for j in range(2,int(sqrt(i))):
        if i%j == 0:
            judge = 0
    if judge ==1:
        print(i)

# 方法三：所有的自然数均可由6x+i表示，其中6x,6x+2,6x+3,6x+4均可由2或3整除，质数一定出现在6x两侧。
#        那么接下来就只需要判断6x两侧的数是否为质数就行了。
from math import sqrt

raw = int(input('请输入待判断的数：'))
judge = 1

if raw <= 3:
    pass
elif not(raw%6 == 1 or raw%6 == 5):
    judge = 0

for i in range(5,int(sqrt(raw))+1):
    if raw % i == 0:
        judge = 0
    else:
        pass
if judge:
    print('this is a parime number.')
else:
    print('this is not a prime number.')












