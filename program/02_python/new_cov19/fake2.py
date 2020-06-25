import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager
import pprint

myfont = font_manager.FontProperties(fname = 'C:\Windows\Fonts\simfang.ttf')

N = 6500000000  # 人群总数
E_0 = 0  # 初始潜伏者
I_0 = 1  # 初始感染者
R_0 = 0  # 初始抵抗者
S_0 = N - E_0 - I_0 - R_0

alpha = 0.07  # 单个易感者单次接触单个感染者被感染的概率
beta = 10  # 单个易感者单天有效接触的人数
eta = 0.01  # 单个易感者单位时间与单个潜伏者接触被感染的概率
omega = 15  # 易感者与潜伏者接触的概率
gamma = 0.20  # 单位时间内潜伏者转化为感染者的概率（一般取潜伏期的倒数）
delta = 1/9  # 单位时间内感染者痊愈成为抵抗者的概率

# INI为初始状态下的人群情况
INI = (S_0,E_0,I_0,R_0)

def before(inivalue):
    s, e, i, r = inivalue  # X是初始数值列表
    t = 0
    res = []
    res.append([329999999, 0, 1, 0, 0])
    while True:
        s -= (s * i * alpha * beta + s * e * eta * omega)/N
        e += (s * i * alpha * beta + s * e * eta * omega)/N - gamma * e
        i += gamma * e - delta * i
        r = delta * i
        t += 1
        if i > 3000000:
            break
        res.append([s, e, i, r, t])

    return np.array(res)

def after(init):  # [3.19871286e+08 7.24615452e+06 3.51320524e+06 3.90356138e+05  3.70000000e+01]
    s, e,i,r,t = init

    res = []
    res.append(res1[-1])

    while True:
        t += 1

        e += -e * (1 /25)
        i += -i * (1 /30)
        r += e * (1 / 25) + i * (1 / 30)

        res.append([s,e, i, r, t])
        # print(res)

        if i+e<8000:
            break
    return np.array(res)


# 函数调用
res1 = before(INI)
res2 = after(res1[-1])
# s_list = res[:, 0]
e_list_bef = res1[:, 1]
i_list_bef = res1[:, 2]
r_list_bef = res1[:, 3]
day_list_bef =res1[:, 4]

e_list_aft = res2[:, 1]
i_list_aft = res2[:, 2]
r_list_aft = res2[:, 3]
day_list_aft =res2[:, 4]

# 设置图片分辨率
plt.figure(figsize=(20,8),dpi=100)

# 设置x，y轴刻度
x_labels = [ x for x in range(int(res2[-1][-1]+1)) if x %5 == 0]
plt.xticks(x_labels,fontproperties = myfont,
           fontsize = 15)

# 设置坐标轴label
plt.xlabel('天数',fontproperties = myfont)
plt.ylabel('人数',fontproperties = myfont)

#设置图像标题
plt.title('各人群数量与时间的关系（隔离前后）',fontproperties = myfont,fontsize = 15, color = 'r')

#设置网格
plt.grid(alpha = 0.5)

# 对应曲线数据
# plt.plot(day_list[100], s_list[100], label = 'Susceptibles')
plt.plot(day_list_bef, e_list_bef, label = 'Exposed', color = 'b')
plt.plot(day_list_bef, i_list_bef, label = 'Infects' , color = 'r')
plt.plot(day_list_bef, r_list_bef, label = 'Resistance', color = 'y')

plt.plot(day_list_aft, e_list_aft, label = 'Exposed', color = 'b')
plt.plot(day_list_aft, i_list_aft, label = 'Infects', color = 'r')
plt.plot(day_list_aft, r_list_aft, label = 'Resistance', color = 'y')



# 设置图例
plt.legend(prop = myfont,loc = 'upper left')

plt.show()






