#!/usr/bin/env python
# coding: utf-8

# # Implementing a handwritten digit classifier using a neural network

# ## Data Preparation

# In[1]:


# importing libraries
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt


# In[2]:


# Loading Data Set
from keras.datasets import mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()


# In[3]:


#Creating Flipped Data Set

x_train_flipped = 255- x_train
x_test_flipped = 255 - x_test


# In[4]:


#Creating Mixed of Flipped and corresponding orignal image

a =  x_train[:int(x_train.shape[0]*0.5)]
b =  x_train_flipped[:int(x_train_flipped.shape[0]*0.5)]
x_train_mix = np.append(a,b,axis=0)

a =  x_test[:int(x_test.shape[0]*0.5)]
b =  x_test_flipped[:int(x_test_flipped.shape[0]*0.5)]
x_test_mix = np.append(a,b,axis=0)

y_train_mix = np.append(y_train[:int(y_train.shape[0]*0.5)],y_train[:int(y_train.shape[0]*0.5)],axis=0)
y_test_mix = np.append(y_test[:int(y_test.shape[0]*0.5)],y_test[:int(y_test.shape[0]*0.5)],axis=0)


# ### Data Visualisation

# In[5]:


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


# In[6]:


# Visualising 10 random sample from flipped training data
indexes = np.random.randint(0, x_train_flipped.shape[0], size=10)
images = x_train_flipped[indexes]

# plot the 10 mnist digits
plt.figure(figsize=(4, 4))
for i in range(len(indexes)):
    plt.subplot(2, 5, i + 1)
    image = images[i]
    plt.imshow(image, cmap='gray')
    plt.axis('off')

plt.show()
plt.close('all')


# ### Resize and Normalizing Data
# 
# 

# In[7]:


image_size = x_train.shape[1]
input_size = image_size **2
# resize and normalize
x_train = np.reshape(x_train, [-1, input_size])
x_train = x_train.astype('float32') / 255
x_test = np.reshape(x_test, [-1, input_size])
x_test = x_test.astype('float32') / 255

x_train_flipped = np.reshape(x_train_flipped, [-1, input_size])
x_train_flipped = x_train_flipped.astype('float32') / 255
x_test_flipped = np.reshape(x_test_flipped, [-1, input_size])
x_test_flipped = x_test_flipped.astype('float32') / 255


x_train_mix = np.reshape(x_train_mix, [-1, input_size])
x_train_mix = x_train_mix.astype('float32') / 255
x_test_mix = np.reshape(x_test_mix, [-1, input_size])
x_test_mix = x_test_mix.astype('float32') / 255


# ## Designing Model Architecture using keras

# In[8]:


#Importing Keras layers 

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.utils import to_categorical, plot_model
from keras.callbacks import History 


# In[9]:


# compute the number of labels
num_labels = len(np.unique(y_train))


# In[10]:


# convert to one-hot vector
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

y_train_mix = to_categorical(y_train_mix)
y_test_mix = to_categorical(y_test_mix)


# In[11]:


# model is a 3-layer MLP with ReLU and dropout after each layer
#Both the first and second MLP layers are identical in nature with 256 units each, followed by relu activation and dropout.

# setting network parameters
hidden_units = 256
dropout = 0.45


model = Sequential()
model.add(Dense(hidden_units, input_dim=input_size))
model.add(Activation('relu'))
model.add(Dropout(dropout))
model.add(Dense(hidden_units))
model.add(Activation('relu'))
model.add(Dropout(dropout))
model.add(Dense(num_labels))
model.add(Activation('softmax'))


# In[12]:


#Compilation of model
#Using categorical_crossentropy as the loss function

model.compile(loss='categorical_crossentropy', optimizer='SGD',metrics=['accuracy'])


# ## Model Fitting

# ### For Batch Size 256

# In[13]:


#Setting Batch Size
batch_size = 256

history = History()
model.fit(x_train, y_train, epochs=20, batch_size=batch_size ,callbacks=[history])

loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy with batch size 256: %.1f%%" % (100.0 * acc))

loss_256 = history.history['loss']


# In[14]:


#Setting Batch Size for flipped image
batch_size = 256

history = History()
model.fit(x_train_flipped, y_train, epochs=20, batch_size=batch_size ,callbacks=[history])

loss, acc = model.evaluate(x_test_flipped, y_test, batch_size=batch_size)
print("\nTest accuracy with batch size 256: %.1f%%" % (100.0 * acc))

loss_256_flipped = history.history['loss']


# In[15]:


#Setting Batch Size for mix sample
batch_size = 256

history = History()
model.fit(x_train_mix, y_train_mix, epochs=20, batch_size=batch_size ,callbacks=[history])

loss, acc = model.evaluate(x_test_mix, y_test_mix, batch_size=batch_size)
print("\nTest accuracy with batch size 256: %.1f%%" % (100.0 * acc))

loss_256_mix = history.history['loss']


# ### For Batch Size 128

# In[16]:


#Setting Batch Size
batch_size = 128

history = History()
model.fit(x_train, y_train, epochs=20, batch_size=batch_size ,callbacks=[history])

loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy with batch size 128: %.1f%%" % (100.0 * acc))

loss_128 = history.history['loss']


# In[17]:


#Setting Batch Size for flipped image
batch_size = 128

history = History()
model.fit(x_train_flipped, y_train, epochs=20, batch_size=batch_size ,callbacks=[history])

loss, acc = model.evaluate(x_test_flipped, y_test, batch_size=batch_size)
print("\nTest accuracy with batch size 128: %.1f%%" % (100.0 * acc))

loss_128_flipped = history.history['loss']


# In[18]:


#Setting Batch Size for mix sample
batch_size = 128

history = History()
model.fit(x_train_mix, y_train_mix, epochs=20, batch_size=batch_size ,callbacks=[history])

loss, acc = model.evaluate(x_test_mix, y_test_mix, batch_size=batch_size)
print("\nTest accuracy with batch size 128: %.1f%%" % (100.0 * acc))

loss_128_mix = history.history['loss']


# ### For Batch Size 64

# In[19]:


#Setting Batch Size
batch_size = 64

history = History()
model.fit(x_train, y_train, epochs=20, batch_size=batch_size ,callbacks=[history])

loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy with batch size 64: %.1f%%" % (100.0 * acc))

loss_64 = history.history['loss']


# In[20]:


#Setting Batch Size for flipped image
batch_size = 64

history = History()
model.fit(x_train_flipped, y_train, epochs=20, batch_size=batch_size ,callbacks=[history])

loss, acc = model.evaluate(x_test_flipped, y_test, batch_size=batch_size)
print("\nTest accuracy with batch size 64: %.1f%%" % (100.0 * acc))

loss_64_flipped = history.history['loss']


# In[21]:


#Setting Batch Size for mix sample
batch_size = 64

history = History()
model.fit(x_train_mix, y_train_mix, epochs=20, batch_size=batch_size ,callbacks=[history])

loss, acc = model.evaluate(x_test_mix, y_test_mix, batch_size=batch_size)
print("\nTest accuracy with batch size 64: %.1f%%" % (100.0 * acc))

loss_64_mix = history.history['loss']


# ### For Batch Size 32

# In[22]:


#Setting Batch Size
batch_size = 32

history = History()
model.fit(x_train, y_train, epochs=20, batch_size=batch_size ,callbacks=[history])

loss, acc = model.evaluate(x_test, y_test, batch_size=batch_size)
print("\nTest accuracy with batch size 32: %.1f%%" % (100.0 * acc))

loss_32 = history.history['loss']


# In[23]:


#Setting Batch Size for flipped image
batch_size = 32

history = History()
model.fit(x_train_flipped, y_train, epochs=20, batch_size=batch_size ,callbacks=[history])

loss, acc = model.evaluate(x_test_flipped, y_test, batch_size=batch_size)
print("\nTest accuracy with batch size 32: %.1f%%" % (100.0 * acc))

loss_32_flipped = history.history['loss']


# In[24]:


#Setting Batch Size for mix sample
batch_size = 32

history = History()
model.fit(x_train_mix, y_train_mix, epochs=20, batch_size=batch_size ,callbacks=[history])

loss, acc = model.evaluate(x_test_mix, y_test_mix, batch_size=batch_size)
print("\nTest accuracy with batch size 32: %.1f%%" % (100.0 * acc))

loss_32_mix = history.history['loss']


# ### Comparison

# In[40]:


plt.style.use("seaborn")
plt.xlabel("Epoch")
plt.ylabel("Error")
plt.title("Comparison of reduction in Error(In Orignal Sample)")

x = [i for i in range(1,21)]
plt.xticks(np.arange(min(x), max(x)+1, 1.0))

plt.plot(x,loss_32,label="Batch Size 32")
plt.plot(x,loss_64,label="Batch Size 64")
plt.plot(x,loss_128,label="Batch Size 128")
plt.plot(x,loss_256,label="Batch Size 256")

plt.legend()

plt.show()


# In[39]:


# Comparision in case of Flipped images
plt.style.use("seaborn")
plt.xlabel("Epoch")
plt.ylabel("Error")
plt.title("Comparison of reduction in Error(In Flipped Sample)")

x = [i for i in range(1,21)]
plt.xticks(np.arange(min(x), max(x)+1, 1.0))

plt.plot(x,loss_32_flipped,label="Batch Size 32")
plt.plot(x,loss_64_flipped,label="Batch Size 64")
plt.plot(x,loss_128_flipped,label="Batch Size 128")
plt.plot(x,loss_256_flipped,label="Batch Size 256")

plt.legend()
plt.show()


# In[38]:


plt.style.use("seaborn")
plt.xlabel("Epoch")
plt.ylabel("Error")
plt.title("Comparison of reduction in Error(In Mixed Sample)")

x = [i for i in range(1,21)]
plt.xticks(np.arange(min(x), max(x)+1, 1.0))

plt.plot(x,loss_32_mix,label="Batch Size 32")
plt.plot(x,loss_64_mix,label="Batch Size 64")
plt.plot(x,loss_128_mix,label="Batch Size 128")
plt.plot(x,loss_256_mix,label="Batch Size 256")

plt.legend()

plt.show()


# In[37]:


plt.style.use("seaborn")
plt.xlabel("Epoch")
plt.ylabel("Error")
plt.title("Comparison of reduction in Error for batch size 32")

x = [i for i in range(1,21)]
plt.xticks(np.arange(min(x), max(x)+1, 1.0))

plt.plot(x,loss_32,label="Orignal")
plt.plot(x,loss_32_flipped,label="Flipped")
plt.plot(x,loss_32_mix,label="Mix")


plt.legend()

plt.show()


# In[36]:


plt.style.use("seaborn")
plt.xlabel("Epoch")
plt.ylabel("Error")
plt.title("Comparison of reduction in Error for batch size 64")

x = [i for i in range(1,21)]
plt.xticks(np.arange(min(x), max(x)+1, 1.0))

plt.plot(x,loss_64,label="Orignal")
plt.plot(x,loss_64_flipped,label="Flipped")
plt.plot(x,loss_64_mix,label="Mix")


plt.legend()

plt.show()


# In[35]:


plt.style.use("seaborn")
plt.xlabel("Epoch")
plt.ylabel("Error")
plt.title("Comparison of reduction in Error for batch size 128")

x = [i for i in range(1,21)]
plt.xticks(np.arange(min(x), max(x)+1, 1.0))

plt.plot(x,loss_128,label="Orignal")
plt.plot(x,loss_128_flipped,label="Flipped")
plt.plot(x,loss_128_mix,label="Mix")


plt.legend()

plt.show()


# In[34]:


plt.style.use("seaborn")
plt.xlabel("Epoch")
plt.ylabel("Error")
plt.title("Comparison of reduction in Error for batch size 256")

x = [i for i in range(1,21)]
plt.xticks(np.arange(min(x), max(x)+1, 1.0))

plt.plot(x,loss_256,label="Orignal")
plt.plot(x,loss_256_flipped,label="Flipped")
plt.plot(x,loss_256_mix,label="Mix")



plt.legend()

plt.show()


# In[ ]:




