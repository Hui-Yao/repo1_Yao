#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author = Hui_Yao

'''字典的增删改查
创建：dict（）函数可以通过关键字创建字典，也可将序列（列表内嵌两元素的列表，元组；元组内嵌两元素元组列表）
     直接使用大括号创建字典和使用键作为索引，键都要加上引号；
     使用关键字创建字典时，其实是将变量名转化为键，不用加引号
增： dict[key] = value
     list1.update(list2)
删: del;pop()
改：
查：

注： 1.字典是无序的，所以不存在索引，切片
    2.键必须是不可变对象，如字符串，元组，数字等；值可以是任何对象，包括用户自定义的对象
    3.
'''
dog = dict(catagery = 'husky',sex = 'male')
cat = dict((['name','jack'],['sex','male']))
print(dog,dog['sex'],cat)

dog['color'] = 'golden'
print(dog)


person = {'name':'hui','age':23,'job':'IT'}

person.clear()      #1.clear——请空列表
person.copy()       #2.copy——浅复制

list1 = [1,2,3]
la3 = person.fromkeys(list1,10)    #3.fromkeys(seq[,value])——以指定序列中的值为键，创建新字典
print(la3)                         #可以指定键的值，默认为none

person = {'name':'hui','age':23,'job':'IT'}

la4 = person.get('name')                 #4.get(key[,default = None])——通过键，返回对应的值
la4_1 = person.get('sex','balabala')     #若不存在，默认返回none，也可以指定返回别的值
print(la4,la4_1)

la5 = person.items()    #5.items——返回一个可遍历对象，其内层为原字典的键值对组成的一个个元组
la6 = person.keys()     #6.keys——返回一个可遍历对像，其内容为原字典的键
la7 = person.values()   #7.values——返回一个可遍历对像，其内容为原字典的值

print(la5,list(la5),tuple(la5))
print(la6,la7)

la8 = person.pop('job')     #8.pop(key)——删除指定键的以及对应的值，并返回其值
print(la8)

la9 = person.popitem()      #9.popitem——随机删除一个键值对，并以元组的形式将其返回
print(la9)

person = {'name':'hui','age':23,'job':'IT'}

la10 = person.setdefault('age')  #10.sedefault(key[,value])——返回指定键的值，若该键不存在，则再致电中添加该键值对
la10_1 = person.setdefault('sex','male')    #并返回该新的value
print(la10,la10_1)


la11 = person.update(dog)       #list1.update(list2)——将list2合并入list1中，若两者有相同的键，则以list2的取代list1的
print(person)



