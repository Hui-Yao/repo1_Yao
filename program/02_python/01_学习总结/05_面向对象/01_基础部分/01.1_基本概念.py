#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''面向过程与面向对象：
1.面向过程（procedual programing）：
定义：将一个大问题拆分成一个个小问题，然后将小问题逐一解决。
适用：简单的，单人完成的小脚本

2.面向对象(object-oriented programing,简称OOP):
定义：将实体进行抽象、归纳、总结，创建模板，使用模板来生成实体。
适用：复杂，大型的程序


'''

##不传私有变量版本
# class Dog:  #类的命名要用驼峰体，即首字母大写，不要用下划线，这是官方规范
#     dog_type = 'husky'      #属性，类属性，类变量  |  定义在顶层的是公有属性
#
#     def dog_bite(self):     #方法
#         print('{} attack!'.format(self.dog_type))
#
# dog1 = Dog()    #实例化，用模板生成实际的个体的过程
# dog2 = Dog()
# dog1.dog_bite()     #类属性与类方法的调用都要依附在实例上，    实例.类属性（方法）
#
# # def Dog.dog_roar():      #好像不能在类外部定义类方法
# # def dog1.dog_roar():
#
# dog1.d_aaa = 'aaa'      #可以在类外部新定义 实例 属性，
# Dog.dog_sex = 'male'    #也可以在类外定义公有属性
# print(dog1.dog_type,dog1.d_aaa)
#
# Dog.dog_type = 'chaiquan'
# print(dog1.dog_type,dog2.dog_type)
# '''
# 可以在类外部修改类的公有属性，
# 如果用该类生成的实例的公有属性a没有被修改过，则在外部修改类中的属性，生成的实例的相应公有属性也会被修改
#   原因在于python的指向机制。   类属性为实例属性的默认值，类属性与实例属性指向同一数据，当类属性修改时，
# 实例属性也被修改了
# '''
#
# dog1.dog_type = 'jinmao'
# print(dog1.dog_type)
#
# Dog.dog_type = 'zhuzhu'   #
# print(dog1.dog_type,dog2.dog_type)
# '''
# 如果在实例上修改了类的公有属性b，再在类里修改公有属性b，则该属性不会被改变。
# 因为实例的属性b指向的也是类中实例b所指向的数据，修改实例属性的值，则实例属性b的指向改变，
# 与类属性的指向就不相同了，所以此时修改类属性，并不会改变实例属性的值
# '''


# 传私有变量版本
class Dog:  # 类的命名要用驼峰体，即首字母大写，不要用下划线，这是官方规范
    dog_type = 'husky'  # 类属性，类变量,公有属性，由所有实例共享的属性
    cage = []           #  即在实例a中修改该公共属性，在实例b中查询该属性，也是会发生改变
                        #也可以理解为类属性的复制语句只会在该类第一次实例化时实行，后面都不会执行

    def __init__(self,name,age):
        self.name = name        #实例属性，实例变量，由每个实例独享
        '''
        self即为dog1。语句实际为 dog1.name = name 
        这个语句的作用即为将传入的参数与实例绑定,以便数据在类中流通
        (由构造函数，将数据传入所创建的实例的空间，如此该实例的其他函数也能在该空间中找到数据，即实现了数据的流通)
        '''
        self.age = age
        '''
        init函数称为初始化方法，构造方法，用来：
        1.进行一些初始化操作，会在定义类时自动执行，哪怕没有进行实例化
        2.接收并定义一些私有属性，
        3.初始化方法必须在其他函数的前面，因为自动执行初始化函数时，传入的参数才与类绑定，
          该实例的内存空间中才会有该参数，其他的方法才能使用这些数据
        '''
    def dog_bite(self):
        # print('{} attack!'.format(self.dog_type,name,age))
        #无法直接调用传入init函数中的参数，因为作用域不满足。想要调用的话，必须和实例本身绑定
        print(self.name, self.age)
        print('{} attack!'.format(self.dog_type))



dog1 = Dog('xigua',3)
'''
实例化时会自动将实例本身传入，上句实际上执行的是  dog1 = Dog(dog1,'xigua',3)
输出dog1和类中self的内存地址，会发现是相同的，由此可验证之。
传入实例本身是为了将私有变量与实例绑定，也为了类中方法的数据流通

'''
dog2 = Dog('pingguo',2)

dog1.dog_bite()     #实际上执行的是  dog1.dog_bite(dog1)
