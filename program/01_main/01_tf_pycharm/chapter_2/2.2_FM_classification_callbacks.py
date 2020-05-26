#导入包
import numpy as np
import tensorflow as tf
from tensorflow import keras
import os

#导入数据
FM = keras.datasets.fashion_mnist
(x_train_all, y_train_all), (x_test_raw, y_test) = FM.load_data()
x_train_raw, y_train = x_train_all[:50000], y_train_all[:50000]
x_valid_raw, y_valid = x_train_all[50000:], y_train_all[50000:]

#对数据进行标准化

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x_train = scaler.fit_transform( x_train_raw.astype(np.float32).reshape(-1,1)).reshape(-1,28,28)
x_valid = scaler.transform(x_valid_raw.astype(np.float32).reshape(-1,1)).reshape(-1,28,28)
x_test = scaler.transform(x_test_raw.astype(np.float32).reshape(-1,1)).reshape(-1,28,28)

#建立模型
model = keras.models.Sequential()
model.add(keras.layers.Flatten(input_shape = (28,28)))
model.add(keras.layers.Dense(units = 600,activation = 'sigmoid'))
model.add(keras.layers.Dense(units = 400,activation = 'sigmoid'))
model.add(keras.layers.Dense(units = 10,activation = 'softmax'))

model.compile(loss = 'sparse_categorical_crossentropy',
                optimizer = 'adam',
                metrics = ['accuracy'])

logdir = os.path.join('./log_callback')
if not os.path.exists(logdir):
    os.mkdir(logdir)
output_floder = os.path.join(logdir,'tfboard.h5')
callbacks = [
    keras.callbacks.EarlyStopping(monitor='val_loss', patience = 5, min_delta = 1e-2),
    keras.callbacks.ModelCheckpoint(output_floder,save_best_only = True),
    keras.callbacks.TensorBoard(logdir)
]


model.fit(x_train, y_train,
          validation_data = (x_valid,y_valid),
          batch_size=500,
          epochs = 7,
          callbacks = callbacks
         )

model.evaluate(x_test,y_test)

'''
EarlyStopping(~):
    Function:被检测的指标不再改善，则停止训练。
    Augment：
        monitor:Quantity to be monitored.（被检测的指标）
        min_delta:最小变化量
        patience：Number of epochs with no improvement after which training will be stopped.
                （如果指标的变化量数次小于指定的min_delta，则停止训练，patience就是用来指定这个数次到底是多少。）

ModelCheckPoint(~):
    Function:Save the model after every epoch.
    Augment:
        filepath: string, path to save the model file.
        monitor: quantity to monitor.
        save_best_only:如果这个值设为True，那么

TensorBoard：
    Function：使模型的变化可视化
    Augment：
        log_dir: the path of the directory where to save the log files to be parsed by TensorBoard.
                ——保存日志文件的位置

    使用tensorboard的具体步骤：
    1.在命令行中切换到安装了tensorflow的环境中，并输入如下命令：
        tensorboard --logdir=path_to_your_log_filefolder
    2.在浏览器中访问如下端口：localhost:6006


'''





