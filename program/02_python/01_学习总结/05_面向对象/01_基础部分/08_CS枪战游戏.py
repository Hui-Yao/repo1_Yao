#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

class Solider:
    '''定义人这个类'''
    def __init__(self,name,sex,life_val):
        self.name = name
        self.sex = sex
        self.life_val = life_val
        self.weapon = Gun()        #组合关系

    def determine_life_val(self):
        print(self.life_val)
        return self.life_val


class Gun:
    def m4a1(self,obj1,obj2):
        attack_val = 60
        obj2.life_val -= attack_val
        print('{0} shoot {1},{1} left {2} HP...'.format(obj1.name,obj2.name,obj2.life_val))

    # def ak47(self):
    #     attack_val = 80


class Lurker(Solider):
    '''定义潜伏者'''
    def __init__(self,name,sex,life_val,role):
        super(Lurker, self).__init__(name,sex,life_val)
        self.role = 'lurker'


class Defender(Solider):
    '''定义保卫者'''
    def __init__(self,name,sex,life_val,role):
        super(Defender, self).__init__(name,sex,life_val)
        self.role = 'defender'


l1 = Lurker('black','m',100,'lurker')
# l1.determine_life_val()
d1 = Defender('white','m',100,'defender')
l1.weapon.m4a1(l1,d1)


