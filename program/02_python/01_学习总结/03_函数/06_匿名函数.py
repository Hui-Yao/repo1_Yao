#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
定义：不指定函数名的函数，用完即释放。可以将之赋值给变量（给该内存区域加上一个门牌），以实现多次调用。

使用场合：程序一次性调用，用完即扔的（常和sorted（），filter（）等函数配合使用）

规则：1.一般有一行表达式，必须有返回值。lanmbda后的整个为表达式，引号前面为变量，引号后面为返回值（也即封装的逻辑）
     2.可以没有参数（相当于def定义的无参函数），也可以有多个参数，也可使用默认参数，可变参数。
       只能使用lambda表达式中定义的参数，不能使用全局变量。
     3.引号后面应为一个表达式。如果是一些语句的话会执行语句并返回none。

调用：整个匿名函数可以看做是def定义的函数的函数名。（lambda ...）（参数）
     所以sorted函数中指定key时：key = lambda xxx,key = def定义的函数名（不用加括号）
'''

#目标1：计算两数之和
sum =lambda x,y : x+y
print(sum(1,5))
#等价
print((lambda y,x=1 : x+y)(y = 5))
'''
包含lambda的括号看做是函数体，x y都是默认参数，
(y = 5)看做是传入参数，进行调用，y=5,x还是等于1，故和为6
'''
print((lambda x,y,*args : print(x,y,args))(1,5,6))  #执行引号后的语句，返回值为none。
print(lambda : True)                                #无参数
'''
引号前面为设置的变量，引号后既是返回值，也是封装的逻辑。
分析(lambda x,y : x+y)(1,5)
1.将（1,5）依次传给（x，y）
2.引号后进行计算，并返回相应的值

'''

#目标2：求一个列表中大于3的元素
apple = [1,2,3,4,5]
ele = list(filter(lambda x:x>3,apple))  #filter返回的是一个可迭代对象，需用list方法处理一下
print(ele)
'''
filter（规则，待过滤对象）
'''

melon = [{'name':'abc','age':20},{'name':'def','age':30},{'name':'ghi','age':25}]
print(sorted(melon,key = lambda x:x['age']))   #每次把前面对象的一个元素传到后面
                                               #melon是列表，其内的元素是字典，所以sorted实际排序的是字典
#目标3：按键值对的值来排序
dict1 = {3:8,9:5,4:1,7:7}
print(sorted(dict1.items(),key = lambda x : x[1]))

#目标4：按字符串的最后一个字母排序
orange = ['abc', 'b', 'AAz', 'ef']
def lastchar(x):
    return x[-1]

print(sorted(orange,key = lastchar))    #传入函数名即可
print(sorted(orange,key = lambda x : x[-1]))



#key = str.lower()  将所有元素变小写，再按所有元素的首字母排序
#key = len      按数据宽度排序
#key = abs      按数据的绝对值排序


