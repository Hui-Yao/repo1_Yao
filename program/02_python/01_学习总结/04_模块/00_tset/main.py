#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"



import test1_module     #调用本目录下的模块
test1_module.test1()

import test2_package    #导入包，会发现__init__.py中的print语句执行了
test2_package.test2_module.test2()

#import的搜索路径与路径搜索
import sys
# print(sys.path)
sys.path.insert(0,'/home/hui/program/01_python/01_学习总结/04_模块/00_tset/test33_module')   #这里可以用os模块的
print(sys.path)     #可以看见该目录已经被添加进去了

import test3_module     #test3_module与main.py不在同一级目录，也不再系统指定位置，所以要将其所在目录写明
test3_module.test3()





