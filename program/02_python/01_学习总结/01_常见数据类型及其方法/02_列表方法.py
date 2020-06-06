'''列表的增删改查
1.创建：list()函数
2.增：1.append()实现在末尾加上
     2.insert（）实现在中间插入
     3.切片——list[len(list):] = 列表或元组  实现在最后插入
            lsit[x:x] = 列表或元组          实现在索引为x的元素之前插入
3.删：del；pop（）；remove（）
4.改：...
5.查：索引，切片，
6.拼接：list1 + list2；list1.extend（list2）
        前者不会修改两个列表，后者会修改第一个列表
7.乘：*——使该列表元素复制多份，课可以用创建空列表

'''

dog1 = ['Apple',123,'blink']
tiger2 = ['two','tigers','456']

dog1.append(tiger2)     #1.append(element)——将element添加入原列表中，element是什么形式，加到列表里也还是什么形式
print(dog1)             #append是一个语句，不是一个原地操作符，所以不能连用append。
dog1.append('star')
print(dog1)


dog1 = ['Apple',123,'blink']
tiger2 = ['two','tigers','456']

ha2 = dog1.count(123)   #2.count()——返回数组中某元素的数量
xi2 = dog1.count('turtle')
print(ha2,xi2)

ha3 = dog1.copy()   #3.copy——浅复制一份源列表
print(ha3)
dog1.clear()    #4.clear——清空源列表，使之成为空列表
print(dog1)


dog1 = ['Apple',123,'blink']
tiger2 = ['two','tigers','456']

dog1.extend(tiger2)     #5.list1.extend(list2)——将list2的元素合并入list1中，这回改变list1
print('extend()方法：',dog1)             #注意：这与append不同，append会使list1成为一个嵌套列表
'''
extend(seq)方法相当于list[len(list):] = seq,对序列会进行分解再添加进原列表。若seq为字符串，则会分解为单个字符
append（seq）方法：seq是什么就添加进去什么。比如seq是列表，则形成嵌套列表

'''


dog1 = ['Apple',123,'blink']
tiger2 = ['two','tigers','456']

ha6 = dog1.index(123)   #6.index(element [,start [,end]])——输出某元素在列表红的索引；如不存在则报错.
                        # 如果写两个索引，那就是指定了头和尾；如果只写一个索引，那就是制定了开始端，也就是在这个索引以后的序列去找
# ha6_1 = dog1.index(111)
print(ha6)
# print(ha6_1)

dog1.insert(1,'dog')      #7.insert(index,element)——在指定索引前插入元素
print(dog1)

dog1 = ['Apple',123,'blink']
tiger2 = ['two','tigers','456']

dog1.pop(0)        #8.pop（index）——删除列表中指定索引的元素并返回被删除的项（会修改原列表）；默认删除最后一个item
print('pop方法:',dog1)        #如果索引超出范围或则列表为空则报错

dog1 = ['Apple',123,'blink']
tiger2 = ['two','tigers','456']

dog1.remove(123)     #9.remove(value)——删除列表中的指定值，若该元素不存在则报错
print('remove方法：',dog1)

dog1 = ['Apple',123,'blink']
tiger2 = ['two','tigers','456']

dog1.reverse()
ha10 = reversed(tiger2)
ha10_1 = list(ha10)
print('reverse'.center(20,'*'),'\n',dog1,tiger2,ha10,ha10_1)
'''
10.reverse()——将原列表反序，这会修改原列表，若想保留原列表，可以用切片方法将整个列表复值给另一个变量，再操作该变量
   无返回值；
   reverse()只对列表有效
   
reversed()方法会复制（深copy）一个原列表的副本进行操作，不会修改原列表
reversed（）函数也可将序列反转，有返回值，但返回的是一个可迭代对象，需要通过list等函数将其进行转换
reversed()对所有序列接有效
'''

lion = ['l','i','o','n']
rat = ['r','a','t']
duck = ['d','u','c','k']

lion.sort()
rat1 = rat[:]
rat1.sort()
duck1 = sorted(duck)

print(lion,rat,rat1,duck,sorted(duck),duck1)
'''
11.sort()方法可对原列表进行排序，这会修改原列表；若想保留原列表，则使用切片方法复制一份，不可使用直接赋值
   sort（）方法无返回值；
   通过指定不同的参数，可实现不同的排序方式
   sort()方法只对列表有效

   sorted()方法会复制一份原列表的副本进行操作，不会修改原列表
   sorted()方法返回的排序后的列表，不是可迭代对象
   sorted()方法也可指定参数以修改排序顺序
   sorted()方法对所有序列皆有效

'''

dog1 = ['Apple',123,'blink']
tiger2 = ['two','tigers','456']







