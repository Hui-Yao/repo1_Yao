#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

from concurrent.futures import ThreadPoolExecutor
from threading import current_thread,Thread
import os,time,random




def task(name):
    print('%s的pid：%s'%(name,os.getpid()))
    time.sleep(random.randint(1,3))

pool = ThreadPoolExecutor()
for i in range(10):
    pool.submit(task,'线程%s'%i)

'''pool.submit()
向进程池提交任务，则线程池会创建相应的进程。
这个提交任务是异步提交，也就是说提交完任务无需等待任务执行，接着便会去执行下面的代码。

'''
pool.shutdown()












