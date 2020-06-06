#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

#方法一：在外部定义一个函数，作为子进程（这里指的是sub_func）

import multiprocessing
# from multiprocessing import  process

def sub_func(apple,pear = 'pear'):
    print('%s and %s in the subprocess...'%(apple,pear))

p1 = multiprocessing.Process(target = sub_func,args=('simon',),kwargs={'pear':'pear1'})
'''
multiprocessing的的Process类用来为主进程创建子进程，常用参数有：
target：指派子进程执行的任务       子进程的参数由args和kwargs指定
args：指定子任务的位置参数，注意括号里至少需要一个逗号（其实就是args只能传递元祖）
kwargs：用来指定关键字参数（kwargs传递字典）

注：当子进程很多时，各子进程的执行顺序是不一定的。

'''


p1.start()      #给操作系统传递信号，说需要执行子进程，而具体子进程与父进程的执行顺序，由操作系统决定。
                #可能信号一发出去，操作系统就响应且执行了，那么子进程就先于操作系统执行完，
                #也可能信号发出过了一些时间才给执行，那么子进程就后于主进程执行。
print('in the main process...')




