#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author = Hui_Yao

'''关于打开文件的模式：
1.r、w、a为打开文件的基本模式，对应着只读、只写、追加模式；
2.b、t、+、U这四个字符，与以上的文件打开模式组合使用，二进制模式，文本模式，读写模式、通用换行符，根据实际情况组合使用；

注：r+:以读的模式（不会覆盖源文件）打开文件，也可以写，但是只能卸载最后面（等于追加）
    w+：以写的模式（会覆盖源文件）打开文件，用的不多；a+用的也不多

'''


f = open(r'/home/hui/desktop/yesterday','r',encoding = 'utf-8')     #1.open(FilePath,mode,encoding)
song1 = f.read()
print(song1)

f.seek(0)        #2.seek(offset[,whence])——重新移动文本指针，offset为偏移量，whence为对offset的修饰
                #whence：0（默认）——从文件头开始偏移；1——从当前位置；2——从文件末尾

print('tell()'.ljust(20,'*'),f.tell())    #2.tell——返回当前指针所在位置，以字节计算

'''
指针位置的的计算与字符编码方式的关系：
windows默认的编码方式是Gbk，linux默认的是utf-8，python默认的是utf-8，下面也能看到

Gbk中一个中文占2字节，utf-8中占3字节（unicode中占两个字节，），对与‘苹果好吃’四个字，从文件头开始偏移4个字节，
使用gbk编码则指针刚好移动至‘果’和‘好’中间，可以正常输出前两个字，而使用utf-8时，光标移至‘果’字的字节中间，不完整，
无法正常输出。
'''

print('readline'.ljust(15,'*'),f.readline())     #3.readline()——一次读取一行

f.seek(0)
print('f.readlines()'.ljust(30,'*'),f.readlines())    #4.readlines()——将所有行输出成为一个列表

f.seek(0)

f2 = open('/home/hui/desktop/MoonRiver','w+',encoding='utf-8')

f2.write ('moon river \nwide than a mile \ni`ll cross you in style someday\n')
#5.write(str)——将字符串写入文件中，若是想写入新文件中，则需要用open创建一个文件
#注：若write中给定的字符串参数个数多于一个，则会导致文件无内容
f2.flush()       #6.flush()——将写的数据实时存入硬盘中

moon = ['oh dreammaker\n','you heart breaker\n']
f2.writelines(moon)     #7.writelines（seq）——可以使用序列作为参数，序列每个元素后需要\n

f2.flush()

# print(f2)

print('f2.name'.ljust(20,'*'),f.name)

# f2.truncate()     #用于截断文件
# print(f2)

f.close()       #9.close——用于关闭文件

#用with进行文件操作，操作完以后会自动关闭
#所谓的关闭文件后系统会自动关闭文件：如果你运行完程序后程序没有关闭（没有×掉），文件句柄之类的会一直存在内存中，造成内存浪费
with open('/home/hui/desktop/balabala','w',encoding='utf-8') as f3:
    f3.write('if you miss the train i`m on \nyou`ll know that i`m gone')




