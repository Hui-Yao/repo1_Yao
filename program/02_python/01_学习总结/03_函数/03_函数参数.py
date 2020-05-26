#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''return语句：
用于终止函数
其后的的参数可以使任何情况——无参数，一个参数，多个参数（返回的是一个元素），变量，表达式，函数（高阶函数）
'''

'''函数的参数：
1.必须参数：可用位置参数与关键字参数指定。
    1.1 位置参数根据一一对应的位置来给必须参数传值，关键字参数通过指定文件名来传值，这可以不按顺序来。
    1.2 关键字参数不能在位置参数前面,哪怕必须参数能对应上。
    
2.默认参数：非必穿参数，也可通过位置，与关键字参数传入

3.可变参数：
    3.1 *args：收集多余的位置参数，形成一个元组
    3.2 **kwargs：收集多余的关键字参数，以形成一个字典

定义参数的顺序：
def dunc(必须参数，默认参数，*args,**kwargs)

'''

#必须参数
def apple(x,y,z):
    print(x)
    print(y)
    print(z)

apple(1,2,3)
apple(1,z=3,y=2)
#apple(1,y=2,3)     #会报错

def orange(x,y=2,*args):
    print(x,y,args)

orange(1,3,4,5,6)   #1 3 (4, 5, 6)
orange(*(1,2,3,4))  #1 2 (3, 4)    用序列(列表，元组)赋值的话，还是先要将必须参数与默认参数赋值完。

def pear(x,y=2,*args,**kwargs):
    print(x,y,args,kwargs)

pear(1,3,'hello','check',name = 'jack',age = '18',**{'name2':'jack','age2':18})

person = {'name':'jack','age':18}
pear(1,3,'hello','check',**person)  #也可用**dict来传入关键字参数


