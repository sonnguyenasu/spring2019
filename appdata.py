from __future__ import division, absolute_import, print_function
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

from tensorflow import keras
from tensorflow.keras import layers

import seaborn as sns
import mysql.connector as mc

cnx = mc.connect(user = 'root', database = 'hello', password = 'password')
cursor = cnx.cursor()
query = 'SELECT * FROM AppData'
cursor.execute(query)

res = (cursor.fetchall())
column_names = ['AppId','rating','reviews','installs','size','price','Business','Comics','Communication','Dating','Other']
res = pd.DataFrame(res, columns = column_names)
res = res.dropna()
train_data = res.sample(frac = 0.8, random_state = 0)
test_data = res.drop(train_data.index)

'''
sns.pairplot(train_data[['rating','reviews','size','installs']], diag_kind = 'kde')
plt.show()
'''
train_data.pop('price')
test_data.pop('price')
train_label = train_data.pop('reviews')
test_label = test_data.pop('reviews')

train_stats = train_data.describe()
train_stats = train_stats.transpose()

print(train_stats)
def norm(x):
	return (x - train_stats['mean'])/(train_stats['std'])

normed_test = norm(test_data)
normed_train = norm(train_data)

model = keras.Sequential([
	layers.Dense(64, activation = tf.nn.relu, input_shape = [len(train_data.keys())]),
	layers.Dense(64, activation = tf.nn.relu),
	layers.Dense(1)
])
model.compile(loss = 'mean_squared_error', optimizer = keras.optimizers.RMSprop(0.01), metrics = ['mean_absolute_error', 'mean_squared_error'])

class PrintDot(keras.callbacks.Callback):
	def on_epoch_end(self, epoch, logs):
		if epoch % 100 == 0:
			print('')
		print('.', end = ' ')
#early_stop = keras.callbacks.EarlyStopping(monitor = 'val_loss', patience = 10)
history = model.fit(normed_train, train_label, epochs = 1000, validation_split = 0.2, verbose = 0, callbacks = [PrintDot()])

def plot_history(history):
	hist = pd.DataFrame(history.history)
	hist['epoch'] = history.epoch
	plt.figure()
	plt.xlabel('#epoch')
	plt.ylabel('mean_absolute_error')
	plt.plot(hist['epoch'], hist['mean_absolute_error'], label = 'Train Error')
	plt.plot(hist['epoch'], hist['val_mean_absolute_error'], label = 'Val Error')
	plt.legend()
	plt.figure()
	plt.xlabel('#epoch')
	plt.ylabel('mean_squared_error')
	plt.plot(hist['epoch'], hist['mean_squared_error'], label = 'Train Error')
	plt.plot(hist['epoch'], hist['val_mean_squared_error'], label = 'Val Error')
	plt.legend()
	#plt.show()
plot_history(history)


test_prediction = model.predict(normed_test).flatten()
plt.figure()

plt.scatter(test_label, test_prediction)
plt.xlabel('True')
plt.ylabel('Predict')
plt.axis('square')
plt.axis('equal')
plt.xlim([0, plt.xlim()[1]])
plt.ylim([0, plt.ylim()[1]])
plt.plot([-10000, 1000000000], [-10000, 1000000000])

print(model.evaluate(normed_test, test_label))

plt.figure()
error = test_prediction - test_label
plt.hist(error, bins = 10000)
plt.show()