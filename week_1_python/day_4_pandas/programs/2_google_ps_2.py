##########################################################################
# Data Copyright - 
# The data used in this program is Copyright of Lavanya Gupta @
# https://www.kaggle.com/lava18/google-play-store-apps
##########################################################################
# Program is copyright Ⓒ of Ajay Tech @ https://ajaytech.co
##########################################################################
# TODO - 
# DATA ANALYSIS
# 1.    List all the unique app "Categories"
# 2.    What is the average ( mean ) rating of the apps
# 3.    Get the mean rating per each category
# 4.    Which category has the highest mean price
# 5.    List the top 10 pricier apps
# 6.    How many apps with price > 10$
# 7.    What percentage of the apps are PAID
# 8.    Is there a difference in size of FREE vs PAID apps on average ?
# 9.    How large is the difference in the average installations of FREE vs paid apps ?
##########################################################################
# LEARNING - 
# 1.    How to multiply/compare the values of a column 
# 2.    How to get the unique values of a column 
# 3.    How to get the mean of a column
# 4.    How to perform group by operations on categorical columns
# 5.    How to sort a particular column
# 6.    How to calculate the count of rows grouped by a criteria
##########################################################################

import pandas as pd 
import numpy as np
import math

google_ps_d = pd.read_csv("./data/google_play_store_clean.csv")

# 1.    List all the unique app "Categories"
print ( google_ps_d["Category"].unique() )

# 2.    What is the average ( mean ) rating of the apps
print ( google_ps_d["Rating"].mean())

# 3.    Get the mean rating per each category
print ( google_ps_d.groupby(["Category"]).mean())

# 4.    Which category has the highest mean price
mean = google_ps_d.groupby(["Category"]).mean()
mean.sort_values("Price", axis = 0, ascending = False, inplace = True)
print ( mean )           

# 5.    List the top 10 pricier apps
sorted = google_ps_d.sort_values("Price", axis = 0, ascending = False)
print ( sorted.iloc[:,[0,1,7]].head(10))

# 6.    How many apps with price > 10$
print ( google_ps_d[google_ps_d["Price"] > 10].shape  )

# 7.    What percentage of apps are PAID ?
paid = google_ps_d.groupby(["Type"]).size()["Paid"]
free = google_ps_d.groupby(["Type"]).size()["Free"]
# or use the count() aggregate function
# google_ps_d.groupby(["Type"]).count()

print ( "Percentage of paid apps = " , math.trunc ( paid/(paid+free) * 100 ) , "%" )

# 8.    Is there a difference in size of FREE vs PAID apps on average ?
print ( google_ps_d.groupby(["Type"]).mean().loc[:,["Size"]])

# 9.    How large is the difference in the average installations of FREE vs paid apps ?
print ( google_ps_d.groupby(["Type"]).mean().loc[:,["Installs"]])


