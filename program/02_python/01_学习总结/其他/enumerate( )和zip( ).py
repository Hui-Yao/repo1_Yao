#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author = "Hui_Yao"

#enumerate()
fruit = ['apple','orange','pear','pineapple']
print(enumerate(fruit))
print(list(enumerate(fruit)))
print(tuple(enumerate(fruit)))
'''
enumerate:枚举，列举
enumerate（list、tuple、dict）——生成一个可遍历对象
再使用list或tuple方法转换后，可生成一个列表或元组
其内部元素是索引与其对应元素所组成的元组（如果作用的对象是dict，那么返回的值是key的值，而不是value的值）

[(0, 'apple'), (1, 'orange'), (2, 'pear'), (3, 'pineapple')]
((0, 'apple'), (1, 'orange'), (2, 'pear'), (3, 'pineapple'))
'''

#zip()
name = ['jack','mike','lily']
age = (10,11,12)
num = [1001,1002,1003]
sex = 'mmf'

student = zip(name,age,num,sex)
print(student)
print(list(student))

'''
zip(seq1,seq2,...)——用于整合多个序列，生成一个可迭代对象。
经list，tuple方法处理后，其内部元素是各个序列对应位置元素所组成的元组。
如果元素数量不同，则处理完最短序列就结束。
'''

