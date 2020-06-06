#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''导入模块：
1.定义：以一定的逻辑来组织python代码（变量，函数，类，逻辑），用来解决某一类问题的，以.py结尾的python文件。

2.导入：
2.1 import module_name :导入一个模块
2.2 import module1,module2,... :导入多个模块，要用逗号分开
2.3 from module import * ：将文件中的代码导入，并不会导入模块。可能会有冲突问题
    from module import func(func1,func2,name1,name2,...)
2.4 from module import func as func1 :改变变量名，解决冲突问题

       注：模块的文件名：test.py   import时的模块名：test

3.importの本质
    3.1 import module1：将module1.py文件的内容解释一遍，再赋值给变量module1，即import module1 为 module1 = ‘module1.py’
        from module1 import func1  将module1.py文件中的func1函数这一部分解释一遍
    3.2 import的搜索路径（名词）
        import sys
        print(sys.path)  #以列表的形式输出import的搜索路径
    3.3 import路径搜索（动词）
    sys.path返回的是一个列表，列表中的内容是存放模块的位置。python解释器只会在指定的目录找，再下一层的都不会去找了。
    列表是有序的，import会按照列表中的顺序依次搜索模块（第一个位置是当前文件夹）
    如果模块没有放在规范的地方，可以用sys.path.insert(0,想要加入的搜索路径)来添加搜索路径，这样优先使用，
    否则最后才会用那个路径去搜索。

    总结：分析 import module1
    1.module1模块对应module1.py文件
    2.首先在当前目录寻找module1.py文件（因为当前目录在sys.path列表的第一个）
    3.当前目录没找到，按sys.path列表依次向后找
    4.找到module1.py后，将其中的内用解释一遍，付给变量module1；没找到则～～～

4.模块分类：
1.内置模块（标准库）：python自带
2.开源模块：比如去github上下载
3.自定义模块：自己写




'''

'''包（package）
1.定义：以一定的逻辑组织python的模块的，含有__init__.py的文件夹

2.导入包：import package_name

3.import包の本质：执行包目录下的__init__.py文件（可以在init文件中写一个print语句验证一下）

4.导入package1后想在程序中调用package1下的的模块

'''
