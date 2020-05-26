#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
1.私有属性（方法）：在属性或方法的前面加上两个下划线，即变成了私有的了。
  私有属性（方法）实际上并不是真正的私有，而是在类内部进行了变形，所以在外部同样可以访问私有属性（方法）
2.什么是封装？
  限制某些关键属性、方法的调用权限，使之只能在类内部进行操作，不能在外部进行调用，增加了代码的安全性
'''

class Human:
    role = 'Human'      #类属性，公有属性

    def __init__(self,name,life_val):
        self.name = name    #实例属性
        self.__life_val = life_val      #私有属性
        '''注意这三个属性的叫法'''

    def __got_attack(self):
        print('{}`s life_val left {}'.format(self.name,self.__life_val-20))
        print('在外部调用私有方法')

    def got_attack(self):
        self.__got_attack()

jack = Human('jack',100)
print(jack.name)
# print(jack.__life_val)        #按常规方法在外部不能访问类的私有变量

# jack.__got_attack()         #在外部也不能直接访问类的私有方法

jack.got_attack()       #类中定义的方法可以调用私有方法

print(jack._Human__life_val)
jack._Human__got_attack()
'''
知道了类名与属性名（方法名），在外部也可以调用私有属性（方法）
调用方法：   实例名._类名__属性名（方法名）
'''



