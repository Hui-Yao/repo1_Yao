#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

#求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。
# 例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

a = int(input('请输入叠数：'))
b = int(input('请输入相加次数：'))

sum = 0
var = [None]*b

for i in range(b):
    var[i] = (a if i == 0 else var[i-1]*10+a)
    sum += var[i]

print('sum = ',end='')
for i in range(b):

    if i == b-1:
        print('%s '%var[i],end='')
    else:
        print('%s+'%var[i],end ='')

print('= %s'%sum)




