

import csv
import time
import numpy

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

ratings_array = numpy.array(ratings)

start_time = time.time()

# Add 1 to all the ratings to correct for a data error.
ratings_array += 1

average = sum(ratings_array) / len(ratings_array)

end_time = time.time()
print ( "Average rating across a range of 1M electronics products is " , average)
print ( "Average time taken = ", (end_time - start_time))

