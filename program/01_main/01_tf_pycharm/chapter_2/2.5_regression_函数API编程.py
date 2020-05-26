#导入包
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import tensorflow as tf
from tensorflow import keras

'''
wide and deep 模型是将wide模型（所有稀疏特征直接连接到输出神经元）和deep模型（DNN）结合起来，可用于分类问题也可用于回归问题。

其中的一些概念：
稀疏特征（sparse feature）：只能从有限特定的值中取值。比如性别只能从男女中选择。职业也只能在一些特定值中选取。
                          稀疏特征可以用one-hot表示。
密集特征（dense feature）:用向量来表示。每个特征都都用向量来表示，特征间的差距可以由向量间的差距表示（男-女 = 国王-王后）。
                            

稀疏特征密集化（dense embeddings）：将稀疏特征表示为密集特征，比如word2rec算法。

'''


#分成数据集和测试集
housing = fetch_california_housing()
# print(housing.data.shape)

x_train_all, x_test_raw, y_train_all, y_test = train_test_split(
    housing.data, housing.target, random_state = 7)
x_train_raw, x_valid_raw, y_train, y_valid = train_test_split(
    x_train_all, y_train_all, random_state = 11)

#对数据进行标准化处理
sca = StandardScaler()
x_train = sca.fit_transform(x_train_raw)
x_valid = sca.transform(x_valid_raw)
x_test = sca.transform(x_test_raw)

model = keras.models.Sequential()

input = keras.layers.Input(shape = x_train.shape[1:])
hidden1 = keras.layers.Dense(30, activation = 'relu')(input)
hidden2 = keras.layers.Dense(30, activation = 'relu')(hidden1)

concate = keras.layers.concatenate([input, hidden2])    #

output = keras.layers.Dense(1)(concate)

model = keras.models.Model(inputs = [input],
                           outputs = [output])



model.compile(loss = 'mean_squared_error', optimizer = 'adam')
#因为是回归模型，所以判断模型好坏的标准就是均方差的大小，而不需要加上评价标准 metrics = ['accuracy']

history = model.fit(x_train, y_train,
                    validation_data = (x_valid, y_valid),
                    callbacks = [keras.callbacks.EarlyStopping(patience = 5, min_delta = 1e-3)],
                    epochs = 10)

model.evaluate(x_train, y_train, verbose = False)

def plot_learning_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 2)
    plt.show()
plot_learning_curves(history)











