# data preprocessing template
# -------------------------------------------------------------
# 1. Importing the dataset
dataset = read.csv('Data.csv')
# 导入dataset中部分数据
# dataset = dataset[,2:3]


# -------------------------------------------------------------
# 2. taking care of missing data
dataset$Age[is.na(dataset$Age)] = mean(dataset$Age,na.rm = T)
dataset$Salary[is.na(dataset$Salary)] = mean(dataset$Salary,na.rm = T)

dataset$Country = factor(dataset$Country, 
                         levels=c('France','Spain','Germany'),
                         labels=c(1,2,3))
dataset$Purchased = factor(dataset$Purchased, 
                         levels=c('No','Yes'),
                         labels=c(0,1))

# -------------------------------------------------------------
# 3. splitting the dataset into the traning set and test set
install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set = subset(dataset,split == TRUE)
test_set = subset(dataset,split == FALSE)

# 6. feature Scaling 特征缩放
# country 和 purchase并不是 numberic，是分类因子，并不能做特征缩放
# training_set = scale(training_set)
# test_set = scale(test_set)

training_set[,2:3] = scale(training_set[,2:3])
test_set[,2:3] = scale(test_set[,2:3])





