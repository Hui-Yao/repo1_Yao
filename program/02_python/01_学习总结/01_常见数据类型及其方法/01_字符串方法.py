'''字符串的增删改查
创建：使用‘’.join(sequence，可迭代对象),可以将序列转化为字符串；用双引号或者单引号括起来，不括起来会被认为是变量名
增：
删：del
改：无
查：切片，索引

其他：
+：用于字符串拼接
*：将字符串扩展至多份

01_str.capitalize():将第一个元素大写，其余元素小写。返回规则化后的字符串，不修改原字符串。
02_str.casefold():将所有语言中的字母变小写。返回修改后的字符串，不改变原字符串。      注：lower()仅仅是将英文字母小写。
03_str.center(width,str1):以指定字符串str1填充str两侧width宽度的空间，并返回该结果。不修改原字符串。
04_str.count(str1):统计str中str1元素的数量并返回。
05_str.encode('encoding'):以encoding指定的编码方式编码str，并返回。
06_str.find(substr,[start,[end]])：找出字符串（指定范围）中,子字符串substr所在位置的最小索引（子字符串首字母索引）
   str.rfind()：从右边开始找
07_str.isalnum()：判断字符串是不是全部由数字与字母组成
       isalpha():判断字符串是否全由字母组成
       isdigit():判断字符串是否全由数字组成
       isdentifier():判断字符串是不是一个标识符，也即判断字符串是不是一个合法的变量名
       isdecimal():方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
       isnumeric():方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
       isspace():判断该字符串是否为空格（包括\n,\t, ,）
       istitle():判断该字符串是否为标题形式的，即首字母大写
       islowwer():判断该字符串中所有英文字母是否全为小写
       isupper():判断该字符串中多有字母是否全为大写







'''
# 字符串方法
char1 = 'Apple_ApPle'
char2 = 'bNana_bNana'
char3 = '312oraNgE'

la1 = char2.capitalize()  # 1.capitalize——有返回值——将首字母大写，其余字母小写
ha1 = char3.capitalize()
print('01_capitalize方法:',la1, char2)
print('01_capitalize方法:',ha1, char3)

'''capitalize（）与title（）的区别
capitalize（）是使整个字符串首字母变大写，其余字母全变小写。如果第一个字符不是字母，则相当于lower（）
title（）是使字符串中所有的字母组的首字母变大写，其余字母全变小写。有多少个连续的字母组，就有多少个大写字母。

'''
la2 = char1.casefold()  # 2.casefold——有返回值——将所有字母（不局限与英文）变为小写，lower（）方法只能将英文字母变为小写
ha2 = char2.casefold()
print('02_caseflod方法：',la2, char1)
print('02_caseflod方法：',ha2, char2)

la3 = char1.center(50, '*')  # 3.center（width,str）——有返回值——以指定宽度与指定字符串填充所操作的字符串的两侧
print('03_center方法：',la3,char1)

la4 = char1.count('p')  # 4.count(str)——有返回值——返回字符串中某元素的数量
print('04_count方法：',la4)

ga1 = '太阳'.encode('utf-8')  # encode(encoding,error) 方法以 encoding 指定的编码格式编码字符串。
print('05_count方法：',ga1)  # errors参数可以指定不同的错误处理方案

ga2 = 'haha\txixi'.expandtabs(20)  # expandtabs(num)——以指定数量的空格代替字符串中的tab，默认为8个空格
print(ga2)

la5 = char1.find('pp')  # 5.find(substr,[start,[end]])——找出字符串（指定范围）中
ha5 = char1.find('pp', 5, 9)  # 子字符串所在位置的最小索引（子字符串首字母索引）
la5_1 = char1.rfind('pp')  # rfind()——除了从右边查找外，与上相同
print(la5, ha5, la5_1)

la6 = 'today is a {} day'.format('sunny')  # 6.format——字符串格式化方法之一
print(la6)

la7 = char1.index('pp')  # 7.index(substr[,start[,end]])——查询子字符串是否存在于S中，存在则返回子字符串的首字母索引，不存在则报错
# 与find方法的区别在于，当子字符串不存在返回-1，且find方法不能用于列表
la7_1 = char1.rindex('pp')  # rindex()——从右边开始查找
print(la7, la7_1)

la8 = char1.isalnum()  # 8.isalnum——判断字符串是不是全部由数字与字母组成
la9 = char1.isalpha()  # 9.isalpha——判断字符串是否全由字母组成
la10 = char1.isdigit()  # 10.isdigit——判断字符串是否全由数字组成
la11 = char1.isidentifier()  # 11.isdentifier——判断字符串是不是一个标识符，也即判断字符串是不是一个合法的变量名
la12 = char1.isdecimal()  # 12.isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
la13 = char1.isnumeric()  # 13.isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。
la14 = char1.istitle()  # 14.istitle——判断该字符串是否为标题形式的，即首字母大写
la14_1 = char2.istitle()
la14_2 = char3.istitle()
print(la14, la14_1, la14_2)
la15 = char1.isspace()  # 17.isspace——判断该字符串是否为空格（包括\n,\t, ,）
la16 = char1.islower()  # 15.islowwer——判断该字符串中所有英文字母是否全为小写
la17 = char1.isupper()  # 16.isupper——判断该字符串中多有字母是否全为大写
la18 = char1.lower()  # 18.lower——将字符串中所有字母变为小写
la19 = char1.upper()  # 19.upper——将字符串中所有字母变为大写
la19_1 = char1.swapcase()  # swapcase()——交换大小写

la20 = '|'.join(char1)  # 20.sep.join(seq)——以指定的分隔符（sep）将字符串(seq)分隔，返回新的字符串
print('join方法',la20)  # join方法对于字符串而言试讲每个字符都分开,但仍是一个字符串;

la21 = char1.ljust(50, '*')  # 21.ljust(width,fillchar)——指定宽度，以指定字符串填充S的左侧
la22 = char1.rjust(50, '*')  # 21.rjust(width,fillchar)——指定宽度，以指定字符串填充S的右侧
print(la21, '\n', la22)  # 配合上center（），齐了

transtab = char1.maketrans('Ap', '12')  # 22.str.maketrans(input,output) 方法用于创建字符映射的转换表(transtab)，
# 第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串,表示转换的目标。
la23 = char1.translate(transtab)  # 23.str.translate(transtab)——使用转换表对字符串进行转换
print(la23)

la24 = char1.partition('pP')  # 24.partition(sep)——从左边查找自指定的分隔符是否存在与S中，存在则以元祖的形式返回/
la24_1 = char1.partition('**')  # 该分隔符前部分，分隔符本身，分隔符后部分。不存在则返回源字符串，以及两个空格
print('partition():',la24, la24_1)

la25 = char1.rpartition('pp')  # 25.rpatition(sep)——除了从右边开始查找外，遇上相同

la26 = char1.replace('Apple', 'Orange', 1)  # 26.replace(old,new,count)——以新的字符串替换旧的字符串，可以指定最大的替换数量
print('replace方法:',la26)

la27 = char1.startswith('A')  # 27.startwith(str)——判断字符串是否以str开头
la28 = char1.endswith('A')  # 28.endwith（str）——判断字符串是否以str结尾
print(la27, la28)

la29 = char1.split('_')  # 29.split(sep，maxsplit)——以指定字符串分割字符串，并且可以指定最大分割次数
la30 = char1.rsplit('lalal')  # 30.rsplit(sep,maxsplit)——从右开始
print('split(),rsplit()',la29, la30)
'''partition()与split()de的区别:
partition()会返回三个部分（前，分隔符，后）形成元组。分隔符不存在则返回源字符串与两个空字符串。
split（）只会返回两个部分（不会返回分隔符）形成列表。分隔符不存在则返回只包含源字符串一个元素的列表。
'''


la31 = '    ha xi\the \ ga****'.strip('*')  # 31.strip(substr='x')——移除字符串两边的substr，默认移除空格
la32 = '    ha xi\the \n ga   '.rstrip()  # 32.rstrip（substr）——移除右边的
print(la31)
print(la32)

la33 = 'apple-bBB-3ddd'.title()  # 33.title（）——将字符串中所有字母组的首字母变为大写，其余字母小写
print(la33)

la34 = char1.zfill(50)  # 34.zifill(width)——将源字符串右对齐，前面填充0

la34 = max(char1)  # max,min方法返回该字符串中按ascii排序的最大个最小值
la35 = min(char1)
print(la34, la35)

la36 = len(char1)  # len方法返回字符串的长度


#将序列，可迭代对象转化为字符串的方法
print(''.join(reversed('abcd')))  # 在可迭代对象中插入none，将可迭代对象转化为字符串
