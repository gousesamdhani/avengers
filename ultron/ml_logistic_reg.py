#Import Library
import numpy as np
from sklearn.linear_model import LogisticRegression
#Assumed you have, X (predictor) and Y (target) for training data set and x_test(predictor) of test_dataset
# Create logistic regression object

x_train = np.array([ [270.7, 56], [273.3, 55], [277.55, 54], [277.05, 51], [277.9,50], [277.2, 49], [275.85,48], [276.35,47], [271.65,44], [270.2,43], [268.95,42], [270.5,41], [269.35,40], [269.65,37], [270.7,36], [272.3,35], [270.45,34], [268.25,30], [269.2,29], [271.75,28] ])

y_train = np.array([0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1])

x_test = np.array([ [267.30,27], [265.05,26], [269.85,23], [267.80,22], [269.90,21], [273.25,20], [272.05,19] ])


model = LogisticRegression()
# Train the model using the training sets and check score
model.fit(x_train, y_train)
model.score(x_train, y_train)
#Equation coefficient and Intercept
print('Coefficient: \n', model.coef_)
print('Intercept: \n', model.intercept_)
#Predict Output
predicted= model.predict(x_test)
print(predicted)
