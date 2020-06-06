#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

from threading import Thread
from threading import current_thread
#与线程中的current_process类似，current_thread用于表示当前运行的线程
from threading import active_count
#用以统计当前位置存活（正在执行）的线程
from threading import enumerate
#以列表的形式返回当前存活的线程

def f():
    print('线程的名字：',current_thread().getName())

t1 = Thread(target=f,name='儿砸线程')   #可以在创建子线程时指定名字
t1.start()
t1.setName('二儿砸线程')     #可以用t.setName('str')方法重新指定线程名

print('主线程中输出线程的名字：',t1.getName())

print(current_thread().getName())   #最顶层抓取到的线程是主线程，也即控制线程

print(active_count())
print(enumerate())






