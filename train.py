import numpy as np
import keras
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras import optimizers

X = np.random.randn(100,2)
y = 2*X[:,0] + 3*X[:,1] + 4 + .2*np.random.randn(100) #noise added

#Building model
model = Sequential([Dense(1, input_shape = (2,), activation = 'linear')])

#gradient descent optimizer and loss function
sgd = optimizers.SGD(lr = 0.1)
model.compile(loss = 'mse', optimizer = sgd)

class PrintDot(keras.callbacks.Callback):
	def on_epoch_end(self, epoch, logs):
		if epoch % 100 == 0:
			print('')
		print('.', end = ' ')

#Train the model
model.fit(X,y,epochs = 1000, validation_split= 0.2, verbose =0, batch_size = 2, callbacks = [PrintDot()])

print(model.get_weights())
