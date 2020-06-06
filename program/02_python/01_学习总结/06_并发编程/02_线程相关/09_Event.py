#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
Event适用的情况是，一个线程中的运行进度要依靠另一个进程的信号。

Event兑现各种那个包含了可由线程设置的信号标志，初始情况下，信号值为假。如果有线程等待一个Event对象，
而且这个Event对象的信号为假，那么这个线程将会一直堵塞直至该标志为真。

一个线程如果将一个Event对象的信号标志设置为真,它将唤醒所有等待这个Event对象的线程。
如果一个线程等待一个已经被设置为真的Event对象,那么它将忽略这个事件, 继续执行

Event常用方法：
event.is_set():返回此Event对象的信号值
event.wait()：如果 event.isSet()==False将阻塞线程；
event.set()： 设置event的状态值为True，所有阻塞池的线程激活进入就绪状态， 等待操作系统调度；
event.clear()：恢复event的状态值为False。


'''

from threading import Thread,Event
import threading
import time,random
def conn_mysql():
    count=1
    while not event.is_set():   #event.is_set()返回当前Event对象中信号值的真假。
        if count > 3:
            raise TimeoutError('链接超时')
        print('<%s>第%s次尝试链接' % (threading.current_thread().getName(), count))
        event.wait(0.5)
        count+=1
    print('<%s>链接成功' %threading.current_thread().getName())
def check_mysql():
    print('\033[45m[%s]正在检查mysql\033[0m' % threading.current_thread().getName())
    time.sleep(random.randint(2,4))
    event.set()     #只有check函数中将信号值设置为真，前面的两个连接函数才能该继续执行
if __name__ == '__main__':
    event=Event()
    conn1=Thread(target=conn_mysql)
    conn2=Thread(target=conn_mysql)
    check=Thread(target=check_mysql)
    conn1.start()
    conn2.start()
    check.start()








