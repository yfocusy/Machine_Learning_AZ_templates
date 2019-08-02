#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 10:26:02 2018

@author: yuli510
"""

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

# 处理分类数据字符串
# Encoding categorical data
# Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()


# 处理avoding dummy variable trip, 取1后边的所有列
X = X[:,1:]

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
# 本题不需要特征缩放，因为标准库里边已经有了
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

# Fitting Multiple linear Regression to the training set 
# 创建回归器，并且用training_set拟合回归器
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train)

# predicting the test set results
# 并且用training_set拟合回归器,目前用了所有的自变量。用了 All-in
y_pred = regressor.predict(X_test)


# building the optimal model using Backward Elimination
# 反向淘汰算法，剔除自变量中，影响小的(P value 大)
import statsmodels.formula.api as sm
# 常数 b0*1 ，但是标准库中不包含常数项，需要自己加一列
X_train = np.append(arr = np.ones((40,1)), values = X_train, axis = 1)
# opt 里还有最佳的variables选择
X_opt = X_train[:,[0,1,2,3,4,5]]
# 创建新的回归器
regressor_OLS = sm.OLS(y_train, exog = X_opt).fit()
regressor_OLS.summary()

# x2的p value最大 = 0.85 ，剔除
X_opt = X_train[:,[0,1,3,4,5]]
regressor_OLS = sm.OLS(y_train, exog = X_opt).fit()
regressor_OLS.summary()

# x1的p value最大 = 0.729 ，剔除
X_opt = X_train[:,[0,3,4,5]]
regressor_OLS = sm.OLS(y_train, exog = X_opt).fit()
regressor_OLS.summary()

# x2的p value最大 = 0.65，剔除
X_opt = X_train[:,[0,3,5]]
regressor_OLS = sm.OLS(y_train, exog = X_opt).fit()
regressor_OLS.summary()

# x2的p value最大 = 0.071，剔除,因为选了SL=0.05
X_opt = X_train[:,[0,3]]
regressor_OLS = sm.OLS(y_train, exog = X_opt).fit()
regressor_OLS.summary()

# 此时留下的唯一的data_set中的第三列,p value = 0
# 结论：在研发上投入高，profit。
'''
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
const       4.842e+04   2842.717     17.032      0.000    4.27e+04    5.42e+04
x1             0.8516      0.033     25.542      0.000       0.784       0.919
==============================================================================
Omnibus:                       13.132   Durbin-Watson:                   2.325
Prob(Omnibus):                  0.001   Jarque-Bera (JB):               16.254
Skew:                          -0.991   Prob(JB):                     0.000295
Kurtosis:                       5.413   Cond. No.                     1.57e+05
==============================================================================
'''