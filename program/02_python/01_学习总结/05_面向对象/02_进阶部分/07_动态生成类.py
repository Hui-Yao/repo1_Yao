#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
首先明确：type函数是python底层创建类的元类：type实例化成为类，类进一步实例化成为实例


使用type函数动态生成类： type(‘类名’，（父类，），各种函数)



'''
import types

print(dir(types))

class Dog():
    role = 'dog'
    def __init__(self,name):
        self.name = name

    def run(self):
        print('running...')

def eat():
    print('eating...')

haku = Dog('haku')

#以下验证了type是python内建元类
print(type(haku))   #实例Haku的类型是Dog
print(type(Dog))    #类Dog的类型type，所以验证了所有类都是由type创建的

print(haku.__class__)               #对象的__class__属性返回该对象的类型
print(haku.__class__.__class__)     #同上，验证了type是元类

print(int.__class__.__class__)

print(isinstance(eat,types.FunctionType))
print(isinstance(haku.run,types.MethodType))
print(type(Dog.run),type(haku.run))  #类的‘方法’的类型是Function，实例的方法的类型是Method

'''
types模块中Method方法用于给类（实例）绑定新方法

当type（）有三个参数时，其作用就是创建类对象：
  第一个参数：name表示类名称，字符串类型
  第二个参数：bases表示继承对象（父类），元组类型，单元素使用逗号
  第三个参数：attr表示属性，这里可以填写类属性、类方式、静态方法，采用字典格式，key为属性名，value为属性值

'''


def __init__(self,name,age):
    self.name = name
    self.age = age

def run(self):
    print('running...')

Dog = type('Dog',(object,),{'role':'dog','__init__':__init__,'run':run})

d = Dog('erha','4')
print(d.name)
d.run()


