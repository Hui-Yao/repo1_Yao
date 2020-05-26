#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

print(abs(-5))      #1.abs()

list1 = [1,2,0,6]
list2 = [2,54,1]
print(all(list1),all(list2))    #2.all(object)——如果obj全为真，返回true，否则返回fslse
print(any(list1),any(list2))    #3.any（object）——只要obj中有一个元素为真，就返回True，否则返回false

print(bin(1),bin(2),bin(4),bin(8))  #4.bin（）——返回该元素的二进制形式

print(bool('qdeqw'),bool(list1),bool([0]))  #5.bool()——判断真假
print(bool(0),bool([]),bool(''))

def test():
    print('hahaha')

print(callable(test))       #6.callable（）——判断obj是否可调用
print(callable(lambda : True))
print(callable(list1))

print(chr(98),chr(100))     #7.chr（）——返回数字对应的AScii码
print(ord('s'),ord('j'))    #8.ord（）——返回obj对应的数字

print(divmod(10,3),divmod(9,4))     #9.divmod（）——返回商与余数

print(list(filter(lambda x:x>3,list1)))     #10.filter（）——将后面的数据一次传入前面并判断
                                            #符合条件的就输出，不符合就不输出
print(list(map(lambda x:x**2,list1)))       #11.map（）——将后面的数据一次传入前面并进行相关操作，返回


print(frozenset({1,4,3,5,6,6}))     #12.frozenset（）——变为不可变集合
