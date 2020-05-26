#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

import sys      #sys模块：负责程序python解释器的交互

# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])
# print('参数个数为：',len(sys.argv))
# print('参数列表为：',sys.argv)

'''1.sys.argv[x]
作用：sys.argv[x]用来接受命令行传入的参数
性质：sys.argv是一个参数列表,
sys.argv[0]代表的是当前文件的绝对路径。
argv[1],argv[2]...代表的都是外部传入的值。

注：与sys.argv相关的操作可在命令行进行操作，也可在pycharm按Alt+F12（调出终端）进行操作。

参考：https://www.cnblogs.com/yoyoketang/p/9542458.html

'''

print(sys.path)         #2.sys.path——返回python模块的搜索路径
print(sys.platform)     #3.sys.platform——输出当前平台
print(sys.version)      #4.sys.version——返回python解释器的版本信息
print(sys.getdefaultencoding())     #5.sys.getdefaultencoding()——返回平台默认编码
print('------',sys.modules.keys())
'''
6.sys.modules是一个全局  字典 ，是在python启动后就加载在内存中的，字典sys.modules对于加载模块起到了缓冲的作用。
当某个模块第一次导入，字典sys.modules将自动记录该模块。当第二次再导入该模块时，python会直接到字典中查找，
从而加快了程序运行的速度。

sys.modules的作用在同一个程序中两次导入同一个模块才会体现出来。
并不是说在a程序中首次加载了模块1，在b程序中输出sys.module时也会出现模块1的存放位置。

'''


sys.exit('对不起，程序已退出！')   #7.sys.exit()——退出程序，并会抛出一个异常；可以配合python的异常捕捉



print(sys.path)         #sys.exit()以后的程序都不会再执行了
