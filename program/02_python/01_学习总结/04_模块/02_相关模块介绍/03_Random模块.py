#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author = "Hui_Yao"

import random
print(random.random())              #1.random.random()-无参数——生成一个随机的浮点数，其值位于0到1之间
print(random.uniform(1,10))         #2.random.uniform(start,end)-两个必须参数——返回指定范围内的一个随机浮点数
print(random.randint(1,10))         #3.random.randint(start,end)-两必须参数——返回指定范围内的一个随机整数
print(random.randrange(1,50,5))     #4.random.randrange(start,end,step)-三必须参数——返回间隔随机的数
print(random.choice('ilikeapple'))  #5.random.choice(seqence)——返回序列中的一个随机元素

num = [1,2,3,4,5]
random.shuffle(num)                 #6.random.shuffle(seqence)——是一个序列随机排序
print(num)                          #这会改变原序列

lala = [6,7,8,9,10]
haha = random.sample(lala,3)        #7.random.sample(seq,num)——截取一个序列中的指定数量的元素，并进行随机排序
print(haha)                         #这不会改变原序列


