# Ⓒ Ajaytech - https://ajaytech.co
#
# This program is not intended to teach you Machine Learning. 
# Instead it is intended to show what Machine Learning can solve 
# that conventional programming cannot solve

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Import the Boston Housing dataset
from sklearn.datasets import load_boston
boston = load_boston()

# Convert the boston object into a dataframe
df_boston = pd.DataFrame(boston.data)

# Set the columns of the data frame
df_boston.columns = boston.feature_names

# Set the target price in the data frame
df_boston['PRICE'] = boston.target

# Set the predictors and response variables

# Number of rooms ( RM ) is the predictor 
predictor = pd.DataFrame(df_boston['RM'])

# The price of the house ( PRICE ) is the response variable
response   = df_boston['PRICE']

# Fit the model
lm = LinearRegression().fit(predictor, response)


# Slope and intercept
slope       = lm.coef_
intercept   = lm.intercept_

# get the line points
rm_sorted = np.array(df_boston['RM'] )
rm_sorted.sort()
line = rm_sorted * slope[0] + intercept

# Predict how good the fit is based on the test data
predict = lm.predict(predictor)

plt.scatter(df_boston['RM'],df_boston['PRICE'], marker='.')
plt.title(" Number of rooms vs Price")
plt.xlabel("Number of Rooms")
plt.ylabel("Price")
plt.plot ( rm_sorted, line, 'r')
plt.show()

