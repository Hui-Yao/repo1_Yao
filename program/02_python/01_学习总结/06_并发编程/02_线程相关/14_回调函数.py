#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''同步调用与异步调用：
同步调用：提交完任务以后，程序需要在原地等待任务执行完毕，才会去执行接下来的代码
异步调用：提交完任务以后，不去管任务的执行情况，直接取执行接下来的代码

同步调用与IO阻塞有关系么？
    IO阻塞指的是程序执行时要从硬盘上读取数据，进而整个程序停留在了等待独处数据的位置。在这个停留的时间，
    程序一直卡调用位置，并没有往下执行（cpu也转而取执行其他进程了），所以叫阻塞。

    同步调用如果执行的是很大规模的纯运算的任务，程序也会在调用的位置停留，但是在停留的时间内，cpu一直在计算，
    只不过运算量大了些，活了些时间。

'''

from concurrent.futures import ProcessPoolExecutor
import requests
import os

def get_page(url):
    print('<进程%s> get %s' %(os.getpid(),url))
    respone=requests.get(url)
    if respone.status_code == 200:
        return {'url':url,'text':respone.text}

def parse_page(res):
    res=res.result()
    print('<进程%s> parse %s' %(os.getpid(),res['url']))
    parse_res='url:<%s> size:[%s]\n' %(res['url'],len(res['text']))
    with open('db.txt','a') as f:
        f.write(parse_res)

urls=[
    'https://www.baidu.com',
    'https://www.python.org',
    'https://www.openstack.org',
    'https://help.github.com/',
    'http://www.sina.com.cn/'
]

p=ProcessPoolExecutor(3)
for url in urls:
    p.submit(get_page,url).add_done_callback(parse_page)
    #parse_page拿到的是一个future对象obj，需要用obj.result()拿到结果

'''
线/进程池中其他两个方法：
    pool.submit(func1).result()     
    在提交任务到线程池中之后，等待任务执行完成并获取执行结果。
    这是同步调用。
    
    pool.submt(func1).add_done_callback(func2)
    提交到到进程池中的任务执行完以后自动执行func2。这是异步调用，程序无序等待函数的
'''















