#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''什么是自省（反射，映射）？
吾日三省吾身，日常生活中 自省 的意思为自我反省。
在面向对象的语言中，自省意为
    检测某些事物以确定它是什么（它的类型），它知道什么（它的属性）以及它能做什么（它的方法）。
    也可以理解为；在我们不确定程序中的某些事物的信息时，通过某些手段让程序自省高数我们想获知的信息。

自省在python中主要体现为4个函数：
1.dir
2.type
3,isinstance
4.hasattr,setattr,getattr,delattr   (专门用于判断 类或实例 中是否存在相关属性与方法)


参考：   https://www.cnblogs.com/ArsenalfanInECNU/p/9110262.html
'''

class Dog:
    race = 'dog'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def walk(self):
        print('this dog is walking...')

    def eat(self):
        print('this dog is eating...')

def talk1(self):
    print('{} is talking...'.format(self.name))

def talk2(self):
    print('{} is talking again...'.format(self.name))


xiaohei = Dog('xiaohei',3)

#1.hasattr(obj or exp，property or func)
print(hasattr(xiaohei,'name2'))
print(hasattr(xiaohei,'walk'))      #判断类或实例中是否含有某属性或方法

#2.getattr():获取类或实例的属性与方法（门牌号）的值
# print(getattr(Dog,'name'))
print(getattr(Dog,'race'))      #__init__内定义的是实例属性，而不是类属性，在Dog内get name属性会报错
print(getattr(Dog,'eat'))
eat2 = getattr(Dog,'eat')       #通过getattr获得的值可以进行赋值
eat2(xiaohei)


#3.setattr（）：为类或实例 绑定新的属性或方法
setattr(xiaohei,'sex','male')       #绑定新的静态属性
print(xiaohei.sex)

setattr(xiaohei,'speak',talk1)      #绑定新的方法，绑定的新方法要原本就存在。
xiaohei.speak(xiaohei)              #将新方法绑定在实例上，调用时要自行传入实例当做参数传入

setattr(Dog,'speak2',talk2)         #将新方法绑定在类上，在调用时不用传入实例参数，其会将调用该方法的实例本身传入，
xiaohei.speak2()                    #等同于原生方法

#4.delattr（）：删除实例或类的属性或方法,其效果相当于del obj.pro(func)

delattr(xiaohei,'name')     #属性可删除
print(xiaohei.name)

delattr(xiaohei,'walk')     #方法也可删除
xiaohei.walk()

