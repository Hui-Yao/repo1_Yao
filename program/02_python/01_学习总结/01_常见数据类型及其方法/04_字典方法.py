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
查：dict.get(key)  通过字典的键查找值得方法是非常快的

注： 1.字典是无序的，所以不存在索引，切片
    2.键必须是不可变对象，如字符串，元组，数字等；值可以是任何对象，包括用户自定义的对象
    3.如果字典中给同一个键赋值多次，则这个键对应的value是最后传入的那个value
       {1:2, 1:3, 2:3} --> {1:3, 2:3}
    4.key in dict 用时 1.088 秒   dict.get(key) 用时 1.294 秒    dict[key] 用时 1.01 秒
     通过key获取value的方式中，dict[key]的速度快于dict.get(key)
     在判断某字典中是否包含某key时，key in dict要快于dict.get(key)，dict[key]如果key不存在则会报错
     也就是说能不用dict.get()就不用，因为这个方法都有替代方法，且速度更快。
'''
#1.clear——请空列表
#2.copy——浅复制
#3.fromkeys(seq[,value])——以指定序列中的值为键，创建新字典.  可以指定键的值，默认为none
#4.get(key[,default = None])——通过键，返回对应的值.  若不存在，默认返回none，也可以指定返回别的值
#5.items——返回一个可遍历对象，其内层为原字典的键值对组成的一个个元组
#6.keys——返回一个可遍历对像，其内容为原字典的键
#7.values——返回一个可遍历对像，其内容为原字典的值
#8.pop(key)——删除指定键的以及对应的值，并返回其值
#9.popitem——随机删除一个键值对，并以元组的形式将其返回
#10.sedefault(key[,value])——返回指定键的值，若该键不存在，则再致电中添加该键值对   并返回该新的value
# list1.update(list2)——将list2合并入list1中，若两者有相同的键，则以list2的取代list1的



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

print('多次给同一个key赋值：',{1:2, 1:3, 2:3})


