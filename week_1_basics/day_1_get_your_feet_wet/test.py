import numpy as np

a = np.arange(20).reshape(5,4)
print ( a)
b = a[ a<5 & a>10 ]

print (b)