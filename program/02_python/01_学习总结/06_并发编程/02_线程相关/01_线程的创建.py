#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
1. 每个进程至少包含一个控制线程（主线程）
2. 进程是一个资源单位，为开启一个进程，变要向系统申请一些内存一类的资源
   进程间的资源隔离
   线程是执行单位，同一个进程内的线程共享资源，
3. 开启新进程所消耗的资源远大于开启一个新线程的资源

4. 可以创建自己的线程类，与创建自己的进程类类似


'''


from threading import Thread    #Thread一看就是一个类

def sayhi(name):
    print('hi,{}!'.format(name))

th = Thread(target=sayhi,args=(1000,))
th.start()

print('in the main thread!')

#运行原理与进程类似





