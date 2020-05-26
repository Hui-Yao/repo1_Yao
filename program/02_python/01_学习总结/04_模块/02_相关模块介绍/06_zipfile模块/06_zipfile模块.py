#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

import zipfile      #zip包是先打包在压缩

'''使用zipfile进行压缩：
1.以w模式打开（创建）文件，
2.每次用z.write(file)就往指定的压缩文件里多加一些东西，不是创建新文件
3.z.close()


'''

z = zipfile.ZipFile('zipfile_compress','w')     #默认压缩到当前路径

z.write('zipfile_test1')

z.write('__init__.py')

z.close()


'''使用zipfile进行解压：
1.以r模式打开文件
2.z,extractall()
3.z.close()

'''

z = zipfile.ZipFile('zipfile_compress','r')

z.extractall()

z.close()



'''也可接呀指定文件，而不全解压

z = zipfile.ZipFile("node.zip",'r')
for item in z.namelist():
     if item == 'test.py':
             z.extract('test.py')       #这里是extract（）不是extractall（）
z.close()

'''

