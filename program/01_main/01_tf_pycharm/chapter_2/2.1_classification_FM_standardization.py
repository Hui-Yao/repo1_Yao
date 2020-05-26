#导入包
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import sklearn
import pandas as pd
import os
import sys
import time
import tensorflow as tf
from tensorflow import keras

# print(tf.__version__)
# print(sys.version_info)
# for module in mpl, np, pd, sklearn, tf, keras:
#     print(module.__name__, module.__version__)

# 加载数据集，输出数据集形状，并将训练集分出一部分为验证集
fashion_mnist = keras.datasets.fashion_mnist
(x_train_all,y_train_all),(x_test,y_test) = fashion_mnist.load_data()
x_train,y_train = x_train_all[:55000],y_train_all[:55000]
x_valid,y_valid = x_train_all[55000:],y_train_all[55000:]

# type(fashion_mnist)
# for i in x_train_all,y_train_all,x_test,y_test:
#     print(i.shape)

# 对数据进行标准化
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

x_train_scaled = scaler.fit_transform(
    x_train.astype(np.float32).reshape(-1, 1)
).reshape(-1, 28, 28)
x_valid_scaled = scaler.transform(
    x_valid.astype(np.float32).reshape(-1, 1)
).reshape(-1, 28, 28)
x_test_scaled = scaler.transform(
    x_test.astype(np.float32).reshape(-1, 1)
).reshape(-1, 28, 28)

# reshape中某个维度设为-1，意为先计算别的维度，最后由别的维度确定这个维度的数值。-1可以出现在任何一个维度上。

# standardscaler这个类只能接受二维数组，所以要将图片先转为二维数组

# StandardScaler.fit_transform():(1)使训练集均值为0，方差为1；并且记住调用该函数的集合的均值与方差，供后面的standardscaler.transform（）使用。
# StandardScaler.transform():使用fit_transform记住的均值与方差，对当前数据集进行转换。

# 训练集调用fit_transform(),验证集与测试集调用transform()而不能调用fit_transform()，因为只有用训练集的均值与方差，擦能真实地反映模型的训练结果。

#构建模型

model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape = (28,28)))    #原始数据是图片，首先要展平成一维向量
model.add(keras.layers.Dense(units = 700,activation = 'relu'))
model.add(keras.layers.Dense(units = 300, activation = 'relu'))
model.add(keras.layers.Dense(units = 10, activation = 'softmax'))

model.compile(loss = 'sparse_categorical_crossentropy',     #如果标签是一个向量，那么就不要sparse，否则就加sparse
              optimizer = 'adam',
              metrics = ['accuracy'] )

#训练（拟合）
history = model.fit(x_train_scaled,y_train,validation_data=(x_valid_scaled,y_valid),batch_size=200, epochs = 10)

#评估
model.evaluate(x_test_scaled,y_test)

#输出训练曲线图
def plot_show(history):
    data = pd.DataFrame(history.history)
    data.plot(figsize = (8,5))
    plt.grid(True)
    plt.gca().set_ylim(0,1)
    plt.show()
plot_show(history)