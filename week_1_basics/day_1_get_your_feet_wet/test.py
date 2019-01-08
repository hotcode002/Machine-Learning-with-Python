import numpy as np

a = np.arange(20).reshape(5,4)
print ( a)

a[:,0] = a[:,0] * 10

print ( a )