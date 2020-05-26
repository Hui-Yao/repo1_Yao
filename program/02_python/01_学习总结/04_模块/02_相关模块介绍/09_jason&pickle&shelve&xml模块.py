#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
json  and  pickle是用于序列化的两个模块。
所谓序列化，就是将内存中的数据转换为字符串，使其能被存入硬盘或是通过网络传输出去。

json和pickle的区别：
    1.json是可以在不同语言之间交换数据的，而pickle只在python之间使用。

    2.json只能序列化最基本的数据类型，而pickle可以序列化所有的数据类型，包括类，函数都可以序列化。


shelve是对pickle的更高一层的封装
xml是被jason替代的。。。
'''

'''json和pickle的四个方法：

json.load()     # 将一个存储在文件中的json对象（str）转化为相对应的python对象
json.loads()    # 将一个json对象（str）转化为相对应的python对象
json.dump()     # 将python的对象转化为对应的json对象（str),并存放在文件中
json.dumps()    # 将python的对象转化为对应的json对象（str)
                #没有s的会操作文件，有s的只是进行转换，不会对文件操作
调用方法是常常与文件操作——open（）配合使用。
从文件中读数据： json.load(open('filename','r',encoding = 'utf-8'))
写数据去文件：   json.dump('data',open('filename','w',encoding = 'utf-8'))


pickle使用与json完全相同。


'''



