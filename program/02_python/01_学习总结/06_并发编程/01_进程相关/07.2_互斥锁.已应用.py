#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

from multiprocessing import Process,Lock
import time

def mission(name,lock):  #要把锁传入要应用的子程序
    lock.acquire()        #上锁
    print('%s 1'%name)
    time.sleep(1)
    print('%s 2'%name)
    time.sleep(1)
    print('%s 3'%name)
    lock.release()        #解锁

lock = Lock()  # 造一把锁，锁名不一定需要是lock，开心就好。造锁要在需要锁的子进程之前。
for i in range(3):
  # lock = Lock()   #只能造一把锁，造多把锁是无效的，会报错：AssertionError: can only join a child process
    p = Process(target=mission,args=('进程%s'%i,lock))
    p.start()



