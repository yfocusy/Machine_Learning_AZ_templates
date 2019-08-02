# data preprocessing template
# -------------------------------------------------------------
# 1. Importing the dataset
dataset = read.csv('Salary_Data.csv')
# 导入dataset中部分数据
# dataset = dataset[,2:3]


# -------------------------------------------------------------
# 3. splitting the dataset into the traning set and test set
install.packages('caTools')
library(caTools)
set.seed(123)
  split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset,split == TRUE)
test_set = subset(dataset,split == FALSE)

# 6. feature Scaling 特征缩放
# country 和 purchase并不是 numberic，是分类因子，并不能做特征缩放
# training_set = scale(training_set)
# test_set = scale(test_set)

# training_set[,2:3] = scale(training_set[,2:3])
# test_set[,2:3] = scale(test_set[,2:3])

regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)

# predicting the test set results
y_pred = predict(regressor, newdata = test_set)


# Visualising the training set results
install.packages('ggplot2')
library(ggplot2)
ggplot()+
  geom_point(aes(x=training_set$YearsExperience, y=training_set$Salary),
             color='red') +
  geom_line(aes(x=training_set$YearsExperience, y=predict(regressor,newdata=training_set)),
            color='blue')+
  ggtitle("Salary vs Experience (Training set)") + 
  xlab("year of Experience") +
  ylab("Salary")


# Visualising the training set results
#install.packages('ggplot2')
#library(ggplot2)
ggplot()+
  geom_point(aes(x=test_set$YearsExperience, y=test_set$Salary),
             color='green') +
  geom_line(aes(x=training_set$YearsExperience, y=predict(regressor,newdata=training_set)),
            color='blue') +
  ggtitle("Salary vs Experience (Training set)") + 
  xlab("year of Experience") +
  ylab("Salary")





