#导入包
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tensorflow import keras

# 加载数据集，输出数据集形状，并将训练集分出一部分为验证集
fashion_mnist = keras.datasets.fashion_mnist
(x_train_all,y_train_all),(x_test,y_test) = fashion_mnist.load_data()
x_train,y_train = x_train_all[:55000],y_train_all[:55000]
x_valid,y_valid = x_train_all[55000:],y_train_all[55000:]

# 数据处理
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


# 构建模型
# 批归一化：将对数据进行诡异化地思想引入到神经网络中，将每一层地输出进行归一化，能缓解梯度消失，能使函数更容易收敛；但是会加大计算量,但是模型的训练速度是变快了的
# 在具体地某一层后加上 model.add(keras.layers.BatchNormalization())

model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape=(28, 28)))
for i in [400, 400, 300, ]:
    model.add(keras.layers.Dense(units=i, activation='relu'))
    model.add(keras.layers.BatchNormalization())

    """也可以将activation加在批归一化之后（这种更好），形式如下：
    model.add(keras.layers.Dense(100))
    model.add(keras.layers.BatchNormalization())
    model.add(keras.layers.Activation('relu'))
    """
model.add(keras.layers.Dense(units=10, activation='softmax'))

model.compile(loss='sparse_categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

history = model.fit(x_train_scaled, y_train, validation_data=(x_valid_scaled, y_valid), batch_size=5000, epochs=10)



'''
selu : 可以实现归一化地激活函数
selu运行速度比relu慢，但是在这个例子中正确率提高了5个百分点。

AlphaDropout: 1. 均值和方差不变 2. 归一化性质也不变
Alpha Dropout是一种保持输入均值和方差不变的Dropout，该层的作用是通过缩放和平移使得在dropout时也保持数据的自规范性。
Alpha Dropout与SELU激活函数配合较好。
'''
model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape = (28,28)))
for i in [300, 300, 300,]:
    model.add(keras.layers.Dense(units = i, activation = 'relu'))
    model.add(keras.layers.AlphaDropout(rate=0.5))    #直接写0.5也行
# model.add(keras.layers.Dropout(rate=0.5))

model.add(keras.layers.Dense(units = 10, activation = 'softmax'))

model.compile(loss = 'sparse_categorical_crossentropy',
              optimizer = 'adam',
              metrics = ['accuracy'] )

history = model.fit(x_train_scaled,y_train,validation_data=(x_valid_scaled,y_valid),batch_size=5000, epochs = 10)

#绘制训练曲线图
def plot_show(history):
    data = pd.DataFrame(history.history)
    data.plot(figsize = (8,5))
    plt.grid(True)
    plt.gca().set_ylim(0,2)
    plt.show()
plot_show(history)


