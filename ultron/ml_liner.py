#Import Library
#Import other necessary libraries like pandas, numpy...
import numpy as np
from sklearn import linear_model
#Load Train and Test datasets
#Identify feature and response variable(s) and values must be numeric and numpy arrays

x_train = np.array([ [270.7, 56], [273.3, 55], [277.55, 54], [277.05, 51], [277.9,50], [277.2, 49], [275.85,48], [276.35,47], [271.65,44], [270.2,43], [268.95,42], [270.5,41], [269.35,40], [269.65,37], [270.7,36], [272.3,35], [270.45,34], [268.25,30], [269.2,29], [271.75,28] ])

y_train = np.array([4.25, 5.6, 5.4, 7.8, 6.05, 6.3, 6.45, 6.35, 4.35, 2.75, 2.45, 2.75, 2.95, 2.3, 2.15, 2.2, 5, 2.05, 1.35, 1.55])

x_test = np.array([ [267.30,27], [265.05,26], [269.85,23], [267.80,22], [269.90,21], [273.25,20], [272.05,19] ])

#x_train = x_train.reshape(-1, 1)
#y_train= y_train.reshape(-1, 1)
#x_test= x_test.reshape(-1, 1)

# Create linear regression object
linear = linear_model.LinearRegression()
# Train the model using the training sets and check score
linear.fit(x_train, y_train)
linear.score(x_train, y_train)
#Equation coefficient and Intercept
print('Coefficient: \n', linear.coef_)
print('Intercept: \n', linear.intercept_)
#Predict Output
predicted= linear.predict(x_test)
print (predicted)


