#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname = '/usr/share/fonts/YaheiConsolas/YaHeiConsolas.ttf')

y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y_10 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

x_3 = range(1,32)
x_10 = range(51,82)
x_ = list(x_3) + list(x_10)     #只能有一个ｘ轴的数据

x_labels = ['3月{}号'.format(i) for i in x_3]
x_labels += ['10月{}号'.format(i-52) for i in x_10]   #也只能有一个ｘ轴标签

plt.figure(figsize=(20,8),dpi = 100)

plt.xticks(x_[::3],x_labels[::3],fontproperties = my_font,rotation = 45)

plt.xlabel('时间',fontproperties = my_font)
plt.ylabel('温度',fontproperties = my_font)
plt.title('时间与温度的关系',fontproperties = my_font)

plt.scatter(x_3,y_3,label = '3月份')
plt.scatter(x_10,y_10,label = '10月份')

plt.legend(loc = 'upper left' , prop = my_font)

plt.show()






