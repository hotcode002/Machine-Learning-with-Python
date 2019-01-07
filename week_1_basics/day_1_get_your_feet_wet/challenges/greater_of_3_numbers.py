# In this challenge, we will have to find the greater of 3 numbers
# without using list structure

print ( "Enter 3 numbers - ")

first   = int( input ( "Enter first number - ") )
second  = int( input ( "Enter second number - ") )
third   = int( input ( "Enter third number - ") )

if first > second :
    greater = first
else :
    greater = second

if third > greater :
    print ("The largest number is - ", third)
else :
    print ( "The largest number is - ", greater)