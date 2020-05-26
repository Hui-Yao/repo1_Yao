#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

#目标编写装饰器timmer（），为函数test（）统计运行时间

import time

def timmer(func):
    def deco(*args,**kwargs):     #现在这个deco才是test函数，有参数也往这里deco的括号里加，
        start_time = time.time()  #可以将deco函数编写为任何你想要的函数
        res = func(*args,**kwargs)      #有参数这里也要加，因为这是真正的被修饰的函数
        #返回值前可以在加些代码
        stop_time = time.time()
        print('the run time of test:',stop_time-start_time)
        return res      #这样可以实现返回原函数的返回值
    # print(test1)   #不知道为什么输出不了test1的地址
    return deco

@timmer         #@timmer等价于test = timmer（test），这里直接就调用了timmer函数,同时也声明了test（）函数
def test1():     # 在a函数上加@b，相当于在a函数下面协商这样的语句——a = b（a）
    time.sleep(1)
    print('in the test1.')
@timmer
def test2(name):        #修饰有参数，有返回值的函数
    time.sleep(1)
    print('the author is:',name)
    return 'hui_yao'

test1()
print(test2('hui'))

