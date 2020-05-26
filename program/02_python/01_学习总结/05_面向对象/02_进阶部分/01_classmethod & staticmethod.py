#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
装饰器：@classmethod(类方法)
效果：用以装饰类方法，使之不能访问实例变量。

'''

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


'''
装饰器：@staticmethod（静态方法）
效果：修饰类方法后，类方法不能再访问类的所有其他属性与方法。
     被类方法仍然挂靠在该类下，但是断绝了该类方法与该类的所有联系。
     
'''

class Bird:

    def __init__(self,name):
        self.name = name

    def fly(self):      #不加静态方法，按括号，会自动补全self
        print('{} is flying...'.format(self.name))

    @staticmethod
    def fly2():         #加了装饰器，自动补全的括号里啥都没有
        print('{} flys again...')

    @staticmethod
    def fly3(self):     #自行给他加上self
        print('{} flys triple...'.format(self.name))

maque = Bird('dada')

maque.fly()
maque.fly2()
maque.fly3(maque)    #需要自己传入maque这个参数

'''
加上了@staticmethod装饰器的方法 与 定义在顶层的函数的区别就是：
前者需要通过类来调用，后者不需要通过类来调用


'''

