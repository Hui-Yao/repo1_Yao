#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

#问题：建立合理的生产者消费者模型，不是说生产者生产一个，消费者消费一个，这会造成生产与消费之间的相互限制（生产了才有的吃，吃完了才能再生产）
#目标：建立一个容器，使生产者只顾生产，消费者只顾消费，解决生产与消费间的这种限制

from multiprocessing import Process,Queue
import time

def producer(q,name,food):
    for i in range(1,6):
        time.sleep(0.5)
        product = '%s<%s>'%(food,i)
        q.put(product)
        print('producer<%s> maked %s<%s>'%(name,food,i))


def consumer(q,name):
    while True:
        food = q.get()
        if food == None:
            break
        time.sleep(0.5)
        print('---consumer<%s> eated %s'%(name,food))


q = Queue()

p1 = Process(target=producer,args=(q,'alex','bread'))
p2 = Process(target=producer,args=(q,'simon','bun'))
p3 = Process(target=producer,args=(q,'jack','noddle'))

c1 = Process(target=consumer,args=(q,'lily'))
c2 = Process(target=consumer,args=(q,'mary'))


p1.start()
p2.start()
p3.start()
c1.start()
c2.start()

p1.join()       #先让生产者把食物放进去，再放结束信号
p2.join()
p3.join()

q.put(None)     #不能在生产者放食物前放结束信号，不然序列中第一个元素就是结束信号,生产者放不了食物，消费者也吃不到食物了
q.put(None)     #



print('the main process is finished...')


