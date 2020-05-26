#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

class Person:
    '''创建人这个对象'''
    role = 'human'

    def __init__(self,name,attack_value,life_value = 100):
        self.name = name
        self.life_value = life_value
        self.attack_value = attack_value

    def beat(self,dog):
        print('{0}打了{1}一棒，{1}还剩{2}血'.format(self.name,dog.name,dog.life_value-self.attack_value))

class Dog:
    '''创建狗这个对象'''
    role = 'dog'

    def __init__(self,name,attack_value,life_value = 100):
        self.name = name
        self.life_value = life_value
        self.attack_value = attack_value

    def bite(self,person):
        print('{0}咬了{1}一口，{1}还剩{2}血'.format(self.name,person.name,person.life_value-self.attack_value))

p1 = Person('jack',50)
d1 = Dog('husky',40)

p1.beat(d1)

d1.bite(p1)

