#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''

'''
class Animal:
    '定义一个父类'
    type = 'mamal'      #类属性
    def __init__(self,name,sex):
        self.name = name
        self.sex = sex

    def eat(self):
        print('{} is eating...'.format(self.name))

class Dog(Animal):      #狗这个类中不修改
    pass

d1 = Dog('mjj','m')
print('the dog`s name is %s'%d1.name)
d1.eat()



class Huaman(Animal):       #人这个类中各种修改
    type = 'superb mamal'   #修改父类属性
    def __init__(self,name,sex,age):    #修改父类构造方法，加上一个age属性
        # Animal.__init__(self,name,sex)
        # super(Huaman, self).__init__(name,sex)
        super().__init__(name,sex)
        '''修改父类构造函数的方法有三种，或者说有两种
            1.直接指定确定的父类名进行修改
            2.使用super方法
            '''
        self.age = age

    def eat(self):
        super(Huaman, self).eat()
        print('吃瓜～～～')     #修改父类方法，为其加上一个输出语句



p1 = Huaman('jack','m',23)
p1.eat()

