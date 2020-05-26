#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
当代码执行错误时，会产生异常，分强异常与若异常，强异常会导致整个程序都无法执行，所以强异常无法捕捉，而若异常可以捕捉。
1.异常处理的作用：当程序出现错误时，我们一般不希望给用户看到令人懵逼的异常提醒，通过异常处理，可以增加程序的友好性。
2.python的异常其实也都是class，都继承于BaseException这个基类。所以异常是有继承关系的，即子异常于父异常，
如果except子 和 except 父，那么就只会捕捉到父异常而不会捕捉到子异常。

常见的异常有：
Exception               这个异常基本上可以捕捉python内建的所有异常。
AttributeError          试图访问一个对象没有的属性，比如foo.x，但是foo没有属性x
IOError                 输入/输出异常；基本上是无法打开文件
ImportError             无法引入模块或包；基本上是路径问题或名称错误
IndentationError        语法错误（的子类） ；代码没有正确对齐
IndexError              下标索引超出序列边界，比如当x只有三个元素，却试图访问x[5]
KeyError                试图访问字典里不存在的键
KeyboardInterrupt       Ctrl+C被按下
NameError               使用一个还未被赋予对象的变量
SyntaxError             Python代码非法，代码不能编译(个人认为这是语法错误，写错了）
TypeError               传入对象类型与要求的不符合
UnboundLocalError       试图访问一个还未被设置的局部变量，基本上是由于另有一个同名的全局变量，导致你以为正在访问它
ValueError              0传入一个调用者不期望的值，即使值的类型是正确的

'''

try:
    apple = 'apple'
    print(apple.banana)
# except Exception as e:
#     print(e)

except AttributeError as a:     #因为变量apple没有属性banana，所以爆出了AttributeError
    print(a)
    print('该变量没有这个属性哦！')    #输出友好的异常提醒

#万能异常Exception一般用在异常处理的最后，用于捕捉那些没有预料到的异常
except Exception as a:
    print(a)

else:
    print('不发生异常，就走这里。。。')
finally:
    print('发布发生异常，都会走这里。。。')


