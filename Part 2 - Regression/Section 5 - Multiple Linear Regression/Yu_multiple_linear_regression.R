# data preprocessing template
# -------------------------------------------------------------
# 1. Importing the dataset
dataset = read.csv('50_Startups.csv')
# 导入dataset中部分数据
# dataset = dataset[,2:3]


# -------------------------------------------------------------
# 2. taking care of missing data
# dataset$Age[is.na(dataset$Age)] = mean(dataset$Age,na.rm = T)
# dataset$Salary[is.na(dataset$Salary)] = mean(dataset$Salary,na.rm = T)
# 
# dataset$Country = factor(dataset$Country, 
#                          levels=c('France','Spain','Germany'),
#                          labels=c(1,2,3))
# dataset$Purchased = factor(dataset$Purchased, 
#                            levels=c('No','Yes'),
#                            labels=c(0,1))


# 2. 文字类分类数据处理
dataset$State = factor(dataset$State,
                       levels=c("New York", "California","Florida"),
                       labels=c(1,2,3))
# -------------------------------------------------------------
# 3. splitting the dataset into the Traning_set and Test_set
install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset,split == TRUE)
test_set = subset(dataset,split == FALSE)

# 6. feature Scaling 特征缩放。在R中在多元线性回归中，包含了。
#    无需再加
# country 和 purchase并不是 numberic，是分类因子，并不能做特征缩放
# training_set = scale(training_set)
# test_set = scale(test_set)

# training_set[,2:3] = scale(training_set[,2:3])
# test_set[,2:3] = scale(test_set[,2:3])

# Fitting Multiple Linear Regression to the Training_set
regressor = lm(formula=Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
               data = training_set)
# . = 其他所有自变量
# regressor = lm(formula=Profit ~ .,
#                 data = training_set)

# ！！！根据多元的数据summary分析：
# 将多元-->转化为一元
# regressor = lm(formula=Profit ~ R.D.Spend,
#                data = training_set)

# R自动舍弃了State里边的一个自变量，防止了Dummy Variables trip
# 分析R返回的数据：
# 1） P Value= 越小variable与model关联越大
# 2） *** = Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1 
# 3)  只有一个自变量（研发投入） 对因变量profit影响大，
#     将多元-->转化为单元




# --多元summary---------------------------------------------------------------
# Call:
#   lm(formula = Profit ~ ., data = training_set)
# 
# Residuals:
#   Min     1Q Median     3Q    Max 
# -33128  -4865      5   6098  18065 

# Coefficients:
#                     Estimate Std. Error t value Pr(>|t|)    
# (Intercept)      4.965e+04  7.637e+03   6.501 1.94e-07 ***
# R.D.Spend        7.986e-01  5.604e-02  14.251 6.70e-16 ***
# Administration  -2.942e-02  5.828e-02  -0.505    0.617    
# Marketing.Spend  3.268e-02  2.127e-02   1.537    0.134    
# State2           1.213e+02  3.751e+03   0.032    0.974    
# State3           2.376e+02  4.127e+03   0.058    0.954    
# ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1

# --一元summary---------------------------------------------------------------
# Call:
#   lm(formula = Profit ~ R.D.Spend, data = training_set)
# 
# Residuals:
#   Min     1Q Median     3Q    Max 
# -34334  -4894   -340   6752  17147 
# 
# Coefficients:
#   Estimate Std. Error t value Pr(>|t|)    
# (Intercept) 4.902e+04  2.748e+03   17.84   <2e-16 ***
#   R.D.Spend   8.563e-01  3.357e-02   25.51   <2e-16 ***
#   ---
#   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
# 
# Residual standard error: 9836 on 38 degrees of freedom
# Multiple R-squared:  0.9448,	Adjusted R-squared:  0.9434 
# F-statistic: 650.8 on 1 and 38 DF,  p-value: < 2.2e-16


# Predicting the Test set results
y_pred = predict(regressor, newdata=test_set)

# Buliding the optimal model using Backward Elimination
regressor = lm(formula=Profit ~ R.D.Spend + Administration + Marketing.Spend + State,
               data = training_set)
summary(regressor)

regressor = lm(formula=Profit ~ R.D.Spend + Administration + Marketing.Spend,
               data = training_set)
summary(regressor)

regressor = lm(formula=Profit ~ R.D.Spend + Marketing.Spend,
               data = training_set)
summary(regressor)

regressor = lm(formula=Profit ~ R.D.Spend,
               data = training_set)
summary(regressor)
# -------------------------------------------------------
# Multiple R-squared 为误差值，（预测值-原来值）平方，越接近1，拟合误差越小。
# Residual standard error: 9836 on 38 degrees of freedom
# Multiple R-squared:  0.9448,	Adjusted R-squared:  0.9434 
# F-statistic: 650.8 on 1 and 38 DF,  p-value: < 2.2e-16




