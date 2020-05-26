#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"



from multiprocessing import Process
import os,time

def mission(order,n):
    print('in the subprocess [{}],it`s pid is {}'.format(order,os.getpid()))
    time.sleep(n)

p1 = Process(target=mission,args=(1,3))
p2 = Process(target=mission,args=(2,2))
p3 = Process(target=mission,args=(3,1))

p1.start()
p2.start()
p3.start()

start_time = time.time()
p1.join()
p2.join()
p3.join()
end_time = time.time()
'''
p.join()方法，保证当前子程序在此处执行完，再执行主程序。  join()中可以选填timeout参数，限制子程序最长执行时间。

join（）方法并不会使程序串行执行，依然是并发执行。
从执行结果显示的时间也可推断出：
当子程序1在睡的时候，cpu转去执行了子程序2，再又转去执行了子程序3
所以总的执行时间为最长的时间3，而不是总时间3+2+1 = 6

'''
#怎样就一定是串行执行呢？子程序start后立马join
# p1.start()
# p1.join()
# p2.start()
# p2.join()

print('end of the main process...')
print('the whole code has ran for %s seconds.'%(end_time-start_time))



