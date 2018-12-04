# Ⓒ Ajaytech - https://ajaytech.co
#
# This program is not intended to teach you Machine Learning. 
# Instead it is intended to show what Machine Learning can solve 
# that conventional programming cannot solve

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn

# Import the Boston Housing dataset
from sklearn.datasets import load_boston
boston = load_boston()

# Set the columns to the data frame
bos.columns = boston.feature_names
print(bos.head())