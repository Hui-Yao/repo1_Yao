#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Author = "Hui_Yao"

import time
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def loaddata(path):
    '''
    加载原始数据，并对数据进行处理
    :param path: 文件所在位置
    :return: 特征数据-data_x,实际值-data_y
    '''
    dataset = pd.read_table(path,header=None) #dataset是一个dataframe
    dataset.columns = ['x1','x2','label']
    dataset.insert(0,'x0',1)    #插入x0，便于假设函数的表示
    # print(dataset)
    feature_columns = [i for i in dataset.columns if i != 'label']
    data_x = dataset[feature_columns]
    data_y = dataset['label']
    return data_x,data_y

def sigmoid(z):
    '''
    联系函数，保证模型的输出值在0与1之间
    :param z:
    :return: 经联系函数转换后的值
    '''
    return 1/1+np.exp(-z)

def cost_function(xMat,yMat,origin):
    '''

    :param xMat:
    :param yMat:
    :param origin:
    :return:
    '''
    m,n = xMat.shape
    hypothesis = sigmoid(np.dot(xMat,origin))
    cost = (-1/m)*(yMat*np.log(hypothesis)+(1-yMat)*np.log(1-hypothesis))
    return cost

def BGD(path,):
    data_x,data_y = loaddata(path)
    xMat = np.mat(data_x)
    yMat = np.mat(data_y)
    m,n = xMat.shape
    weights = np.array([1,1,1])






loaddata('/home/hui/program/machine_learning/gradient_descent_test/testSet.txt')




