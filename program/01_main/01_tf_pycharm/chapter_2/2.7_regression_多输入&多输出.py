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

#对数据进行标准化处理
sca = StandardScaler()
x_train = sca.fit_transform(x_train_raw)
x_valid = sca.transform(x_valid_raw)
x_test = sca.transform(x_test_raw)

#多输入

#搭建模型
input_wide = keras.layers.Input(shape = [5])
input_deep = keras.layers.Input(shape = [6])

hidden1 = keras.layers.Dense(30, activation = 'relu')(input_deep)
hidden2 = keras.layers.Dense(30, activation = 'relu')(hidden1)

concate = keras.layers.concatenate([input_wide, hidden2])

output = keras.layers.Dense(1)(concate)

model = keras.models.Model(inputs = [input_wide,input_deep],
                          outputs = [output])

model.compile(loss = 'mse', optimizer = 'sgd', )


#模型从构建到编译，都与实际的数据无关。在fit之前，都可以对原本的数据进行操作，如分割等。
x_train_wide, x_train_deep = x_train[:,:5], x_train[:,2:]
x_valid_wide, x_valid_deep = x_valid[:,:5], x_valid[:,2:]
x_test_wide, x_test_deep = x_test[:,:5], x_test[:,2:]

history = model.fit([x_train_wide, x_train_deep], y_train,
          validation_data = ([x_valid_wide, x_valid_deep], y_valid),
          epochs = 10)

#多输入&多输出
#多个输入与输出分别都要用中括号括起来，使输入与输出都只有一个项

#搭建模型
input_wide = keras.layers.Input(shape = [5])
input_deep = keras.layers.Input(shape = [6])

hidden1 = keras.layers.Dense(30, activation = 'relu')(input_deep)
hidden2 = keras.layers.Dense(30, activation = 'relu')(hidden1)

concate = keras.layers.concatenate([input_wide, hidden2])

output1 = keras.layers.Dense(1)(concate)
output2 = keras.layers.Dense(1)(hidden2)

model = keras.models.Model(inputs = [input_wide,input_deep],
                          outputs = [output1, output2])

model.compile(loss = 'mse', optimizer = 'sgd', )


#模型从构建到编译，都与实际的数据无关。在fit之前，都可以对原本的数据进行操作，如分割等。
x_train_wide, x_train_deep = x_train[:,:5], x_train[:,2:]
x_valid_wide, x_valid_deep = x_valid[:,:5], x_valid[:,2:]
x_test_wide, x_test_deep = x_test[:,:5], x_test[:,2:]

history = model.fit([x_train_wide, x_train_deep], [y_train,y_train],
          validation_data = ([x_valid_wide, x_valid_deep], [y_valid, y_valid]),
          epochs = 10)

model.evaluate([x_test_wide, x_test_deep], [y_test, y_test], verbose = False)

def plot_learning_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 2)
    plt.show()
plot_learning_curves(history)






