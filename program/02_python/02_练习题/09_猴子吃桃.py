#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

#猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个;第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
# 以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。


left = int(input('请输入剩余桃子数：'))
day = int(input('请输入天数：'))

for i in range(day-1):
    left = (left+1)*2

print('第一天采了%s个桃子'%left)

