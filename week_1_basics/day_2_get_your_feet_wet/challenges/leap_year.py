# Check if a year is a leap year or not.
# Logic - If the number is
# 1. not divisible by 4, then it is not a leap year
# 2. divisible by 4 and divisible by 100, but not by 400, then its not a leap year
# 3. divisble by 4 and 400, then its a leap year

# The second and third conditions above might sound confusiong. Here is the gist - 
# Not all numbers divisible by 4 are leap years. The exception being, at the turn of
# the century, that year should be divible by 400 as well. This condition only applies
# to the years at the end of a century. If it is not a century year, it just has to be
# divisible by 4. 


year = int ( input ("Enter the year to verify - "))

if year%4 == 0:
    if year%100 == 0 : 
        if year%400 == 0 :
            print ( year, " is a leap year")
        else : 
            print ( year, " is not a leap year")
    else : 
        print ( year, " is a leap year" )
else : 
    print ( year, " is not a leap year")
