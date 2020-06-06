#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
将for循环和if语句整合在一起用以生成(返回)新列表的方法。
语法：[元素位 for循环 if语句]
原理：将for循环（产生元素）与if语句（过滤元素）的结果传递给 元素位，用以生成列表。
注意：（1）for循环内可以使用多个变量、多层嵌套、也可以并列多个for循环
     （2）for循环后的if是一个筛选条件，直接将符合条件的值传到前面的数据位，所以不能待else
         而最开始的元素位可以进行三目元素运算符操作，可以带else，也可以叠加多层。

'''


#目标1:输出一个列表，其元素为0~9
# 普通方法
a = []
for i in range(0,10):
    a.append(i)
print(a)
# 列表生成式
a2 = [i for i in range(0,10)]    #复习一下：range（）函数左闭右开，生成的是一个可迭代对象
print('a2:',a2)

#目标2：输出一个列表，输出0~9中偶数的平方,奇数的立方
b = []
for i in range(0,9):
    if i%2 == 0:
        b.append(i**2)
    else:
        b.append(i**3)
print(b)
#列表生成式
b2 = [i**2 if i%2 == 0 else i**3 for i in range(0,9)]
print('b2:',b2)

#目标3：输出99乘法表
c = ['%s*%s = %s'%(m,n,m*n) for m in range(1,10) for n in range(1,10)]
print(c)

