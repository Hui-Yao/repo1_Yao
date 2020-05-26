from tensorflow import keras
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_california_housing

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

#构建模型
model = keras.models.Sequential()
model.add(keras.layers.Dense(units=50,activation='relu', input_shape=x_train.shape[1:]))
model.add(keras.layers.Dense(20, activation='relu'))
model.add(keras.layers.Dense(1))

model.compile(loss='mse', optimizer='adam')

history = model.fit(x_train, y_train, validation_data=(x_valid, y_valid), batch_size=500, epochs=20)

model.evaluate(x_test, y_test)

def plot_learning_curves(history):
    pd.DataFrame(history.history).plot(figsize=(8, 5))
    plt.grid(True)
    plt.gca().set_ylim(0, 2)
    plt.show()
plot_learning_curves(history)





