import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np



myfont = font_manager.FontProperties(fname = 'C:\Windows\Fonts\simfang.ttf')
N = 330000000

# 进行隔离时各人群数量
init = [3.29978832e+08, 1.47611963e+04, 7.54066662e+03, 8.37851847e+02, 2.50000000e+01]


k = init[1]/init[0]  # 隔离者中潜伏感染者的占比
m = 2  # 隔离潜伏者每天接触的人数（家人）
n = 0.1  # 每天没接触一个人被感染的概率

# 潜伏者与感染者对易感者的影响
alpha = 0.005  # 单个易感者单次接触单个感染者被感染的概率
beta = 5   # 单个易感者单天接触的感染者人数
eta = 0.1 * alpha  # 单个易感者单天与单个潜伏者接触被感染的概率
omega = 1.2 * beta  # 单个易感者单天接触潜伏者的人数


gamma = 1/10  # 单位时间内潜伏者转化为感染者的概率（一般取潜伏期的倒数）
rho = 0.7  # 感染者去医院的比例

# 住院恢复概率不一样
delta1 = 1/20  # 未住院者单天恢复的概率（取恢复时间的倒数）
delta2 = 1/10  # 住院者单天恢复的概率

mu = 0.7  # 居家隔离率

sigma = 0.001  # 隔离易感人群转化为易感人群的概率

lambda2 = 1/7  # 隔离有病者爆发时间的倒数

def social_distance(init):
    s1, e1, i, r, t = init
    mu = 0.6
    q= s1 * mu  # 居家隔离人数
    s = s1 - q  #不隔离的人数

    qe = q * k  # 隔离无病者
    # 隔离后，潜伏者分为了隔离的和每个里的
    qs = q * (1 - k)  # 隔离潜伏者
    e = e1 * (1 - mu)

    h = rho * i  # 住院者
    v = (1 - rho) * i  # 不住院者
    res = []
    res.append(init)
    while True:
        qs += -sigma * qs - m * n * qe
        qe += m * n * qe - lambda2 * qe
        s += sigma * qs - v * alpha * beta - e * eta * omega
        e += v * alpha * beta + e * eta * omega - gamma * e
        h +=  gamma * e * rho - delta2 * h
        v += gamma * e * (1-rho) - delta1 * v
        r += delta1 * v + delta2 * h
        t += 1
        if t> 10000:
            print("太多啦"*10)
            return res
        if t > 100:
            mu = 0.3
        res.append([s+qs, e, v+h, r, t])
        if v+h<50:
            break

    return np.array(res)

res = social_distance(init)

print(res[-1][-1])

# s_list = res[:, 0]
e_list = res[:, 1]
i_list = res[:, 2]
r_list = res[:, 3]
day_list =res[:, 4]

# 设置图片分辨率
plt.figure(figsize=(20,8),dpi=100)

# 设置x，y轴刻度
plt.xticks(range(int(res[-1][-1]) + 1),fontproperties = myfont,
           fontsize = 15)

# 设置坐标轴label
plt.xlabel('天数',fontproperties = myfont)
plt.ylabel('人数',fontproperties = myfont)

#设置图像标题
plt.title('各人群数量与时间的关系',fontproperties = myfont,fontsize = 15)

#设置网格
plt.grid(alpha = 0.5)

# 对应曲线数据
# plt.plot(day_list[100], s_list[100], label = 'Susceptibles')
plt.plot(day_list, e_list, label = 'Exposed')
plt.plot(day_list, i_list, label = 'Infects')
plt.plot(day_list, r_list, label = 'Resistance')




# 设置图例
plt.legend(prop = myfont,loc = 'upper left')

plt.show()

# plt.savefig(r'C:\Users\HuiYao\Desktop\before_SEIR')








