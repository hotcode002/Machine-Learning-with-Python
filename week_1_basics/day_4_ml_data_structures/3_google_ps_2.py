##########################################################################
# Data Copyright - 
# The data used in this program is Copyright of Lavanya Gupta @
# https://www.kaggle.com/lava18/google-play-store-apps
##########################################################################
# Program is copyright Ⓒ of Ajay Tech @ https://ajaytech.co
##########################################################################
# TODO - 
# ##################################################################################
# BEGIN - Data Wrangling
##################################################################################
# 1. Say, the Google Playstore data comes from 3 different sources. Combine these
#       sources into 1 big data frame row-by-row. The files are available as
#       google_play_store_p1.csv , google_play_store_p2.csv, google_play_store_p3.csv
# 2. Once again, say, the Google Playstore data comes from 3 different sources. 
#       This time, each of these data sources only gives us a specific set of 
#       columns. Combine these column-wise as follows. 
#       google_play_store_1_5.csv - App, Category, Ratings, Reviews, Size
#       google_play_store_5_10.csv - Installs, Type, Price, Content Rating, Genres
#       google_play_store_11_13.csv - Last Updated, Current Version, Android Version
##########################################################################
# LEARNING - 
# 1.    How to concatenate data frames row-wise
# 2.    How to concatenate data frames column-wise
##########################################################################

import pandas as pd 
import numpy as np

# Skip the first row to ignore copyright information.
google_ps_1 = pd.read_csv("./data/google_play_store_p1.csv",skiprows=1)
google_ps_2 = pd.read_csv("./data/google_play_store_p2.csv",skiprows=1)
google_ps_3 = pd.read_csv("./data/google_play_store_p3.csv",skiprows=1)

# 1. Say, the Google Playstore data comes from 3 different sources. Combine these
#       sources into 1 big data 
#       ## What happens if you do ignore_index = False
google_ps_d = pd.concat( [google_ps_1, google_ps_2,google_ps_3], ignore_index=True)
print ( google_ps_d)

# Skip the first row to ignore copyright information.
google_ps_1 = pd.read_csv("./data/google_play_store_1_5.csv",skiprows=1)
google_ps_2 = pd.read_csv("./data/google_play_store_6_10.csv",skiprows=1)
google_ps_3 = pd.read_csv("./data/google_play_store_11_13.csv",skiprows=1)

# 2. Once again, say, the Google Playstore data comes from 3 different sources. 
#       This time, each of these data sources only gives us a specific set of 
#       columns. Combine these column-wise as follows. 
google_ps_d = pd.concat( [google_ps_1, google_ps_2,google_ps_3], axis = 1)
print ( google_ps_d)
