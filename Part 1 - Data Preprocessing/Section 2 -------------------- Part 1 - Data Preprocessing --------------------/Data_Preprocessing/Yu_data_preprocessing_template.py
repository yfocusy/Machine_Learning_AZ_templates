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
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values

# -------------------------------------------------------------
# 2. taking care of missing data
# use mean to replace NaN data
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN",strategy= "mean", axis=0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

# -------------------------------------------------------------
# 3. Encoding categorical data 
# country labels ==> number 
# dummy encoding 虚拟编码 france 100  onehotEncoder
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
labelencoder_X = LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
onehotencoder = OneHotEncoder(categorical_features=[0]) # 处理第0列
X = onehotencoder.fit_transform(X).toarray()

# -------------------------------------------------------------
# 4. purchase 
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)

# -------------------------------------------------------------
# 5. splitting the dataset into the traning set and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.2, random_state=0)

# -------------------------------------------------------------
# 6. feature Scaling 特征缩放
# 目前项目，python中对所有对象特征缩放
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


# 7. y此题代表两个类别，并不需要做特征缩放



