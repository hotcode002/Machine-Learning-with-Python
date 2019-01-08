###############################################################################
# 1. Instead of using intermediary lists, read the CSV file directly into numpy
#    arrays using numpy's inbuilt function genfromtxt(). This is much faster.
# 2. Also, we have found that sensor 6 has malfunctioned and we would rather
#    ignore it for the time being for analysis.
# 3. Sensor 1 seems 10% hypersensitive. Cut down it's value by 10% overall.
# 4. Also, we have found that the rows 1 to 10 have got corrupted and would 
#    need to be ignored for analysis. 
###############################################################################
# Task - Calculate the average temperature of Delhi over the past 20 years
###############################################################################
# Learning - 1. use numpy's genfromtxt to read files directly into arrays.
#            2. how to handle different delimiters, comments, column headers etc
#            3. how to specify the data type for numpy arrays

import csv
import time
import numpy as np

temp_data = np.genfromtxt( "./data/delhi_temperature_1m_missing.csv", 
                            delimiter       = ",",
                            comments        = "#",
                            dtype           = float,
                            skip_header     = 3,
                            filling_values  = 30 )

# Remove the last column ( 6th ), axis = 1 is across columns
temp_data = np.delete(temp_data,5,axis=1)

# Reduce the sensitivity of first sensor by 10 %
temp_data[:,0] = temp_data[:,0] * 0.9
print ( temp_data )

# Remove rows 1-10
print ( temp_data.shape)
temp_data = np.delete(temp_data,range(10),axis=0)
print ( temp_data.shape)