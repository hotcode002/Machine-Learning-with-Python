###############################################################################
# 1. Sensor 1 seems 10% hypersensitive. Cut down it's value by 10% overall.
# 2. Add 0.2 to all the data points to accomodate for a data error
# 3. Adjust the sensitivity of the sensors as follows 
#    - sensor 1 ( -12% )
#    - sensor 2 (  15% )
#    - sensor 3 (  21% )
#    - sensor 4 (  -9% )
#    - sensor 5 (  18% )
#    - sensor 6 (  -4% )
# 4. Calculate the accuracy of the sensors by measuring it against the mean
###############################################################################
# Task - Calculate the average temperature of Delhi over the past 20 years
###############################################################################
# Learning - 1. understand numpy's broadcast functionality

import numpy as np

temp_data = np.genfromtxt( "./data/delhi_temperature.csv", 
                            delimiter       = ",",
                            comments        = "#",
                            dtype           = float,
                            skip_header     = 3)

# 1. Reduce the sensitivity of first sensor by 10 %
temp_data[:,0] = temp_data[:,0] * 0.9
print ( temp_data )

# 2. Add 0.2 to all the data points
temp_data += 0.2

# 3. Adjust the sensitivity of the sensors as follows
#    The 1x6 dim array is broadcast as nx6 array
#    where n is the number or rows in temp_data
adjust = np.array ([.88,1.15,1.21,.91,1.18,.96])
temp_data_adjust = temp_data * adjust

# 4. Calculate the accuracy of the sensors by comparing it against the mean
# Read the data again, as we have done quite some manipulations
temp_data = np.genfromtxt( "./data/delhi_temperature.csv", 
                            delimiter       = ",",
                            comments        = "#",
                            dtype           = float,
                            skip_header     = 3)
mean = np.mean( temp_data, axis = 1)
temp_data = temp_data - mean[:,None]
mean = np.mean( temp_data, axis = 1)
print ( mean )