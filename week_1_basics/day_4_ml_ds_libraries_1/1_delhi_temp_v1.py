import csv
import time

f = open ( "./data/delhi_temperature.csv")
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

average = []
# Calculate the average hourly temperature
for index, t in enumerate(temp_s1) :
    sum = temp_s1[index] + temp_s2[index] + temp_s3[index] + \
            temp_s4[index] + temp_s5[index] + temp_s6[index]
    average.append(sum/6)

print ( average[0:100])
