#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

import json,time
from multiprocessing import Process,Lock

# num_of_ticket = json.load(open('ticket.txt','r',encoding='utf-8'))
#   把票数统计放到外面的话，就只有第一次是从文件种读数据，后面的次数都不是，所有查票数的操作要放到函数中去，每次都得从文件中获取数据

def num_of_ticket():
    return json.load(open('ticket.txt'))


def search(name):
    num = num_of_ticket()
    time.sleep(0.5)
    print('%s正在查票，票数剩余%s张。'%(name,num['count']))


def get(name,lock):
    # lock.acquire()
    num = num_of_ticket()
    time.sleep(0.5)

    if num['count']>0:
        print('%s正在购票...'%name)
        num["count"]-=1
        time.sleep(0.5)
        json.dump(num,open('ticket.txt','w'))
        print('%s购票成功，剩余票数为%s张'%(name,num["count"]))   #这个写法就不报错
        # lock.release()
    else:
        print('票数不足，%s购票失败。'%name)
        # lock.release()
        #如果有lock.release(),则判断语句的每个子语句相应的地方都得加上lock.release。否则后面的子进程不会执行。


def task(name,mute):
    search(name)
    with lock:         #相当于在with的子语句开头执行lock.acquire()，当所有子语句执行完以后执行lock.release()
        get(name,mute)

lock = Lock()


for i in range(1,6):
    name = '乘客<%s>'%i
    p = Process(target=task,args=('乘客[%s]'%i,lock))
    p.start()


