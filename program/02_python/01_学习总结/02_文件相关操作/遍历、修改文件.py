#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author = Hui_Yao

f = open('/home/hui/desktop/yesterday','r',encoding='utf-8')
f2 = open('/home/hui/desktop/yesterday2','w',encoding='utf-8')

for line in f:
    if '我小时候' in line:
        line = line.replace('我','小灰灰')
        print(line)
    f2.write(line)

'''  
for line in f.readlines():
    if '我小时候' in line:
        line = line.replace('我','小灰灰')
        print(line)
    f2.write(line)
    
上面的方法也可以实现同样的功能，但是使用f.readlines()方法，其原理是将文件的所有读入内存，再在内存中遍历，
这个方法的问题是不适于大文件。

使用in f则是存一句，操作一句，删一句。这种方法更好。

'''