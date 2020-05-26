#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

#方法二：通过创建子类，其中定义函数，来创建子进程。

from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,name):
        super(MyProcess, self).__init__()
        self.name = name

    def run(self):
        print('%s is in the subprocess...'%self.name)

p1 = MyProcess('eagle')     #由子类创建的实例，就当做是子进程。
p1.start()

print('in the main process...')





