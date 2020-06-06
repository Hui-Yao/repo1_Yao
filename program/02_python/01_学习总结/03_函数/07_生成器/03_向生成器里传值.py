#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

def printer():
    "实验向生成器里传数据"
    while 2:            #这里不用循环的话，yield执行完后不会再往上走
        n = yield      #yield后面不要接东西，不然就不能传值了
        print('生成器中传入的数值：',n)


p = printer()
p.__next__()    #在生成器中将语句执行到yield处

for i in 'apple':
    p.send(i)     #传值要使用send方法
