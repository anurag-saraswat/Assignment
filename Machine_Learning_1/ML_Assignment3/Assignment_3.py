#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn


# # Preparing Data

# Predicting Death Event or heart failure using feautres such as platelets , ejection fraction

# In[2]:


data = pd.read_csv('./DataSet/heart_failure_clinical_records_dataset.csv')
data = data.sample(frac=1)
data = data.drop(columns=["diabetes", "high_blood_pressure","sex", "smoking" ,"anaemia"])
print("Data Set")
print(data.head)


# In[3]:


# 70-30 Split

Data_Train_70 = data.iloc[:int(len(data)*0.7)]
Data_Test_30 = data.iloc[int(len(data)*0.7):]

y_train_70 = np.array(Data_Train_70["DEATH_EVENT"])
x_train_70 = np.array(Data_Train_70.drop(columns=["DEATH_EVENT"]))
y_test_30 = np.array(Data_Test_30["DEATH_EVENT"])
x_test_30 = np.array(Data_Test_30.drop(columns=["DEATH_EVENT"]))

# Normalizing Data

u = np.mean(x_train_70,axis=0)
std = np.std(x_train_70,axis=0)

x_train_70 = (x_train_70-u)/std
x_test_30 = (x_test_30-u)/std


# In[4]:


# 80-20 Split
Data_Train_80 = data.iloc[:int(len(data)*0.8)]
Data_Test_20 = data.iloc[int(len(data)*0.8):]

y_train_80 = np.array(Data_Train_80["DEATH_EVENT"])
x_train_80 = np.array(Data_Train_80.drop(columns=["DEATH_EVENT"]))
y_test_20 = np.array(Data_Test_20["DEATH_EVENT"])
x_test_20 = np.array(Data_Test_20.drop(columns=["DEATH_EVENT"]))

# Normalizing Data

u = np.mean(x_train_80,axis=0)
std = np.std(x_train_80,axis=0)

x_train_80 = (x_train_80-u)/std
x_test_20 = (x_test_20-u)/std


# In[5]:


# 90-10 Split
Data_Train_90 = data.iloc[:int(len(data)*0.8)]
Data_Test_10 = data.iloc[int(len(data)*0.8):]

y_train_90 = np.array(Data_Train_90["DEATH_EVENT"])
x_train_90 = np.array(Data_Train_90.drop(columns=["DEATH_EVENT"]))
y_test_10 = np.array(Data_Test_10["DEATH_EVENT"])
x_test_10 = np.array(Data_Test_10.drop(columns=["DEATH_EVENT"]))

# Normalizing Data

u = np.mean(x_train_90,axis=0)
std = np.std(x_train_90,axis=0)

x_train_90 = (x_train_90-u)/std
x_test_10 = (x_test_10-u)/std


# # Half Space

# In[6]:


from sklearn.linear_model import Perceptron
percept = Perceptron()


# In[7]:


# For 70-30  split
percept.fit(x_train_70,y_train_70)
score_70 = percept.score(x_test_30,y_test_30)


# In[8]:


# For 80-20  split
percept.fit(x_train_80,y_train_80)
score_80 = percept.score(x_test_20,y_test_20)


# In[9]:


# For 90-10  split
percept.fit(x_train_90,y_train_90)
score_90 = percept.score(x_test_10,y_test_10)


# In[10]:


print("\n Prediction Score/Accuracy using Half Space Classifier (Using Perceptron): ")
print("Percentage Score at 70-30 split :",score_70*100)
print("Percentage Score at 80-20 split :",score_80*100)
print("Percentage Score at 90-10 split :",score_90*100)


# #  Logistic Regression

# ## Using Library

# In[11]:


from sklearn.linear_model import LogisticRegression
model = LogisticRegression()


# In[12]:


# For 70-30  split
model.fit(x_train_70,y_train_70)
score_70 = model.score(x_test_30,y_test_30)


# In[13]:


# For 80-20 split

model.fit(x_train_80,y_train_80)
score_80 = model.score(x_test_20,y_test_20)


# In[14]:


# For 90-10 split
model.fit(x_train_90,y_train_90)
score_90 = model.score(x_test_10,y_test_10)


# In[15]:


print("\n Prediction Score/Accuracy using In-Built Logistic Regression Function: ")
print("Percentage Score at 70-30 split :",score_70*100)
print("Percentage Score at 80-20 split :",score_80*100)
print("Percentage Score at 90-10 split :",score_90*100)


# ## Using SGD Procedure

# In[16]:


def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def hypothesis(X,w):
    '''
        x - entire array(m,n+1)
        w - np.array(n+1,1)
    '''
    
    return sigmoid(np.dot(X,w))

def error(X,y,w):
    '''
       x - (m,n+1)
       y - (m,1)
       w = (n+1,1)
       return:
            scaler_value = loss
    '''

    hypo = hypothesis(X,w)
    err = -1*np.mean((y*np.log(hypo) + ((1-y) *np.log(1-hypo))))
    
    return err

def gradient(X,y,w):
    '''
       x - (m,n+1)
       y - (m,1)
       w = (n+1,1)
       return:
            gradient vector - (n+1,1)
    '''
    
    hypo = hypothesis(X,w)
    grad = -np.dot(X.T,(y-hypo))
    #print(y.shape,hypo.shape)
    m = X.shape[0]
    return grad/m
    

def gradient_descent(X,y,lr=0.5,max_itr = 500):
    
    n = X.shape[1]
    
    w = np.zeros((n,1))
    
    error_list = []

    for i in range(max_itr) :
        err = error(X,y,w)
        error_list.append(err)
        grad = gradient(X,y,w)
        
        # Update w
        w = w - lr*grad
        
    return w,error_list
        
#Converting confidence score into corresponding label    
def predict(x,w):
    h = hypothesis(x,w)
    output = np.zeros(h.shape)
    output[h>0.5] = 1
    output = output.astype('int')
    return output

#Finding Accurecy of model
def accuracy(actual,pred):
    acc = np.sum(actual == pred)/actual.shape[0]
    return acc*100


# In[17]:


# For 70-30  split

x_train = x_train_70
y_train = y_train_70

x_test = x_test_30
y_test = y_test_30

y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)

ones = np.ones((x_train.shape[0],1))
x_train = np.hstack((ones,x_train))

ones = np.ones((x_test.shape[0],1))
x_test = np.hstack((ones,x_test))

w,error_list = gradient_descent(x_train,y_train)
y_predict = predict(x_test,w)
score_70 = accuracy(y_test,y_predict)


# In[18]:


# For 80-20  split

x_train = x_train_80
y_train = y_train_80

x_test = x_test_20
y_test = y_test_20

y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)

ones = np.ones((x_train.shape[0],1))
x_train = np.hstack((ones,x_train))

ones = np.ones((x_test.shape[0],1))
x_test = np.hstack((ones,x_test))

w,error_list = gradient_descent(x_train,y_train)
y_predict = predict(x_test,w)
score_80 = accuracy(y_test,y_predict)


# In[19]:


# For 90-10  split

x_train = x_train_90
y_train = y_train_90

x_test = x_test_10
y_test = y_test_10

y_train = y_train.reshape(-1,1)
y_test = y_test.reshape(-1,1)

ones = np.ones((x_train.shape[0],1))
x_train = np.hstack((ones,x_train))

ones = np.ones((x_test.shape[0],1))
x_test = np.hstack((ones,x_test))

w,error_list = gradient_descent(x_train,y_train)
y_predict = predict(x_test,w)
score_90 = accuracy(y_test,y_predict)


# In[20]:


print("\n Prediction Score/Accuracy using Logistic Regression using Gradient Descent: ")
print("Percentage Score at 70-30 split :",score_70)
print("Percentage Score at 80-20 split :",score_80)
print("Percentage Score at 90-10 split :",score_90)


# # SVM Classifier

# ## Using Gaussian kernel

# In[21]:


from sklearn.svm import SVC
svm = SVC(kernel = 'rbf')


# In[22]:


# For 70-30  split
svm.fit(x_train_70,y_train_70)
score_70 = svm.score(x_test_30,y_test_30)
num = svm.support_vectors_
vect_70 = num.shape[0]


# In[23]:


# For 80-20 split
svm.fit(x_train_80,y_train_80)
score_80 = svm.score(x_test_20,y_test_20)
num = svm.support_vectors_
vect_80 = num.shape[0]


# In[24]:


# For 90-10 split
svm.fit(x_train_90,y_train_90)
score_90 = svm.score(x_test_10,y_test_10)
num = svm.support_vectors_
vect_90 = num.shape[0]


# In[25]:


print("\n Prediction Score using SVM Gaussian Kernel: ")
print("Percentage Score at 70-30 split :",score_70*100)
print("Percentage Score at 80-20 split :",score_80*100)
print("Percentage Score at 90-10 split :",score_90*100)

print("\n Number of support vector using SVM Gaussian Kernel: ")
print("Number of support vectors in 70-30 split :",vect_70)
print("Number of support vectors in 80-20 split :",vect_80)
print("Number of support vectors in 90-10 split :",vect_90)


# ## Using Polynomial Kernel

# In[26]:


from sklearn.svm import SVC
svm = SVC(kernel = 'poly')


# In[27]:


# For 70-30  split
svm.fit(x_train_70,y_train_70)
score_70 = svm.score(x_test_30,y_test_30)
num = svm.support_vectors_
vect_70 = num.shape[0]


# In[28]:


# For 80-20 split
svm.fit(x_train_80,y_train_80)
score_80 = svm.score(x_test_20,y_test_20)
num = svm.support_vectors_
vect_80 = num.shape[0]


# In[29]:


# For 90-10 split
svm.fit(x_train_90,y_train_90)
score_90 = svm.score(x_test_10,y_test_10)
num = svm.support_vectors_
vect_80 = num.shape[0]


# In[30]:


print("\n Prediction Score using SVM Polynomial Kernel: ")
print("Percentage Score at 70-30 split :",score_70*100)
print("Percentage Score at 80-20 split :",score_80*100)
print("Percentage Score at 90-10 split :",score_90*100)

print("\n Number of support vector using SVM Polynomial Kernel: ")
print("Number of support vectors in 70-30 split :",vect_70)
print("Number of support vectors in 80-20 split :",vect_80)
print("Number of support vectors in 90-10 split :",vect_90)


# ## Using Linear Kernel

# In[31]:


from sklearn.svm import SVC
svm = SVC(kernel = 'linear')


# In[32]:


# For 70-30  split
svm.fit(x_train_70,y_train_70)
score_70 = svm.score(x_test_30,y_test_30)
num = svm.support_vectors_
vect_70 = num.shape[0]


# In[33]:


# For 80-20 split
svm.fit(x_train_80,y_train_80)
score_80 = svm.score(x_test_20,y_test_20)
num = svm.support_vectors_
vect_80 = num.shape[0]


# In[34]:


# For 90-10 split
svm.fit(x_train_90,y_train_90)
score_90 = svm.score(x_test_10,y_test_10)
num = svm.support_vectors_
vect_90 = num.shape[0]


# In[35]:


print("\n Prediction Score using SVM Linear Kernel: ")
print("Percentage Score at 70-30 split :",score_70*100)
print("Percentage Score at 80-20 split :",score_80*100)
print("Percentage Score at 90-10 split :",score_90*100)

print("\n Number of support vector using SVM Linear Kernel: ")
print("Number of support vectors in 70-30 split :",vect_70)
print("Number of support vectors in 80-20 split :",vect_80)
print("Number of support vectors in 90-10 split :",vect_90)


# In[ ]:




