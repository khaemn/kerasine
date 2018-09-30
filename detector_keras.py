# https://rosettacode.org/wiki/Poker_hand_analyser
from keras.models import Sequential
from keras.layers import Dense, Activation
from keras.utils import plot_model
from keras.optimizers import SGD

import matplotlib.pyplot as plt
import numpy as np

# fix random seed for reproducibility
seed = 7
np.random.seed(seed)
np.set_printoptions(precision=2, suppress=True)

inputFilename = "trainingdata.txt"
modelFile = 'models/ololo.h5'

dataset = np.loadtxt(inputFilename, delimiter=",")
# split into input (X) and output (Y) variables
X = dataset[:,:10]
Y = dataset[:,10:]

print("First X:", X[0])
print("First Y:", Y[0])

test =     np.array([[1,10, 1,11, 1,13, 1,12, 1, 1],
                     [2,13, 2, 1,4,4,1,5,2,11]])

expected = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1,0,0,0,0,0,0,0,0,0]])

print("Test: ", test)
print("Expect: ",expected)


model = Sequential()

model.add(Dense(10, input_dim=10, activation='tanh'))
#model.add(Dense(10, activation='tanh'))

model.add(Dense(10, activation='sigmoid'))

sgd = SGD(lr=0.1)

model.compile(loss='mean_squared_error', metrics=['accuracy' ], optimizer=sgd)

model.load_weights(modelFile)

history = model.fit(X, Y, batch_size=1, epochs=10)

model.save_weights(modelFile)

# list all data in history
print(history.history.keys())

# summarize history for accuracy
plt.plot(history.history['binary_accuracy'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# summarize history for loss
plt.plot(history.history['loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

print("\n\n\nExpected:\n", expected)

print("\nPrediction: \n", model.predict(test))

