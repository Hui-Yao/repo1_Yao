#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author = Hui_Yao

'''集合的增删改查：
创建：{}，set（）方法
增：
删：
改：
查

集合分两种：set和frozenset
set是支持元素增删的，frozen是不支持修改的

注： 1.集合是无序的
    2.天生去重，在集合中无法存放重复的元素
    3.集合中的元素都是不可变类型的，无法故可变类的数据

集合的关系运算：
&   isdisjoint（）
|   union（）
^   symmetric_difference()
-   difference（）

'''

web = {'jack','mike','ming','monk'}
java = {'lily','jack','john'}

web.add('peter')    #1.add(element)——向集合中添加元素
print(web)

web.clear()         #2.clear
web.copy()          #3.copy

web = {'jack','mike','ming','monk'}
java = {'lily','jack','john'}

la4 = web.difference(java)    #4.set1.difference(set2)——求set1对于set2的差集;相当于-
la4_1 = web - java            #这两种方法求差集会返回一个新集合，不会改变原集合
print(web,la4,la4_1)

web.difference_update(java)    #5.difference_update()与上的区别是：其会直接修改原集合，而不返回值
print(web)

web = {'jack','mike','ming','monk'}
java = {'lily','jack','john'}

web.discard('ming')       #6.discard()——删除集合中的指定元素；若元素不存在，则啥也不做
print(web)

web = {'jack','mike','ming','monk'}
java = {'lily','jack','john'}
la7 = web.intersection(java)    #7.intersection()——求两个的交集;相当于&
la7_1 = web & java              #这两种方法求交集会返回一个新集合，不会改变原集合
print(la7,la7_1)

#web.intersection_update()      #8.intersection()方法，参考difference_update

print(web.isdisjoint(java),'\n',web.isdisjoint({123}))      #9.set1.isdisjoint(set2)——判断两者是否无交集

print(web.issubset(java))       #10.issubset()——判断前者是不是后者的子集

print(web.issuperset(java))     #11.issuperset()——判断前者是不是后者的父集

print(web.pop())     #12.pop——随机删除一个集合元素，并返回其值

web = {'jack','mike','ming','monk'}
java = {'lily','jack','john'}

web.remove('ming')      #13.remove(element)——删除集合中的指定元素，如果不存在则报错，而discard则是啥都不做
print(web)

web = {'jack','mike','ming','monk'}
java = {'lily','jack','john'}
la13 = web.symmetric_difference(java)    #14.symmetric_difference()——返回两级和中不共有的元素
la13_1 = web ^ java                      #相当于^
print(la13)
print(la13_1)

# web.symmetric_difference_update(jave)   #15.symmetric_difference-update（）——...

web.update(java)    #16.update()-将两个集合合并,会修改原集合
print(web)

web = {'jack','mike','ming','monk'}
java = {'lily','jack','john'}

la17 = web.union(java)      #17.union（）——求并集，不改变原列表
la17_1 = web | java
print(la17,la17_1)

