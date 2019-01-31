import random
import math

random_numbers = []
for i in range(1000) :
    random_numbers.append(math.trunc( random.uniform(50,98) ))

print ( random_numbers)