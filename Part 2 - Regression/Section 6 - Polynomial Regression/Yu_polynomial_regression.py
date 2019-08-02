#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 23:24:01 2018

@author: yuli510
"""

# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Position_Salaries.csv')
# 包含自变量的应该是矩阵，所以有：
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2].values
# 数据数据太少，不分割。用来拟合的数据越多越好
# Splitting the dataset into the Training set and Test set
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""



# 创建两个模型，一个线性，一个多项式，用于对比
# linear regression 
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

# polynomial regression
from sklearn.preprocessing import PolynomialFeatures
# degree 为最高次数
poly_reg = PolynomialFeatures(degree=2)
# 包含自变量不同次数的矩阵
X_poly = poly_reg.fit_transform(X)
lin_reg_2 = LinearRegression()
lin_reg_2.fit(X_poly,y)



