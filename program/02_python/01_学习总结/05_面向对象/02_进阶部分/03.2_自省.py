#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
__name__:用于判断该模块是被主动执行还是被动导入
1.主动执行：__name__ = '__main__'
2.被动导入：__name__ = 模块名


'''

import module_usingfortest

print(hasattr(module_usingfortest,'apple'))     #hasattr自省可以用来判断导入的模块中是存在某些变量与方法
print(hasattr(module_usingfortest,'eat'))


