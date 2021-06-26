#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries and Data Set


# Importing Library 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



data= pd.read_excel('./DataSet/ICC Test Bat 3001.xlsx')
player = list(data['Player'])
match = list(data['Mat'])
innings = list(data['Inn'])
runs = list(data['Runs'])
highest_score = list(data['HS'])
average = list(data['Avg'])
hundred = list(data[100])
fifty = list(data[50])



# Cleaning Data
for i in range(0,len(average)):
    if(average[i] == '-'):
        average[i] = 0.0

for i in range(0,len(hundred)):
    if(hundred[i] == '-'):
        hundred[i] = 0
        
for i in range(0,len(fifty)):
    if(fifty[i] == '-'):
        fifty[i] = 0

for i in range(0,len(innings)):
    if(innings[i] == '-'):
        innings[i] = 0

for i in range(0,len(runs)):
    if(runs[i] == '-'):
        runs[i] = 0




print(data.head())


# # Familiarization with DataFrames, Matplotlib

print("--------Familiarization with DataFrames, Matplotlib--------------------")

#Using Dataframe constructor in Pandas to create your own Dataframe.
data_frame = pd.DataFrame({'Player':player, 'Match':match, 'Innings':innings, 'Runs':runs, 'Highest_Score':highest_score})


#Adding column Average to data set
data_frame['Average'] = average



# Printing First five record
print(data_frame.head())


# Printing data of first column 'Player'
print(data_frame['Player'].head()) #Print First five record


#  Printing five row starint from index 5
print(data_frame[5:10])


# Printing data of first five row and of column with index 0 and 3
print(data_frame.iloc[:5,[0,3]])


# Adding column Century and Half-Century Scored by Player
data_frame['Century']=hundred
data_frame['Half-Century'] = fifty
print(data_frame.head())



# Sorting Data On the Basis Of Average of Player
sorted_data_frame = data_frame.sort_values('Average',ascending=False)
print(data_frame.head())



#Printing all records whose average is greater than '100'

new_data = data_frame[data_frame['Average'] >100]
print(new_data)





# Finding total run scored by these all Players
total_run = data_frame['Runs'].sum()

# Finding percentage participation of each player in total runs
lst = (data_frame['Runs'] / total_run)*100

# Add Column Participation in new_data frame which will denote share of individual player in total runs

data_frame['Participation'] = lst.values
print(data_frame.head())

# Create new data frame containing first 25 data set 
new_data = data_frame.iloc[:25]

# Exporting Data Frame to Pickel File
new_data.to_pickle("./CricketData.pickel")

# Reading Pickel File
pickel_data = pd.read_pickle("./CricketData.pickel")
print(pickel_data)



# Ploting Scatter Plot between Century and Half-Century Scored by Player 

x = pickel_data["Century"]
y = pickel_data["Half-Century"]
plt.style.use("seaborn")
plt.title("Ploting Scatter Plot between Century and Half-Century Scored by Player")
plt.xlabel("Century")
plt.ylabel("Half-Century")
plt.scatter(x, y)
plt.show()


#  Implement linear regression

print("-----------Implement linear regression------------")

# Removing Records from data frame for sake of convenience
# These points affects visualisation e.g player who plays very less matches affects generalisation
data_frame.set_index("Innings")
for i in range(0,75):
    data_frame = data_frame.drop(i,axis=0)
    


# Using Pseudo-Inverse



#Reading DataFrame as Numpy 
x, y = data_frame.Innings.values, data_frame.Runs.values
x = x.reshape((len(x), 1)) #Reshaping Data

A = np.transpose(x).dot(x)
B = y.dot(x)
w = np.linalg.inv(A).dot(B)

line_reg = x.dot(w)

# plot data and predictions
plt.style.use("seaborn")
plt.title("Using Pseudo-Inverse")
plt.xlabel("Innings")
plt.ylabel("Runs")
plt.scatter(x, y)
plt.plot(x,line_reg , color='red')
plt.show()


# Using sk-learn


from sklearn.linear_model import LinearRegression
model = LinearRegression()
x_, y_ = data_frame.Innings.values, data_frame.Runs.values
x_ = x_.reshape((len(x), 1))
model.fit(x_,y_)
#print(model.coef_,model.intercept_)

plt.plot(x_,model.predict(x_),color='black')
plt.title("Using sk-learn")
plt.style.use("seaborn")
plt.xlabel("Innings")
plt.ylabel("Runs")
plt.scatter(x_,y_)
plt.show()


#  Comparison


plt.style.use("seaborn")
plt.xlabel("Innings")
plt.ylabel("Runs")
plt.title("Comparison Between Output of sk-learn and Pseudo-Inverse")
plt.scatter(x, y)
plt.plot(x,line_reg , color='red',label="Using Pseudo-Inverse")
plt.plot(x_,model.predict(x_),color='black',label="Using sk-learn")
plt.legend()

plt.show()




