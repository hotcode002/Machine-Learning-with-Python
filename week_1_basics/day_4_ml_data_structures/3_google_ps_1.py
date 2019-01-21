##########################################################################
# Data Copyright - 
# The data used in this program is Copyright of Lavanya Gupta @
# https://www.kaggle.com/lava18/google-play-store-apps
##########################################################################
# Program is copyright Ⓒ of Ajay Tech @ https://ajaytech.co
##########################################################################
# TODO - 
# ##################################################################################
# BEGIN - Data Cleaning
##################################################################################
# 1. Drop all the null values ( NaN, NaT etc )
# 2. Clean the "Installs" column
#       - Strip it of + and , 
#       - Convert it to integer
# 3. Clean the "Size" column
#       - Strip it of the MB indicator - 'M'
#       - Strip it of the text "Varies by Device" and replace it with NaN
#       - Strip all NAs
#       - Convert it to integer
#       - Convert it to KB by multiplying it by 1000
# 3. Clean the "Price" column 
#       - Strip it of $
#       - Convert it to float
# 4. Clean the "Reviews" column
#       - Convert it to integer
#
# # DATA ANALYSIS
# 5. List all the unique app "Categories"
# 6. What is the average ( mean ) rating of the apps
# 7. Get the mean rating per each category
# 8. Which category has the highest mean price
# 9. List the top 10 pricier apps
# 10. How many apps with price > 10$
# 11.   Is there a difference in size of FREE vs PAID apps on average ?
# 12.   How large is the difference in the average installations of FREE vs paid apps ?
##########################################################################
# LEARNING - 
# 1.    How to skip rows from reading a csv file into a data frame
# 2.    How to drop NaNs from a data frame
# 3.    How to replace string values in the cells of a data frame
# 4.    How to convert the column type of a df from object to String or integer or float
# 5.    How to multiply/compare the values of a column 
# 6.    How to get the unique values of a column 
# 7.    How to get the mean of a column
# 8.    How to perform group by operations on categorical columns
# 9.    How to sort a particular column
# 10.   How to calculate the count of rows grouped by a criteria
##########################################################################

import pandas as pd 
import numpy as np
import math

# Skip the first row to ignore copyright information
google_ps_d = pd.read_csv("./data/google_play_store.csv",skiprows=1)

##################################################################################
# BEGIN - Data Cleaning
##################################################################################

# axis = 0 (default)drops all rows that contain at least one missing value
# axis = 1 drops all columns that contain at least one missing value

# how = "any" (default) drops rows/columns that have at least one missing value
# how = "all" drops rows/columns that have all missing values only
google_ps_d.dropna( inplace = True )
# google_ps_d.dropna( axis=0, how='any', inplace = True )

# Convert the Installs from string to a number
# - Strip the string of commas and +
google_ps_d["Installs"] = google_ps_d["Installs"].str.replace(",","")
google_ps_d["Installs"] = google_ps_d["Installs"].str.replace("+","")
# - Convert the string to an integer
google_ps_d["Installs"] = pd.to_numeric(google_ps_d["Installs"], downcast = "integer")

# Convert the Size from string to integer
# - Strip the string of M
google_ps_d["Size"] = google_ps_d["Size"].str.replace("M","")
# - Strip the string of "Varies with device" and replace with NaN
google_ps_d["Size"] = google_ps_d["Size"].replace("Varies with device",np.nan)
# - Drop all rows that have NaN
google_ps_d.dropna(axis = 0 , how="any", inplace = True)

# - Convert to integer and multiply by 1000 ( to convert MB to KB  - this avoids decimals )
google_ps_d["Size"] = pd.to_numeric(google_ps_d["Size"], downcast = "float")
google_ps_d["Size"] = google_ps_d["Size"] * 1000

# - Strip the $ symbol in price for float calculation
google_ps_d["Price"] = google_ps_d["Price"].str.replace("$","") 
google_ps_d["Price"] = pd.to_numeric(google_ps_d["Price"], downcast = "float")

# - Convert Reviews column also to an integer. Comment this for now and see
#   how the aggregate functions ( like mean() work
google_ps_d["Reviews"] = pd.to_numeric(google_ps_d["Reviews"], downcast = "integer")

##################################################################################
# END - Data Cleaning
##################################################################################

# List all the unique categories
print ( google_ps_d["Category"].unique() )

# What is the mean rating of the apps
print ( google_ps_d["Rating"].mean())

# List the average rating across each of the category
print ( google_ps_d.groupby(["Category"]).mean())

# Which category has the highest mean price ?
mean = google_ps_d.groupby(["Category"]).mean()
mean.sort_values("Price", axis = 0, ascending = False, inplace = True)
print ( mean )           

# List the top 10 pricier apps
sorted = google_ps_d.sort_values("Price", axis = 0, ascending = False)
print ( sorted.iloc[:,[0,1,7]].head(10))

# How many apps with price > 10 $
print ( google_ps_d[google_ps_d["Price"] > 10].shape  )

# What percentage of apps are PAID ?
paid = google_ps_d.groupby(["Type"]).size()["Paid"]
free = google_ps_d.groupby(["Type"]).size()["Free"]
# or use the count() aggregate function
# google_ps_d.groupby(["Type"]).count()

print ( "Percentage of paid apps = " , math.trunc ( paid/(paid+free) * 100 ) , "%" )

# 11.   Is there a difference in size of FREE vs PAID apps on average ?
print ( google_ps_d.groupby(["Type"]).mean().loc[:,["Size"]])

# 12.   How large is the difference in the average installations of FREE vs paid apps ?
print ( google_ps_d.groupby(["Type"]).mean().loc[:,["Installs"]])


