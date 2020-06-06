#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

from multiprocessing import Process
import time

def mission(name):
    print('%s 1'%name)
    time.sleep(1)
    print('%s 2'%name)
    time.sleep(1)
    print('%s 3'%name)

for i in range(3):
    p = Process(target=mission,args=('进程%s'%i,))
    p.start()
#相当于
#   p1.start()
#   p2.start()
#   p3.start()
#只是发了三个信号

'''
将mission函数视为打印机，我们希望的效果应该是子进程0全执行完，再执行进程1，再执行进程2.

但实际上可以看见进程0执行了一部分到了睡的时间，cpu又转去执行进程1，1睡了，又转去执行2，
三个子进程都睡了一秒后，cpu执行哪个子程序其实不定，所以可以看见进程1先于进程1执行。
for循环只是发了三个信号，具体的执行顺序每一轮都是不一定的。

'''


