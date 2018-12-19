# Calculate the sum of digits in a number
# import math ( if you need to use the floor function)

i = int ( input("Enter a number - "))

total = 0
while ( i > 0 ) :
    # This is modulo division. It gives the remainder after the division.
    digit = i%10
    total = total + digit
    
    # This is floor division. It will 'floor' the result.
    i = i // 10

    # or you can use the floor function - which does the same. 
    # i = math.floor ( i/10 )

print ( "The sum of the digits of ",i," is", total)