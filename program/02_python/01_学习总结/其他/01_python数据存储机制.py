#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
原理：    a = 2
对于上面语句，python解释器干了两件事：
（1）先在内存划分了一块内存空间，用以存放数据 2
（2）在内存中开创另一块内存空间，用以保存变量 a
（3）使 a 指向数据 2 （实际上是指向所在的地址）


1.不可变对象
程序中如果多个变量的值为同一不可变数据，则只有一个数据被这些变量引用，所以他们的内存地址都相同

2.可变对象
所有的的内存地址都不同。= =
那个数据，其他变量的内存地址都不相同


'''

#不可变对象
a1 = 256
a2 = 256
print(id(256))
print(id(a1),'\n',id(a2),'\n')

b1 = 257
b2 = 257
print(id(257))
print(id(b1),'\n',id(b2),'\n')

c1 = 468416541856
c2 = 468416541856
print(id(468416541856))
print(id(c1),'\n',id(c2),'\n')

d1 = 'apple'
d2 = 'apple'
print(id('apple'))
print(id(d1),'\n',id(d2),'\n')

#可变对象
e1 = [1,2,3]
e2 = [1,2,3]
print(id([1,2,3]))
print(id(e1),'\n',id(e2),'\n')
