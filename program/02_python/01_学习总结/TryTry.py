# -*- coding: utf-8 -*-

# 分类问题，变量有两个，通过两个变量得到标签值

import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt


def loaddata(filename):
    """
    加载原始数据集
    通过原始数据集，返回列名分别为（x0,x1,x2）和（label）的两个dataframe
    """
    dataSet = pd.read_table(filename, header=None)#得到的是dataframe类型的数据
    dataSet.columns = ['X1', 'X2', 'label']#给各列添加列名
    dataSet.insert(0, 'X0', 1)#添加一个x0，方便hΘ(x)的表示
    columns = [i for i in dataSet.columns if i != 'label']    #过滤得到dataframe的各个变量名
    data_x = dataSet[columns]    #得到列名为x0,x1,x2的dataframe
    # print('dataxxxx',data_x)
    data_y = dataSet[['label']]    #得到y的series
    return data_x,data_y


#sigmoid函数
def sigmoid(y):
    s = 1.0/(1.0+np.exp(-y))
    return s

def cost(xMat,weights,yMat):
    """
    计算损失函数
    xMat: 特征数据-矩阵
    weights: 参数
    yMat: 标签数据-矩阵
    return: 损失函数
    """
    m, n = xMat.shape
    hypothesis = sigmoid(np.dot(xMat, weights))  # 预测值
    cost = (-1.0 / m) * np.sum(yMat.T * np.log(hypothesis) + (1 - yMat).T * np.log(1 - hypothesis))  # 损失函数
    return cost



def BGD_LR(data_x,data_y,alpha=0.1,maxepochs=10000,epsilon=1e-4):
    """
    使用批量梯度下降法BGD求解逻辑回归
    data_x: 特征数据
    data_y: 标签数据
    aplha: 步长，该值越大梯度下降幅度越大
    maxepochs: 最大迭代次数
    epsilon: 损失精度
    return: 模型参数
    """
    starttime = time.time()
    xMat = np.mat(data_x)   #得到一个100×3的特征矩阵
    # print('xmatttt:',xMat.shape)
    yMat = np.mat(data_y)   #得到一个100×1的标签矩阵
    m,n = xMat.shape    #m = 100,n = 3
    weights = np.ones((n,1)) #初始化模型参数 , 创建一个元素全为1的3×1的数组
    # print('weights的类型：',type(weights))
    epochs_count = 0
    loss_list = []
    epochs_list = []

    while epochs_count < maxepochs:#无限迭代
        loss = cost(xMat,weights,yMat) #上一次损失值
        hypothesis = sigmoid(np.dot(xMat,weights)) #预测值
        # print('hypothesisssssss:',type(hypothesis))
        error = hypothesis -yMat #预测值与实际值误差
        grad = ( 1.0/m)*np.dot(xMat.T,error) #损失函数的梯度
        # print('grad的值',grad)
        last_weights = weights #上一轮迭代的参数 ， 这个参数没有用到
        weights = weights - alpha*grad #参数更新
        loss_new = cost(xMat,weights,yMat)#当前损失值
        print(loss_new)
        if abs(loss_new-loss)<epsilon:#终止条件，如果达到了允许的误差范围，则终止迭代
            break
        loss_list.append(loss_new)
        epochs_list.append(epochs_count)
        '''
        两个列表分别记录所有的误差值与对应的误差，用于绘制图像（迭代次数与误差值关系的图像？）
        '''
        epochs_count += 1
    print(loss_new)
    print("批量梯度下降算法耗时：", time.time() - starttime)
    print('迭代到第{}次，结束迭代！'.format(epochs_count))
    plt.plot(epochs_list,loss_list)
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.show()
    return weights



if __name__ == '__main__':
    data_x,data_y = loaddata('/home/hui/program/machine_learning/gradient_descent_test/testSet.txt')
    weights_bgd = BGD_LR(data_x, data_y, alpha=0.1, maxepochs=10000, epsilon=1e-4)
    # weights_sgd = SGD_LR(data_x, data_y, alpha=0.1, maxepochs=10000, epsilon=1e-4)
    # weights_mbgd = MBGD_LR(data_x, data_y, alpha=0.1, batch_size=3, maxepochs=10000,epsilon=1e-4)

