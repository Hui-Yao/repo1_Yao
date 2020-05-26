'''如何使用sklearn的超参数搜索？
（1）定义keras模型函数（将要搜索的超参数作为函数的参数），使用KerasRegressor类将keras模型转换为sklearn模型。
（2）以字典的形式构建超参数的分布（注意字典中代表参数的‘key’要与1中函数的参数相同）
（3）调用sklearn.model_selction中的Randomizedsearchcv制作一个模型训练器（可以这么理解？），
    进行训练，从村联结果中选择最好模型，保存下来
'''
from tensorflow import keras
from matplotlib import pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import RandomizedSearchCV

houses = fetch_california_housing()
# print(houses.data.shape)
# print(houses.target.shape)
# print(houses.DESCR)

x_train_all, x_test_raw, y_train_all, y_test = train_test_split(houses.data, houses.target, random_state=1)
x_train_raw, x_valid_raw, y_train, y_valid = train_test_split(x_train_all, y_train_all, random_state=2)

# for i in [x_train_raw, x_valid_raw, x_test_raw]:
#     print(i.shape)

ss = StandardScaler()
x_train = ss.fit_transform(x_train_raw)
x_valid = ss.transform(x_valid_raw)
x_test = ss.transform(x_test_raw)

def kr_model(hidden_layers = 3, layer_size = 30, learn_rate = 0.01):
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(units=layer_size, activation='relu',input_shape = x_train.shape[1:]))
    for i in range(hidden_layers-1):
        model.add(keras.layers.Dense(units=layer_size, activation='relu',input_shape = x_train.shape[1:]))
    model.add(keras.layers.Dense(1))
    optimizer = keras.optimizers.SGD(learn_rate)
    #需要在外部自定义optimizer，然后在optimizer中设置learn_rate
    model.compile(loss = 'mse', optimizer=optimizer)
    return model

sk_model = KerasRegressor(build_fn = kr_model)
sk_model.fit(x_train, y_train,
             validation_data=(x_valid, y_valid),
             epochs = 11,
             )

from scipy.stats import reciprocal
para_range = {'hidden_layers':[1, 2, 3, 4],
              'layer_size':np.arange(1,100),
              'learn_rate':reciprocal(1e-4,1e-2),}

#这个para_range中的参数要与keras模型函数中的参数相同，因为最后调用的还是自己构建keras模型函数。


random_search_cv = RandomizedSearchCV(sk_model, para_range,
                                      n_iter=10, n_jobs = 1, cv = 3)
#n_iter:保存的参数组的组数  n_jobs:并行训练的模型个数
#cross_validation机制：将原来的训练集分为n份，其中n-1份用来训练，1份当做验证集，cv就是用来指定n的值。
random_search_cv.fit(x_train, y_train,
                     validation_data = (x_valid, y_valid),
                     batch_size = 500, epochs = 10,
                     callbacks = [keras.callbacks.EarlyStopping(patience=3, min_delta=1e-3 )])

#
print(random_search_cv.best_params_) #输出最好的参数
print(random_search_cv.best_score_)  #输出最好的得分
print(random_search_cv.best_estimator_) #输出最好的模型

model = random_search_cv.best_estimator_.model #调用最好的模型
model.evaluate(x_test, y_test)