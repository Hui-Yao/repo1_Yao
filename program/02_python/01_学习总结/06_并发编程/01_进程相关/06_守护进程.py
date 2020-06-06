#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''守护进程：
可通过设置p.deamon = True,将子进程设置成守护进程，守护进程有以下特性：
    1. 当主进程执行完成后，守护进程也会死亡
    2. 守护进程不能创建子进程。
守护进程只可能在主进程的前面执行，不可能在后面执行。

'''

from multiprocessing import Process
import time

def mission(name,n):
    print('in the subprocess [{}]'.format(name))
    time.sleep(n)

p1 = Process(target=mission,args=(1,1))
p2 = Process(target=mission,args=(2,2))

p1.daemon = True
p1.start()
p2.start()

print('in the main process')

'''
可以看到，子进程2执行了，但子进程1没执行。
原因代码向系统发了执行子进程1的信号后，还没来得及执行，主进程已经执行完了，没执行的子进程1就被杀死了。
（有一种可能性是子进程2一发送信号就被执行了。）
而子进程2不管主进程是否执行完，都会被执行。


'''




