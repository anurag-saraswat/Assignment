# -*- coding: utf-8 -*-
"""ML_Assignment_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NlcF9Egm1JDfA1I6n7-taj8_caVZ_t-b
"""

# Commented out IPython magic to ensure Python compatibility.
# importing libraries
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
# %matplotlib inline

# Loading Data Set
from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

print(len(x_train),len(x_test))

"""### Data Visualisation"""

# Visualising 10 random sample from training data
indexes = np.random.randint(0, x_train.shape[0], size=10)
images = x_train[indexes]

# plot the 10 mnist digits
plt.figure(figsize=(4, 4))
for i in range(len(indexes)):
    plt.subplot(2, 5, i + 1)
    image = images[i]
    plt.imshow(image, cmap='gray')
    plt.axis('off')

plt.show()
plt.close('all')

"""### Resize and Normalizing Data"""

image_size = x_train.shape[1]
input_size = image_size **2
# resize and normalize
x_train = np.reshape(x_train, [-1, input_size])
x_train = x_train.astype('float32') / 255
x_test = np.reshape(x_test, [-1, input_size])
x_test = x_test.astype('float32') / 255

"""# Importing Libraries"""

#Importing Keras layers 
import keras
from keras.models import Model
from keras.layers import *
from keras import optimizers

# compute the number of labels
num_labels = len(np.unique(y_train))

# Convert labels to One Hot Encoded
num_digits = 10
y_train = keras.utils.to_categorical(y_train, num_digits)
y_test = keras.utils.to_categorical(y_test, num_digits)

"""#1) Varying the number of hidden layers from 0 to 2

## 2 Hidden Layer
"""

# Input Parameters
n_input = 784 # number of features
n_hidden_1 = 100
n_hidden_2 = 100
n_hidden_3 = 100
num_digits = 10

# Total Parameter = 99710

Inp = Input(shape=(784,))
x = Dense(n_hidden_1, activation='relu', name = "Hidden_Layer_1")(Inp)
x = Dense(n_hidden_2, activation='relu', name = "Hidden_Layer_2")(x)
output = Dense(num_digits, activation='softmax', name = "Output_Layer")(x)

model = Model(Inp, output)
print(model.summary())

# Insert Hyperparameters
learning_rate = 0.1
training_epochs = 20
batch_size = 100
sgd = optimizers.SGD(lr=learning_rate)

# Using  Stochastic Gradient Descent as our optimizing methodology
model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])

# Using 10 percent of training as validation data
history1 = model.fit(x_train, y_train,batch_size = batch_size,epochs = training_epochs,verbose = 2,validation_split=0.1)

loss_2, acc_2 = model.evaluate(x_test, y_test, batch_size=batch_size)

"""## 1 Hidden Layer"""

# Input Parameters
n_input = 784 # number of features
n_hidden_1 = 100
num_digits = 10

# Total Parameter = 79510

Inp = Input(shape=(784,))
x = Dense(n_hidden_1, activation='relu', name = "Hidden_Layer_1")(Inp)
output = Dense(num_digits, activation='softmax', name = "Output_Layer")(x)

model = Model(Inp, output)
print(model.summary())

# Insert Hyperparameters
learning_rate = 0.1
training_epochs = 20
batch_size = 100
sgd = optimizers.SGD(lr=learning_rate)

# Using  Stochastic Gradient Descent as our optimizing methodology
model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])

# Using 10 percent of training as validation data
history1 = model.fit(x_train, y_train,batch_size = batch_size,epochs = training_epochs,verbose = 2,validation_split=0.1)

loss_1, acc_1 = model.evaluate(x_test, y_test, batch_size=batch_size)

"""## 0 Hidden Layer"""

# Input Parameters
n_input = 784 # number of features
num_digits = 10

# Total parameter = 7850

Inp = Input(shape=(784,))
output = Dense(num_digits, activation='softmax', name = "Output_Layer")(Inp)
model = Model(Inp, output)
print(model.summary())

# Insert Hyperparameters
learning_rate = 0.1
training_epochs = 20
batch_size = 100
sgd = optimizers.SGD(lr=learning_rate)

# Using  Stochastic Gradient Descent as our optimizing methodology
model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])

# Using 10 percent of training as validation data
history1 = model.fit(x_train, y_train,batch_size = batch_size,epochs = training_epochs,verbose = 2,validation_split=0.1)

loss_0, acc_0 = model.evaluate(x_test, y_test, batch_size=batch_size)



"""## Result"""

print("Accuracy achieved Using 0 Hidden Layer: ", round((acc_0*100),2))
print("Accuracy achieved Using 1 Hidden Layer: ", round((acc_1*100),2))
print("Accuracy achieved Using 2 Hidden Layer: ", round((acc_2*100),2))

"""# 2) Trying sigmoid and relu activation functions for the hidden layer nodes.

## Using Relu
"""

# Input Parameters
n_input = 784 # number of features
n_hidden_1 = 100
n_hidden_2 = 100
n_hidden_3 = 100
num_digits = 10

# Total Parameter = 99710

Inp = Input(shape=(784,))
x = Dense(n_hidden_1, activation='relu', name = "Hidden_Layer_1")(Inp)
x = Dense(n_hidden_2, activation='relu', name = "Hidden_Layer_2")(x)
output = Dense(num_digits, activation='softmax', name = "Output_Layer")(x)

model = Model(Inp, output)

# Insert Hyperparameters
learning_rate = 0.1
training_epochs = 20
batch_size = 100
sgd = optimizers.SGD(lr=learning_rate)

# Using  Stochastic Gradient Descent as our optimizing methodology
model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])

# Using 10 percent of training as validation data
history1 = model.fit(x_train, y_train,batch_size = batch_size,epochs = training_epochs,verbose = 2,validation_split=0.1)

loss_relu, acc_relu = model.evaluate(x_test, y_test, batch_size=batch_size)

"""## Using Sigmoid"""

# Input Parameters
n_input = 784 # number of features
n_hidden_1 = 100
n_hidden_2 = 100
n_hidden_3 = 100
num_digits = 10

# Total Parameter = 99710

Inp = Input(shape=(784,))
x = Dense(n_hidden_1, activation='sigmoid', name = "Hidden_Layer_1")(Inp)
x = Dense(n_hidden_2, activation='sigmoid', name = "Hidden_Layer_2")(x)
output = Dense(num_digits, activation='softmax', name = "Output_Layer")(x)

model = Model(Inp, output)

# Insert Hyperparameters
learning_rate = 0.1
training_epochs = 20
batch_size = 100
sgd = optimizers.SGD(lr=learning_rate)

# Using  Stochastic Gradient Descent as our optimizing methodology
model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])

# Using 10 percent of training as validation data
history1 = model.fit(x_train, y_train,batch_size = batch_size,epochs = training_epochs,verbose = 2,validation_split=0.1)

loss_sigmoid, acc_sigmoid = model.evaluate(x_test, y_test, batch_size=batch_size)

"""## Result"""

print("Accuracy achieved Using Relu activation function for Hidden Layer: ", round((acc_relu*100),2))
print("Accuracy achieved Using Sigmoid activation function for Hidden Layer: ", round((acc_sigmoid*100),2))

"""# 3. Not using any nonlinearity in the network"""

# Input Parameters
n_input = 784 # number of features
n_hidden_1 = 100
n_hidden_2 = 100
n_hidden_3 = 100
num_digits = 10

# Total Parameter = 99710

Inp = Input(shape=(784,))
x = Dense(n_hidden_1, activation='linear', name = "Hidden_Layer_1")(Inp)
x = Dense(n_hidden_2, activation='linear', name = "Hidden_Layer_2")(x)
output = Dense(num_digits, activation='softmax', name = "Output_Layer")(x)

model = Model(Inp, output)

# Insert Hyperparameters
learning_rate = 0.1
training_epochs = 20
batch_size = 100
sgd = optimizers.SGD(lr=learning_rate)

# Using  Stochastic Gradient Descent as our optimizing methodology
model.compile(loss='categorical_crossentropy',optimizer='sgd',metrics=['accuracy'])

# Using 10 percent of training as validation data
history1 = model.fit(x_train, y_train,batch_size = batch_size,epochs = training_epochs,verbose = 2,validation_split=0.1)

loss_linear, acc_linear = model.evaluate(x_test, y_test, batch_size=batch_size)

print("Accuracy achieved Using Linear activation function for Hidden Layer: ", round((acc_linear*100),2))

