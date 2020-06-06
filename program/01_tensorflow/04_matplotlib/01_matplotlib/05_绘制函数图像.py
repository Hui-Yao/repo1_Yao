#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

from matplotlib import pyplot as plt
import numpy as np

#创建函数
f = lambda z : 1/np.exp(-z)

#创建x轴上的数据的准备
start = -100
stop = 100
step = 0.1

dot_num = (stop - start)/step
x = np.linspace(start,stop,dot_num,endpoint=True)     #创建x轴上的数据
'''
np.linspace(start,stop,dot_num)--生成等差数列
start/stop:起点/终点
dot_num:点数
endpoint = True/False     默认包括stop，false则不包括
'''
y = f(x)    #创建y轴上的数据

plt.figure(figsize=(20,8),dpi = 80)

plt.plot(x,y,label = 'sigmoid')

plt.grid()

plt.axis('equal')   #设置x y轴方向上的刻度长度一至。
plt.xlim(-100,100)
plt.ylim(-100,100)

plt.plot([2*min(x),2*max(x)],[0,0],label = 'x-axis')
'''
如果图像不止在第一象限，需要自行绘制x轴，
[2*min(x),2*max(x)]：前面表示x轴上的数据，起点为x最小值的两倍，终点为x最大值的两倍
[0,0]：表示y的坐标全为0
'''
plt.plot([0,0],[2*min(y),2*max(y)],label = 'y-axis')    #自行绘制y轴
plt.legend()
plt.show()
