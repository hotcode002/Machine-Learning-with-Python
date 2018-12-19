# Find how many lower and upper case characters are there in a string

s = input ( "Enter the string to be searched - ")

counter_l = 0   # counter for lower case
counter_u = 0   # counter for upper case

for i in range(len(s)) :
    if s[i].islower() == True :
        counter_l = counter_l + 1
    elif s[i].isupper() == True:
        counter_u = counter_u + 1

print ( "The number of upper case characters is ", counter_u)
print ( "The number of lower case characters is ", counter_l)