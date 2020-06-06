#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

from multiprocessing import Process
import os

def mission(num):
    print('在第{}个子进程，其pid是{}'.format(num,os.getpid()))

p1 = Process(target= mission,args=(1,))
p2 = Process(target= mission,args=(2,))
p3 = Process(target= mission,args=(3,))
p4 = Process(target= mission,args=(4,))

p1.start()  #p.start()只是给操作系统传递信号，说需要执行子进程，而具体子进程与父进程的执行顺序，由操作系统决定。
p2.start()  #可能信号一发出去，操作系统就响应且执行了，那么子进程就先于操作系统执行完，
p3.start()  #也可能信号发出过了一些时间才给执行，那么子进程就后于主进程执行。
p4.start()

print('in the main process...')

'''

多运行几次，你会发现，子进程执行顺序不定，而且子进程可能在主进程前面执行。。。
进程执行顺序由操作系统决定，主进程指示向操作系统发送信号，什么时候执行要看操作系统的统筹。。。

'''