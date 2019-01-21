##########################################################################
# Data Copyright info - 
# The data used in this program is Copyright of
# https://www.kaggle.com/lava18/google-play-store-apps
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
##########################################################################
# LEARNING - 
# 1. What is a data frame
# 2. How to read data from file to a data frame using pandas 
# 3. Rows and columns in a data frame
# 4. Shape, min,max,average of values in a data frame
# 5. How to rename columns of a data frame
# 6. How to get the individual column values of a data frame
# 7. How to add a new column to a data frame
# 8. How to slice a data frame by rows, columns
#    - Row & column based slicing using iloc
# 9. How to filter out data from a data frame
#    - Filter out data from any row/column based on its value
#    - Single & multiple filters using boolean masks
##########################################################################

import pandas as pd 
import numpy as np

google_ps_d = pd.read_csv("./data/google_play_store.csv")

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

# What percentage of apps are FREE ?

