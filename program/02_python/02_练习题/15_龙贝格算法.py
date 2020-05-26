#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

'''
要求计算e(-x(2))在[0,1000]上的积分，并自动控制误差

'''

import math

a = 0               #下限
b = 1000            #上限
err = 10**-int(input('输入需求的进度：'))       #指定精度
T = []              #复合梯形序列
S = []              #辛普森序列
C = []              #科特斯序列
R = []              #龙贝格序列

def func(x):
    '''
    定义被积函数
    '''
    return math.exp(-x**2)


def Romberg(a,b,err,func):
    '''
    龙贝格算法
    '''
    h = b - a   #区间总长度
    T.append(h * (func(a) + func(b)) / 2)   #初始
    ep=err+1
    m=0     #与小区间的数量有关
    while(ep>=err):     #结束循环的条件
        m=m+1   #通过m的递增，实现依次更新生成T，S，C，R
        t=0
        for i in range(2**(m-1)-1):
            t=t+func(a+(2*(i+1)-1)*h/2**m)*h/2**m
        t=t+T[-1]/2
        T.append(t)
        if m>=1:
            S.append((4**m*T[-1]-T[-2])/(4**m-1))
        if m>=2:
            C.append((4**m*S[-1]-S[-2])/(4**m-1))
        if m>=3:
            R.append((4**m*C[-1]-C[-2])/(4**m-1))
        if m>4:
            # ep=abs(10*(R[-1]-R[-2]))
            ep=abs(R[-1]-R[-2])     #计算精度
Romberg(a,b,err,func)
print(T)
print(S)
print(C)
print(R)
print(R[-1])









