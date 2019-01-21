##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
###############################################################################
# Instead of doing vectorized operations (of adding arrays ), create a single 
# numpy array by creating a matrix ( 2D ) and use the numpy array's inbuilt 
# mean operator to calculate the average.
###############################################################################
# Task - Calculate the average temperature of Delhi over the past 20 years
###############################################################################
# Learning - 1. stack lists as columns of a 2-D numpy array.
#            2. use numpy's inbuilt mean function
#            3. understand the concept of axis ( axis = 0, axis = 1 etc )

import csv
import time
import numpy as np

f = open ( "./data/delhi_temperature_1m.csv")
temp_data = csv.reader(f)

# 6 lists to hold 6 sensor data
temp_s1 = []
temp_s2 = []
temp_s3 = []
temp_s4 = []
temp_s5 = []
temp_s6 = []

for temp in temp_data :
    temp_s1.append(temp[0])
    temp_s2.append(temp[1])
    temp_s3.append(temp[2])
    temp_s4.append(temp[3])
    temp_s5.append(temp[4])
    temp_s6.append(temp[5])

del temp_s1[:3], temp_s2[:3], temp_s3[:3], temp_s4[:3], temp_s5[:3], temp_s6[:3]

# Convert the temperatures to floats

temp_s1 = [float(i) for i in temp_s1]
temp_s2 = [float(i) for i in temp_s2]
temp_s3 = [float(i) for i in temp_s3]
temp_s4 = [float(i) for i in temp_s4]
temp_s5 = [float(i) for i in temp_s5]
temp_s6 = [float(i) for i in temp_s6]


temp_array = np.column_stack( (temp_s1,temp_s2,temp_s3,temp_s5,temp_s5,temp_s6 ))

# Calculate the average hourly temperature
start_time = time.time()
average = np.mean ( temp_array, axis = 1)
end_time = time.time()
print ( "time taken = ", (end_time - start_time))

print ( average )