#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
三目运算符的格式（官方）：
# first version -- no parens
level = 1 if logging else 0
# second version -- no parens
level = (1 if logging else 0)

含义：当if成立时，取if前的值，不成立则取else后的值

推荐使用第二种


'''



a = int(input('请输入第一个数：'))
b = int(input('请输入第二个数：'))

# max = a if a>=b else  b
# print(max)

max = (a if a>=b else  b)
print(max)

#三目运算可以多重嵌套
lala = lambda x:(10 if x>10 else (-10 if x<-10 else x))
print(lala(19))

