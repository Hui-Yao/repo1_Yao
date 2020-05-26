#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''全局变量与局部变量
定义：1.全局变量：在程序顶层定义的变量称为全局变量，其作用域为函数的任何位置
     2.局部变量：在子程序（函数）中定义的变量成为局部变量，其作用域为该子程序及其内部程序，不能在更高一层的区域使用

特性：1.全局变量可以在程序的任何位置调用，但当局部变量与全局变量重名时，局部变量会覆盖全局变量
     2.局部变量是相对的，a函数内嵌b函数，b函数内嵌c函数，若三个函数中皆有同名变量，则b会覆盖a的，c会覆盖a、b的
     3.

'''

apple_color = 'red'

def apple(apple):
    apple_color = 'cyan'
    print(apple_color)

apple(apple_color)      #对于字符串，数值，元组等不可变数据，局部变量是不能修改全部变量的
print(apple_color)


fruit = ['apple','orange','pear']

def change_fruit(fruit):
    fruit[2] = 'pineapple'
    print(fruit)

change_fruit(fruit)     #对于列表，字典，集合等可变对象，局部变量可以修改全局变量
print(fruit)


fruit2 = {'apple','orange','pear'}

def change_fruit2(fruit2):
    fruit2.add('pineapple')
    print(fruit2)

change_fruit2(fruit2)
print(fruit2)

