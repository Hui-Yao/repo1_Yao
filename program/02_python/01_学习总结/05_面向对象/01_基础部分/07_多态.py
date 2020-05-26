#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
什么是多态？
    不同种表现形式，同一种调用方式（函数式、抽象类调用）。


'''

# class Animal:
#     def run(self):
#         print('animal is running...')


class Man(Animal):
    def run(self):
        print('a man is running...')

class dog(Animal):
    def run(self):
        print('a dog is running...')





