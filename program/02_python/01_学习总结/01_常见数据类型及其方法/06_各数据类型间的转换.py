# scalar(int, float), str, list, tuple, set, dict
#eval（）可以将特定形式的str转换成相应类型

int1 = 120
float1 = 10.1
str1 = 'apple'
str2 = '123'
list1 = ['p','e', 'a', 'r']
list2 = [1, 2, 3 ,4]
list3 = ['1', '2', '3', '4']
tuple1 = ('c', 'h', 'e', 'r', 'r','y')
tuple2 = (4, 5, 6, 7)
tuple3 = ('4', '5', '6', '7')
set1 = {'o', 'r', 'a', 'n', 'g', 'e'}
set2 = {10, 11, 12, 13}
dict1 = {'dog':100, 'pig':200, 'cat':300}


########################################################int与str、list（tuple）的转换
#int to str: 使用str()
int_str = str(int1)
float_str = str(float1)
print('int to str:',type(int_str),int_str)
print('float to str:',type(float_str),float_str)
#str to int;使用int（）
str_int = int(str2)
print('str to int:',type(str_int),str_int)

#int to list:list(str(int)),先将整数转化为str，在将str转化为list
int_list = list(str(int1))
print('int to list:', type(int_list), int_list)
#list3 = ['1', '2', '3', '4'] to int:先将内部元素为字符串的列表转化为字符串，再通过int（）将str转化为int
list3_int = int(''.join(list3))
print('list to int',type(list3_int), list3_int)
#list2 = [1, 2, 3 ,4] to int：先将内部元素转化为字符串，再同上
list4 = [str(i) for i in list2 ]
list2_int = int(''.join(list4))
print('list2 to int:',type(list2_int),list2_int)

## int与tuple的转换，与int和list的转换方法一致

#int与set，dict的转化没什么意义

###############################################################str与list（tuple）、dict的转换
#str to list:通过eval(),list(),split()将三种不同形式的字符串转为列表
s = "['p','e', 'a', 'r']"
print('eval方法:',eval(s))

str1_list = list(str1)
print(str1_list)

s2 = 'a,b,c'
s2_list = s2.split(',')
print('split方法',s2_list)

#list转化str：'',join(list)

#str转换为dict采用eval（），dict转化为str用str


#########################################################list与dict转换
#将两个列表转换为字典
k = ['a', 'b', 'c']
v = [1, 2, 3]
print(dict(zip(k, v)))

#将内嵌列表转化为字典
haha = [['a',1], ['b',2], ['c',3]]
print(dict(haha))

#通过dict.keys ,dict.values获得dict的key 和 value组成的列表


