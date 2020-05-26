#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
__new__ 方法：在构造函数执行前执行，其作用是执行一些在实例化前要做的工作(具体作用比如实现 单例模式 )。

注意：自行修改new方法的话，最后要调用并返回构造函数，不然就不会进行实例属性的初始化



'''

class Printer:
    task = []
    instance = None

    def __init__(self,number):
        self.number = number

    def add_task(self):
        self.task.append(self.number)

    def __new__(cls, *args, **kwargs):
        # print(Printer)    #   输出能容相同，可知此cls即为该类
        # print(cls)
        if cls.instance == None:
            cls.instance = object.__new__(cls)  #如果没有进行过实例，则进行实例化
                                                #如果进行过实例化，则不再进行实例化，而直接返回
        return cls.instance





word = Printer(1)
browser = Printer(2)
cad = Printer(3)



