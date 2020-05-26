#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''mro（method resolution order）：方法解析顺序
   子类：subclass
   父类：baseclass，superclass
1.在Python2.3之前，采用的都是经典类，搜索顺序采的是深度优先；
  但是由于深度优在某些特殊情况下会出一些bug，所以在Python2.3之后，采用的都是C3算法，
  在多数情况下都可以将C3视为深度优先，确保安全的话可以使用.mro()方法进行确认
2.Python3中默认都是新式类，写不写object都可，但建议还是按官方推荐写上
3.

'''

class A:
    pass
    # def lala(self):
    #     print('it`s A')

class B1:
    pass
    # def lala(self):
    #     print('it`s B1')

class C1:
    def lala(self):
        print('it`s C1')

class B(A,B1):
    pass
    # def lala(self):
    #     print('it`s B')

class C(A,C1):
    pass
    # def lala(self):
    #     print('it`s C')

class D(B):
    pass
    # def lala(self):
    #     print('it`s D')

class E(C):
    pass
    # def lala(self):
    #     print('it`s E')

class F(D,E):
    pass
    # def lala(self):
    #     print('it`s F')

haha = F()
haha.lala()
print(F.mro())      #使用  类名.mro()  可查询该类的继承顺序
