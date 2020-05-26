#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

from types import MethodType

class Dog:
    pass

def run(self):
    print('running...')

d = Dog()
d1 = Dog()

d.run = MethodType(run,d)
d.run()

# d1.run()      #给实例绑定，对其他实例不会生效

Dog.run = MethodType(run,Dog)

d1.run()        #对类绑定。则对所有实例都绑定

'''
如果给实例绑定的方法与原本类中的方法同名，则由新的覆盖原本类中的，小的会覆盖大的
'''




