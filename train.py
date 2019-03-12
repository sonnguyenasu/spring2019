import numpy as np
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

#Train the model
model.fit(X,y,epochs = 100, batch_size = 2)

print(model.get_weights())
