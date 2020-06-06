#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
在上一个Queue版本中，需要添加结束信号才能保证程序结束，有点low。


JoinableQueue也是用于创建队列，它与Queue的区别就是多了两个方法：.join()  .task_done()
.task_done():向.join()发送信号，表明从队列中取得的这个数据已经处理完毕。应该每取一个数据发一个taskdone。
.join():当队列中的所有数据均返回了taskdone信号，也就是队列中所有数据均被处理，队列空了的时候，结束堵塞。
否则一直堵塞队列，使该子进程与队列一直保持运行状态。

保证了队列信息的互通，那么如何保证consumer进程（中的while循环）的结束呢？
    将consumer设置成主程序的守护进程。
    在主程序执行完之前，通过p.join（）保证producer进程的执行；通过 queue.join() 保证队列中所有数据均被处理；
    producer子进程执行完以后，主进程也执行完了，那么作为守护进程的consumer进程也会被杀死。
'''

from multiprocessing import Process,JoinableQueue
import time

def producer(q,name,food):
    for i in range(1,6):
        time.sleep(0.5)
        product = '%s<%s>'%(food,i)
        q.put(product)
        print('producer<%s> maked %s<%s>'%(name,food,i))
    q.join()
'''
在生产者程序中加入queue.join()，生产食物（数据）的部分会很快执行，
然后整个子进程便等待着消费者发来信号，保证队列种所有数据均被处理，然后生产者程序也执行完了。
'''

def consumer(q,name):
    while True:
        food = q.get()
        time.sleep(0.5)
        print('---consumer<%s> eated %s'%(name,food))
        q.task_done()
'''
每从队列种取出并处理完一个数据，就发送一个task-done信号，最后保证所有数据均被处理完。

'''

q = JoinableQueue()

p1 = Process(target=producer,args=(q,'alex','bread'))
p2 = Process(target=producer,args=(q,'simon','bun'))
p3 = Process(target=producer,args=(q,'jack','noddle'))

c1 = Process(target=consumer,args=(q,'lily'))
c2 = Process(target=consumer,args=(q,'mary'))


p1.start()
p2.start()
p3.start()

c1.daemon = True
c2.daemon = True
c1.start()
c2.start()

p1.join()       #先让生产者把食物放进去，再放结束信号
p1.join()
p1.join()

print('the main process is finished...')


