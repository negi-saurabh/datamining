# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 10:48:45 2019

@author: Tom
"""

#Assignment 1 Task 2
#Titanic Kaggle Competition

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Read in data, Trainset and Testset
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
datadescription = train.describe()


# Start exploration using plots

# start main plot
plt.figure(figsize=[14,20])
    #barplot for relative gender survival rates
surv_rate_male = np.average(train[train.Sex=='male'].Survived)
surv_rate_female = np.average(train[train.Sex=='female'].Survived)
x = ['male', 'female']
y = [surv_rate_male,surv_rate_female]
plt.subplot(4,2,1)
plt.title('Survival rates by gender')
plt.bar(x,y)
plt.ylabel('Survival Rate')
    # histogram for survival rates by age
plt.subplot(4,2,2)
plt.title('Survival frequency by age')
train.Age.plot.hist()
train[train.Survived==1].Age.plot.hist()
plt.ylabel('Frequency')
plt.legend(['Total','Survived'])
    # histogram for survival rates by age (males)
plt.subplot(4,2,3)
plt.title('Male survival by age')
train[train.Sex =='male'].Age.plot.hist()
train[train.Sex =='male'][train.Survived==1].Age.plot.hist()
plt.ylabel('Frequency')
plt.legend(['Total','Survived'])
    # histogram per gender for survival rates by age (females)
plt.subplot(4,2,4)
plt.title('Female survival by age')
train[train.Sex =='female'].Age.plot.hist()
train[train.Sex =='female'][train.Survived==1].Age.plot.hist()
plt.ylabel('Frequency')
plt.legend(['Total','Survived'])

#barplot for ticket price vs survival rates
plt.subplot(4,2,5)
train.Fare.plot.hist()
train[train.Survived==1].Fare.plot.hist()
plt.title('Survival by ticket price')
plt.legend(['Total','Survived'])

#barplot for class vs survival rates
surv_rate_first= np.average(train[train.Pclass== 1].Survived)
surv_rate_second= np.average(train[train.Pclass== 2].Survived)
surv_rate_third= np.average(train[train.Pclass== 3].Survived) 
x = ['1','2','3']
y = [surv_rate_first,surv_rate_second,surv_rate_third]
plt.subplot(4,2,6)
plt.bar(x,y)
plt.title('Survival rate by passenger class')
plt.ylabel('Survival rate')

#barplot for siblings&spouse vs survival rates
S = max(train.SibSp)
y = np.zeros(S)
for i in range(S):
    y[i] = np.average(train[train.SibSp == i].Survived)
x = list(range(S))
plt.subplot(4,2,7)
plt.ylabel('Survival rate')
plt.bar(x,y)
plt.title('Survival rate by amount of siblings or spouses on board')
#barplot for parents and children vs survival rates
P = max(train.Parch)
y = np.zeros(P)
for i in range(P):
    y[i] = np.average(train[train.Parch == i].Survived)
x = list(range(P))
plt.subplot(4,2,8)
plt.ylabel('Survival rate')
plt.bar(x,y)
plt.title('Survival rate by amount of parents or children on board')















