#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
死锁：两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，若无外力作用，
它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程，如下就是死锁
'''
# from threading import Thread,Lock
# import time
# mutexA=Lock()
# mutexB=Lock()
# class MyThread(Thread):
#     def run(self):
#         self.func1()
#         self.func2()
#
#     def func1(self):
#         '''
#         这个函数不是没有作用，是为了在前一个线程拿着B锁在睡的时候，
#         别的线程要去抢A锁，进而造成混乱卡住。
#
#         '''
#         mutexA.acquire()
#         print('\033[41m%s 拿到A锁\033[0m' %self.name)
#         mutexB.acquire()
#         print('\033[42m%s 拿到B锁\033[0m' %self.name)
#         mutexB.release()
#         mutexA.release()
#
#     def func2(self):
#         mutexB.acquire()
#         print('\033[43m%s 拿到B锁\033[0m' %self.name)
#         time.sleep(2)
#         '''
#         当线程1拿着互斥锁B睡两秒的时候，线程2拿到了互斥锁A，
#         但是线程1睡完后要去取互斥锁A，却发现被线程1拿着，
#         线程2想拿到互斥锁B，却被线程1拿着，
#         这就尬住了
#
#         '''
#         mutexA.acquire()
#         print('\033[44m%s 拿到A锁\033[0m' %self.name)
#         mutexA.release()
#         mutexB.release()
#
# if __name__ == '__main__':
#     for i in range(10):
#         t=MyThread()
#         t.start()


'''
这个RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，
从而使得资源可以被多次require。直到一个线程所有的acquire都被release，
其他的线程才能获得资源。上面的例子如果使用RLock代替Lock，则不会发生死锁，
二者的区别是：递归锁可以连续acquire多次，而互斥锁只能acquire一次

'''
from threading import Thread,RLock
import time
mutexA=mutexB=RLock() #一个线程拿到锁，counter加1,该线程内又碰到加锁的情况，则counter继续加1，这期间所有其他线程都只能等待，等待该线程释放所有锁，即counter递减到0为止
#这里其实也没有所谓的A锁B锁，只有一把锁？
class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()

    def func1(self):
        mutexA.acquire()
        print('\033[41m%s 拿到A锁\033[0m' %self.name)
        mutexB.acquire()
        print('\033[42m%s 拿到B锁\033[0m' %self.name)
        mutexB.release()
        mutexA.release()

    def func2(self):
        mutexB.acquire()
        print('\033[43m%s 拿到B锁\033[0m' %self.name)
        time.sleep(2)
        mutexA.acquire()
        print('\033[44m%s 拿到A锁\033[0m' %self.name)
        mutexA.release()
        mutexB.release()

if __name__ == '__main__':
    for i in range(10):
        t=MyThread()
        t.start()





