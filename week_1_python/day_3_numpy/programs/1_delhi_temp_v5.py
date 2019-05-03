##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
###############################################################################
# 1. Instead of using intermediary lists, read the CSV file directly into numpy
#    arrays using numpy's inbuilt function genfromtxt(). This is much faster.
# 2. Also, we have found that sensor 6 has malfunctioned and we would rather
#    ignore it for the time being for analysis.
# 3. Also, we have found that the rows 1 to 10 have got corrupted and would 
#    need to be ignored for analysis. 
# 4. Split the array into 2 parts for further processing
#    -- Sensors 1,2,3 
#    -- Sensors 4,5
# 5. Combine both the arrays into 1 and
#    -- compute the row level means
#    -- append it as the last column, give it a name - mean
###############################################################################
# Task - Calculate the average temperature of Delhi over the past 20 years
###############################################################################
# Learning - 1. use numpy's genfromtxt to read files directly into arrays.
#            2. how to handle different delimiters, comments, column headers etc
#            3. how to specify the data type for numpy arrays
#            4. delete columns from a numpy array
#            5. delete rows from a numpy array
#            6. manipulate all the values in a column ( vectorized operations)
#            7. splice numpy arrays using indexing

import numpy as np

# 1. Use numpy's inbuilt genfromtxt function to read CSV directly to array
temp_data = np.genfromtxt( "./data/delhi_temperature_1m_missing.csv", 
                            delimiter       = ",",
                            comments        = "#",
                            dtype           = float,
                            skip_header     = 3,
                            filling_values  = 30 )

# 2. Remove the last column ( 6th ), axis = 1 is across columns
temp_data = np.delete(temp_data,5,axis=1)

# 3. Remove rows 1-10
print ( temp_data.shape)
temp_data = np.delete(temp_data,range(10),axis=0)
print ( temp_data.shape)

# 4. Split the array into 2 parts for further processing
# We could use the split() or array_split() function as well. 
temp_data_1 = temp_data[:,0:3]
temp_data_2 = temp_data[:,3:5]

# 5. combine both the arrays into 1 array and
temp_data_all = np.append(temp_data_1, temp_data_2,axis=1)
# [:,None] is used to create a new dimension to a vector
# essentially converting a vector to a nx1 matrix
mean_all = np.mean(temp_data_all,axis=1)[:,None]
temp_data_all_mean = np.append(temp_data_all, mean_all,axis=1)
print ( temp_data_all_mean)
