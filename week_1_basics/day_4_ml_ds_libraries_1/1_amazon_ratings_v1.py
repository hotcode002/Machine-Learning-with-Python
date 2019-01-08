

import csv
import time

file = open ( "./data/amazon_ratings.csv")

ratings = []

ratings_tuple = csv.reader(file)

for row in ratings_tuple :
    ratings.append(row[2])

# Remove the first 2 elements in the csv
del ratings[:2]

# Convert all the elements in the list from string to int
# What happens when you don't do it ?
ratings = [int(i) for i in ratings]

# calculate the average
print ( len(ratings))

start_time = time.time()
average = sum(ratings) / len(ratings)
end_time = time.time()
print ( "Average rating across a range of 1M electronics products is " , average)
print ( "Average time taken = ", (end_time - start_time))
