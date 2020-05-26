#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

class Dog:

    def __init__(self,name):
        self.name = name

    def run(self):          #一般情况下自动补全，括号里是self
        print(self)
        print(self.name)

    @classmethod
    def eat(cls):          #加了@classmethod后，自动补全变成了cls
        print(cls)
        # print(cls.name)

lala = Dog('lala')
lala.run()          #这里输出的self是Dog类的实例，并且可以访问实例变量name
lala.eat()          #这里输出的cls是Dog这个类，不能访问实例变量name，不然会报错

print('dir 不带参数'.center(50,'*'))
print(dir())
'''
dir() 函数不带参数时，以列表的形式返回当前范围内的变量、方法和定义的类型（比如说类对象）
    1.如果当前范围中定义了类，dir函数会返回 类对象，但不会返回类中的变量，方法
'''

print('dir 带参数'.center(50,'*'))
print(dir(lala))
'''
dir() 函数带参数时，返回参数的属性（dog.name）、方法(dog.run,dog.eat)列表
'''

