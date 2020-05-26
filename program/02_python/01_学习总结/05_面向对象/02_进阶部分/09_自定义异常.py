#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
自定义异常：在某些情况下，程序出现的异常并不包含于python的内建异常，此时则需要自行构建异常。
比如你写了一个软件，当这个软件与QQ连接不上时会出现错误，此时就要你自己构建一个异常QQConnectionError。

但我现在还不是很理解。。。
'''

#自定义异常的格式
class MyException(BaseException): # BaseException是所有异常的基类
    def __init__(self,msg):
        self.message = msg
    def __str__(self):
        return self.message
try:
    raise MyException("我的错误")
except MyException as e:
    print(e)



