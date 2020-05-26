#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
@property：将类中方法的调用方式修改为属性的调用方式（即不用加括号）



'''

#目标：通过装饰器@property将类方法的调用方式修改，使顾客能通过调用类属性的方式查询到航班的状态

class Flight:
    '''航班类'''
    def __init__(self,name):
        self.name = name

    def check_status(self):
        '''检查航班状态'''
        print('connecting to the airport api...')
        print('checking the flight status...')
        print('return the status of this flight...')
        return 1

    @property
    def flight_status(self):
        flight_condition = self.check_status()

        if flight_condition == 0:
            print('this flight is canceled...')
        elif flight_condition == 1:
            print('this flight is ready to fly...')
        elif flight_condition == 2:
            print('this flight fliying in the sky...')
        else:
            print('the business is busy,please check later...')

    @flight_status.setter
    def flight_status(self,new_status):     #修改属性方法
        flight_condition = {0:'canceled',1:'ready',2:'flying'}
        print('this flight status has changed to be {}...'.format(flight_condition.get(new_status)))

    @flight_status.deleter
    def flight_status(self):
       print('status removed...')


f = Flight('by747')

f.flight_status     #给类方法加上@property后，调用时不需要加括号，按属性方法进行调用即可

f.flight_status = 0     #
'''
要对加了@property的类方法赋值，则要重新写一个同名类方法，将函数修改成相应内容，
并在类方法前面加上@property.setter

'''
del f.flight_status     #形式上的删除，但实际上还是没有删除，仍然可以调用第一个flight_status方法

f.flight_status




