#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

#作用：暂停指定秒数，再执行某函数

from threading import Timer,Thread

def hi(name):
    print('hello {}!'.format(name))

ttt = Timer(5,hi,args=('jack',))
ttt.start()



