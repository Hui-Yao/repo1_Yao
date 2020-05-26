#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
折线图：用于表现数据的变化
'''

from matplotlib import pyplot as plt
from matplotlib import font_manager

myfont = font_manager.FontProperties(fname = 'C:\Windows\Fonts\simfang.ttf')
#FontManager是font_manager下的一个类

'''
linux/mac 下可通过以下方法查看系统支持的字体及位置。
fc-list:查看系统下的所有字体
fc-list :lang=zh   查看系统下的左右中文字体，list后有一个空格

windows下字体储存再C:\Windows\Fonts下
找到想用的字体，右键选择属性，便可查看其代号：xxxx.ttf
那么字体的位置便是C:\Windows\Fonts\\font_name.ttf
'''
#在xticks()　函数中设置fontproperties = myfont　即可

x = range(1,25)
y1 = [11,9,9,10,11,11,14,15,15,17,19,20,21,20,19,17,16,\
     16,15,15,14,13,13,12]
y2 = [11,9,9,14,11,11,14,16,15,17,19,20,21,25,19,17,16,\
     16,15,12,14,15,13,11]

#1. 设置图片大小与分辨率,在show和savefig前才会有效果
plt.figure(figsize=(10,6),dpi=100)

x_labels = ['{}点'.format(i) for i in range(1,25)]
#2. 设置x,y轴的刻度,
plt.xticks(range(1,25),x_labels,rotation = 45,fontproperties = myfont,
           fontsize = 15)
# plt.xticks([11,9,9,10,11,11,14,15,15,17,19,20,21,20,19,17,16,\
#      16,15,15,14,13,13,12],[i*10 for i in range(1,25)])
# plt.xticks(range(1,25),['fun']*24)
plt.yticks(range(min(y1),max(y1)+1))
'''
前面设置的ｘ，ｙ的数值决定的是坐标轴的范围，默认不适用xticks()函数时，整个轴会被均匀地
布上刻度与坐标。

xticks(locations,labels,rotation,fontproperties,fontsize)，yticks()
两个函数格式完全相同。
    locations：是一个list_alike类型的数据，表示的是显示刻度的位置。
    (这个参数并不能代替前面的ｘ参数，比如当指定的刻度只是整个ｘ范围的一部分时，
    ｘ轴的其余部分并不会消失，只是那一部分轴上没有刻度)
    这个列表可以使随意的，也就是或轴上的刻度可以使不均匀的。
    如果不指定第二个数据，则每个刻度处都写上其距离远点的距离。
    
    labels：也是一个list_alike的数据，表示的是刻度处显示的东西。
    labels和locations两个列表的维度应该是一样的。
要画多张图就是使用多次plt.plot()
xticks()负责搭建图像的框架，plot(),scatter()负责在框架上画出线或点，两者互不干扰
'''

#设置ｘ，ｙ轴的名称
plt.xlabel('时间/hour',fontproperties = myfont)
plt.ylabel('温度/℃',fontproperties = myfont)

#设置图像标题
plt.title('一天中时间与温度的关系',fontproperties = myfont,fontsize = 15)

#设置网格
plt.grid(alpha = 0.5)
'''
alpha = num  指定透明度
axis = 'both'/'x'/'y'  指定显示的网格线的方向
color
linestyle = '-'/'--'/'-.'/''
linewidth = num  指定网格线的宽度

注：grid中没有规定网格线间距的参数，因为间距是根据xticks,yticks指定的位置来绘制的
'''

#3. 绘图，但不会显示图片
plt.plot(x,y1,label = '南昌',color = 'k',linestyle = '--',linewidth = '7',alpha = '0.6')
plt.plot(x,y2,label = '九江',color = 'r')


#设置图例
plt.legend(prop = myfont,loc = 'upper left')
'''
1. 要显示图例的话，首先要在plt.plot()添加参数，label = 'r',不然不会显示
2. prop设置字体
3. loc设置图例的位置
4. plt.legend()要在plt.plot() 即画图之后，不然不会显示。
'''

#4.在图形界面中展示出图像
plt.show()

# #5. 保存图片
# plt.savefig('/home/hui/desktop/mat_test')
# plt.savefig('C:\Users\HuiYao\Desktop')




