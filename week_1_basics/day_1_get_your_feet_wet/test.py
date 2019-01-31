import random
import math

random_numbers = []
for i in range(100) :
    random_numbers.append(math.trunc( random.random() * 100 ))

print ( random_numbers)