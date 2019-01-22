##########################################################################
# Data Copyright - 
# The data used in this program is Copyright of Lavanya Gupta @
# https://www.kaggle.com/lava18/google-play-store-apps
##########################################################################
# Program is copyright Ⓒ of Ajay Tech @ https://ajaytech.co
##########################################################################
# TODO - 
# ##################################################################################
# DATA WRANGLING
# 1. Say, the Google Playstore data comes from 3 different sources. Combine these
#       sources into 1 big data frame row-by-row. The files are available as
#       google_play_store_p1.csv , google_play_store_p2.csv, google_play_store_p3.csv
# 2. Once again, say, the Google Playstore data comes from 3 different sources. 
#       This time, each of these data sources only gives us a specific set of 
#       columns. Combine these column-wise as follows. 
#       google_play_store_1_5.csv - App, Category, Ratings, Reviews, Size
#       google_play_store_5_10.csv - Installs, Type, Price, Content Rating, Genres
#       google_play_store_11_13.csv - Last Updated, Current Version, Android Version
# ##################################################################################
# DATA CLEANING
##################################################################################
# 3. Drop all the null values ( NaN, NaT etc )
# 4. Clean the "Installs" column
#       - Strip it of + and , 
#       - Convert it to integer
# 5. Clean the "Size" column
#       - Strip it of the MB indicator - 'M'
#       - Strip it of the text "Varies by Device" and replace it with NaN
#       - Strip all NAs
#       - Convert it to integer
#       - Convert it to KB by multiplying it by 1000
# 6. Clean the "Price" column 
#       - Strip it of $
#       - Convert it to float
# 7. Clean the "Reviews" column
#       - Convert it to integer
# 8. Replace "Android Ver" column with the corresponding Android version name
#       - file android_versions.csv contains the mapping between numeric version and name
##########################################################################
# LEARNING - 
# 1.    How to skip rows from reading a csv file into a data frame
# 2.    How to drop NaNs from a data frame
# 3.    How to replace string values in the cells of a data frame
# 4.    How to replace all the values in a column from a list mapping.
# 5.    How to convert the column type of a df from object to String or integer or float
# 6.    Write data frames to CSV files
##########################################################################

import pandas as pd 
import numpy as np
import math

# 1. Say, the Google Playstore data comes from 3 different sources. Combine these
#       sources into 1 big data 
#       ## What happens if you do ignore_index = False
# Skip the first row to ignore copyright information.
google_ps_1 = pd.read_csv("./data/google_play_store_p1.csv",skiprows=1)
google_ps_2 = pd.read_csv("./data/google_play_store_p2.csv",skiprows=1)
google_ps_3 = pd.read_csv("./data/google_play_store_p3.csv",skiprows=1)

google_ps_d = pd.concat( [google_ps_1, google_ps_2,google_ps_3], ignore_index=True)
print ( google_ps_d)

# 2. Once again, say, the Google Playstore data comes from 3 different sources. 
#       This time, each of these data sources only gives us a specific set of 
#       columns. Combine these column-wise as follows. 
# Skip the first row to ignore copyright information.
google_ps_1 = pd.read_csv("./data/google_play_store_1_5.csv",skiprows=1)
google_ps_2 = pd.read_csv("./data/google_play_store_6_10.csv",skiprows=1)
google_ps_3 = pd.read_csv("./data/google_play_store_11_13.csv",skiprows=1)

google_ps_d = pd.concat( [google_ps_1, google_ps_2,google_ps_3], axis = 1)
print ( google_ps_d)

##################################################################################
# BEGIN - Data Cleaning
##################################################################################

# Skip the first row to ignore copyright information
google_ps_d = pd.read_csv("./data/google_play_store.csv",skiprows=1)

# 3. Drop all the null values ( NaN, NaT etc )
# axis = 0 (default)drops all rows that contain at least one missing value
# axis = 1 drops all columns that contain at least one missing value

# how = "any" (default) drops rows/columns that have at least one missing value
# how = "all" drops rows/columns that have all missing values only
google_ps_d.dropna( inplace = True )
# google_ps_d.dropna( axis=0, how='any', inplace = True )

# 4. Clean the "Installs" column
#       - Strip it of + and , 
#       - Convert it to integer
google_ps_d["Installs"] = google_ps_d["Installs"].str.replace(",","")
google_ps_d["Installs"] = google_ps_d["Installs"].str.replace("+","")
google_ps_d["Installs"] = pd.to_numeric(google_ps_d["Installs"], downcast = "integer")

# 5. Clean the "Size" column
#       - Strip it of the MB indicator - 'M'
#       - Strip it of the text "Varies by Device" and replace it with NaN
#       - Strip all NAs
#       - Convert it to integer
#       - Convert it to KB by multiplying it by 1000
google_ps_d["Size"] = google_ps_d["Size"].str.replace("M","")
google_ps_d["Size"] = google_ps_d["Size"].replace("Varies with device",np.nan)
google_ps_d.dropna(axis = 0 , how="any", inplace = True)
google_ps_d["Size"] = pd.to_numeric(google_ps_d["Size"], downcast = "float")
google_ps_d["Size"] = google_ps_d["Size"] * 1000

# 6. Clean the "Price" column 
#       - Strip it of $
#       - Convert it to float
google_ps_d["Price"] = google_ps_d["Price"].str.replace("$","") 
google_ps_d["Price"] = pd.to_numeric(google_ps_d["Price"], downcast = "float")

# 7. Clean the "Reviews" column
#       - Convert it to integer
google_ps_d["Reviews"] = pd.to_numeric(google_ps_d["Reviews"], downcast = "integer")

# 8. Replace "Android Ver" column with the corresponding Android version name
#       - file android_versions.csv contains the mapping between numeric version and name
google_ps_d["Android Ver"].replace( android_versions["version"].tolist(),
                                    android_versions["name"].tolist(),
                                    inplace = True )
# - Drop all rows that have NaN
google_ps_d.dropna(axis = 0 , how="any", inplace = True)                                    

##################################################################################
# END - Data Cleaning
##################################################################################

# Write the clean version of the play store data to file
google_ps_d.to_csv("./data/google_play_store_clean.csv")

