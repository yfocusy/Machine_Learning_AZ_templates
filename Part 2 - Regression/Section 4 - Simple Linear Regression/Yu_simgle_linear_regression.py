#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 17:39:25 2018

@author: yuli510
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 07:55:27 2018

@author: yuli510
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# -------------------------------------------------------------
# 1. importing the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,1].values


# -------------------------------------------------------------
# 5. splitting the dataset into the traning set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 1/3, random_state=0)

# -------------------------------------------------------------
# 6. feature Scaling 特征缩放
# 目前项目，python中对所有对象特征缩放
'''
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
'''


# fitting simple Linear Regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

# predicting the test set results
y_pred = regressor.predict(X_test)


# visualising the traing set results
# 画图 for training_set 
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color='blue')
#plt.title("Salary Vs Experience (Training set)")
#plt.xlabel("year of Experience")
#plt.ylabel("Salary")
#plt.show()


# visualising the test set results
# 画图 for test_set
plt.scatter(X_test, y_test, color = 'green')
plt.plot(X_train, regressor.predict(X_train), color='blue')
plt.title("Salary Vs Experience (Training set)")
plt.xlabel("year of Experience")
plt.ylabel("Salary")
plt.show()






