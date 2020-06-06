#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

import shutil       #对文件，文件夹，有压缩包进行处理
'''
os模块提供了对目录或者文件的新建/删除/查看文件属性，还提供了对文件以及目录的路径操作。
但是，os文件的操作还应该包含移动 复制  打包 压缩 解压等操作，这些os模块都没有提供。

shutil模块就是对os中文件操作的补充。--移动 复制  打包 压缩 解压。
'''


# f1 = open(r'/home/hui/program/01_python/01_学习总结/99_实验数据库/04_模块/05_shutil实验素材/sunny_src','r')
# f2 = open(r'/home/hui/program/01_python/01_学习总结/99_实验数据库/04_模块/05_shutil实验素材/sunny_copyfileobj','w')
#
# shutil.copyfileobj(f1,f2)
'''
1.shutil.copyfileobj(fi,f2[,length = 16*1024])
将f1的(部分)内容复制给f2,这个length = 16*1024指的是文件大小，而不是多少行之类的。
使用本函数，f1,f2都必须原本就要存在，而且要先用open（）把两个文件打开，不然会报错。
更推荐下面的shutil.copyfile()
'''

shutil.copyfile(r'/home/hui/program/01_python/01_学习总结/99_实验数据库/04_模块/05_shutil实验素材/sunny_src',r'/home/hui/program/01_python/01_学习总结/99_实验数据库/04_模块/05_shutil实验素材/sunny2_copyfile')
#2.shutil.copyfile(f1,f2)——f2可不存在，也需要用open（）打开两个文件，一句话搞定

shutil.copymode('/home/hui/program/01_python/01_学习总结/99_实验数据库/04_模块/05_shutil实验素材/sunny_src',r'/home/hui/program/01_python/01_学习总结/99_实验数据库/04_模块/05_shutil实验素材/sunny3_copymode')
#3.shutil.copymode(f1,f2)——只将f1的权限复制给f2，其他的都不变（内容，属组，owner）

# shutil.copystat('/home/hui/program/01_python/01_学习总结/99_实验数据库/04_模块/05_shutil实验素材/sunny_src','/home/hui/program/01_python/01_学习总结/99_实验数据库/04_模块/05_shutil实验素材/sunny4_copystat')
#4.shutil.copystat(f1,f2)——将f1的所有stat信息（包括权限，组，用户，时间等）复制给f2，不复制文件内容
#emmm...执行程序第的全选问题还没搞透

shutil.copy(r'/home/hui/program/01_python/01_学习总结/99_实验数据库/04_模块/05_shutil实验素材/sunny_src',r'/home/hui/program/01_python/01_学习总结/99_实验数据库/04_模块/05_shutil实验素材/sunny5_copy')
#5.shutil.copy(f1,f2)——将f1的文件内容与权限赋给f2，相当与copymode与copyfile的组合

shutil.copy2('f1','f2')     #6.shutil.copy2(f1,f2)——将f1的文件内容与全部状态信息都赋给f2，相当于copyfile与copystat的组合

# shutil.copytree(src, dst, symlinks=False, ignore=None, copy_function=copy2,ignore_dangling_symlinks=False)
#7.shutil.copytree()——递归的复制文件内容及状态信息

shutil.rmtree('path', ignore_errors=False, onerror=None)
#shutil.rmtree()——递归地删除文件

shutil.move(src, dst)    #8.shutil.move()递归的移动文件

shutil.make_archive(base_name,format(zip),root_dir,owner,group,logger)


'''
9.shutil.make_archive()——创建压缩包并返回文件路径，例如：zip、tar
base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
如：www                        =>保存至当前路径
如：/Users/wupeiqi/www =>保存至/Users/wupeiqi/
format：	压缩包种类，“zip”, “tar”, “bztar”，“gztar”
root_dir：	要压缩的文件夹路径（默认当前目录）
owner：	用户，默认当前用户
group：	组，默认当前组
logger：	用于记录日志，通常是logging.Logger对象

'''
'''
shutil模块对文件的亚索是调用的zipfile，tarfile模块。
且shutil模块只能对文件进行压缩，不能解压，解压需要使用到zipfile和tarfile。
'''

