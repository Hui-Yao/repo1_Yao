#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"


'''面向对象 双下划线方法产生作用的原理：
在python里，万物皆对象，不同的类中有不同的方法。
1.列表是一个类，对列表执行len方法，会调用列表这个类中所定义的len方法。
2.对于我们新创建的类，我们可以选择执行默认的len方法，也可以对len方法进行重新定义。

'''

class Person:

    def __init__(self,name):
        self.name = name

    def __len__(self):
        print('change the func len...')
        return len(self.name)
    def __hash__(self):     #与修改len方法的原理，形式完全相同
        pass

    def __eq__(self, other):    
        # print(self.name,other.name)
        print('judge ...')

    def __del__(self):
        print('析构方法执行啦...')
    '''
    构造方法（函数）：在对象初始化时执行，其作用是进行一些初始化操作，如进行定义变量
    
    析构方法:与构造方法相反，在对象消散时执行，其作用是进行一些善后工作，如清空占用的内存空间等
    
    '''


simon = Person('simon')
benjamin = Person('benjamin')
apple = 'apple'

print(len(simon))
#在person类中已修改len方法，对所生成的实例调用len方法，会触发我们所定义的len方法，而不是默认的

print(simon == apple)    #当一个实例出现在 == 的一边时，会触发__eq__方法。

print('apple')
del simon           #当simon这个对象消散时，析构方法执行了。。。

print('peach')

#当程序结束时，空间释放，对象也消散了，所以构造函数也执行了。。。
