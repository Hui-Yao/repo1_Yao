#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

from matplotlib import pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc")

barwidth = 0.2

a = ["猩球崛起3：终极之战","敦刻尔克","蜘蛛侠：英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

x14 = list(range(len(a)))
x15 = [i+barwidth for i in x14]
x16 = [i+barwidth for i in x15]

plt.xticks(x15,a,fontproperties = my_font)

plt.bar(x14,b_14,width = 0.2,color = 'orange',label = '14号')
plt.bar(x15,b_15,width = 0.2,color = 'blue',label = '15号')
plt.bar(x16,b_16,width = 0.2,color = 'red',label = '16号')

plt.legend(prop = my_font)

plt.show()





