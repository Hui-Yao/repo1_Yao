#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

from threading import Thread
import time

def first():
    print(111)
    time.sleep(1)
    print(100)

def second():
    print(222)
    time.sleep(2)
    print(200)

t1 = Thread(target=first)
t2 = Thread(target=second)

# t1.daemon = True
'''把t1设置为守护线程时：
因为t2的执行时间更久，在t2的执行过程中，守护进程t1便执行完了，所以所有都会输出
'''
t1.start()
t2.setDaemon(True)
'''把t2设置为守护线程时：
当守护线程t2在睡2s的过程中，主进程已经执行完了，t2被强行结束，便不会打印200
'''
t2.start()

print('main***')

