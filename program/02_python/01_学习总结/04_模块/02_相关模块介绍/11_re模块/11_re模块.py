#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"


#引子：去除模特空姐的联系方式
f = open('模特空姐联系方式','r')

tel_list = []
for i,j in enumerate(f):
    if i == 0:
        continue
    tel_list.append(j.split()[4])

print(tel_list)


import re   #正则表达式就是以规则来匹配字符串（而不是像字符串方法中以内容来匹配）

f.seek(0)
#用正则表达式完成
model_info = f.read()
print(re.findall('1[0-9]{10}',model_info))


'''
1.常见字符及其含义
    '.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
    '^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
    '$'     匹配字符结尾， 若指定flags MULTILINE ,re.search('foo.$','foo1\nfoo2\n',re.MULTILINE).group() 会匹配到foo1
    '*'     匹配*号前的字符0次或多次， re.search('a*','aaaabac')  结果'aaaa'
    '+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
    '?'     匹配前一个字符1次或0次 ,re.search('b?','alex').group() 匹配b 0次
    '{m}'   匹配前一个字符m次 ,re.search('b{3}','alexbbbs').group()  匹配到'bbb'
    '{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
    '|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
    '(...)' 分组匹配， re.search("(abc){2}a(123|45)", "abcabca456c").group() 结果为'abcabca45'
    '[...]' 只匹配中括号中的一个字符
    
    
    '\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的，相当于re.match('abc',"alexabc") 或^
    '\Z'    匹配字符结尾，同$ 
    '\d'    匹配数字0-9
    '\D'    匹配非数字
    '\w'    匹配[A-Za-z0-9]
    '\W'    匹配非[A-Za-z0-9]
    's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
    '(?P...)' 分组匹配 re.search("(?P[0-9]{4})(?P[0-9]{2})(?P[0-9]{4}



2.re的匹配语法有以下几种

    re.match 从字符串开头开始匹配
    re.search 从头开始找，只匹配一次
    re.findall 把所有匹配到的字符放到以列表中的元素返回
    re.split 以匹配到的字符当做列表分隔符，返回除开分隔符以外的内容
    re.sub 匹配字符并替换
    re.fullmatch 全部匹配，必须全部相同
    re.compile(pattern, flags=0)    先将匹配规则进行解析，再进行匹配，适用与处理规则相同的大规模匹配


3.Flags标志符

    re.I(re.IGNORECASE): 忽略大小写（括号内是完整写法，下同）
    re.M(MULTILINE): 多行模式，改变’^’和’$’的行为
    re.S(DOTALL): 改变’.’的行为,make the ‘.’ special character match any character at all, including a newline; without this flag, ‘.’ will match anything except a newline.
    re.X(re.VERBOSE) 可以给你的表达式写注释，使其更可读，

注：
1.正则表达式，返回类型为表达式对象的

    如：<_sre.SRE_Match object; span=(6, 7), match='a'>  
    
    返回对象的，需要用正则方法取字符串，
    
    方法有
    
    group() # 获取匹配到的所有结果，不管有没有分组将匹配到的全部拿出来，有参取匹配到的第几个如2
    groups() # 获取模型中匹配到的分组结果，只拿出匹配到的字符串中分组部分的结果
    groupdict() # 获取模型中匹配到的分组结果，只拿出匹配到的字符串中分组部分定义了key的组结果
    
2.匹配到的字符串里出现空字符

正则匹配到空字符的情况，如果规则里只有一个组，而组后面是*就表示组里的内容可以是0个或者多过，
这样组里就有了两个意思，一个意思是匹配组里的内容，二个意思是匹配组里0内容（即是空白）所以尽量避免用*否则会有可能匹配出空字符串



https://www.cnblogs.com/zjltt/p/6955965.html
https://book.apeland.cn/details/338/
'''







