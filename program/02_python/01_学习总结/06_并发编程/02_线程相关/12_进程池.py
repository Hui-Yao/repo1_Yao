#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process
import os,time,random


def task(name):
    print('%s的pid：%s'%(name,os.getpid()))
    time.sleep(random.randint(1,3))

pool = ProcessPoolExecutor()
# for i in range(10):
#     pool.submit(task,'进程%s'%i)
#     print('如果连续输出这句话，说明是异步提交')

pool.map(task,range(10))    #map()方法相当于for循环与pool.submit()的结合，与上面一段代码相同效果

'''pool.submit()
向进程池提交任务，则线程池会创建相应的进程。
这个提交任务是异步提交，也就是说提交完任务无需等待任务执行，接着便会去执行下面的代码。

'''

pool.shutdown()
'''
相当于pool.close()+pool.join()，在此位置会封住进程池的入口，并且执行完进程池中的所有任务（进程）
默认参数wait = True,意为 等待池内所有任务执行完毕回收完资源后才继续
       wait = False,意为 继续向下执行，并不会等待进程池中的所有任务执行完
       
'''


'''
进程0的pid：31555
进程1的pid：31557
进程2的pid：31558
进程3的pid：31556
进程4的pid：31557
进程5的pid：31555
进程6的pid：31558
进程7的pid：31556
进程8的pid：31555
进程9的pid：31558

如果不指定进程池可同时处理的进程的数量，则默认为电脑的核数
在输出中，只有4个不同的pid，也就证明了进程池只能驱动cpu同时处理4个进程
'''












