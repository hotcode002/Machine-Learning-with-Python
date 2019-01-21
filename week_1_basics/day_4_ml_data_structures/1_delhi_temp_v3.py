###############################################################################
# Do the same operation in Python - instead of lists, use numpy arrays. Compare
# the time take between lists and numpy arrays for the same task.
###############################################################################
# Task - Calculate the average temperature of Delhi over the past 20 years
###############################################################################
# Learning - 1. Create numpy array
#            2. Understand how Vectorized operations work
#            3. Prove that vectorized operations in numpy are significantly
#               faster than lists
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

temp_s1_a = np.array(temp_s1)
temp_s2_a = np.array(temp_s2)
temp_s3_a = np.array(temp_s3)
temp_s4_a = np.array(temp_s4)
temp_s5_a = np.array(temp_s5)
temp_s6_a = np.array(temp_s6)

# Calculate the average hourly temperature
start_time = time.time()
temp_avg = ( temp_s1_a + temp_s2_a + temp_s3_a + \
             temp_s4_a + temp_s5_a + temp_s6_a ) / 6
end_time = time.time()
print ( "time taken = ", (end_time - start_time))


