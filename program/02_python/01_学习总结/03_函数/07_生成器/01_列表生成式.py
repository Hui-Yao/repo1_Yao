#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''列表生成式：
定义：将for循环和if语句整合在一起用以生成新列表的方法。
语法：[元素位 for循环 if语句]
原理：将for循环（产生元素）与if语句（过滤元素）的结果传递给 元素位，用以生成列表。

其中for循环可以多层嵌套，if语句只能进行一个判断(因为只有元素位一个接受位),
元素位也可进行各种操作（例如使用该元素对象的方法等等）。并且在以上三个位置中都可以调用别的函数！！


'''


#目标1:输出一个列表，其元素为0~9
a = []
for i in range(0,10):
    a.append(i)

print(a)


a2 = [i for i in range(0,10)]    #复习一下：range（）函数左闭右开，生成的是一个可迭代对象
print(a2)

#目标2：输出一个列表，输出0~9中偶数的平方,奇数的立方
b = []
for i in range(0,9):
    if i%2 == 0:
        b.append(i**2)

print(b)

b2 = [i**2 for i in range(0,9) if i%2 == 0]
print(b2)

#目标3：输出99乘法表

c = ['%s*%s = %s'%(m,n,m*n) for m in range(1,10) for n in range(1,10)]
print(c)

