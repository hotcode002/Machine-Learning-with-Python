import numpy as np

a = np.arange(20).reshape(5,4)
print ( a)

b = np.arange(20,40).reshape(5,4)

print (b)
c = a>5
d = a<15

e = c & d
print ( e)
print (a[e])

# c = a[a>5 & a<15]
# print ( c )

# d = a * b

# print ( c)

# print ( d)

# a_10 = np.full ( (3,3),True)
# a_5  = np.full ( (3,3), False )

# a_5_v = np.array([5,10,15])
# print ( a_10 & a_5 )
