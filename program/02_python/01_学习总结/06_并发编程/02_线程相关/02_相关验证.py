#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

#1. 开启一个新的进程的消耗比开启一个新线程的大

##创建进程的速度
# from multiprocessing import Process
#
# def hi():
#     print('how you doing?')
#
# p1 = Process(target=hi)
# p1.start()
# print('in the main process/thread')


##创建线程的速度
# from threading import Thread
#
# def hello():
#     print('hello!')
#
# t1 = Thread(target=hello)
# t1.start()
# print('in the main!')

'''
1. 创建进程，会发现一定是主进程中的先打印，因为创建一个子进程的时间相对较久
2. 创建线程，会发现一般是那个进程的的输出语句在前则先打印那个
'''

#2. 进程间的资源、内存隔离，同一进程下的子线程资源共享
from multiprocessing import Process
from threading import Thread

n = 10
def hello():
    global n
    n = 1

p1 = Process(target=hello)
p1.start()
p1.join()
print('进程：',n)


t1 = Thread(target=hello)
t1.start()
t1.join()
print('线程：',n)

#查看pid
import os
def gaga():
    print('线程所属进程PID：',os.getpid())
    print('线程的父进程PID：',os.getppid())
t2 = Thread(target=gaga)

print('子进程的PID：',p1.pid)
print('主进程的PID：',os.getpid(),os.getppid())
t2.start()

'''
可以看到线程所属进程就是当前主进程，他们的pid相同

'''








