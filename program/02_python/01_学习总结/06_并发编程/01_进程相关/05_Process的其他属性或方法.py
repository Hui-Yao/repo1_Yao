#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

from multiprocessing import Process

def mission():
    print('in the subprocess...')

p1 = Process(target=mission())
p1.start()
print(p1.pid)               #1.p.pid:通过pid属性直接查看
print('1:',p1.is_alive())        #2.p.is_alive():判断子进程是否执行完成，执行完返回False，未执行完返回True
p1.terminate()              #3.p.terminate():给操作系统发信号让杀死子进程，注意，只是发信号
print('2:',p1.is_alive())
p1.join()
print('3:',p1.is_alive())

'''程序在第二个is_alive之前给操作系统发了terminate信号，为什么第二个依然返回True？
      注意，p.terminate()只是给操作系统发了信号，但是操作系统并不一定立马响应，所以仍然返回True，
      但是在p1.join()后，操作系统一定开始执行子程序，也就一定会杀死该子程序，所以第三个一定返回False

'''



