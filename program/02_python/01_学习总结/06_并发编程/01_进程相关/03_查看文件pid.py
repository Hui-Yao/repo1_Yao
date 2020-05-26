#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"


'''
os.getpid()的返回值为当前进程的pid
os.getppid()的返回值为父进程的pid

注：主程序在pycharm运行，则其父进程为pycharm
    主进程在终端运行，则其父进程为终端

'''

from multiprocessing import Process as Pro
import os

class MyProcess(Pro):

    def run(self):
        print('the pid of subprocess is %s'%os.getpid())
        print('the pid of parent process is %s'%os.getppid())

subp = MyProcess()

subp.start()

print('the pid of main process is %s'%os.getpid())
print('the interprter of this code is %s'%os.getppid())

print('11111',subp.pid)     #也可以直接调用子进程下的pid属性查看文件pid

