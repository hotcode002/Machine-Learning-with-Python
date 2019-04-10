##########################################################################
# Program is copyright of Ajay Tech @ https://ajaytech.co
##########################################################################
# In this program we will calculate the number of days
# to the user entered birth date.
# 1. date object
# 2. operations on date object

import datetime

birth_date = input ( "Enter your birthday (MM DD YYYY)- " )

# Convert the user entered string to datetime format
d = birth_date.split(" ")
birth_date = datetime.date( int(d[2]) , int(d[0]) , int(d[1]))

today = datetime.date.today()
birth_date = datetime.date(birth_date.year,birth_date.month, birth_date.day)

# Birthday has already passed - Calculate until next birthday
if today.month   > birth_date.month  :
    birth_date = datetime.date(today.year + 1, birth_date.month,birth_date.day)

# Looks like we are in the same month as your birthday. 
elif today.month == birth_date.month  :
    # looks like we have already passed the day. Wait until next year
    if today.day > birth_date.day :
        birth_date = datetime.date(today.year +1 , birth_date.month,birth_date.day)
    # We are very close now. Just days away
    elif today.day <= birth_date.day :
        birth_date = datetime.date(today.year , birth_date.month,birth_date.day)

# Calculate the difference
delta = birth_date - today

print ( "You have ", delta.days, " days until your birthday")
