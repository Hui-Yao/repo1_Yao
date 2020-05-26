#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

import json,time
from multiprocessing import Process

# num_of_ticket = json.load(open('ticket.txt','r',encoding='utf-8'))
#   把票数统计放到外面的话，就只有第一次是从文件种读数据，后面的次数都不是，所有查票数的操作要放到函数中去，每次都得从文件中获取数据

def num_of_ticket():
    # print(type(json.load(open('ticket.txt'))['count']))   #是 int 类型
    # print(json.load(open('ticket.txt')))      #是字典
    return json.load(open('ticket.txt'))


def search(name):
    num = num_of_ticket()
    time.sleep(0.5)
    print('%s正在查票，票数剩余%s张。'%(name,num['count']))


def get(name):
    num = num_of_ticket()
    time.sleep(0.5)

    if num['count']>0:
        print('%s正在购票...'%name)
        num["count"]-=1
        time.sleep(0.5)
        json.dump(num,open('ticket.txt','w'))
        print('%s购票成功，剩余票数为%s张'%(name,num["count"]))   #这个写法就不报错
        # print('%s购票成功，剩余票数为%s张'%(name,num_of_ticket()["count"]))
        #这个写法时而报错，时而不报错，dont know why

    else:
        print('票数不足，购票失败。')


def task(name):
    search(name)
    get(name)

for i in range(1,6):
    name = '乘客<%s>'%i
    p = Process(target=task,args=('乘客[%s]'%i,))
    p.start()
    p.join()    #
'''
使用join（）方法后，整个子程序所执行的全都代码都是串行执行，连查票也是串行执行，但这并不是我们想要的，
我们希望的是查票并行（很多人可以同时查票），买票串行（同一时间只能有一个人在买票），保证数据安全。


'''



