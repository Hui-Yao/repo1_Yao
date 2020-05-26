#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
回想一下进程queue的作用？
    进程间的内存空间是隔离的，为了实现进程间的数据交换，就需要 进程queue

线程queue的作用？
    虽然线程间的内存空间是共享的，但是为了数据交流的安全性，所以需要线程queue。
    queue is especially useful in threaded programming when information must be
    exchanged safely between multiple threads.
'''

import queue

q = queue.Queue()
q.put()



