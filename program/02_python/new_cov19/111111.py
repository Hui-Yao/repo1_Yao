import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager

myfont = font_manager.FontProperties(fname = 'C:\Windows\Fonts\simfang.ttf')




def funcSEIR(inivalue):
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
        if i > 10000:
            break
        res.append([s, e, i, r, t])


    return np.array(res)