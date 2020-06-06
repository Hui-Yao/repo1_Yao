#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
hash值：利用散列算法，对于任意长度的输入，得到相同位数的输出的值，这个值成为hash值。
       但是，不同的输出可能会得到相同的hash值，这称为hash碰撞。
       hash（）函数在程序的一次运行中得到的hash值是唯一不变的，但是在运行这个程序得到的值就不一样了。

md5值：对hash值进行进一步的计算，得到128位的二进制数输出。
       md5值不管在什么平台，什么环境得到的值都是一样的；并且发生hash碰撞的概率更低。
       md2,md3,md4是md5的前身，反正已经没人使用了。
       md5的作用：1.防止篡改（哪怕一亿个对象里修改了一个，得到的MD5值也完全不同）
                 2.密码非明文（你输入的密码是明文，但是存在公司数据库里的是进过MD5加密再经过加盐的）
                 3.数字证书（网站防劫持等）

小知识：1.脱库：数据库被盗
       2.撞库：对字符串进行枚举，比较MD5值，宠儿得到密码
       3.加盐：将密码转换成的MD5值再进行处理

sha—1值：与MD5一样都是从md4发展来的，但是算法与MD5不同，得到的是160位的二进制数，更安全。
现在加密上用的最多的sha—256.

MD5与sha的比较
sha更安全，应用于加密
MD5加密速度更快，应用于校验，防篡改。

md5.sha1,sha256...加密算法的调用方法都相同
'''

import hashlib

#md5
m = hashlib.md5()       #声明m为一个MD5对象
m.update(b'huiyao')      #
print(m.digest())       #接受处理对象后再生成md5值，digest（）生成的是二进制MD5值
print(m.hexdigest())    #hexdigest()生成的是十六进制的MD5值，可读性更高
m.update('苹果'.encode('utf-8'))  #python不能处理unicode的文件
print(m.hexdigest())

#sha1
m2 = hashlib.sha1()
m2.update(b'huiyao')
print(m2.hexdigest())

m2.update('苹果'.encode('utf-8'))
print(m2.hexdigest())


