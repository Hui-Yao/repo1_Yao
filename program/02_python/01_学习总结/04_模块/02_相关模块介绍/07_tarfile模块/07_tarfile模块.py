#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

import tarfile      #tar包是只打包不压缩

'''
除了压缩时使用的是t.add（file）外，其余皆与zipfile相同

压缩方法：
1.t = tarfile.TarFile(,)
2.t.add()
3.t.close()

'''

t = tarfile.TarFile('tarfile_compress','w')

t.add('__init__.py')

print('hello world!')

t.add('tarfile_test1')

t.close()

'''
解压方法与zip包完全相同

'''

t2 = tarfile.TarFile('tarfile_compress','r')

t2.extractall()

t2.close()


#解压指定文件的方法参考zipfile



