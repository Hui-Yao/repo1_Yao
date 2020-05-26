#导入包
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import tensorflow as tf
from tensorflow import keras

#分成数据集和测试集
housing = fetch_california_housing()
# print(housing.data.shape)

x_train_all, x_test_raw, y_train_all, y_test = train_test_split(
    housing.data, housing.target, random_state = 7)
x_train_raw, x_valid_raw, y_train, y_valid = train_test_split(
    x_train_all, y_train_all, random_state = 11)

'''
train_test_split方法默认是将集合分为3:1；
对于同一组数据，设置相同random_state值，则每次分出来的结果是一样的。
'''

#对数据进行标准化处理
sca = StandardScaler()
x_train = sca.fit_transform(x_train_raw)
x_valid = sca.transform(x_valid_raw)
x_test = sca.transform(x_test_raw)

model = keras.models.Sequential()

model.add(keras.layers.Dense(8,activation='relu', input_shape = x_train.shape[1:]))
model.add(keras.layers.Dense(1))

model.compile(loss = 'mean_squared_error', optimizer = 'adam')
#因为是回归模型，所以判断模型好坏的标准就是均方差的大小，而不需要加上评价标准 metrics = ['accuracy']

history = model.fit(x_train, y_train,
          validation_data = (x_valid, y_valid),
          callbacks = [keras.callbacks.EarlyStopping(patience = 5, min_delta = 1e-3)],
          epochs = 20)

model.evaluate(x_train, y_train, verbose = False)

def plot_learning_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 2)
    plt.show()
plot_learning_curves(history)












