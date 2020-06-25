import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

myfont = font_manager.FontProperties(fname = 'C:\Windows\Fonts\simfang.ttf')

# 隔离前参数
N = 650000000  # 人群总数
e1 = 0  # 初始潜伏者
i1 = 1  # 初始感染者
r1 = 0  # 初始抵抗者
s1 = N - e1 - i1 - r1  # 最初易感者人数

alpha_bef = 0.1  # 单个易感者单次接触单个感染者被感染的概率
beta_bef = 10  # 单个易感者单天有效接触的人数
eta_bef = 0.01  # 单个易感者单位时间与单个潜伏者接触被感染的概率
omega_bef = 15  # 易感者与潜伏者接触的概率
gamma_bef = 0.20  # 单位时间内潜伏者转化为感染者的概率（一般取潜伏期的倒数）
delta_bef = 1/9  # 单位时间内感染者痊愈成为抵抗者的概率

init_crowd_bef = (s1, e1, i1, r1, N)
init_params_bef = (alpha_bef, beta_bef, eta_bef, omega_bef, gamma_bef, delta_bef)


# 隔离后参数

# 潜伏者与感染者对易感者的影响
alpha_aft = 0.005  # 单个易感者单次接触单个感染者被感染的概率
beta_aft = 5   # 单个易感者单天接触的感染者人数
eta_aft = 0.1 * alpha_aft  # 单个易感者单天与单个潜伏者接触被感染的概率
omega_aft = 1.2 * beta_aft  # 单个易感者单天接触潜伏者的人数

gamma_aft = 1/10  # 单位时间内潜伏者转化为感染者的概率（一般取潜伏期的倒数）
rho_aft = 0.7  # 感染者去医院的比例

# 住院恢复概率不一样
delta1_aft = 1/20  # 未住院者单天恢复的概率（取恢复时间的倒数）
delta2_aft = 1/10  # 住院者单天恢复的概率

mu_aft = 0.7  # 居家隔离率

sigma_aft = 0.001  # 隔离易感人群转化为易感人群的概率

lambda_aft = 1/7  # 隔离有病者爆发时间的倒数

init_params_aft = (alpha_aft, beta_aft, eta_aft, omega_aft, gamma_aft, rho_aft, \
                   delta1_aft, delta2_aft, mu_aft, sigma_aft, lambda_aft)

def before_quarantine(init_crowd, init_params):
    s, e, i, r ,N = init_crowd  # 隔离前初始人群分布
    alpha, beta, eta, omega, gamma, delta = init_params
    t = 0  # 时间计时
    res = []
    res.append([329999999, 0, 1, 0, 0])
    while True:
        s -= (s * i * alpha * beta + s * e * eta * omega)/N  # 易感者每日更新
        e += (s * i * alpha * beta + s * e * eta * omega)/N - gamma * e  # 潜伏者每日更新人数
        i += gamma * e - delta * i  # 感染者没人更新人数
        r = delta * i  # 抵抗者没人更新人数
        t += 1
        if i > 10000:
            break
        res.append([s, e, i, r, t])

    return np.array(res)  # 返回5元素的列表


def after_quarantine(init_crowd, init_params):
    '隔离后的传染模型'
    s1, e1, i, r, t = init_crowd
    alpha, beta, eta, omega, gamma, rho, delta1, delta2, mu, sigma, lambda2 = init_params

    k = init_crowd[1]/init_crowd[0]  # 隔离人群中，潜伏者所占比例
    m = 2.5  # 隔离潜伏者每日人数更新
    n = 0.1  # 隔离潜伏者单次接触隔离易感者的传染概率

    q= s1 * mu  # 居家隔离人数
    s = s1 - q  #不隔离的人数

    qe = q * k  # 隔离无病者
    # 隔离后，潜伏者分为了隔离的和每个里的
    qs = q * (1 - k)  # 隔离潜伏者
    e = e1 * (1 - mu)

    h = rho * i  # 住院者
    v = (1 - rho) * i  # 不住院者
    res = []
    res.append(init_crowd)

    while True:
        qs += -sigma * qs - m * n * qe  # 隔离易感者每日人数变化
        qe += m * n * qe - lambda2 * qe  # 隔离潜伏者每日人数变化
        s += sigma * qs - v * alpha * beta - e * eta * omega  # 易感者每日人数变化
        e += v * alpha * beta + e * eta * omega - gamma * e  # 潜伏者每日人数变化
        h +=  gamma * e * rho - delta2 * h  # 住院者每日人数变化
        v += gamma * e * (1-rho) - delta1 * v  # 未住院感染者每日人数变化
        r += delta1 * v + delta2 * h  # 康复人群每日人数变化
        t += 1

        res.append([s+qs, e, v+h, r, t])
        if v+h<5000:
            break

    return np.array(res)


res1 = before_quarantine(init_crowd_bef, init_params_bef)

res2 = after_quarantine(tuple(res1[-1]), init_params_aft)

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
plt.title('各人群数量与时间的关系',fontproperties = myfont,fontsize = 15, color = 'r')

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