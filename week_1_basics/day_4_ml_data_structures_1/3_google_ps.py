##########################################################################
# Data Copyright info - 
# The data used in this program is Copyright of
# https://www.kaggle.com/lava18/google-play-store-apps
##########################################################################
# TODO - 
# 1. Drop all the null values ( NaN, NaT etc )
# 2. Check what is the
#    - average rating of the apps on the store ? 
#    - average number of reviews of the apps on the store ? 
# 3. Che
# 3. Which category does most of the apps belong to ?
# 4. Calculate the average stock price and set it as a new coulmn - average
#    - average =  (adj_high + adj_open)/2
# 5. What is the maximum adjusted volume till date ?
# 6. When did the maximum adjusted volume occur ?
# 7. Filter out just the data for 2018
# 8. Filter out all the rows where the adjusted volume is > 100 M
# 9. Filter out only the first 5 columns
#    - Open, High, Low, Close, Volume
#    - For these 5 columns, filter out all the rows with adjusted volume > 100 M
#    - On top of this, filter out rows with Open value > 100
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

google_ps_d = pd.read_csv("./data/google_play_store.csv")

print ( google_ps_d.shape )


# axis = 0 (default)drops all rows that contain at least one missing value
# axis = 1 drops all columns that contain at least one missing value

# how = "any" (default) drops rows/columns that have at least one missing value
# how = "all" drops rows/columns that have all missing values only
google_ps_d.dropna( inplace = True )
# google_ps_d.dropna( axis=0, how='any', inplace = True )

print ( google_ps_d.shape )

# What is the average rating 
print ( google_ps_d["Rating"].mean())

# Does not work. Why ?
print ( google_ps_d["Reviews"].mean() )

google_ps_d['Reviews'] = pd.to_numeric(google_ps_d['Reviews'], downcast='integer')
print ( google_ps_d["Reviews"].mean() )

print ( google_ps_d.dtypes )
