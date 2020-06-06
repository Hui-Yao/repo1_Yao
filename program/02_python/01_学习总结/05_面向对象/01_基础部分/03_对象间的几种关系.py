#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''类之间的几种关系：
1.依赖关系：类a中使用了类b中的变量（数据），则没有类b，类a就不完整，即类a对类b有依赖
2.关联关系：关联关系，通过定义第三方类来实现

'''

#2.关联关系
#目标：使男女自由恋爱，分手
class Boy:
    '''定义一个男孩类'''
    def __init__(self,name,relation,sex = 'm'):
        self.name = name
        self.sex = sex
        self.relation = relation


class Girl:
    '''定义一个女孩类'''
    def __init__(self, name,relation,sex='fm'):
        self.name = name
        self.sex = sex
        self.relation = relation

class Relationship:
    '''定义一个关系类'''
    def __init__(self):
          self.couple = []

    def make_couple(self,boy = None,girl = None):
        self.couple = [boy,girl]

    def get_partner(self,obj):
        for i in self.couple:
            if obj != i:
                print('%s的对象是%s'%(obj.name,i.name))
                break
        else:
            print('你个single dog！')

    def break_up(self):
        print('{}和{}分手了'.format(self.couple[0].name,self.couple[1].name))
        self.couple.clear()


relation = Relationship()

b1 = Boy('jack',relation)
g1 = Girl('lily',relation)

relation.make_couple(b1,g1)     #两人确立恋爱关系

b1.relation.get_partner(b1)     #男孩脱单了

g1.relation.break_up()      #女孩跟男孩分手了

b1.relation.get_partner(b1) #男孩发现自己是个单身狗了


#组合关系

class Dog:
    '''定义狗'''
    role = 'dog'
    def __init__(self,name,attack_val):
        self.name = name
        self.attack_val = attack_val
        self.life_val = 100

    def bite(self,obj):
        print('{0}咬了{1}一口，{1}还剩血量{2}。。。'.format(self.name,obj.name,obj.life_val-self.attack_val))

class Weapon:
    '定义武器'

    def ak47(self,obj):
        attack_val = 80
        obj.life_val -=attack_val
        self.print_log(obj)     #print_log()前面需要self，不然的话不知道是谁调用的这个函数，print_log函数有个参数为类
        '''如果函数是在某个类中定义的，那么他一定有个参数是self，相应的，在调用他时也需要通过某个类对象来调用'''

    def print_log(self, obj):
        print('{}被攻击了，还剩血量{}。。。'.format(obj.name, obj.life_val))


class Human:
    '定义人'
    role = 'human'

    def __init__(self,name):
        self.name = name
        self.life_val = 100
        self.weapon = Weapon()

d1 = Dog('jesse',60)
p1 = Human('jack')
d1.bite(p1)
p1.weapon.ak47(d1)
